import connexion
import six

from swagger_server.models.auth_error import AuthError  # noqa: E501
from swagger_server.models.client_credential_response import ClientCredentialResponse  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server import util


def fetch_token(grant_type, client_id, client_secret, scope):  # noqa: E501
    """fetch a token

    Return an access token based on clientID and clientSecret. # noqa: E501

    :param grant_type: 
    :type grant_type: str
    :param client_id: 
    :type client_id: str
    :param client_secret: 
    :type client_secret: str
    :param scope: 
    :type scope: str

    :rtype: ClientCredentialResponse
    """
    # TODO: Implement
    return "123"
