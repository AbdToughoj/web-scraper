import requests
from bs4 import BeautifulSoup

URL= 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations)

def get_citations_needed_report(URL):
    URL= 'https://en.wikipedia.org/wiki/History_of_Mexico'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    with open ('citations_report.txt','w') as file:
        for citation in citations:
            paragraph = citation.find_parent("p").text.strip()
            file.write(f"{paragraph}\n")
            file.write("\n")
            file.write("\n")

                   
print("citations count =", get_citations_needed_count(URL))
get_citations_needed_report(URL)