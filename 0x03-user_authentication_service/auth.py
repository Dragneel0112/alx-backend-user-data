#!/usr/bin/env python3
'''
Authentication module for encryption etc.
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''
    Encodes a password (hashed)
    '''
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
