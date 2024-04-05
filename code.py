from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Sample documents
documents = [
    {"id": 1, "title": "The impact of AI on society", "content": "Exploring the effects of artificial intelligence on social structures.", "date": "2021-01-01", "author": "Jane Doe"},
    {"id": 2, "title": "Introduction to Machine Learning", "content": "A beginner's guide to machine learning concepts.", "date": "2021-02-15", "author": "John Smith"},
    # Add more documents as needed
]

# Indexing documents
for doc in documents:
    es.index(index="my-search-engine", id=doc["id"], document=doc)



documents = [
    {"id": 1, "title": "The impact of AI on society", "content": "Exploring the effects of artificial intelligence on social structures.", "date": "2021-01-01", "author": "Jane Doe"},
    {"id": 2, "title": "Introduction to Machine Learning", "content": "A beginner's guide to machine learning concepts.", "date": "2021-02-15", "author": "John Smith"},
    {"id": 3, "title": "Advances in Distributed Systems", "content": "A comprehensive review of recent developments in distributed computing.", "date": "2021-03-22", "author": "Alice Johnson"},
    # More documents were added here, but are not shown because of security reasons
]
