#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """
    Class for Basic Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic Auth
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header.split(" ")[0] != "Basic":
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes the value of a base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str)
        """
        Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        decoded = decoded_base64_authorization_header.split(":")
        email = decoded[0]
        pw = decoded[1]

        return (email, pw)
