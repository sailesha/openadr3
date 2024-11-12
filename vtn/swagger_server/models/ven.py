# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.model_date_time import ModelDateTime  # noqa: F401,E501
from swagger_server.models.object_id import ObjectID  # noqa: F401,E501
from swagger_server.models.resource import Resource  # noqa: F401,E501
from swagger_server.models.values_map import ValuesMap  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class Ven(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: ObjectID=None, created_date_time: ModelDateTime=None, modification_date_time: ModelDateTime=None, object_type: str=None, ven_name: str=None, attributes: List[ValuesMap]=None, targets: List[ValuesMap]=None, resources: List[Resource]=None):  # noqa: E501
        """Ven - a model defined in Swagger

        :param id: The id of this Ven.  # noqa: E501
        :type id: ObjectID
        :param created_date_time: The created_date_time of this Ven.  # noqa: E501
        :type created_date_time: ModelDateTime
        :param modification_date_time: The modification_date_time of this Ven.  # noqa: E501
        :type modification_date_time: ModelDateTime
        :param object_type: The object_type of this Ven.  # noqa: E501
        :type object_type: str
        :param ven_name: The ven_name of this Ven.  # noqa: E501
        :type ven_name: str
        :param attributes: The attributes of this Ven.  # noqa: E501
        :type attributes: List[ValuesMap]
        :param targets: The targets of this Ven.  # noqa: E501
        :type targets: List[ValuesMap]
        :param resources: The resources of this Ven.  # noqa: E501
        :type resources: List[Resource]
        """
        self.swagger_types = {
            'id': ObjectID,
            'created_date_time': ModelDateTime,
            'modification_date_time': ModelDateTime,
            'object_type': str,
            'ven_name': str,
            'attributes': List[ValuesMap],
            'targets': List[ValuesMap],
            'resources': List[Resource]
        }

        self.attribute_map = {
            'id': 'id',
            'created_date_time': 'createdDateTime',
            'modification_date_time': 'modificationDateTime',
            'object_type': 'objectType',
            'ven_name': 'venName',
            'attributes': 'attributes',
            'targets': 'targets',
            'resources': 'resources'
        }
        self._id = id
        self._created_date_time = created_date_time
        self._modification_date_time = modification_date_time
        self._object_type = object_type
        self._ven_name = ven_name
        self._attributes = attributes
        self._targets = targets
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt) -> 'Ven':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ven of this Ven.  # noqa: E501
        :rtype: Ven
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ObjectID:
        """Gets the id of this Ven.


        :return: The id of this Ven.
        :rtype: ObjectID
        """
        return self._id

    @id.setter
    def id(self, id: ObjectID):
        """Sets the id of this Ven.


        :param id: The id of this Ven.
        :type id: ObjectID
        """

        self._id = id

    @property
    def created_date_time(self) -> ModelDateTime:
        """Gets the created_date_time of this Ven.


        :return: The created_date_time of this Ven.
        :rtype: ModelDateTime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time: ModelDateTime):
        """Sets the created_date_time of this Ven.


        :param created_date_time: The created_date_time of this Ven.
        :type created_date_time: ModelDateTime
        """

        self._created_date_time = created_date_time

    @property
    def modification_date_time(self) -> ModelDateTime:
        """Gets the modification_date_time of this Ven.


        :return: The modification_date_time of this Ven.
        :rtype: ModelDateTime
        """
        return self._modification_date_time

    @modification_date_time.setter
    def modification_date_time(self, modification_date_time: ModelDateTime):
        """Sets the modification_date_time of this Ven.


        :param modification_date_time: The modification_date_time of this Ven.
        :type modification_date_time: ModelDateTime
        """

        self._modification_date_time = modification_date_time

    @property
    def object_type(self) -> str:
        """Gets the object_type of this Ven.

        Used as discriminator.  # noqa: E501

        :return: The object_type of this Ven.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this Ven.

        Used as discriminator.  # noqa: E501

        :param object_type: The object_type of this Ven.
        :type object_type: str
        """
        allowed_values = ["VEN"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def ven_name(self) -> str:
        """Gets the ven_name of this Ven.

        User generated identifier, may be VEN identifier provisioned out-of-band. venName is expected to be unique within the scope of a VTN   # noqa: E501

        :return: The ven_name of this Ven.
        :rtype: str
        """
        return self._ven_name

    @ven_name.setter
    def ven_name(self, ven_name: str):
        """Sets the ven_name of this Ven.

        User generated identifier, may be VEN identifier provisioned out-of-band. venName is expected to be unique within the scope of a VTN   # noqa: E501

        :param ven_name: The ven_name of this Ven.
        :type ven_name: str
        """
        if ven_name is None:
            raise ValueError("Invalid value for `ven_name`, must not be `None`")  # noqa: E501

        self._ven_name = ven_name

    @property
    def attributes(self) -> List[ValuesMap]:
        """Gets the attributes of this Ven.

        A list of valuesMap objects describing attributes.  # noqa: E501

        :return: The attributes of this Ven.
        :rtype: List[ValuesMap]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List[ValuesMap]):
        """Sets the attributes of this Ven.

        A list of valuesMap objects describing attributes.  # noqa: E501

        :param attributes: The attributes of this Ven.
        :type attributes: List[ValuesMap]
        """

        self._attributes = attributes

    @property
    def targets(self) -> List[ValuesMap]:
        """Gets the targets of this Ven.

        A list of valuesMap objects describing target criteria.  # noqa: E501

        :return: The targets of this Ven.
        :rtype: List[ValuesMap]
        """
        return self._targets

    @targets.setter
    def targets(self, targets: List[ValuesMap]):
        """Sets the targets of this Ven.

        A list of valuesMap objects describing target criteria.  # noqa: E501

        :param targets: The targets of this Ven.
        :type targets: List[ValuesMap]
        """

        self._targets = targets

    @property
    def resources(self) -> List[Resource]:
        """Gets the resources of this Ven.

        A list of resource objects representing end-devices or systems.  # noqa: E501

        :return: The resources of this Ven.
        :rtype: List[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources: List[Resource]):
        """Sets the resources of this Ven.

        A list of resource objects representing end-devices or systems.  # noqa: E501

        :param resources: The resources of this Ven.
        :type resources: List[Resource]
        """

        self._resources = resources