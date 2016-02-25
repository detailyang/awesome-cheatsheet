#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: detailyang
# @Date:   2016-02-25 11:23:59
# @Last Modified by:   detailyang
# @Last Modified time: 2016-02-25 15:13:44

import re
import sys

from requests import get
from requests.exceptions import ConnectionError, MissingSchema

url_re = re.compile('.*\((.*?)\)')

for i in range(ord('a'), ord('z')+1):
    file = 'docs/{alphabet}.md'.format(alphabet=chr(i))
    with open(file) as f:
        for line, content in enumerate(f.readlines()):
            m = re.match(url_re, content)
            if m is None:
                continue
            try:
                result = get(m.group(1))
                if result.status_code >= 400:
                    print('{file} line #{line} {url} return {code}'.format(file=file, line=line,
                        url=m.group(1), code=result.status_code))
                    sys.exit(1)
            except ConnectionError:
                print('{file} line #{line} {url} cannot connect'.format(file=file, line=line,
                        url=m.group(1)))
            except MissingSchema:
                print('{file} line #{line} {url} missing schema'.format(file=file, line=line,
                        url=m.group(1)))


