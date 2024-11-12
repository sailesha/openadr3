# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.report import Report  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReportsController(BaseTestCase):
    """ReportsController integration test stubs"""

    def test_create_report(self):
        """Test case for create_report

        add a report
        """
        body = Report()
        response = self.client.open(
            '/openadr3/3.0.1/reports',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_report(self):
        """Test case for delete_report

        delete a report
        """
        response = self.client.open(
            '/openadr3/3.0.1/reports/{reportID}'.format(report_id=ObjectID()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_all_reports(self):
        """Test case for search_all_reports

        searches all reports
        """
        query_string = [('program_id', ObjectID()),
                        ('event_id', ObjectID()),
                        ('client_name', 'client_name_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/openadr3/3.0.1/reports',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_reports_by_report_id(self):
        """Test case for search_reports_by_report_id

        searches reports by reportID
        """
        response = self.client.open(
            '/openadr3/3.0.1/reports/{reportID}'.format(report_id=ObjectID()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_report(self):
        """Test case for update_report

        update a report
        """
        body = Report()
        response = self.client.open(
            '/openadr3/3.0.1/reports/{reportID}'.format(report_id=ObjectID()),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
