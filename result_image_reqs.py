import json
import requests



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
                      data=json.dumps(payload), headers={'Content-type': 'application/json'}
                      )
    response = json.loads(r.text)

    coll_name = response['data']["token"]["token"]["collectionName"]

    if response['data']["token"]["token"]["image"]["mediaEncoding"]:
        image_link = response['data']["token"]["token"]["image"]["mediaEncoding"]["thumbnail"]
    else: image_link = response['data']["token"]["token"]["image"]["url"]

    return coll_name, image_link