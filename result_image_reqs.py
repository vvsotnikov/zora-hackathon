import json
import requests
import os



if os.path.exists("data/api_key.txt"):
    with open('data/api_key.txt', 'r') as f:
        api_key = f.read()
        headers = {'content-type': 'application/json',
                   'X-API-KEY': api_key}
else: headers = {'content-type': 'application/json'}


def req_img_name(contract, tokenid):
    url = 'https://api.zora.co/graphql'
    payload = {
        'query': f'''query GetTokenImage {{
  token(token: {{address: "{contract}", tokenId: "{tokenid}"}}, network: {{network: ETHEREUM, chain: MAINNET}}) {{
    token {{
      collectionName
      image {{
      url
        mediaEncoding {{
          ... on ImageEncodingTypes {{
            thumbnail
          }}
        }}
      }}
    }}
  }}
}}
''',
        "operationName": "GetTokenImage"
    }
    r = requests.post(url,
                      data=json.dumps(payload), headers=headers)
    response = json.loads(r.text)

    coll_name = response['data']["token"]["token"]["collectionName"]

    if response['data']["token"]["token"]["image"]["mediaEncoding"]:
        image_link = response['data']["token"]["token"]["image"]["mediaEncoding"]["thumbnail"]
    else: image_link = response['data']["token"]["token"]["image"]["url"]

    return coll_name, image_link