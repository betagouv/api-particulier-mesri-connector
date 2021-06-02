from flask_restplus import Resource
from connector.model import StudentSatusModel, parser
import connector.airtable_client as client

api = StudentSatusModel.api
_status = StudentSatusModel.status


@api.route("", strict_slashes=False)
@api.response(404, "Étudiant introuvable")
class StudentStatus(Resource):
    @api.doc("get_student")
    @api.expect(parser)
    @api.marshal_with(_status)
    def get(self):
        args = parser.parse_args()
        student = client.get_student(args["ine"])

        if not student:
            api.abort(404, "Étudiant introuvable")

        return student
