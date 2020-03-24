#!/usr/bin/env python
"""The main entry point. Invoke as `wgs2json' or `python -m wgs2json'.
"""
import sys
from wgs2json.core import WireGuard


def main():
    wg = WireGuard(sys.stdin.read(), sys.argv)
    wg()


if __name__ == '__main__':
    main()
