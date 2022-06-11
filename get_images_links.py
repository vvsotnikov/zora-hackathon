import json
import time

import requests

CONTRACTS = [
    '0xfcAecB01D2e095b2Cf3E5293AfD83BeA5E9fF259',
    '0xf7D134224A66C6A4DDeb7dEe714A280b99044805',
    '0xa8Ad3151f6226eED6fa8F7238A833684f0a86FCd',
    '0x028E6F37b1830BD62AecF5faB3325DF6dF7E0a44',
    '0x0847d1fB2AdC3D1C19B233AFB7d01a631728A415',
    '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D',
    '0xED5AF388653567Af2F388E6224dC7C4b3241C544',
    '0x369156da04B6F313b532F7aE08E661e402B1C2F2',
    '0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7',
    '0x596a0f276ee432d8a28441e55737ff55cf30d0f7',
    '0xbCe3781ae7Ca1a5e050Bd9C4c77369867eBc307e',
    '0x9F9B2B8e268d06DC67F0f76627654b80e219e1d6',
    '0xeF1a89cbfAbE59397FfdA11Fc5DF293E9bC5Db90',
    '0x6728d91abACdbac2f326baa384513a523C21b80a',
    '0x60E4d786628Fea6478F785A6d7e704777c86a7c6',
    '0x500F312864D14BcC73B3760c55FE6567B193437f',
    '0x659A4BdaAaCc62d2bd9Cb18225D9C89b5B697A5A',
    '0xbabe3dEc32FA870b4125B9cAd1CEa498DCB116C9',
    '0x8943C7bAC1914C9A7ABa750Bf2B6B09Fd21037E0'
]


def get_images_links(contracts):
    links = []
    for contract in contracts:
        links += (get_contract_links(contract))
    return links


def build_graphql_request(contract, page_cursor):
    return {
        'query': f'''query ListTokens {{
  tokens(
    where: {{collectionAddresses: "{contract}"}}
    pagination: {{after: "{page_cursor}", limit: 500}}
  ) {{
    nodes {{
      token {{
        image {{
          mimeType
          url
        }}
      }}
    }}
    pageInfo {{
      endCursor
      hasNextPage
      limit
    }}
  }}
}}''',
        "operationName": "ListTokens"
    }


def get_contract_links(contract):
    links = []
    end_cursor = ''
    while True:
        tokens_with_images = 0
        r = requests.post(
            "https://api.zora.co/graphql",
            data=json.dumps(build_graphql_request(contract, end_cursor)),
            headers={'content-type': 'application/json'})
        assert r.status_code == 200
        data = r.json()
        end_cursor = data['data']['tokens']['pageInfo']['endCursor']
        for record in data['data']['tokens']['nodes']:
            if record['token']['image'] and record['token']['image']['url']:
                links.append([
                    parse_ipfs_link(record['token']['image']['url']),
                    record['token']['image']['mimeType']
                ])
            else:
                tokens_with_images += 1
        print(f'{contract}: {len(links)}')
        time.sleep(2)
        if (not data['data']['tokens']['pageInfo']['hasNextPage']
                or tokens_with_images == 500):
            break
    return links


def parse_ipfs_link(link: str):
    if link.startswith('ipfs://'):
        link = link.replace('ipfs://', 'https://ipfs.io/ipfs/')
    return link


if __name__ == '__main__':
    images_links = (get_images_links(CONTRACTS))
    print(len(images_links))
    print(set([x[1] for x in images_links]))
    with open('data/images_links.json', 'w') as f:
        json.dump(images_links, f)
