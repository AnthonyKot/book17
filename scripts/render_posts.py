#!/usr/bin/env python3
"""Render posts/NN-vK.md to posts/NN.html using the chapter shell's header and footer. Idempotent."""
import glob, html, os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shell = open(os.path.join(root, 'chapters', '_shell.html'), encoding='utf-8').read()
head = shell[:shell.index('<main class="wrap">') + len('<main class="wrap">')]
tail = shell[shell.index('</main>'):]
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', t)
    return t
def render_md(md):
    out, i, lines = [], 0, md.splitlines()
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.strip() == '---': out.append('<hr>'); i += 1; continue
        if l.startswith('#'):
            n = len(l) - len(l.lstrip('#')); txt = l.lstrip('#').strip()
            if n == 1: i += 1; continue
            out.append('<h%d>%s</h%d>' % (min(n, 4), inline(txt), min(n, 4))); i += 1; continue
        if l.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'): rows.append(lines[i].strip()); i += 1
            rows = [r for r in rows if not re.fullmatch(r'\|?[\s:|-]+\|?', r)]
            if rows:
                cells = lambda r: [c.strip() for c in r.strip('|').split('|')]
                out.append('<div class="ledger-wrap"><table class="ledger"><thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in cells(rows[0])) + '</tr></thead><tbody>')
                for r in rows[1:]: out.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in cells(r)) + '</tr>')
                out.append('</tbody></table></div>')
            continue
        if re.match(r'\s*([-*]|\d+\.)\s', l):
            ordered = bool(re.match(r'\s*\d+\.', l)); items = []
            while i < len(lines) and re.match(r'\s*([-*]|\d+\.)\s', lines[i]):
                item = re.sub(r'^\s*([-*]|\d+\.)\s', '', lines[i]); i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'\s*([-*]|\d+\.)\s', lines[i]):
                    item += ' ' + lines[i].strip(); i += 1
                items.append(item)
            tag = 'ol' if ordered else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag)); continue
        if l.startswith('```'):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith('```'): buf.append(lines[i]); i += 1
            i += 1; out.append('<pre><code>%s</code></pre>' % html.escape('\n'.join(buf))); continue
        if l.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'): buf.append(lines[i][1:].strip()); i += 1
            out.append('<blockquote><p>%s</p></blockquote>' % inline(' '.join(buf))); continue
        para = [l.strip()]; i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('|', '#', '```', '>', '---')) and not re.match(r'\s*([-*]|\d+\.)\s', lines[i]):
            para.append(lines[i].strip()); i += 1
        out.append('<p>%s</p>' % inline(' '.join(para)))
    return '\n'.join(out)
pages = []
for src in sorted(glob.glob(os.path.join(root, 'posts', '*-v*.md'))):
    nn = os.path.basename(src)[:2]; md = open(src, encoding='utf-8').read()
    m = re.search(r'^#\s+(.*)$', md, re.M); title = m.group(1).strip() if m else nn
    m2 = re.search(r'^\*(.+?)\*\s*$', md, re.M); lede = m2.group(1).strip() if m2 else ''
    body = render_md(md)
    body = body.replace('<p><em>%s</em></p>' % inline(lede), '', 1) if lede else body
    page = head.replace('TITLE — Ten Ways In', html.escape(title) + ' — Ten Ways In').replace('ONE SENTENCE.', html.escape(lede[:200]))
    page += '\n<p class="kicker">Post · from chapter %d · %s</p>\n<h1>%s</h1>\n%s\n%s\n<p class="note"><a href="../chapters/%s">The chapter this post was written from</a> · <a href="../index.html">All chapters and posts</a></p>\n' % (int(nn), os.path.basename(src), inline(title), ('<p class="lede">%s</p>' % inline(lede)) if lede else '', body, os.path.basename(glob.glob(os.path.join(root, 'chapters', nn + '-*.html'))[0]))
    page += tail
    dst = os.path.join(root, 'posts', nn + '.html'); open(dst, 'w', encoding='utf-8').write(page)
    pages.append((nn, title, lede, os.path.basename(src)))
    print('  wrote posts/%s.html  (%s)' % (nn, os.path.basename(src)))
