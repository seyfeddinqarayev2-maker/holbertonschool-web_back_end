#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
