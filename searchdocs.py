def search_documents(query, filters=None):
    """
    Search documents in the Elasticsearch index with optional filters.
    
    :param query: The search query string.
    :param filters: A dictionary of filters (e.g., {"author": "Rezvi shah", "date": "2021"}).
    :return: A list of matching documents.
    """
    # Basic query for searching the text
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    }

    # Adding filters if any
    if filters:
        filter_clauses = []
        for field, value in filters.items():
            filter_clauses.append({"term": {field: value}})
        search_body["query"] = {
            "bool": {
                "must": search_body["query"],
                "filter": filter_clauses
            }
        }

    response = es.search(index="my-search-engine", body=search_body)
    return [hit["_source"] for hit in response['hits']['hits']]

# Example search without filters
print("Search results without filters:")
results = search_documents("AI")
for doc in results:
    print(doc)

# Example search with filters
print("\nSearch results with filters:")
filtered_results = search_documents("AI", filters={"author": "Jane Doe"})
for doc in filtered_results:
    print(doc)
