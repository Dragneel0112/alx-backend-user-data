#!/usr/bin/env python3
'''
Authenticates a session with Basic Authentication
'''
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    '''
    Class for session authentication
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Creates session with unique id for the user
        '''
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
