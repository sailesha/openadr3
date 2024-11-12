# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.duration import Duration  # noqa: F401,E501
from swagger_server.models.model_date_time import ModelDateTime  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class IntervalPeriod(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, start: ModelDateTime=None, duration: Duration=None, randomize_start: Duration=None):  # noqa: E501
        """IntervalPeriod - a model defined in Swagger

        :param start: The start of this IntervalPeriod.  # noqa: E501
        :type start: ModelDateTime
        :param duration: The duration of this IntervalPeriod.  # noqa: E501
        :type duration: Duration
        :param randomize_start: The randomize_start of this IntervalPeriod.  # noqa: E501
        :type randomize_start: Duration
        """
        self.swagger_types = {
            'start': ModelDateTime,
            'duration': Duration,
            'randomize_start': Duration
        }

        self.attribute_map = {
            'start': 'start',
            'duration': 'duration',
            'randomize_start': 'randomizeStart'
        }
        self._start = start
        self._duration = duration
        self._randomize_start = randomize_start

    @classmethod
    def from_dict(cls, dikt) -> 'IntervalPeriod':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The intervalPeriod of this IntervalPeriod.  # noqa: E501
        :rtype: IntervalPeriod
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> ModelDateTime:
        """Gets the start of this IntervalPeriod.


        :return: The start of this IntervalPeriod.
        :rtype: ModelDateTime
        """
        return self._start

    @start.setter
    def start(self, start: ModelDateTime):
        """Sets the start of this IntervalPeriod.


        :param start: The start of this IntervalPeriod.
        :type start: ModelDateTime
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def duration(self) -> Duration:
        """Gets the duration of this IntervalPeriod.


        :return: The duration of this IntervalPeriod.
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration: Duration):
        """Sets the duration of this IntervalPeriod.


        :param duration: The duration of this IntervalPeriod.
        :type duration: Duration
        """

        self._duration = duration

    @property
    def randomize_start(self) -> Duration:
        """Gets the randomize_start of this IntervalPeriod.


        :return: The randomize_start of this IntervalPeriod.
        :rtype: Duration
        """
        return self._randomize_start

    @randomize_start.setter
    def randomize_start(self, randomize_start: Duration):
        """Sets the randomize_start of this IntervalPeriod.


        :param randomize_start: The randomize_start of this IntervalPeriod.
        :type randomize_start: Duration
        """

        self._randomize_start = randomize_start