open(os.path.join(root, 'posts', 'index.json'), 'w').write(repr(pages))

# --- all posts on one page, in reading order (nav.py ORDER) -------------------------------
order = re.search(r'ORDER\s*=\s*\[(.*?)\]', open(os.path.join(root, 'scripts', 'nav.py'), encoding='utf-8').read(), re.S).group(1)
order = re.findall(r'"(\d\d)"', order)
bynn = {nn: (title, lede, src) for nn, title, lede, src in pages}
allpage = head.replace('TITLE — Ten Ways In', 'All eleven posts — Ten Ways In').replace('ONE SENTENCE.', 'Every chapter as a standalone post, on one page, in reading order.')
allpage += '\n<p class="kicker">Posts · all eleven on one page · reading order</p>\n<h1>All eleven posts</h1>\n<p class="lede">Read in bulk, pick one. Each post opens on the moment and assumes the reader has never heard of the case.</p>\n<ol class="toc">' + ''.join('<li><a href="#p%s">%s · %s</a></li>' % (nn, int(nn), inline(bynn[nn][0])) for nn in order if nn in bynn) + '</ol>\n'
for nn in order:
    if nn not in bynn: continue
    title, lede, src = bynn[nn]
    md = open(os.path.join(root, 'posts', src), encoding='utf-8').read()
    body = render_md(md)
    body = body.replace('<p><em>%s</em></p>' % inline(lede), '', 1) if lede else body
    allpage += '\n<hr>\n<section id="p%s">\n<p class="kicker">Post · from chapter %d · <a href="%s.html">own page</a></p>\n<h1>%s</h1>\n%s\n%s\n</section>\n' % (nn, int(nn), nn, inline(title), ('<p class="lede">%s</p>' % inline(lede)) if lede else '', body)
allpage += '\n<p class="note"><a href="../index.html">All chapters and posts</a></p>\n' + tail
open(os.path.join(root, 'posts', 'all.html'), 'w', encoding='utf-8').write(allpage)
print('  wrote posts/all.html (%d posts)' % len(order))

# --- LinkedIn cuts, one page ---------------------------------------------------------------
cuts = sorted(glob.glob(os.path.join(root, 'posts', 'linkedin', '*.md')))
if cuts:
    li = head.replace('TITLE — Ten Ways In', 'LinkedIn cuts — Ten Ways In').replace('ONE SENTENCE.', 'Short versions of the posts, about 200 words each, one incident, one quoted line, one primary source.')
    li += '\n<p class="kicker">Posts · LinkedIn cuts</p>\n<h1>LinkedIn cuts</h1>\n<p class="lede">About 200 words each: one incident, one quoted line, one link to the primary source. Paste as-is.</p>\n'
    for c in cuts:
        nn = os.path.basename(c)[:2]; md = open(c, encoding='utf-8').read()
        m = re.search(r'^#\s+(.*)$', md, re.M); t = m.group(1).strip() if m else nn
        li += '\n<hr>\n<section id="l%s">\n<p class="kicker">From post %d · <a href="%s.html">full post</a></p>\n<h2>%s</h2>\n%s\n</section>\n' % (nn, int(nn), nn, inline(t), render_md(md))
    li += '\n<p class="note"><a href="all.html">All eleven posts on one page</a> · <a href="../index.html">All chapters and posts</a></p>\n' + tail
    open(os.path.join(root, 'posts', 'linkedin.html'), 'w', encoding='utf-8').write(li)
    print('  wrote posts/linkedin.html (%d cuts)' % len(cuts))

# --- chapter -> post link, idempotent ----------------------------------------------------
for nn, title, lede, src in pages:
    for ch in glob.glob(os.path.join(root, 'chapters', nn + '-*.html')):
        h = open(ch, encoding='utf-8').read()
        if 'class="post-link"' in h: continue
        h = re.sub(r'(<p class="kicker">[^\n]*</p>\n)', r'\1<p class="note post-link"><a href="../posts/%s.html">Read this chapter as a standalone post</a> · <a href="../posts/all.html">all posts on one page</a></p>\n' % nn, h, count=1)
        open(ch, 'w', encoding='utf-8').write(h)
print('  chapter -> post links in place')

