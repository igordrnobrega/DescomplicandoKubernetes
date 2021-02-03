#!/usr/bin/env python
from pandocfilters import toJSONFilter
import re

"""
Pandoc filter that causes everything between
'<!-- TOC -->' and '<!-- END TOC -->'
to be ignored.  The comment lines must appear on
lines by themselves, with blank lines surrounding
them.
This is meant to keep one TOC at the begnning of the
book.
"""

incomment = False


def comment(k, v, fmt, meta):
    global incomment
    if k == "RawBlock":
        fmt, s = v
        if fmt == "html":
            if re.search("<!-- TOC -->", s):
                incomment = True
                return []
            elif re.search("<!-- END TOC -->", s):
                incomment = False
                return []
    if incomment:
        return []


if __name__ == "__main__":
    toJSONFilter(comment)
