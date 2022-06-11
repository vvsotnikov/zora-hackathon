import streamlit as st

st.set_page_config(
    page_title='Zora-powered NFT AI Scanner',
    page_icon=None,
    layout='wide',
    initial_sidebar_state='expanded',
)
st.title('Zora-powered NFT AI Scanner')

col1, col2 = st.columns(2)
col1.text_input('NFT image search', help='Write your dark NFT fantasy here', placeholder="pixel pirate")
col1.button('Search')
col2.text_input('Generate NFT by owner address', help='Enter your ETH-chain NFT owner address to generate meta-NFT ',
                placeholder="0x0000000000000000000000000000000000000000")
col2.button('Generate')

pic1, pic2 = st.column(2)
pic1 = st.empty()
pic2 = st.empty()
pic3, pic4, pic5 = st.column(3)
pic3 = st.empty()
pic5 = st.empty()
