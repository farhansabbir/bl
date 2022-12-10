import pymongo

db = pymongo.MongoClient("mongodb+srv://root:Hello123@bhalobashacluster0.rcfzj.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)

client = db["banglalink"]
try:
    client.create_collection("data")
except Exception as e:
    print(e)

