#!/usr/bin/env python3
'''
Password encryption and validation
'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Encrypts a password using salt

    Args:
        password: Password to be encrypted

    Return: Encrypted password bytes
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
