# Fiction Search Web crawler

# TODO: 1.Make HTTP GET request to the initial url
# TODO: 2. Parse the response and get all the available links <a href>
# TODO:  3. Follow the extracted links and repeat the same.
# TODO: 4. Break out the loop either on hitten the given depth or if no more links are available.
# I got the reference juas juas juas


# Step 1: Import some libraries
import json
import requests
from bs4 import BeautifulSoup

# TODO: change the stackoverflow page to the AO3 page at the end of code testing
start_url = 'https://archiveofourown.org'


def crawl(url):
    # TODO: remove the comment below if in the end is unecessary
    # print('crawl("%s")' % url)

    response = requests.get(start_url)
    content = BeautifulSoup(response.text, 'lxml')

    links = content.findAll('a')
    title = content.find('title').text
    description = content.find('p').text.strip().replace('\n', ' ')

    # urls = []

    for link in links:
        try:
            pass
        except KeyError:
            pass
    return {
        'url': url,
        'title': title,
        'description': description
    }


result = crawl(start_url)
print(json.dumps(result, indent=2))
