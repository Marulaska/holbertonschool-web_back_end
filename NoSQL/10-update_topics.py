#!/usr/bin/env python3
"""
update document
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    - mongo_collection: pymongo.collection.Collection, the MongoDB collection object
    - name: string, the name of the school to update
    - topics: list of strings, the list of topics approached in the school
    """
    mongo_collection.update_many(
        {'namea': name},
        {'$set': {'topics': topics}}
    )
