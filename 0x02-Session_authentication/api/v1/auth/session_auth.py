#!/usr/bin/env python3
'''
Authenticates a session with Basic Authentication
'''
from .auth import Auth
from flask import request
from models.user import User
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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Retrieves the User ID based on Session ID
        '''
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        '''
        Retrieves the user instance based on Cookie value
        '''
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        '''
        Destroys a session
        '''
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
