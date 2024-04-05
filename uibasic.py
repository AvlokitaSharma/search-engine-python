def display_search_ui():
    while True:
        query = input("Enter your search query or 'exit' to quit: ")
        if query == 'exit':
            break
        results = search_papers(query)
        for result in results:
            print(f"Title: {result['title']}\nAbstract: {result['abstract']}\n\n")

display_search_ui()
