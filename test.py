# -*- coding: utf-8 -*-
"""
    test
    ~~~~~~~~~
    :copyright: (c) 16/7/19 by imaygou.
    :license: BSD, see LICENSE for more details.
"""
from pyjade.ext import html

if __name__ == "__main__":
    print html.process_jade("""
block title
    include examples.comments
""")