import connexion
import six

from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.report import Report  # noqa: E501
from swagger_server import util


class Backend:
    reports: dict[str, Report]

    def __init__(self):
        self.reports = {}

    def get_report(self, report_id: str):
        return self.reports[report_id]

    def set_report(self, report: Report) -> Report:
        report.id = str(len(self.reports))
        self.reports[report.id] = report
        return report

    def delete_report(self, report_id: str) -> Report:
        report = self.reports[report_id]
        del self.reports[report_id]
        return report

    def update_report(self, report_id: str, report: Report) -> Report:
        self.reports[report_id] = report
        return report

    def search_all_reports(self, program_id=None, event_id=None, client_name=None, skip=None, limit=None) -> list[Report]:
        # TODO: Implement filtering
        return list(self.reports.values())


backend = Backend()


def create_report(body=None):  # noqa: E501
    """add a report

    Create a new report in the server. # noqa: E501

    :param body: report item to add.
    :type body: dict | bytes

    :rtype: Report
    """
    if connexion.request.is_json:
        body = Report.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.set_report(body)


def delete_report(report_id):  # noqa: E501
    """delete a report

    Delete the report specified by the reportID in path. # noqa: E501

    :param report_id: object ID of a report.
    :type report_id: dict | bytes

    :rtype: Report
    """
    if connexion.request.is_json:
        report_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.delete_report(report_id)


def search_all_reports(program_id=None, event_id=None, client_name=None, skip=None, limit=None):  # noqa: E501
    """searches all reports

    List all reports known to the server. May filter results by programID, eventID,  and clientName as query param. Use skip and pagination query params to limit response size.  # noqa: E501

    :param program_id: filter results to reports with programID.
    :type program_id: dict | bytes
    :param event_id: filter results to reports with eventID.
    :type event_id: dict | bytes
    :param client_name: filter results to reports with clientName.
    :type client_name: str
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Report]
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        event_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.search_all_reports(program_id, event_id, client_name, skip, limit)


def search_reports_by_report_id(report_id):  # noqa: E501
    """searches reports by reportID

    Fetch the report specified by the reportID in path.  # noqa: E501

    :param report_id: object ID of a report.
    :type report_id: dict | bytes

    :rtype: Report
    """
    if connexion.request.is_json:
        report_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.get_report(report_id)


def update_report(report_id, body=None):  # noqa: E501
    """update a report

    Update the report specified by the reportID in path. # noqa: E501

    :param report_id: object ID of a report.
    :type report_id: dict | bytes
    :param body: Report item to update.
    :type body: dict | bytes

    :rtype: Report
    """
    if connexion.request.is_json:
        report_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Report.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_report(report_id, body)
