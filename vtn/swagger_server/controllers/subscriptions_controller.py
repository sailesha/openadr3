import connexion
import six

from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.object_types import ObjectTypes  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server import util


class Backend:
    subscriptions: dict[str, Subscription]

    def __init__(self):
        self.subscriptions = {}
    
    def get_subscription(self, subscription_id: str):
        return self.subscriptions[subscription_id]
    
    def set_subscription(self, subscription: Subscription) -> Subscription:
        subscription.id = str(len(self.subscriptions))
        self.subscriptions[subscription.id] = subscription
        return subscription
    
    def delete_subscription(self, subscription_id: str) -> Subscription:
        subscription = self.subscriptions[subscription_id]
        del self.subscriptions[subscription_id]
        return subscription
    
    def update_subscription(self, subscription_id: str, subscription: Subscription) -> Subscription:
        self.subscriptions[subscription_id] = subscription
        return subscription
    
    def search_all_subscriptions(self, program_id=None, client_name=None, target_type=None, target_values=None, objects=None, skip=None, limit=None) -> list[Subscription]:
        # TODO: Implement filtering
        return list(self.subscriptions.values())


backend = Backend()


def create_subscription(body):  # noqa: E501
    """create subscription

    Create a new subscription. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.set_subscription(body)


def delete_subscription(subscription_id):  # noqa: E501
    """delete  subscription

    Delete the subscription specified by subscriptionID specified in path. # noqa: E501

    :param subscription_id: object ID of the associated subscription.
    :type subscription_id: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        subscription_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.delete_subscription(subscription_id)


def search_subscription_by_id(subscription_id):  # noqa: E501
    """search subscriptions by ID

    Return the subscription specified by subscriptionID specified in path. # noqa: E501

    :param subscription_id: object ID of the associated subscription.
    :type subscription_id: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        subscription_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.get_subscription(subscription_id)


def search_subscriptions(program_id=None, client_name=None, target_type=None, target_values=None, objects=None, skip=None, limit=None):  # noqa: E501
    """search subscriptions

    List all subscriptions. May filter results by programID and clientName as query params. May filter results by targetType and targetValues as query params. May filter results by objects as query param. See objectTypes schema. Use skip and pagination query params to limit response size.  # noqa: E501

    :param program_id: filter results to subscriptions with programID.
    :type program_id: dict | bytes
    :param client_name: filter results to subscriptions with clientName.
    :type client_name: str
    :param target_type: Indicates targeting type, e.g. GROUP
    :type target_type: str
    :param target_values: List of target values, e.g. group names
    :type target_values: List[str]
    :param objects: list of objects to subscribe to.
    :type objects: list | bytes
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Subscription]
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        objects = [ObjectTypes.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return backend.search_all_subscriptions(program_id, client_name, target_type, target_values, objects, skip, limit)


def update_subscription(subscription_id, body=None):  # noqa: E501
    """update  subscription

    Update the subscription specified by subscriptionID specified in path. # noqa: E501

    :param subscription_id: object ID of the associated subscription.
    :type subscription_id: dict | bytes
    :param body: subscription item to update.
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        subscription_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_subscription(subscription_id, body)
