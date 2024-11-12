import connexion
import six

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server import util


class Backend:
    events: dict[str, Event]

    def __init__(self):
        self.events = {}
    
    def get_event(self, event_id: str):
        return self.events[event_id]
    
    def set_event(self, event: Event) -> Event:
        event.id = str(len(self.events))
        self.events[event.id] = event
        return event
    
    def delete_event(self, event_id: str) -> Event:
        event = self.events[event_id]
        del self.events[event_id]
        return event
    
    def update_event(self, event_id: str, event: Event) -> Event:
        self.events[event_id] = event
        return event
    
    def search_all_events(self, program_id=None, target_type=None, target_values=None, skip=None, limit=None) -> list[Event]:
        # TODO: Implement filtering
        return list(self.events.values())


backend = Backend()


def create_event(body=None):  # noqa: E501
    """create an event

    Create a new event in the server. # noqa: E501

    :param body: Event item to add.
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.set_event(body)


def delete_event(event_id):  # noqa: E501
    """delete an event

    Delete the event specified by the eventID in path.  # noqa: E501

    :param event_id: object ID of event.
    :type event_id: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        event_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.delete_event(event_id)


def search_all_events(program_id=None, target_type=None, target_values=None, skip=None, limit=None):  # noqa: E501
    """searches all events

    List all events known to the server. May filter results by programID query param. May filter results by targetType and targetValues as query params. Use skip and pagination query params to limit response size.  # noqa: E501

    :param program_id: filter results to events with programID.
    :type program_id: dict | bytes
    :param target_type: Indicates targeting type, e.g. GROUP
    :type target_type: str
    :param target_values: List of target values, e.g. group names
    :type target_values: List[str]
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Event]
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.search_all_events(program_id, target_type, target_values, skip, limit)


def search_events_by_id(event_id):  # noqa: E501
    """search events by ID

    Fetch event associated with the eventID in path.  # noqa: E501

    :param event_id: object ID of event.
    :type event_id: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        event_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.get_event(event_id)


def update_event(event_id, body=None):  # noqa: E501
    """update an event

    Update the event specified by the eventID in path. # noqa: E501

    :param event_id: object ID of event.
    :type event_id: dict | bytes
    :param body: event item to update.
    :type body: dict | bytes

    :rtype: Event
    """
    if connexion.request.is_json:
        event_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_event(event_id, body)
