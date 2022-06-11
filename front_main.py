import streamlit as st


st.set_page_config(
    page_title='Zora-powered NFT AI Scanner',
    page_icon=None,
    layout='wide',
    initial_sidebar_state='expanded',
)
st.title('Zora-powered NFT AI Scanner')

col1, col2 = st.columns(2)
pl1, pl2 = st.columns(2)
pl3, pl4, pl5 = st.columns(3)


def search():
    image1 = ('![](https://www.cryptokitties.co/profile/profile-2.png)')
    coll_name1 = "OddFrens"
    token_id1 = '1'
    coll_addr1 = '0xa8ad3151f6226eed6fa8f7238a833684f0a86fcd'

    image2 = ('![](https://www.cryptokitties.co/profile/profile-2.png)')
    coll_name2 = "OddFrens"
    token_id2 = '19782'
    coll_addr2 = '0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7'

    image3 = ('![](https://www.cryptokitties.co/profile/profile-2.png)')
    coll_name3 = "OddFrens"
    token_id3 = '1'
    coll_addr3 = '0xa8ad3151f6226eed6fa8f7238a833684f0a86fcd'

    image4 = ('![](https://www.cryptokitties.co/profile/profile-2.png)')
    coll_name4 = "OddFrens"
    token_id4 = '1'
    coll_addr4 = '0xa8ad3151f6226eed6fa8f7238a833684f0a86fcd'

    image5 = ('![](https://www.cryptokitties.co/profile/profile-2.png)')
    coll_name5 = "OddFrens"
    token_id5 = '1'
    coll_addr5 = '0xa8ad3151f6226eed6fa8f7238a833684f0a86fcd'

    pl1.markdown(
        f"{image1}"
        f"\n\n{coll_name1}#{token_id1} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr1}?a={token_id1} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr1}/{token_id1}")
    pl2.markdown(
        f"{image2}"
        f"\n\n{coll_name2}#{token_id2} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr2}?a={token_id2} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr2}/{token_id2}")
    pl3.markdown(
        f"{image3}"
        f"\n\n{coll_name3}#{token_id3} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr3}?a={token_id3} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr3}/{token_id3}")
    pl4.markdown(
        f"{image4}"
        f"\n\n{coll_name4}#{token_id4} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr4}?a={token_id4} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr4}/{token_id4}")
    pl5.markdown(
        f"{image5}"
        f"\n\n{coll_name5}#{token_id5} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr5}?a={token_id5} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr5}/{token_id5}")


col1.text_input('NFT image search', help='Write your dark NFT fantasy here', placeholder="pixel pirate")
text_req = col1.button('Search', on_click=search)
col2.text_input('Generate NFT by owner address', help='Enter your ETH-chain NFT owner address to generate meta-NFT ',
                placeholder="0x0000000000000000000000000000000000000000")
col2.button('Generate')
