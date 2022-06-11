import hashlib
import json
import os
import random
import time
import urllib.request

from tqdm import tqdm


def load_links():
    with open('data/images_links_old.json', 'r') as f:
        links = json.load(f)
    return links


def download_image(link_mimetype):
    link, mimetype = link_mimetype
    try:
        path = link_mimetype_to_path(link_mimetype)
        urllib.request.urlretrieve(
            link,
            path)
        time.sleep(1)
    except Exception as e:
        print(e)
        print(link)


def link_mimetype_to_path(link_mimetype):
    link, mimetype = link_mimetype
    return (f'data/images/{hashlib.sha224(link.encode()).hexdigest()}'
            f'.{mimetype.split("/")[-1]}')


def download_images_parallel(links):
    with tqdm(total=len(links)) as pbar:
        for link_mimetype in links:
            download_image(link_mimetype)
            pbar.update()


if __name__ == '__main__':
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36')]
    urllib.request.install_opener(opener)
    links = load_links()
    links = [tuple(x) for x in links if
             x[1] in {'image/png', 'image/jpeg', 'image/jpg'}
             and x[0].startswith('http')
             and not os.path.exists(link_mimetype_to_path(x))]
    links = list(set(links))
    random.shuffle(links)
    print(len(links))
    download_images_parallel(links)
