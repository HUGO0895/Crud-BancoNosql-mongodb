import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

cliente=pymongo.MongoClient(os.getenv("bdConect"),server_api=ServerApi('1'))

db=cliente["MercadoLivre"]