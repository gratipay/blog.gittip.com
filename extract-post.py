#!/usr/bin/env python

import re, os, textwrap


FRONT, HEADER, META, THROWAWAY, BODY = range(5)

listing = []

for root, dirs, files in os.walk('post'):
    if 'index.html' not in files:
        continue

    filename = root + '/index.html'

    raw = open(filename)

    state = FRONT
    title = dateline = body = ''

    for line in open(filename):
        line = line.strip()

        if 'class="col0"' in line:
            state = HEADER
            continue
        elif 'note</h2>' in line or 'notes</h2>' in line:
            break

        if state == HEADER:
            if 'h1' in line:
                title = re.match(r'^.*>([^<]+)<.*$', line).groups()[0]
                state = META
        elif state == META:
            if 'div' in line:
                dateline = re.match(r'^.*>([^<]+)$', line).groups()[0]
                state = THROWAWAY
        elif state == THROWAWAY:
            state = BODY
        elif state == BODY:
            if not line:
                continue
            wrapped = '\n'.join(textwrap.wrap(line, 80))
            for tag in ('p', 'li', 'ul', 'ol', 'blockquote', 'div'):
                wrapped = wrapped.replace('<'+tag, '\n\n<'+tag)
            body += wrapped

    body = body[1:]  # strip leading newline

    os.remove(root + '/index.html')
    out = open(root + '/index.md', 'w+')

    print >> out, '---'
    print >> out, 'title:', title
    print >> out, 'dateline:', dateline
    print >> out, 'layout: page'
    print >> out, '---'
    print >> out, body

    listing.append({'title': title, 'href': '/'+root+'/', 'dateline': dateline})

print '''\
---
title: Old Gittip Blog
dateline:
layout: page
---'''
print '<table>'
for post in reversed(listing):
    tr = '<tr><td class="dateline">%(dateline)s</td><td><a href="%(href)s">%(title)s</a></td></tr>'
    print tr % post
print '</table>'
