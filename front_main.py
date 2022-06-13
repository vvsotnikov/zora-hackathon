import requests
import streamlit as st

from result_image_reqs import req_img_name

st.set_page_config(
    page_title='Zora-powered NFT AI Scanner',
    page_icon='🔵',
    layout='wide',
    initial_sidebar_state='expanded',
)
st.markdown(
    """<img src="https://zora.co/assets/og-image.png" alt="drawing" width="500"/>""",
    unsafe_allow_html=True)
st.title('ZORA-powered NFT AI Scanner')
social_md = st.markdown(
    '[GitHub](https://github.com/vvsotnikov/zora-hackathon)' '   [Twitter](https://twitter.com/Neural9000/status/1536295324104507393)',
    unsafe_allow_html=True)
metanft_colab_button = st.markdown(
    'Meta NFT Image Generator available in Colab Jupyter notebook\n\n'
    '[![MetaNFT in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vvsotnikov/zora-hackathon/blob/master/MetaNFT.ipynb)',
    unsafe_allow_html=True)

col1, col2 = st.columns(2)
pl1, pl2, pl3 = st.columns(3)
pl4, pl5, pl6 = st.columns(3)
md1 = pl1.empty()
md2 = pl2.empty()
md3 = pl3.empty()
md4 = pl4.empty()
md5 = pl5.empty()
md6 = pl6.empty()


def text_search():
    search_result = requests.get(
        f'http://zora-server:8000/find_text?query={search_text_input}').json()

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

    md1.markdown(
        f"{image1}"
        f"\n\n{coll_name1}#{token_id1} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr1}?a={token_id1} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr1}/{token_id1}",
        unsafe_allow_html=True)
    md2.markdown(
        f"{image2}"
        f"\n\n{coll_name2}#{token_id2} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr2}?a={token_id2} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr2}/{token_id2}",
        unsafe_allow_html=True)
    md3.markdown(
        f"{image3}"
        f"\n\n{coll_name3}#{token_id3} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr3}?a={token_id3} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr3}/{token_id3}",
        unsafe_allow_html=True)
    md4.markdown(
        f"{image4}"
        f"\n\n{coll_name4}#{token_id4} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr4}?a={token_id4} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr4}/{token_id4}",
        unsafe_allow_html=True)
    md5.markdown(
        f"{image5}"
        f"\n\n{coll_name5}#{token_id5} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr5}?a={token_id5} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr5}/{token_id5}",
        unsafe_allow_html=True)
    md6.markdown(
        f"{image6}"
        f"\n\n{coll_name6}#{token_id6} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr6}?a={token_id6} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr6}/{token_id6}",
        unsafe_allow_html=True)


def image_search():
    image_search_result = requests.post(f'http://zora-server:8000/find_image',
                                        files={'image': search_image_input}).json()

    nft1 = req_img_name(image_search_result[0]["contract"],
                        image_search_result[0]["token_id"])
    image1 = (
        f"""<img src="{nft1[1]}" alt="drawing" width="300"/>""")
    coll_name1 = nft1[0]
    token_id1 = image_search_result[0]["token_id"]
    coll_addr1 = image_search_result[0]["contract"]

    nft2 = req_img_name(image_search_result[1]["contract"],
                        image_search_result[1]["token_id"])
    image2 = (
        f"""<img src="{nft2[1]}" alt="drawing" width="300"/>""")
    coll_name2 = nft2[0]
    token_id2 = image_search_result[1]["token_id"]
    coll_addr2 = image_search_result[1]["contract"]

    nft3 = req_img_name(image_search_result[2]["contract"],
                        image_search_result[2]["token_id"])
    image3 = (
        f"""<img src="{nft3[1]}" alt="drawing" width="300"/>""")
    coll_name3 = nft3[0]
    token_id3 = image_search_result[2]["token_id"]
    coll_addr3 = image_search_result[2]["contract"]

    nft4 = req_img_name(image_search_result[3]["contract"],
                        image_search_result[3]["token_id"])
    image4 = (
        f"""<img src="{nft4[1]}" alt="drawing" width="300"/>""")
    coll_name4 = nft4[0]
    token_id4 = image_search_result[3]["token_id"]
    coll_addr4 = image_search_result[3]["contract"]

    nft5 = req_img_name(image_search_result[4]["contract"],
                        image_search_result[4]["token_id"])
    image5 = (
        f"""<img src="{nft5[1]}" alt="drawing" width="300"/>""")
    coll_name5 = nft5[0]
    token_id5 = image_search_result[4]["token_id"]
    coll_addr5 = image_search_result[4]["contract"]

    nft6 = req_img_name(image_search_result[5]["contract"],
                        image_search_result[5]["token_id"])
    image6 = (
        f"""<img src="{nft6[1]}" alt="drawing" width="300"/>""")
    coll_name6 = nft6[0]
    token_id6 = image_search_result[5]["token_id"]
    coll_addr6 = image_search_result[5]["contract"]

    md1.markdown(
        f"{image1}"
        f"\n\n{coll_name1}#{token_id1} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr1}?a={token_id1} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr1}/{token_id1}",
        unsafe_allow_html=True)
    md2.markdown(
        f"{image2}"
        f"\n\n{coll_name2}#{token_id2} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr2}?a={token_id2} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr2}/{token_id2}",
        unsafe_allow_html=True)
    md3.markdown(
        f"{image3}"
        f"\n\n{coll_name3}#{token_id3} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr3}?a={token_id3} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr3}/{token_id3}",
        unsafe_allow_html=True)
    md4.markdown(
        f"{image4}"
        f"\n\n{coll_name4}#{token_id4} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr4}?a={token_id4} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr4}/{token_id4}",
        unsafe_allow_html=True)
    md5.markdown(
        f"{image5}"
        f"\n\n{coll_name5}#{token_id5} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr5}?a={token_id5} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr5}/{token_id5}",
        unsafe_allow_html=True)
    md6.markdown(
        f"{image6}"
        f"\n\n{coll_name6}#{token_id6} "
        f"\n\nEtherscan link: https://etherscan.io/token/{coll_addr6}?a={token_id6} "
        f"\n\nZORA link: https://zora.co/collections/{coll_addr6}/{token_id6}",
        unsafe_allow_html=True)


def schedule_text_search():
    st.session_state.run_text_search = True


def schedule_image_search():
    st.session_state.run_image_search = True


search_text_input = col1.text_input('NFT image search by text',
                                    help='Enter your dark NFT fantasy here',
                                    placeholder="pixel art 8 bit",
                                    on_change=schedule_text_search)

search_image_input = col2.file_uploader(
    'NFT image search by image',
    type=['png', 'jpg', 'jpeg'],
    help='Load your NFT image to find NFTs with simmilar images',
    on_change=schedule_image_search)
if 'run_text_search' in st.session_state and st.session_state.run_text_search and search_text_input:
    text_search()
    st.session_state.run_text_search = False
if 'run_image_search' in st.session_state and st.session_state.run_image_search and search_image_input:
    image_search()
    st.session_state.run_image_search = False
