from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Assuming 'papers' is a list of dictionaries with titles and abstracts from the crawler
paper_texts = [paper['title'] + ' ' + paper['abstract'] for paper in papers]
vectorizer = TfidfVectorizer()
paper_vectors = vectorizer.fit_transform(paper_texts)

def search_papers(query):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, paper_vectors)
    matched_indices = similarities.argsort()[0][-5:][::-1]  # Top 5 matches
    return [papers[i] for i in matched_indices]

# Example search
search_results = search_papers("machine learning in medical diagnosis")
