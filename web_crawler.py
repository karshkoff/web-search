from bs4 import BeautifulSoup as BeaSoup
import requests
import urllib

def continue_crawl(search_history, next_url, max_len = 25):
    ''' Checking the input list
    search_history: list urls
    next_url: current url
    '''

    if next_url in search_history:
        print('URL has already found {}'.format(next_url))
        return False
    elif len(search_history) > max_len:
        print('Search history list cannot be more 25 links')
        return False
    return True

def find_next_link(next_url):
    ''' Finding a first link in mw-content-text
    next_url: current url
    '''
    # Get html text
    response = requests.get(next_url)
    html = response.text
    soup = BeaSoup(html, 'html.parser')

    # Find first link
    first_link = ''
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_link = element.find("a", recursive=False).get('href')
            break

    if not first_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)

    return first_link

next_url = 'https://en.wikipedia.org/wiki/Motocross'
search_history = []

# Checking conditionals:
# - next url has't already found (cycle)
# - element count don't equal 25
while continue_crawl(search_history, next_url):
    #Find next link in html
    print(next_url)
    search_history.append(next_url)
    next_url = find_next_link(next_url)

print("Searching is done:")
