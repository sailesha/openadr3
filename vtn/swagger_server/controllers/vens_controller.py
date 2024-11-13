import connexion
import six

from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.resource import Resource  # noqa: E501
from swagger_server.models.ven import Ven  # noqa: E501
from swagger_server import util


class ResourceBackend:
    resources: dict[str, Resource]

    def __init__(self):
        self.resources = {}
    
    def get_resource(self, resource_id: str):
        return self.resources[resource_id]
    
    def set_resource(self, resource: Resource) -> Resource:
        resource.id = str(len(self.resources))
        self.resources[resource.id] = resource
        return resource
    
    def delete_resource(self, resource_id: str) -> Resource:
        resource = self.resources[resource_id]
        del self.resources[resource_id]
        return resource
    
    def update_resource(self, resource_id: str, resource: Resource) -> Resource:
        self.resources[resource_id] = resource
        return resource
    
    def search_all_resources(self, resource_name=None, target_type=None, target_values=None, skip=None, limit=None) -> list[Resource]:
        # TODO: Implement filtering
        return list(self.resources.values())


class Backend:
    vens: dict[str, Ven]
    resources: dict[str, Resource]

    def __init__(self):
        self.vens = {}
        self.resources = {}
    
    def get_ven(self, ven_id: str):
        return self.vens[ven_id]
    
    def set_ven(self, ven: Ven) -> Ven:
        ven.id = str(len(self.vens))
        self.vens[ven.id] = ven
        self.resources[ven.id] = ResourceBackend()
        return ven
    
    def delete_ven(self, ven_id: str) -> Ven:
        ven = self.vens[ven_id]
        del self.vens[ven_id]
        del self.resources[ven_id]
        return ven
    
    def update_ven(self, ven_id: str, ven: Ven) -> Ven:
        self.vens[ven_id] = ven
        return ven
    
    def search_all_vens(self, ven_name=None, target_type=None, target_values=None, skip=None, limit=None) -> list[Ven]:
        # TODO: Implement filtering
        return list(self.vens.values())

    def get_ven_resource(self, ven_id: str, resource_id: str) -> Resource:
        return self.resources[ven_id].get_resource(resource_id)
    
    def set_ven_resource(self, ven_id: str, resource: Resource) -> Resource:
        return self.resources[ven_id].set_resource(resource)
    
    def delete_ven_resource(self, ven_id: str, resource_id: str) -> Resource:
        return self.resources[ven_id].delete_resource(resource_id)
    
    def update_ven_resource(self, ven_id: str, resource_id: str, resource: Resource) -> Resource:
        return self.resources[ven_id].update_resource(resource_id, resource)
    
    def search_all_ven_resources(self, ven_id: str, resource_name=None, target_type=None, target_values=None, skip=None, limit=None) -> list[Resource]:
        return self.resources[ven_id].search_all_resources(resource_name, target_type, target_values, skip, limit)

    
backend = Backend()


def create_resource(body, ven_id):  # noqa: E501
    """create resource

    Create a new resource. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param ven_id: Numeric ID of ven.
    :type ven_id: dict | bytes

    :rtype: Resource
    """
    if connexion.request.is_json:
        body = Resource.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.set_ven_resource(ven_id, body)


def create_ven(body):  # noqa: E501
    """create ven

    Create a new ven. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Ven
    """
    if connexion.request.is_json:
        body = Ven.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.set_ven(body)


def delete_ven(ven_id):  # noqa: E501
    """delete  ven

    Delete the ven specified by venID specified in path. # noqa: E501

    :param ven_id: object ID of ven.
    :type ven_id: dict | bytes

    :rtype: Ven
    """
    return backend.delete_ven(ven_id)


def delete_ven_resource(ven_id, resource_id):  # noqa: E501
    """delete  ven resource

    Delete the ven resource specified by venID and resourceID specified in path. # noqa: E501

    :param ven_id: object ID of the associated ven.
    :type ven_id: dict | bytes
    :param resource_id: object ID of the resource.
    :type resource_id: dict | bytes

    :rtype: Resource
    """
    return backend.delete_ven_resource(ven_id, resource_id)


def search_ven_by_id(ven_id):  # noqa: E501
    """search vens by ID

    Return the ven specified by venID specified in path. # noqa: E501

    :param ven_id: object ID of ven.
    :type ven_id: dict | bytes

    :rtype: Ven
    """
    return backend.get_ven(ven_id)


def search_ven_resource_by_id(ven_id, resource_id):  # noqa: E501
    """search ven resources by ID

    Return the ven resource specified by venID and resourceID specified in path. # noqa: E501

    :param ven_id: object ID of the associated ven.
    :type ven_id: dict | bytes
    :param resource_id: object ID of the resource.
    :type resource_id: dict | bytes

    :rtype: Resource
    """
    return backend.get_ven_resource(ven_id, resource_id)


def search_ven_resources(ven_id, resource_name=None, target_type=None, target_values=None, skip=None, limit=None):  # noqa: E501
    """search ven resources

    List all ven resources associated with ven with specified venID. May filter results by resourceName as query params. May filter results by targetType and targetValues as query params. Use skip and pagination query params to limit response size.  # noqa: E501

    :param ven_id: Numeric ID of ven.
    :type ven_id: dict | bytes
    :param resource_name: Indicates resource objects with resourceName
    :type resource_name: str
    :param target_type: Indicates targeting type, e.g. GROUP
    :type target_type: str
    :param target_values: List of target values, e.g. group names
    :type target_values: List[str]
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Resource]
    """
    return backend.search_all_ven_resources(ven_id, resource_name, target_type, target_values, skip, limit)


def search_vens(ven_name=None, target_type=None, target_values=None, skip=None, limit=None):  # noqa: E501
    """search vens

    List all vens. May filter results by venName as query param. May filter results by targetType and targetValues as query params. Use skip and pagination query params to limit response size.  # noqa: E501

    :param ven_name: Indicates ven objects w venName
    :type ven_name: str
    :param target_type: Indicates targeting type, e.g. GROUP
    :type target_type: str
    :param target_values: List of target values, e.g. group names
    :type target_values: List[str]
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Ven]
    """
    return backend.search_all_vens(ven_name, target_type, target_values, skip, limit)


def update_ven(ven_id, body=None):  # noqa: E501
    """update  ven

    Update the ven specified by venID specified in path. # noqa: E501

    :param ven_id: object ID of ven.
    :type ven_id: dict | bytes
    :param body: ven item to update.
    :type body: dict | bytes

    :rtype: Ven
    """
    if connexion.request.is_json:
        body = Ven.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_ven(ven_id, body)


def update_ven_resource(ven_id, resource_id, body=None):  # noqa: E501
    """update  ven resource

    Update the ven resource specified by venID and resourceID specified in path. # noqa: E501

    :param ven_id: object ID of the associated ven.
    :type ven_id: dict | bytes
    :param resource_id: object ID of the resource.
    :type resource_id: dict | bytes
    :param body: resource item to update.
    :type body: dict | bytes

    :rtype: Resource
    """
    if connexion.request.is_json:
        body = Resource.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_ven_resource(ven_id, resource_id, body)
