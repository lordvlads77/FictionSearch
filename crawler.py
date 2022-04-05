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


def crawl(url, depth):
    # TODO: remove the comment below if in the end is unecessary
    # print('crawl("%s")' % url)

    try:
        print('Crawling url: "%s"' % url)
        response = requests.get(start_url)
    except:
        print('Failed to perform HTTP GET request on "%s"\n' % url)
        return

    content = BeautifulSoup(response.text, 'lxml')

    title = content.find('title').text
    description = content.findAll('p')[2]

    if description is None:
        description = ''
    else:
        description = description.text.strip().replace('\n', ' ')

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

    for link in links:
        try:
            print('following url "%s" on depth: "%d"' % (link['href'], depth))

            if 'http' not in link['href']:
                follow_url = url + link['href']
            else:
                follow_url = link['href']

            crawl(follow_url, depth - 1)
        except KeyError:
            pass

    return result


result = crawl(start_url, 1)
print(json.dumps(result, indent=2))
