#!/usr/bin/env python3
"""
This module contains a function that inserts a new document
in a MongoDB collection based on keyword arguments.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        **kwargs: Key/value pairs representing the document fields.

    Returns:
        ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
