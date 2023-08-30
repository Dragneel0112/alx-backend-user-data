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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Validates password to encrypted one

    Args:
        hashed_password: Encrypted password
        password: Password to validate

    Return: True if passwords match, else False
    '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
