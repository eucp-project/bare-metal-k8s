import sys
from tempfile import NamedTemporaryFile
import shutil


ip = sys.argv[1]
print(ip)
with open('hosts.ini') as fp, NamedTemporaryFile(mode='w', delete=False) as tmp:
    mode = None
    name = ""
    i = -1
    for line in fp:
        if ip in line:
            raise ValueError("node ip already exists in hosts.ini")
        if '[all]' in line:
            mode = 'all'
        elif '[workers]' in line:
            mode = 'workers'
        else:
            i += 1
        if not line.strip():
            if mode == 'all':
                name = f"node{i}"
                tmp.write(f"{name} ansible_host={ip}\n")
                mode = None
            elif mode == 'workers':
                print('WORKERS')
                tmp.write(f"{name}\n")
                mode = None
        tmp.write(line)
    if mode == 'workers':
        tmp.write(f"{name}\n")
shutil.move(tmp.name, 'hosts.ini')
print(name)
