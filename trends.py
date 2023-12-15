import requests
from bs4 import BeautifulSoup

BASE_TRENDING_URL = 'https://github.com/trending'
POSSIBLE_TRENDING_VALUES = ['daily', 'weekly', 'monthly']


def fetch_trending_page(since='daily'):
    if since.lower() == 'daily':
        url = BASE_TRENDING_URL
    else: # in a future it can be language-specific url
        if since.lower() not in POSSIBLE_TRENDING_VALUES:
            url = BASE_TRENDING_URL
        else:
            url = BASE_TRENDING_URL + '?since=' + since.lower()
    response = requests.get(url)
    response.raise_for_status()  # Check if request was successful
    return response.text


def parse_trending_repos(html):
    soup = BeautifulSoup(html, 'html.parser')
    repo_elements = soup.select('.Box-row')
    trending_repos = []

    for repo in repo_elements:
        stars_text = repo.select_one('.float-sm-right').text.replace(
            '\n', '').strip() if repo.select_one('.float-sm-right') else None
        stars_per_day = int(stars_text.split()[0].replace(
            ',', '')) if stars_text else None
        repo_info = {
            'owner': repo.select_one('.h3.lh-condensed').text.replace('\n', '').strip().split('/')[0].strip(),
            'name': repo.select_one('.h3.lh-condensed').text.replace('\n', '').strip().split('/')[1].strip(),
            'description': repo.select_one('.col-9.text-gray.my-1').text.replace('\n', '').strip() if repo.select_one('.col-9.text-gray.my-1') else None,
            'stars_per_day': stars_per_day,
            'language': repo.select_one('.d-inline-block.ml-0.mr-3').text.replace('\n', '').strip() if repo.select_one('.d-inline-block.ml-0.mr-3') else None,
            'url': 'https://github.com' + repo.select_one('.h3.lh-condensed').select_one('a').attrs['href']
        }
        trending_repos.append(repo_info)

    return trending_repos

def get_trending_repos(since="daily"):
    html = fetch_trending_page(since)
    return parse_trending_repos(html)
