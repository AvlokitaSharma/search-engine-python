import requests
from bs4 import BeautifulSoup

def crawl_academic_papers(start_url, max_pages):
    urls_to_crawl = [start_url]
    crawled_urls = set()
    papers = []

    while urls_to_crawl and len(papers) < max_pages:
        current_url = urls_to_crawl.pop(0)
        if current_url in crawled_urls:
            continue

        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for paper in soup.find_all("div", class_="paper-details"):
            title = paper.find("h2").text
            abstract = paper.find("p", class_="abstract").text
            papers.append({"title": title, "abstract": abstract})

        # Find links to other papers (simplified)
        for link in soup.find_all("a"):
            href = link.get("href")
            if href not in crawled_urls:
                urls_to_crawl.append(href)

        crawled_urls.add(current_url)

    return papers

# Example usage
start_url = 'http://avlokitasharma/papers/prof'
papers = crawl_academic_papers(start_url, 100)
