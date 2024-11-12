# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object_types import ObjectTypes  # noqa: F401,E501
from swagger_server.models.values_map import ValuesMap  # noqa: F401,E501
from swagger_server.models.one_ofnotification_object import OneOfnotificationObject  # noqa: F401,E501
from swagger_server import util


class Notification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, object_type: ObjectTypes=None, operation: str=None, object: OneOfnotificationObject=None, targets: List[ValuesMap]=None):  # noqa: E501
        """Notification - a model defined in Swagger

        :param object_type: The object_type of this Notification.  # noqa: E501
        :type object_type: ObjectTypes
        :param operation: The operation of this Notification.  # noqa: E501
        :type operation: str
        :param object: The object of this Notification.  # noqa: E501
        :type object: OneOfnotificationObject
        :param targets: The targets of this Notification.  # noqa: E501
        :type targets: List[ValuesMap]
        """
        self.swagger_types = {
            'object_type': ObjectTypes,
            'operation': str,
            'object': OneOfnotificationObject,
            'targets': List[ValuesMap]
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'operation': 'operation',
            'object': 'object',
            'targets': 'targets'
        }
        self._object_type = object_type
        self._operation = operation
        self._object = object
        self._targets = targets

    @classmethod
    def from_dict(cls, dikt) -> 'Notification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The notification of this Notification.  # noqa: E501
        :rtype: Notification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_type(self) -> ObjectTypes:
        """Gets the object_type of this Notification.


        :return: The object_type of this Notification.
        :rtype: ObjectTypes
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: ObjectTypes):
        """Sets the object_type of this Notification.


        :param object_type: The object_type of this Notification.
        :type object_type: ObjectTypes
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501

        self._object_type = object_type

    @property
    def operation(self) -> str:
        """Gets the operation of this Notification.

        the operation on on object that triggered the notification.  # noqa: E501

        :return: The operation of this Notification.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation: str):
        """Sets the operation of this Notification.

        the operation on on object that triggered the notification.  # noqa: E501

        :param operation: The operation of this Notification.
        :type operation: str
        """
        allowed_values = ["GET", "POST", "PUT", "DELETE"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def object(self) -> OneOfnotificationObject:
        """Gets the object of this Notification.

        the object that is the subject of the notification.  # noqa: E501

        :return: The object of this Notification.
        :rtype: OneOfnotificationObject
        """
        return self._object

    @object.setter
    def object(self, object: OneOfnotificationObject):
        """Sets the object of this Notification.

        the object that is the subject of the notification.  # noqa: E501

        :param object: The object of this Notification.
        :type object: OneOfnotificationObject
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def targets(self) -> List[ValuesMap]:
        """Gets the targets of this Notification.

        A list of valuesMap objects.  # noqa: E501

        :return: The targets of this Notification.
        :rtype: List[ValuesMap]
        """
        return self._targets

    @targets.setter
    def targets(self, targets: List[ValuesMap]):
        """Sets the targets of this Notification.

        A list of valuesMap objects.  # noqa: E501

        :param targets: The targets of this Notification.
        :type targets: List[ValuesMap]
        """

        self._targets = targets
