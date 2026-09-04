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
