import requests
from bs4 import BeautifulSoup

# 1.1) Write a function to Get and parse HTML content from a Wikipedia page
def get_wikipedia_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# 1.2) Write a function to Extract article title
def extract_article_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', {'class': 'firstHeading'}).text
    return title

# 1.3) Write a function to Extract article text for each paragraph with their respective headings
def extract_article_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    article_content = {}
    headings = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
    
    for heading in headings:
        heading_text = heading.text
        paragraphs = []
        next_element = heading.find_next_sibling()
        
        while next_element and next_element.name not in ['h2', 'h3', 'h4', 'h5', 'h6']:
            if next_element.name == 'p':
                paragraphs.append(next_element.text)
            next_element = next_element.find_next_sibling()
        
        article_content[heading_text] = '\n'.join(paragraphs)
    
    return article_content

# 1.4) Write a function to collect every link that redirects to another Wikipedia page
def extract_internal_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    internal_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/'):
            internal_links.append(href)
    return internal_links

# 1.5) Wrap all the previous functions into a single function that takes a Wikipedia link
def scrape_wikipedia_page(url):
    html = get_wikipedia_html(url)
    if html:
        title = extract_article_title(html)
        content = extract_article_content(html)
        links = extract_internal_links(html)
        return {'title': title, 'content': content, 'links': links}
    else:
        return None

# 1.6) Test the last function on a Wikipedia page of your choice
if __name__ == "__main__":
    wikipedia_url = 'https://en.wikipedia.org/wiki/Web_scraping'
    scraped_data = scrape_wikipedia_page(wikipedia_url)
    if scraped_data:
        print("Title:", scraped_data['title'])
        print("Content:")
        for heading, paragraph in scraped_data['content'].items():
            print(f"--- {heading} ---\n{paragraph}\n")
        print("Internal Links:")
        for link in scraped_data['links']:
            print(link)
    else:
        print("Failed to retrieve data from the Wikipedia page.")
