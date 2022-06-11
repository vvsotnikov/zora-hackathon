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
    '0x8943C7bAC1914C9A7ABa750Bf2B6B09Fd21037E0',
    '0x34d85c9CDeB23FA97cb08333b511ac86E1C4E258',
    '0xB852c6b5892256C264Cc2C888eA462189154D8d7',
    '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e',
    '0x64b6b4142d4D78E49D53430C1d3939F2317f9085',
    '0x306b1ea3ecdf94aB739F1910bbda052Ed4A9f949',
    '0x19b86299c21505cdf59cE63740B240A9C822b5E4',
    '0xd8a5d498ab43Ed060cb6629b97a19e3e4276dD9f',
    '0x23581767a106ae21c074b2276D25e5C3e136a68b',
    '0x248139aFB8d3A2e16154FbE4Fb528A3a214fd8E7',
    '0x80336Ad7A747236ef41F47ed2C7641828a480BAA',
    '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B',
    '0x60E4d786628Fea6478F785A6d7e704777c86a7c6',
    '0x160C404B2b49CBC3240055CEaEE026df1e8497A0',
    '0x41a322b28d0ff354040e2cbc676f0320d8c8850d',
    '0x79FCDEF22feeD20eDDacbB2587640e45491b757f',
    '0x5EaeADdA470245343249452E744e423F489AbBc4',
    '0x76B3AF5F0f9B89CA5a4f9fe6C58421dbE567062d',
    '0xC1ad47aeb274157E24A5f01B5857830aeF962843',
    '0x7D8820FA92EB1584636f4F5b8515B5476B75171a',
    '0xd2F668a8461D6761115dAF8Aeb3cDf5F40C532C6 '
    '0x8b634B2ae70E338865BF9741b4ae935adf2b4C55',
    '0x2e541Cec5CB41E7678ac3c8e91AcB3FC1dB0da07',
    '0x54616C0815c306FC22417b96282cA4AA6F47D357',
    '0x809D8f2B12454FC07408d2479cf6DC701ecD5a9f',
    '0xD497A414bB00803E846B53d07Fcb742831B24906',
    '0xc5B52253f5225835cc81C52cdb3d6A22bc3B0c93',
    '0x9378368ba6b85c1FbA5b131b530f5F5bEdf21A18',
    '0x1A92f7381B9F03921564a437210bB9396471050C',
    '0x75335297cb5029C2a9Acb2b47507F18FFD48E96C',
    '0x5Af0D9827E0c53E4799BB226655A1de152A425a5',
    '0xa3AEe8BcE55BEeA1951EF834b99f3Ac60d1ABeeB',
    '0x4BEcbdf97747413A18C5a2a53321D09198d3a100',
    '0xe785E82358879F061BC3dcAC6f0444462D4b5330',
    '0x3CF57cc9Cf5263748c6f926fF498AC0C6F95B26e',
    '0xDA60730E1feAa7D8321f62fFb069eDd869E57D02',
    '0x5bd815Fd6c096bAB38B4C6553cfce3585194dff9',
    '0x497B54355043E7A0d06Bf5E3C20CeCf859FcC0A8',
    '0xd3605059c3cE9fACf625Fa72D727508B7b7F280F',
    '0xd2F668a8461D6761115dAF8Aeb3cDf5F40C532C6',
    '0xBD4455dA5929D5639EE098ABFaa3241e9ae111Af',
    '0x596a0f276eE432D8a28441e55737fF55cF30d0f7',
    '0x3903d4fFaAa700b62578a66e7a67Ba4cb67787f9',
    '0xc99c679C50033Bbc5321EB88752E89a93e9e83C5',
    '0xaa3FDC4a0700B82c9AA80655624d32701DC92946',
    '0xeB3a9A839dFeEaf71db1B4eD6a8ae0cCB171b227',
    '0xD75B811814Fff5F110Dcc37f25285d90D3e7f63b',
    '0xcAACE84B015330C0Ab4BD003F6fa0B84ec6C64ac',
    '0x845a007D9f283614f403A24E3eB3455f720559ca',
    '0x165a2eD732eb15B54b5E8C057CbcE6251370D6e8',
    '0xf61F24c2d93bF2dE187546B14425BF631F28d6dC',
    '0xCcc441ac31f02cD96C153DB6fd5Fe0a2F4e6A68d',
    '0x892848074ddeA461A15f337250Da3ce55580CA85',
    '0xb4d06d46A8285F4EC79Fd294F78a881799d8cEd9',
    '0x9C8fF314C9Bc7F6e59A9d9225Fb22946427eDC03',
    '0xaaD35C2DadbE77f97301617D82e661776c891Fa9',
    '0x6e0418050387C6C3d4Cd206d8b89788BBd432525',
    '0x8e37dDc122Cc8AF0A47785D060E091D1fBd94941',
    '0x6e0418050387C6C3d4Cd206d8b89788BBd432525',
    '0x0c2E57EFddbA8c768147D1fdF9176a0A6EBd5d83',
    '0xfE8C6d19365453D26af321D0e8c910428c23873F',
    '0x4B103d07C18798365946E76845EDC6b565779402',
    '0x160C404B2b49CBC3240055CEaEE026df1e8497A0',
    '0x75E95ba5997Eb235F40eCF8347cDb11F18ff640B',
    '0xaAF03a65CbD8f01b512Cd8d530a675b3963dE255',
    '0x335b8BA8999fB6b04877f3eC8793E3F0e5Dbe6BA',
    '0x09233d553058c2F42ba751C87816a8E9FaE7Ef10',
    '0x47f3A38990ca12E39255E959F7D97fBE5906Afd4',
    '0xfcAecB01D2e095b2Cf3E5293AfD83BeA5E9fF259',
    '0xD497A414bB00803E846B53d07Fcb742831B24906',
    '0x2912919719414a093deAC78031e90Ba493b8Da34',
    '0x36D7b711390D34e8fe26ad8f2bB14E7C8f0c56e9',
    '0x3110EF5f612208724CA51F5761A69081809F03B7',
    '0x47f3A38990ca12E39255E959F7D97fBE5906Afd4',
    '0x2acAb3DEa77832C09420663b0E1cB386031bA17B',
    '0x4B61413D4392c806E6d0fF5Ee91E6073C21d6430',
    '0x0c2E57EFddbA8c768147D1fdF9176a0A6EBd5d83',
    '0x7d8Fc43BED4D8a49aCd8b5cEa83C04Fd0c69b986',
    '0x1CB1A5e65610AEFF2551A50f76a87a7d3fB649C6',
    '0x500F312864D14BcC73B3760c55FE6567B193437f',
    '0xF60E21fFE1efE709bF020490E36A3EB6b3c6D43d',
    '0x86C10D10ECa1Fca9DAF87a279ABCcabe0063F247',
    '0xa5C0Bd78D1667c13BFB403E2a3336871396713c5',
    '0x0Cfb5d82BE2b949e8fa73A656dF91821E2aD99FD',
    '0xB2A2c7fB3E326c5ef282cB78207fbD9dcBA8e983',
    '0x9690b63Eb85467BE5267A3603f770589Ab12Dc95',
    '0x123b30E25973FeCd8354dd5f41Cc45A3065eF88C',
    '0x2912919719414a093deAC78031e90Ba493b8Da34',
    '0x77640cf3F89A4F1B5CA3A1e5c87f3F5B12ebf87e',
    '0x92aC03D1eB81bB8402FcdBE3Ef43C6Ca0CBbA8f9'
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
