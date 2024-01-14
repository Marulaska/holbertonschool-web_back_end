#!/usr/bin/env python3
"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def print_stats():
    """_summary_
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(str(logs.count_documents({})) + " logs")
    print("\tmethod GET: " + str(logs.count_documents({"method": "GET"})))
    print("\tmethod POST: " + str(logs.count_documents({"method": "POST"})))
    print("\tmethod PUT: " + str(logs.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: " + str(logs.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: "
          + str(logs.count_documents({"method": "DELETE"})))
    print(str(logs.count_documents({"method": "GET", "path": "/status"}))
          + " status check")


if __name__ == "__main__":
    print_stats()
