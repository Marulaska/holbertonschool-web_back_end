#!/usr/bin/env python3
"""
insert a document in python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        Parameters:
    - mongo_collection: pymongo.collection.Collection, the MongoDB collection object
    - **kwargs: Keyword arguments representing the fields and values of the new document

    Returns:
    - ObjectId: The _id of the newly inserted document
    """
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
