import hashlib
import json
import os
import time
import urllib.request

from tqdm import tqdm


def load_links():
    with open('data/images_links.json', 'r') as f:
        links = json.load(f)
    return links


def download_image(link_mimetype):
    link, mimetype = link_mimetype
    try:
        path = link_mimetype_to_path(link_mimetype)
        if not os.path.exists(path):
            urllib.request.urlretrieve(
                link,
                path)
            time.sleep(1)
    except Exception as e:
        print(e)
        print(link)


def link_mimetype_to_path(link_mimetype):
    link, mimetype = link_mimetype
    if mimetype is None:
        extension = ''
    else:
        extension = f'.{mimetype.split("/")[1]}'
    return f'data/images/{hashlib.sha224(link.encode()).hexdigest()}{extension}'


def download_images(links):
    total = sum(len(nft_list) for nft_list in links.values())
    with tqdm(total=total) as pbar:
        for contract, nft_list in links.items():
            for link_mimetype_id in nft_list:
                download_image(link_mimetype_id[:2])
                pbar.update()


def build_inverse_index(links):
    inverse_index = {}
    for contract, nft_list in links.items():
        for link_mimetype_id in nft_list:
            link, mimetype, nft_id = link_mimetype_id
            inverse_index[hashlib.sha224(link.encode()).hexdigest()] = [contract,
                                                                        nft_id]
    return inverse_index


if __name__ == '__main__':
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36')]
    urllib.request.install_opener(opener)
    links = load_links()
    links = {contract: [x for x in nft_list if x[0].startswith('http')]
             for contract, nft_list in links.items()}
    links = {contract: nft_list[:15] for contract, nft_list in links.items()}
    links = {contract: [[link.replace('/ipfs/ipfs/', '/ipfs/'), mime, nft_id]
                        for link, mime, nft_id in nft_list] for contract, nft_list in
             links.items()}
    nft_index = build_inverse_index(links)
    with open('data/nft_index.json', 'w') as f:
        json.dump(nft_index, f, indent=2)
    links = {contract: [x for x in nft_list
                        if not os.path.exists(link_mimetype_to_path(x[:2]))]
             for contract, nft_list in links.items()}
    download_images(links)
