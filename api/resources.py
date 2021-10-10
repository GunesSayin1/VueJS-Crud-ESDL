from flask_restful import Resource, reqparse
from models import ESDLs
import base64
import json
import xmltodict
parser = reqparse.RequestParser()
parser.add_argument('title', help = 'This field cannot be blank', required = True)
parser.add_argument('description', help = 'This field cannot be blank', required = True)
parser.add_argument('published', help = 'This field cannot be blank', required = False)
parser.add_argument('file',help="This",required=False)

def XML_to_JSON(file):
    decoded=base64.b64decode(file)
    data = xmltodict.parse(decoded)
    json_data = json.dumps(data)
    encodedBytes = base64.b64encode(json_data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def published_boolean(status):
    if status == "True":
        return True
    else:
        return False

class ESDL(Resource):

    def get(self):
       return ESDLs.return_all()

    def post(self):
        data = parser.parse_args()
        new_ESDL = ESDLs(
            title = data["title"],
            description = data["description"],
            esdl_file=XML_to_JSON(data["file"])
        )
        try:
            new_ESDL.save_to_db()
            return {
                "message":"ESDL {} was created.".format(data["title"])
            }
        except:
            return{"message":"Something went wrong"},500

    def delete(self):
        return ESDLs.delete_all()

class IdESDL(Resource):
    def get(self,id):
        try:
            return ESDLs.return_id(id)
        except:
            return {"message":"Sth went wrong"}

    def put(self,id):
        data = parser.parse_args()
        ESDLs.update_id(id,data["title"],data["description"],published_boolean(data["published"]))
        return {'message': 'ESDL {} has been updated'.format(id)}

    def delete(self,id):
        ESDLs.delete_id(id)
        return {'message': 'ESDL {} has been deleted'.format(id)}

class Published(Resource):
    def get(self):
        return ESDLs.find_published()
