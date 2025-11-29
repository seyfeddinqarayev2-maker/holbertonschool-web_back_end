#!/usr/bin/env python3
"""
This module contains a function that lists all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: List of all documents in the collection. Returns an empty list if none.
    """
    return list(mongo_collection.find())
