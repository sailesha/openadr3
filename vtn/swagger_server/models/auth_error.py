# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AuthError(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error: str=None, error_description: str=None, error_uri: str=None):  # noqa: E501
        """AuthError - a model defined in Swagger

        :param error: The error of this AuthError.  # noqa: E501
        :type error: str
        :param error_description: The error_description of this AuthError.  # noqa: E501
        :type error_description: str
        :param error_uri: The error_uri of this AuthError.  # noqa: E501
        :type error_uri: str
        """
        self.swagger_types = {
            'error': str,
            'error_description': str,
            'error_uri': str
        }

        self.attribute_map = {
            'error': 'error',
            'error_description': 'error_description',
            'error_uri': 'error_uri'
        }
        self._error = error
        self._error_description = error_description
        self._error_uri = error_uri

    @classmethod
    def from_dict(cls, dikt) -> 'AuthError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The authError of this AuthError.  # noqa: E501
        :rtype: AuthError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> str:
        """Gets the error of this AuthError.

        As described in rfc6749 | invalid_request – The request is missing a parameter so the server can’t proceed with the request. This may also be returned if the request includes an unsupported parameter or repeats a parameter. invalid_client – Client authentication failed, such as if the request contains an invalid client ID or secret. Send an HTTP 401 response in this case. invalid_grant – The authorization code (or user’s password for the password grant type) is invalid or expired. This is also the error you would return if the redirect URL given in the authorization grant does not match the URL provided in this access token request. invalid_scope – For access token requests that include a scope (password or client_credentials grants), this error indicates an invalid scope value in the request. unauthorized_client – This client is not authorized to use the requested grant type. For example, if you restrict which applications can use the Implicit grant, you would return this error for the other apps. unsupported_grant_type – If a grant type is requested that the authorization server doesn’t recognize, use this code. Note that unknown grant types also use this specific error code rather than using the invalid_request above.  # noqa: E501

        :return: The error of this AuthError.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this AuthError.

        As described in rfc6749 | invalid_request – The request is missing a parameter so the server can’t proceed with the request. This may also be returned if the request includes an unsupported parameter or repeats a parameter. invalid_client – Client authentication failed, such as if the request contains an invalid client ID or secret. Send an HTTP 401 response in this case. invalid_grant – The authorization code (or user’s password for the password grant type) is invalid or expired. This is also the error you would return if the redirect URL given in the authorization grant does not match the URL provided in this access token request. invalid_scope – For access token requests that include a scope (password or client_credentials grants), this error indicates an invalid scope value in the request. unauthorized_client – This client is not authorized to use the requested grant type. For example, if you restrict which applications can use the Implicit grant, you would return this error for the other apps. unsupported_grant_type – If a grant type is requested that the authorization server doesn’t recognize, use this code. Note that unknown grant types also use this specific error code rather than using the invalid_request above.  # noqa: E501

        :param error: The error of this AuthError.
        :type error: str
        """
        allowed_values = ["invalid_request", "invalid_client", "invalid_grant", "invalid_scope", "unauthorized_client", "unsupported_grant_type"]  # noqa: E501
        if error not in allowed_values:
            raise ValueError(
                "Invalid value for `error` ({0}), must be one of {1}"
                .format(error, allowed_values)
            )

        self._error = error

    @property
    def error_description(self) -> str:
        """Gets the error_description of this AuthError.

        Should be a sentence or two at most describing the circumstance of the error  # noqa: E501

        :return: The error_description of this AuthError.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description: str):
        """Sets the error_description of this AuthError.

        Should be a sentence or two at most describing the circumstance of the error  # noqa: E501

        :param error_description: The error_description of this AuthError.
        :type error_description: str
        """

        self._error_description = error_description

    @property
    def error_uri(self) -> str:
        """Gets the error_uri of this AuthError.

        Optional reference to more detailed error description  # noqa: E501

        :return: The error_uri of this AuthError.
        :rtype: str
        """
        return self._error_uri

    @error_uri.setter
    def error_uri(self, error_uri: str):
        """Sets the error_uri of this AuthError.

        Optional reference to more detailed error description  # noqa: E501

        :param error_uri: The error_uri of this AuthError.
        :type error_uri: str
        """

        self._error_uri = error_uri
