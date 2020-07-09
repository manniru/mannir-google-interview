#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

MESSAGE = '''
FUYZFAIXEB4SSU5TUkkGGAQAAFJBQUkNBh4CBAsGFBFSTVtOSQwBGgQPDAQQUkFBSQsPFAETHhJG VE9NRgcACgALBQMDDRFSQUFJDwoaBwQcBAwRGxlGTlRJVRsPBg4CHxAJRkJOTgAPAwgIFQdSTVtO SRoTCARNTUFTEwIOSU5TUkkWAw9AUwg=
'''

KEY = 'najaatumannir'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)