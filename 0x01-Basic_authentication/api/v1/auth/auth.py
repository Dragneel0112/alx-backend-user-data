#!/usr/bin/env python3
from typing import List, TypeVar
from flask import Flask, request


class Auth:
    '''
    Class Auth manages API authentication
    '''

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        '''
        Function require auth
        '''
        return False

    def authorization_header(
            self,
            request=None
            ) -> str:
        '''
        Function Auth header
        '''
        request = Flask(__name__)
        return None

    def current_user(
            self,
            request=None
            ) -> TypeVar('User'):
        ''' Current User
        '''
        request = Flask(__name__)
        return None
