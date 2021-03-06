import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_job(word):
    URL = f"https://stackoverflow.com/jobs?r=true&q={word}"
    html = requests.get(URL,headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    pagination = soup.find('div', {"class": "s-pagination"})
    last_page=0
    if pagination:
        pages = pagination.find_all("a")
        last_page = len(pages) - 1
    so_job = []
    for p in range(last_page):
        page_num = p + 1
        url = f"https://stackoverflow.com/jobs?q={word}&r=true&pg={page_num}"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        listResults = soup.find("div", {"class": "listResults"})
        jobs = listResults.find_all("div", {"class": "-job"})
        for job in jobs:
            link = job.find('a', {"class": "s-link"})['href']
            title = job.find('a', {"class": "s-link"})['title']
            company = job.find('h3').find('span').string
            so_job.append({'title': title, 'company': company, 'link': f"https://stackoverflow.com{link}"})

    return so_job
