from pymongo import MongoClient
import os

db_name = os.environ.get('DB_NAME', 'app_db')
request_colletion = os.environ.get('R_COLL', 'requests')
mongo_URI = os.environ.get("MONGO_URI", 'mongodb://localhost:27017')


class MongoConnection:

    _client = None
    _requests = None

    @classmethod
    def _connect_to_mongodb(cls):
        client = MongoClient(mongo_URI)
        cls._client = client

    def _get_database(self):
        if MongoConnection._client is None:
            self._connect_to_mongodb()
        db = MongoConnection._client[db_name]
        return db

    def _create_request_collection(self):
        if MongoConnection._requests is None:
            database = self._get_database()
            MongoConnection._requests = database[request_colletion]

    def get_request_collection(self):
        self._create_request_collection()
        return MongoConnection._requests
