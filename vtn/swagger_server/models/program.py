# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.duration import Duration  # noqa: F401,E501
from swagger_server.models.interval_period import IntervalPeriod  # noqa: F401,E501
from swagger_server.models.model_date_time import ModelDateTime  # noqa: F401,E501
from swagger_server.models.object_id import ObjectID  # noqa: F401,E501
from swagger_server.models.program_program_descriptions import ProgramProgramDescriptions  # noqa: F401,E501
from swagger_server.models.values_map import ValuesMap  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server.models.any_ofprogram_payload_descriptors_items import AnyOfprogramPayloadDescriptorsItems  # noqa: F401,E501
from swagger_server import util


class Program(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: ObjectID=None, created_date_time: ModelDateTime=None, modification_date_time: ModelDateTime=None, object_type: str=None, program_name: str=None, program_long_name: str=None, retailer_name: str=None, retailer_long_name: str=None, program_type: str=None, country: str=None, principal_subdivision: str=None, time_zone_offset: Duration=None, interval_period: IntervalPeriod=None, program_descriptions: List[ProgramProgramDescriptions]=None, binding_events: bool=None, local_price: bool=None, payload_descriptors: List[AnyOfprogramPayloadDescriptorsItems]=None, targets: List[ValuesMap]=None):  # noqa: E501
        """Program - a model defined in Swagger

        :param id: The id of this Program.  # noqa: E501
        :type id: ObjectID
        :param created_date_time: The created_date_time of this Program.  # noqa: E501
        :type created_date_time: ModelDateTime
        :param modification_date_time: The modification_date_time of this Program.  # noqa: E501
        :type modification_date_time: ModelDateTime
        :param object_type: The object_type of this Program.  # noqa: E501
        :type object_type: str
        :param program_name: The program_name of this Program.  # noqa: E501
        :type program_name: str
        :param program_long_name: The program_long_name of this Program.  # noqa: E501
        :type program_long_name: str
        :param retailer_name: The retailer_name of this Program.  # noqa: E501
        :type retailer_name: str
        :param retailer_long_name: The retailer_long_name of this Program.  # noqa: E501
        :type retailer_long_name: str
        :param program_type: The program_type of this Program.  # noqa: E501
        :type program_type: str
        :param country: The country of this Program.  # noqa: E501
        :type country: str
        :param principal_subdivision: The principal_subdivision of this Program.  # noqa: E501
        :type principal_subdivision: str
        :param time_zone_offset: The time_zone_offset of this Program.  # noqa: E501
        :type time_zone_offset: Duration
        :param interval_period: The interval_period of this Program.  # noqa: E501
        :type interval_period: IntervalPeriod
        :param program_descriptions: The program_descriptions of this Program.  # noqa: E501
        :type program_descriptions: List[ProgramProgramDescriptions]
        :param binding_events: The binding_events of this Program.  # noqa: E501
        :type binding_events: bool
        :param local_price: The local_price of this Program.  # noqa: E501
        :type local_price: bool
        :param payload_descriptors: The payload_descriptors of this Program.  # noqa: E501
        :type payload_descriptors: List[AnyOfprogramPayloadDescriptorsItems]
        :param targets: The targets of this Program.  # noqa: E501
        :type targets: List[ValuesMap]
        """
        self.swagger_types = {
            'id': ObjectID,
            'created_date_time': ModelDateTime,
            'modification_date_time': ModelDateTime,
            'object_type': str,
            'program_name': str,
            'program_long_name': str,
            'retailer_name': str,
            'retailer_long_name': str,
            'program_type': str,
            'country': str,
            'principal_subdivision': str,
            'time_zone_offset': Duration,
            'interval_period': IntervalPeriod,
            'program_descriptions': List[ProgramProgramDescriptions],
            'binding_events': bool,
            'local_price': bool,
            'payload_descriptors': List[AnyOfprogramPayloadDescriptorsItems],
            'targets': List[ValuesMap]
        }

        self.attribute_map = {
            'id': 'id',
            'created_date_time': 'createdDateTime',
            'modification_date_time': 'modificationDateTime',
            'object_type': 'objectType',
            'program_name': 'programName',
            'program_long_name': 'programLongName',
            'retailer_name': 'retailerName',
            'retailer_long_name': 'retailerLongName',
            'program_type': 'programType',
            'country': 'country',
            'principal_subdivision': 'principalSubdivision',
            'time_zone_offset': 'timeZoneOffset',
            'interval_period': 'intervalPeriod',
            'program_descriptions': 'programDescriptions',
            'binding_events': 'bindingEvents',
            'local_price': 'localPrice',
            'payload_descriptors': 'payloadDescriptors',
            'targets': 'targets'
        }
        self._id = id
        self._created_date_time = created_date_time
        self._modification_date_time = modification_date_time
        self._object_type = object_type
        self._program_name = program_name
        self._program_long_name = program_long_name
        self._retailer_name = retailer_name
        self._retailer_long_name = retailer_long_name
        self._program_type = program_type
        self._country = country
        self._principal_subdivision = principal_subdivision
        self._time_zone_offset = time_zone_offset
        self._interval_period = interval_period
        self._program_descriptions = program_descriptions
        self._binding_events = binding_events
        self._local_price = local_price
        self._payload_descriptors = payload_descriptors
        self._targets = targets

    @classmethod
    def from_dict(cls, dikt) -> 'Program':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The program of this Program.  # noqa: E501
        :rtype: Program
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ObjectID:
        """Gets the id of this Program.


        :return: The id of this Program.
        :rtype: ObjectID
        """
        return self._id

    @id.setter
    def id(self, id: ObjectID):
        """Sets the id of this Program.


        :param id: The id of this Program.
        :type id: ObjectID
        """

        self._id = id

    @property
    def created_date_time(self) -> ModelDateTime:
        """Gets the created_date_time of this Program.


        :return: The created_date_time of this Program.
        :rtype: ModelDateTime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time: ModelDateTime):
        """Sets the created_date_time of this Program.


        :param created_date_time: The created_date_time of this Program.
        :type created_date_time: ModelDateTime
        """

        self._created_date_time = created_date_time

    @property
    def modification_date_time(self) -> ModelDateTime:
        """Gets the modification_date_time of this Program.


        :return: The modification_date_time of this Program.
        :rtype: ModelDateTime
        """
        return self._modification_date_time

    @modification_date_time.setter
    def modification_date_time(self, modification_date_time: ModelDateTime):
        """Sets the modification_date_time of this Program.


        :param modification_date_time: The modification_date_time of this Program.
        :type modification_date_time: ModelDateTime
        """

        self._modification_date_time = modification_date_time

    @property
    def object_type(self) -> str:
        """Gets the object_type of this Program.

        Used as discriminator  # noqa: E501

        :return: The object_type of this Program.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """Sets the object_type of this Program.

        Used as discriminator  # noqa: E501

        :param object_type: The object_type of this Program.
        :type object_type: str
        """
        allowed_values = ["PROGRAM"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def program_name(self) -> str:
        """Gets the program_name of this Program.

        Short name to uniquely identify program.  # noqa: E501

        :return: The program_name of this Program.
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name: str):
        """Sets the program_name of this Program.

        Short name to uniquely identify program.  # noqa: E501

        :param program_name: The program_name of this Program.
        :type program_name: str
        """
        if program_name is None:
            raise ValueError("Invalid value for `program_name`, must not be `None`")  # noqa: E501

        self._program_name = program_name

    @property
    def program_long_name(self) -> str:
        """Gets the program_long_name of this Program.

        Long name of program for human readability.  # noqa: E501

        :return: The program_long_name of this Program.
        :rtype: str
        """
        return self._program_long_name

    @program_long_name.setter
    def program_long_name(self, program_long_name: str):
        """Sets the program_long_name of this Program.

        Long name of program for human readability.  # noqa: E501

        :param program_long_name: The program_long_name of this Program.
        :type program_long_name: str
        """

        self._program_long_name = program_long_name

    @property
    def retailer_name(self) -> str:
        """Gets the retailer_name of this Program.

        Short name of energy retailer providing the program.  # noqa: E501

        :return: The retailer_name of this Program.
        :rtype: str
        """
        return self._retailer_name

    @retailer_name.setter
    def retailer_name(self, retailer_name: str):
        """Sets the retailer_name of this Program.

        Short name of energy retailer providing the program.  # noqa: E501

        :param retailer_name: The retailer_name of this Program.
        :type retailer_name: str
        """

        self._retailer_name = retailer_name

    @property
    def retailer_long_name(self) -> str:
        """Gets the retailer_long_name of this Program.

        Long name of energy retailer for human readability.  # noqa: E501

        :return: The retailer_long_name of this Program.
        :rtype: str
        """
        return self._retailer_long_name

    @retailer_long_name.setter
    def retailer_long_name(self, retailer_long_name: str):
        """Sets the retailer_long_name of this Program.

        Long name of energy retailer for human readability.  # noqa: E501

        :param retailer_long_name: The retailer_long_name of this Program.
        :type retailer_long_name: str
        """

        self._retailer_long_name = retailer_long_name

    @property
    def program_type(self) -> str:
        """Gets the program_type of this Program.

        A program defined categorization.  # noqa: E501

        :return: The program_type of this Program.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type: str):
        """Sets the program_type of this Program.

        A program defined categorization.  # noqa: E501

        :param program_type: The program_type of this Program.
        :type program_type: str
        """

        self._program_type = program_type

    @property
    def country(self) -> str:
        """Gets the country of this Program.

        Alpha-2 code per ISO 3166-1.  # noqa: E501

        :return: The country of this Program.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this Program.

        Alpha-2 code per ISO 3166-1.  # noqa: E501

        :param country: The country of this Program.
        :type country: str
        """

        self._country = country

    @property
    def principal_subdivision(self) -> str:
        """Gets the principal_subdivision of this Program.

        Coding per ISO 3166-2. E.g. state in US.  # noqa: E501

        :return: The principal_subdivision of this Program.
        :rtype: str
        """
        return self._principal_subdivision

    @principal_subdivision.setter
    def principal_subdivision(self, principal_subdivision: str):
        """Sets the principal_subdivision of this Program.

        Coding per ISO 3166-2. E.g. state in US.  # noqa: E501

        :param principal_subdivision: The principal_subdivision of this Program.
        :type principal_subdivision: str
        """

        self._principal_subdivision = principal_subdivision

    @property
    def time_zone_offset(self) -> Duration:
        """Gets the time_zone_offset of this Program.


        :return: The time_zone_offset of this Program.
        :rtype: Duration
        """
        return self._time_zone_offset

    @time_zone_offset.setter
    def time_zone_offset(self, time_zone_offset: Duration):
        """Sets the time_zone_offset of this Program.


        :param time_zone_offset: The time_zone_offset of this Program.
        :type time_zone_offset: Duration
        """

        self._time_zone_offset = time_zone_offset

    @property
    def interval_period(self) -> IntervalPeriod:
        """Gets the interval_period of this Program.


        :return: The interval_period of this Program.
        :rtype: IntervalPeriod
        """
        return self._interval_period

    @interval_period.setter
    def interval_period(self, interval_period: IntervalPeriod):
        """Sets the interval_period of this Program.


        :param interval_period: The interval_period of this Program.
        :type interval_period: IntervalPeriod
        """

        self._interval_period = interval_period

    @property
    def program_descriptions(self) -> List[ProgramProgramDescriptions]:
        """Gets the program_descriptions of this Program.

        A list of programDescriptions  # noqa: E501

        :return: The program_descriptions of this Program.
        :rtype: List[ProgramProgramDescriptions]
        """
        return self._program_descriptions

    @program_descriptions.setter
    def program_descriptions(self, program_descriptions: List[ProgramProgramDescriptions]):
        """Sets the program_descriptions of this Program.

        A list of programDescriptions  # noqa: E501

        :param program_descriptions: The program_descriptions of this Program.
        :type program_descriptions: List[ProgramProgramDescriptions]
        """

        self._program_descriptions = program_descriptions

    @property
    def binding_events(self) -> bool:
        """Gets the binding_events of this Program.

        True if events are fixed once transmitted.  # noqa: E501

        :return: The binding_events of this Program.
        :rtype: bool
        """
        return self._binding_events

    @binding_events.setter
    def binding_events(self, binding_events: bool):
        """Sets the binding_events of this Program.

        True if events are fixed once transmitted.  # noqa: E501

        :param binding_events: The binding_events of this Program.
        :type binding_events: bool
        """

        self._binding_events = binding_events

    @property
    def local_price(self) -> bool:
        """Gets the local_price of this Program.

        True if events have been adapted from a grid event.  # noqa: E501

        :return: The local_price of this Program.
        :rtype: bool
        """
        return self._local_price

    @local_price.setter
    def local_price(self, local_price: bool):
        """Sets the local_price of this Program.

        True if events have been adapted from a grid event.  # noqa: E501

        :param local_price: The local_price of this Program.
        :type local_price: bool
        """

        self._local_price = local_price

    @property
    def payload_descriptors(self) -> List[AnyOfprogramPayloadDescriptorsItems]:
        """Gets the payload_descriptors of this Program.

        A list of payloadDescriptors.  # noqa: E501

        :return: The payload_descriptors of this Program.
        :rtype: List[AnyOfprogramPayloadDescriptorsItems]
        """
        return self._payload_descriptors

    @payload_descriptors.setter
    def payload_descriptors(self, payload_descriptors: List[AnyOfprogramPayloadDescriptorsItems]):
        """Sets the payload_descriptors of this Program.

        A list of payloadDescriptors.  # noqa: E501

        :param payload_descriptors: The payload_descriptors of this Program.
        :type payload_descriptors: List[AnyOfprogramPayloadDescriptorsItems]
        """

        self._payload_descriptors = payload_descriptors

    @property
    def targets(self) -> List[ValuesMap]:
        """Gets the targets of this Program.

        A list of valuesMap objects.  # noqa: E501

        :return: The targets of this Program.
        :rtype: List[ValuesMap]
        """
        return self._targets

    @targets.setter
    def targets(self, targets: List[ValuesMap]):
        """Sets the targets of this Program.

        A list of valuesMap objects.  # noqa: E501

        :param targets: The targets of this Program.
        :type targets: List[ValuesMap]
        """

        self._targets = targets