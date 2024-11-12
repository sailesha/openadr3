import connexion
import six

from swagger_server.models.object_id import ObjectID  # noqa: E501
from swagger_server.models.problem import Problem  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server import util

class Backend:
    programs: dict[str, Program]

    def __init__(self):
        self.programs = {}
    
    def get_program(self, program_id: str):
        return self.programs[program_id]

    def set_program(self, program: Program) -> Program:
        program.id = str(len(self.programs))
        self.programs[program.id] = program
        return program

    def delete_program(self, program_id: str) -> Program:
        program = self.programs[program_id]
        del self.programs[program_id]
        return program
    
    def update_program(self, program_id: str, program: Program) -> Program:
        self.programs[program_id] = program
        return program
    
    def search_all_programs(self, target_type=None, target_values=None, skip=None, limit=None) -> list[Program]:
        # TODO: Implement filtering
        return list(self.programs.values())


backend = Backend()


def create_program(body=None):  # noqa: E501
    """create a program

    Create a new program in the server. # noqa: E501

    :param body: program item to add.
    :type body: dict | bytes

    :rtype: Program
    """
    if connexion.request.is_json:
        body = Program.from_dict(connexion.request.get_json())  # noqa: E501

    return backend.set_program(body)


def delete_program(program_id):  # noqa: E501
    """delete a program

    Delete an existing program with the programID in path. # noqa: E501

    :param program_id: Object ID of the program object.
    :type program_id: dict | bytes

    :rtype: Program
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.delete_program(program_id)


def search_all_programs(target_type=None, target_values=None, skip=None, limit=None):  # noqa: E501
    """searches all programs

    List all programs known to the server. May filter results by targetType and targetValues as query params. Use skip and pagination query params to limit response size.  # noqa: E501

    :param target_type: Indicates targeting type, e.g. GROUP
    :type target_type: str
    :param target_values: List of target values, e.g. group names
    :type target_values: List[str]
    :param skip: number of records to skip for pagination.
    :type skip: int
    :param limit: maximum number of records to return.
    :type limit: int

    :rtype: List[Program]
    """
    return backend.search_all_programs(target_type, target_values, skip, limit)


def search_program_by_program_id(program_id):  # noqa: E501
    """searches programs by program ID

    Fetch the program specified by the programID in path.  # noqa: E501

    :param program_id: Object ID of the program object.
    :type program_id: dict | bytes

    :rtype: Program
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.get_program(program_id)


def update_program(program_id, body=None):  # noqa: E501
    """update a program

    Update an existing program with the programID in path. # noqa: E501

    :param program_id: Object ID of the program object.
    :type program_id: dict | bytes
    :param body: program item to update.
    :type body: dict | bytes

    :rtype: Program
    """
    if connexion.request.is_json:
        program_id = ObjectID.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = Program.from_dict(connexion.request.get_json())  # noqa: E501
    return backend.update_program(program_id, body)
