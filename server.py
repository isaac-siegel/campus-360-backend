from flask import Flask, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient('mongodb://backend:password@ds155727.mlab.com:55727/campus-360')
db = client['campus-360']
schools_coll = db['schools']
spheres_coll = db['spheres']


@app.route("/get_schools/", methods=['GET'])
def get_schools():
    thing = schools_coll.find({},{"_id": 1, "name": 1})

    return dumps(thing)

@app.route("/get_spheres/", methods=['GET'])
def get_spheres():
    school_id = request.args.get('school_id')

    spheres = list(spheres_coll.find({'school_id': ObjectId(school_id)}))
    print(spheres)
    return dumps(spheres)

@app.route("/get_favorites/", methods=['GET'])
def get_favorites():
    sphere_ids = request.args.getlist('sphere_ids')

    sphere_ids = map(lambda id: ObjectId(id), sphere_ids)

    spheres = list(spheres_coll.find({'_id': {'$in': sphere_ids} }))

    print(spheres)
    return dumps(spheres)


@app.route("/test/", methods=['GET'])
def test():
    return "hello world"

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0')


