#!/usr/bin/env python3
"""Render drafts/NN.pitches.md to pitches/NN.html in the site shell. Idempotent: rerun after
any pitch file changes. Minimal Markdown: #/## headings, paragraphs, **bold**, *em*, `code`,
[text](url), bullet lists."""
import glob, html, os, re
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', t)
    return t
def render(md):
    out, para, ul = [], [], []
    def flush():
        if para: out.append('<p>%s</p>' % inline(' '.join(para))); para.clear()
        if ul: out.append('<ul>%s</ul>' % ''.join('<li>%s</li>' % inline(x) for x in ul)); ul.clear()
    title = None
    for line in md.splitlines():
        if line.startswith('# '):
            flush(); title = line[2:].strip(); continue
        if line.startswith('## '):
            flush(); out.append('<h2>%s</h2>' % inline(line[3:].strip())); continue
        if line.startswith('### '):
            flush(); out.append('<h3>%s</h3>' % inline(line[4:].strip())); continue
        if re.match(r'^\s*[-*] ', line):
            if para: flush()
            ul.append(re.sub(r'^\s*[-*] ', '', line)); continue
        if not line.strip(): flush(); continue
        if ul and line.startswith('  '): ul[-1] += ' ' + line.strip(); continue
        if ul: flush()
        para.append(line.strip())
    flush(); return title, '\n'.join(out)
shell = open(os.path.join(root, 'chapters', '_shell.html'), encoding='utf-8').read()
head = shell.split('<main class="wrap">')[0]
for f in sorted(glob.glob(os.path.join(root, 'drafts', '[0-9][0-9].pitches.md'))):
    nn = os.path.basename(f)[:2]
    title, body = render(open(f, encoding='utf-8').read())
    title = title or 'Chapter %s — pitches' % nn
    page = head.replace('TITLE — Ten Ways In', html.escape(title) + ' — Ten Ways In') \
               .replace('ONE SENTENCE.', 'Candidate angles for chapter %s, with the documents each would rest on.' % nn)
    page += ('<main class="wrap">\n<p class="kicker">Chapter %s · pitches</p>\n<h1>%s</h1>\n%s\n'
             '<p class="note">Source: <code>drafts/%s.pitches.md</code>; documents indexed in '
             '<code>resources/sources/%s/SOURCES.md</code>.</p>\n'
             '<nav class="chapter-nav">\n  <span></span>\n  <a href="../index.html">Contents</a>\n  <span></span>\n</nav>\n'
             '</main>\n<footer class="site-footer"><div class="wrap"><p>Seventeenth in a series built the same way. Corrections welcome.</p></div></footer>\n</body>\n</html>\n'
             % (nn, inline(title), body, nn, nn))
    dest = os.path.join(root, 'pitches', nn + '.html')
    open(dest, 'w', encoding='utf-8').write(page); print('  wrote pitches/%s.html  (%s)' % (nn, title))
