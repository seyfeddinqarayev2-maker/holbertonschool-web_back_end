#!/usr/bin/env python3
"""
This module contains a function that updates the topics of a school
document based on its name in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all documents with the given name, setting their 'topics' field.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set.

    Returns:
        dict: The result of the update operation.
    """
    result = mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
    return result.raw_result
