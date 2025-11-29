#!/usr/bin/env python3
"""
This module contains a function that returns a list of schools
having a specific topic in their 'topics' field.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns all documents in the collection that have the given topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: List of documents containing the specified topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
