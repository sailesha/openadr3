# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.interval import Interval  # noqa: F401,E501
from swagger_server.models.interval_period import IntervalPeriod  # noqa: F401,E501
from swagger_server import util


class ReportResources(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, resource_name: str=None, interval_period: IntervalPeriod=None, intervals: List[Interval]=None):  # noqa: E501
        """ReportResources - a model defined in Swagger

        :param resource_name: The resource_name of this ReportResources.  # noqa: E501
        :type resource_name: str
        :param interval_period: The interval_period of this ReportResources.  # noqa: E501
        :type interval_period: IntervalPeriod
        :param intervals: The intervals of this ReportResources.  # noqa: E501
        :type intervals: List[Interval]
        """
        self.swagger_types = {
            'resource_name': str,
            'interval_period': IntervalPeriod,
            'intervals': List[Interval]
        }

        self.attribute_map = {
            'resource_name': 'resourceName',
            'interval_period': 'intervalPeriod',
            'intervals': 'intervals'
        }
        self._resource_name = resource_name
        self._interval_period = interval_period
        self._intervals = intervals

    @classmethod
    def from_dict(cls, dikt) -> 'ReportResources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The report_resources of this ReportResources.  # noqa: E501
        :rtype: ReportResources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_name(self) -> str:
        """Gets the resource_name of this ReportResources.

        User generated identifier. A value of AGGREGATED_REPORT indicates an aggregation of more that one resource's data  # noqa: E501

        :return: The resource_name of this ReportResources.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name: str):
        """Sets the resource_name of this ReportResources.

        User generated identifier. A value of AGGREGATED_REPORT indicates an aggregation of more that one resource's data  # noqa: E501

        :param resource_name: The resource_name of this ReportResources.
        :type resource_name: str
        """
        if resource_name is None:
            raise ValueError("Invalid value for `resource_name`, must not be `None`")  # noqa: E501

        self._resource_name = resource_name

    @property
    def interval_period(self) -> IntervalPeriod:
        """Gets the interval_period of this ReportResources.


        :return: The interval_period of this ReportResources.
        :rtype: IntervalPeriod
        """
        return self._interval_period

    @interval_period.setter
    def interval_period(self, interval_period: IntervalPeriod):
        """Sets the interval_period of this ReportResources.


        :param interval_period: The interval_period of this ReportResources.
        :type interval_period: IntervalPeriod
        """

        self._interval_period = interval_period

    @property
    def intervals(self) -> List[Interval]:
        """Gets the intervals of this ReportResources.

        A list of interval objects.  # noqa: E501

        :return: The intervals of this ReportResources.
        :rtype: List[Interval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals: List[Interval]):
        """Sets the intervals of this ReportResources.

        A list of interval objects.  # noqa: E501

        :param intervals: The intervals of this ReportResources.
        :type intervals: List[Interval]
        """
        if intervals is None:
            raise ValueError("Invalid value for `intervals`, must not be `None`")  # noqa: E501

        self._intervals = intervals