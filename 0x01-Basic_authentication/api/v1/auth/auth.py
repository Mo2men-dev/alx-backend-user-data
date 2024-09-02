#!/usr/bin/env python3
"""
Auth module
"""
from flask import request


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if auth is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to check Auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get user
        """
        return None
