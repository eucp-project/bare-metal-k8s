import sys
import argparse
from xml.etree import ElementTree as ET
import oca


ADDRESS = 'https://api.hpccloud.surfsara.nl/RPC2'


def parse_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main():
    client = oca.Client(None, address=ADDRESS)
    # [secret,] ID, name, hold/pending, extra-attrs, persistent
    #vmid = client.call('template.instantiate', 10377, 'server', False, options, False)
    listing = client.call('marketpool.info')
    print("Marketplace listing =", listing)


if __name__ == '__main__':
    args = parse_args()
    main()
