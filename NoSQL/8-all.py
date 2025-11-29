/usr/bin/python3

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.

    Returns:
        list: List of all documents in the collection. Returns an empty list if none.
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
