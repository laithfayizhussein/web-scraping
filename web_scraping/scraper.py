import requests
from bs4 import BeautifulSoup
ancor = 'a'
def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup( response.content, 'html.parser')
    all_a = soup.find_all (ancor , { "title" : "Wikipedia:Citation needed"})
    return len(all_a)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup( response.content, 'html.parser')
    find_p = soup.find_all('p')
    paragraph = []
    for all_p in find_p :
        para_c = all_p.find(ancor ,{ "title" : "Wikipedia:Citation needed"})
        if para_c:
            paragraph.append(all_p.text.format())
    return paragraph

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))