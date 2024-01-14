#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
        mongo_collection
        topic (_type_)
    """
    return list(mongo_collection.find({'topics': topic}))
