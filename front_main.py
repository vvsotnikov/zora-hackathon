import requests
import streamlit as st
from result_image_reqs import req_img_name

st.set_page_config(
    page_title='Zora-powered NFT AI Scanner',
    page_icon='🔵',
    layout='wide',
    initial_sidebar_state='expanded',
)
st.title('Zora-powered NFT AI Scanner')

col1, col2 = st.columns(2)
pl1, pl2, pl3 = st.columns(3)
pl4, pl5, pl6 = st.columns(3)


def text_search():
    if search_text_input:
        search_result = requests.get(f'http://zora-front:8000/find_text?query={search_text_input}').json()

        nft1 = req_img_name(search_result[0]["contract"], search_result[0]["token_id"])
        image1 = (
            f"""<img src="{nft1[1]}" alt="drawing" width="300"/>""")
        coll_name1 = nft1[0]
        token_id1 = search_result[0]["token_id"]
        coll_addr1 = search_result[0]["contract"]

        nft2 = req_img_name(search_result[1]["contract"], search_result[1]["token_id"])
        image2 = (
            f"""<img src="{nft2[1]}" alt="drawing" width="300"/>""")
        coll_name2 = nft2[0]
        token_id2 = search_result[1]["token_id"]
        coll_addr2 = search_result[1]["contract"]

        nft3 = req_img_name(search_result[2]["contract"], search_result[2]["token_id"])
        image3 = (
            f"""<img src="{nft3[1]}" alt="drawing" width="300"/>""")
        coll_name3 = nft3[0]
        token_id3 = search_result[2]["token_id"]
        coll_addr3 = search_result[2]["contract"]

        nft4 = req_img_name(search_result[3]["contract"], search_result[3]["token_id"])
        image4 = (
            f"""<img src="{nft4[1]}" alt="drawing" width="300"/>""")
        coll_name4 = nft4[0]
        token_id4 = search_result[3]["token_id"]
        coll_addr4 = search_result[3]["contract"]

        nft5 = req_img_name(search_result[4]["contract"], search_result[4]["token_id"])
        image5 = (
            f"""<img src="{nft5[1]}" alt="drawing" width="300"/>""")
        coll_name5 = nft5[0]
        token_id5 = search_result[4]["token_id"]
        coll_addr5 = search_result[4]["contract"]

        nft6 = req_img_name(search_result[5]["contract"], search_result[5]["token_id"])
        image6 = (
            f"""<img src="{nft6[1]}" alt="drawing" width="300"/>""")
        coll_name6 = nft6[0]
        token_id6 = search_result[5]["token_id"]
        coll_addr6 = search_result[5]["contract"]

        pl1.markdown(
            f"{image1}"
            f"\n\n{coll_name1}#{token_id1} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr1}?a={token_id1} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr1}/{token_id1}", unsafe_allow_html=True)
        pl2.markdown(
            f"{image2}"
            f"\n\n{coll_name2}#{token_id2} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr2}?a={token_id2} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr2}/{token_id2}", unsafe_allow_html=True)
        pl3.markdown(
            f"{image3}"
            f"\n\n{coll_name3}#{token_id3} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr3}?a={token_id3} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr3}/{token_id3}", unsafe_allow_html=True)
        pl4.markdown(
            f"{image4}"
            f"\n\n{coll_name4}#{token_id4} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr4}?a={token_id4} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr4}/{token_id4}", unsafe_allow_html=True)
        pl5.markdown(
            f"{image5}"
            f"\n\n{coll_name5}#{token_id5} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr5}?a={token_id5} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr5}/{token_id5}", unsafe_allow_html=True)
        pl6.markdown(
            f"{image6}"
            f"\n\n{coll_name6}#{token_id6} "
            f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr6}?a={token_id6} "
            f"\n\nZORA link: https://zora.co/collections/{coll_addr6}/{token_id6}", unsafe_allow_html=True)
    else:
        pl1.markdown("Enter your text request to find Image")


