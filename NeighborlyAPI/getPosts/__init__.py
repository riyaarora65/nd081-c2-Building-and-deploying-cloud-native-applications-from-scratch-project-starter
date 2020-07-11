import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighbourlydb:5jDADX7YX11L3Klw7Td7aq7McOaoq08cUR5eDSSJp3C10gpW5lmKsH1x8snfliJRy0VUML2j4gfYMOmv3WEEDQ==@neighbourlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighbourlydb@"
        client = pymongo.MongoClient(url)
        database = client['udacity-mongodb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)