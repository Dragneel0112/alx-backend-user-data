#!/usr/bin/env python3
'''
Basic Authentication
'''
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        '''
        Decodes the Base64 string int Authorization header
        Args:
            base64_authorization_header: auth header with Base64 str
        Returns: Decoded Base64 string
        '''
        if not (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        '''
        Extracts user email and password
        from the Base64 decoded str
        Args:
            decoded_base64_authorization_header: str to extract data
        '''
        if not (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None

        return tuple(decoded_base64_authorization_header.split(':', 1))
