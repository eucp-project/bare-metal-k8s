#! /usr/bin/env python3

import sys
from tempfile import NamedTemporaryFile
import shutil


nodes = {}
with open(sys.argv[1]) as hostfile:
    parse = False
    for line in hostfile:
        if line.strip() == '[all]':
            parse = True
            continue
        elif line.startswith('[') and line.strip().endswith(']'):
            break
        if not parse:
            continue
        name, ip = line.split()
        *_, ip = line.split('=')
        nodes[name] = ip


path = os.path.expanduser("~/.ssh/knownhosts")
with open(path) as fp, NamedTemporaryFile(mode='w', delete=False) as tmp:
    for line in fp:
        name, *_ = line.split()
        ip = name.split(',')[-1]
        if ip in nodes.values():
            continue
        tmp.write(line)
    shutil.move(tmp.name, path)


path = os.path.expanduser("~/.ssh/known
