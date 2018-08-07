#!/usr/bin/env python3

import keyring
from keyring import core
import argparse
import sys
# Python 2 compat:
try:
    input = raw_input
except NameError:
    pass


parser = \
    argparse.ArgumentParser(description='Store a secret in local keychain')

parser.add_argument('--backend', type=str, nargs='?',
                    help='Keyring backend to use')
parser.add_argument('service', type=str,
                    help='service to log into (e.g., URL)')
parser.add_argument('username', type=str,
                    help='Username to use')

args = parser.parse_args()
service = args.service
username = args.username
backend = args.backend

if sys.stdin.isatty():
    password = input('Password: ')
else:
    password = input()

if backend is not None:
    keyring.set_keyring(core.load_keyring(backend))
keyring.set_password(service, username, password)