# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EventPayloadDescriptor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, object_type: str=None, payload_type: str=None, units: str=None, currency: str=None):  # noqa: E501
        """EventPayloadDescriptor - a model defined in Swagger

        :param object_type: The object_type of this EventPayloadDescriptor.  # noqa: E501
        :type object_type: str
        :param payload_type: The payload_type of this EventPayloadDescriptor.  # noqa: E501
        :type payload_type: str
        :param units: The units of this EventPayloadDescriptor.  # noqa: E501
        :type units: str
        :param currency: The currency of this EventPayloadDescriptor.  # noqa: E501
        :type currency: str
        """
        self.swagger_types = {
            'object_type': str,
            'payload_type': str,
            'units': str,
            'currency': str
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'payload_type': 'payloadType',
            'units': 'units',
            'currency': 'currency'
        }
        self._object_type = object_type
        self._payload_type = payload_type
        self._units = units
        self._currency = currency

    @classmethod
    def from_dict(cls, dikt) -> 'EventPayloadDescriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eventPayloadDescriptor of this EventPayloadDescriptor.  # noqa: E501
        :rtype: EventPayloadDescriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_type(self) -> str:
        """Gets the object_type of this EventPayloadDescriptor.

        Used as discriminator.  # noqa: E501

        :return: The object_type of this EventPayloadDescriptor.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this EventPayloadDescriptor.

        Used as discriminator.  # noqa: E501

        :param object_type: The object_type of this EventPayloadDescriptor.
        :type object_type: str
        """
        allowed_values = ["EVENT_PAYLOAD_DESCRIPTOR"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def payload_type(self) -> str:
        """Gets the payload_type of this EventPayloadDescriptor.

        Enumerated or private string signifying the nature of values.  # noqa: E501

        :return: The payload_type of this EventPayloadDescriptor.
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type: str):
        """Sets the payload_type of this EventPayloadDescriptor.

        Enumerated or private string signifying the nature of values.  # noqa: E501

        :param payload_type: The payload_type of this EventPayloadDescriptor.
        :type payload_type: str
        """
        if payload_type is None:
            raise ValueError("Invalid value for `payload_type`, must not be `None`")  # noqa: E501

        self._payload_type = payload_type

    @property
    def units(self) -> str:
        """Gets the units of this EventPayloadDescriptor.

        Units of measure.  # noqa: E501

        :return: The units of this EventPayloadDescriptor.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units: str):
        """Sets the units of this EventPayloadDescriptor.

        Units of measure.  # noqa: E501

        :param units: The units of this EventPayloadDescriptor.
        :type units: str
        """

        self._units = units

    @property
    def currency(self) -> str:
        """Gets the currency of this EventPayloadDescriptor.

        Currency of price payload.  # noqa: E501

        :return: The currency of this EventPayloadDescriptor.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this EventPayloadDescriptor.

        Currency of price payload.  # noqa: E501

        :param currency: The currency of this EventPayloadDescriptor.
        :type currency: str
        """

        self._currency = currency
