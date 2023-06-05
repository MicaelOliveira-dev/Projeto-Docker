from pymongo import MongoClient
import os

mongo_host = os.environ.get('MONGO_HOST')
mongo_port = int(os.environ.get('MONGO_PORT'))

conn = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')