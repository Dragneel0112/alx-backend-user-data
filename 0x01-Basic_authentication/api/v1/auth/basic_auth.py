#!/usr/bin/env python3
'''
Basic Authentication
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    Basic Authentication class
        - inherits from Auth
    '''
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        '''
        Extracts Base64 portion from Authorization Header for Basic
        Authentication
        Args:
            authorization_header: auth_header to extract Base64 code
        Returns: Base64 part of header after Basic
        '''
        if not (authorization_header and isinstance(authorization_header, str)
                and authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]
