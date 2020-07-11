import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighbourlydb:5jDADX7YX11L3Klw7Td7aq7McOaoq08cUR5eDSSJp3C10gpW5lmKsH1x8snfliJRy0VUML2j4gfYMOmv3WEEDQ==@neighbourlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighbourlydb@"
            client = pymongo.MongoClient(url)
            database = client['udacity-mongodb']
            collection = database['posts']

            # query = {'_id': ObjectId(id)} # THIS LINE OF CODE IS NOT WORKING SO COMMENTING IT OUT
            query = {'_id': id}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)