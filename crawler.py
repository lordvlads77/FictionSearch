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
start_url = 'https://www.archiveofourown.org'


def crawl(url, depth):
    try:
        response = requests.get(url)
    except:
        print('Failed to perform HTTP GET request on "%s"' % url)
        return
    # TODO: remove the comment below if in the end is unecessary
    # print('crawl("%s")' % url)
    content = BeautifulSoup(response.text, 'lxml')

    title = content.find('title').text
    description = content.find('p').text.strip().replace('\n', ' ')

    result = {
        'url': url,
        'title': title,
        'description': description
    }

    print('\n\nReturn:\n', json.dumps(result, indent=2))

    if depth == 0:
        return result

    try:
        links = content.findAll('a')
    except:
        return result
    # urls = []

    for link in links:
        try:
            print('following url "%s" on depth: "%d"' % (link['href'], depth))
            crawl(link['herf'], depth - 1)
        except KeyError:
            pass

    return result


result = crawl(start_url, 1)
print(json.dumps(result, indent=2))
