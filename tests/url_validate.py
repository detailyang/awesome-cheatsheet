#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: detailyang
# @Date:   2016-02-25 11:23:59
# @Last Modified by:   detailyang
# @Last Modified time: 2016-02-25 12:35:21

import re
import sys
from requests import get

url_re = re.compile('.*\((.*?)\)')

for i in range(ord('a'), ord('z')+1):
    with open('docs/{alphabet}.md'.format(alphabet=chr(i))) as f:
        for line in f.readlines():
            m = re.match(url_re, line)
            if m is None:
                continue
            result = get(m.group(1))
            if result.status_code >= 400:
                print('{url} return {code}'.format(url = m.group(1), code = result.status_code))
                sys.exit(1)