def image_search():
    image_search_result = requests.get(f'http://zora-front:8000/find_image?query={search_image_input}').json()

    nft1 = req_img_name(image_search_result[0]["contract"], image_search_result[0]["token_id"])
    image1 = (
        f"""<img src="{nft1[1]}" alt="drawing" width="300"/>""")
    coll_name1 = nft1[0]
    token_id1 = image_search_result[0]["token_id"]
    coll_addr1 = image_search_result[0]["contract"]

    nft2 = req_img_name(image_search_result[1]["contract"], image_search_result[1]["token_id"])
    image2 = (
        f"""<img src="{nft2[1]}" alt="drawing" width="300"/>""")
    coll_name2 = nft2[0]
    token_id2 = image_search_result[1]["token_id"]
    coll_addr2 = image_search_result[1]["contract"]

    nft3 = req_img_name(image_search_result[2]["contract"], image_search_result[2]["token_id"])
    image3 = (
        f"""<img src="{nft3[1]}" alt="drawing" width="300"/>""")
    coll_name3 = nft3[0]
    token_id3 = image_search_result[2]["token_id"]
    coll_addr3 = image_search_result[2]["contract"]

    nft4 = req_img_name(image_search_result[3]["contract"], image_search_result[3]["token_id"])
    image4 = (
        f"""<img src="{nft4[1]}" alt="drawing" width="300"/>""")
    coll_name4 = nft4[0]
    token_id4 = image_search_result[3]["token_id"]
    coll_addr4 = image_search_result[3]["contract"]

    nft5 = req_img_name(image_search_result[4]["contract"], image_search_result[4]["token_id"])
    image5 = (
        f"""<img src="{nft5[1]}" alt="drawing" width="300"/>""")
    coll_name5 = nft5[0]
    token_id5 = image_search_result[4]["token_id"]
    coll_addr5 = image_search_result[4]["contract"]

    nft6 = req_img_name(image_search_result[5]["contract"], image_search_result[5]["token_id"])
    image6 = (
        f"""<img src="{nft6[1]}" alt="drawing" width="300"/>""")
    coll_name6 = nft6[0]
    token_id6 = image_search_result[5]["token_id"]
    coll_addr6 = image_search_result[5]["contract"]

    pl1.markdown(
        f"{image1}"
        f"\n\n{coll_name1}#{token_id1} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr1}?a={token_id1} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr1}/{token_id1}", unsafe_allow_html=True)
    pl2.markdown(
        f"{image2}"
        f"\n\n{coll_name2}#{token_id2} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr2}?a={token_id2} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr2}/{token_id2}", unsafe_allow_html=True)
    pl3.markdown(
        f"{image3}"
        f"\n\n{coll_name3}#{token_id3} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr3}?a={token_id3} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr3}/{token_id3}", unsafe_allow_html=True)
    pl4.markdown(
        f"{image4}"
        f"\n\n{coll_name4}#{token_id4} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr4}?a={token_id4} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr4}/{token_id4}", unsafe_allow_html=True)
    pl5.markdown(
        f"{image5}"
        f"\n\n{coll_name5}#{token_id5} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr5}?a={token_id5} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr5}/{token_id5}", unsafe_allow_html=True)
    pl6.markdown(
        f"{image6}"
        f"\n\n{coll_name6}#{token_id6} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr6}?a={token_id6} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr6}/{token_id6}", unsafe_allow_html=True)


search_text_input = col1.text_input('NFT image search by text', help='Enter your dark NFT fantasy here',
                                    placeholder="pixel pirate")
if search_text_input:
    text_search()

search_image_input = col1.file_uploader('NFT image search by image', type=['png', 'jpg', 'jpeg'],
                                        help='Load your NFT image to find NFTs with simmilar images')
if search_image_input:
    image_search()

col2.text_input('Generate NFT by owner address', help='Enter your ETH-chain NFT owner address to generate meta-NFT ',
                placeholder="0x0000000000000000000000000000000000000000")
col2.button('Generate')
