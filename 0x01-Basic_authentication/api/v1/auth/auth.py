#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if auth is required
        """
        if path is None or exluded_paths is None:
            return True

        if not path.endswith("/"):
            path = path + "/"

        for i in range(len(excluded_paths)):
            if not excluded_paths[i].endswith("/"):
                excluded_paths[i] = excluded_paths[i] + "/"

        if path not in excluded_paths:
            return True

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
