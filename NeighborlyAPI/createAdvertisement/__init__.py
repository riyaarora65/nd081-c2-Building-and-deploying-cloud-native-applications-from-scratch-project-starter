import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighbourlydb:5jDADX7YX11L3Klw7Td7aq7McOaoq08cUR5eDSSJp3C10gpW5lmKsH1x8snfliJRy0VUML2j4gfYMOmv3WEEDQ==@neighbourlydb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@neighbourlydb@"
            client = pymongo.MongoClient(url)
            database = client['udacity-mongodb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )