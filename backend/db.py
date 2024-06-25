# from models.chatbot import Query
import pymongo
import var
import streamlit as st

COSMOS_MONGO_USER = st.secrets["COSMOS_MONGO_USER"]
COSMOS_MONGO_PWD = st.secrets["COSMOS_MONGO_PWD"]
COSMOS_MONGO_SERVER = st.secrets["COSMOS_MONGO_SERVER"]

mongo_conn = "mongodb+srv://"+ COSMOS_MONGO_USER+ ":"+ COSMOS_MONGO_PWD+ "@"+ COSMOS_MONGO_SERVER

mongo_client = pymongo.MongoClient(mongo_conn)
db = mongo_client["azure"]


def get_azure_collection():
    COLLECTION_NAME = "azure_collection"
    collection = db[COLLECTION_NAME]
    return collection


# def create(query: Query):
#     db["queries"].insert_one(query)


# def response_get(qryID: int):
#     db["queries"].find_one()
