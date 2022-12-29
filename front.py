import requests
import streamlit as st
from streamlit_option_menu import option_menu   
import gt
st.set_page_config(page_title="Zira",page_icon="/home/sivayogan/Pictures/Screenshots/logo.png",layout="wide")

m=st.markdown("""
<style>
div.stButton > button:first-child{
    background-color:##ff99ff;
    color:Black;
    width:150px;
    height:50px;
}
div.stButton > button:hover{
    background-color:#FF0000;
    color:white;
}
div.stButton > button:click{
    background-color:#FF0000;
    color:white;
}
</style>""",unsafe_allow_html=True)
def load_lottie(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json() 
animation=load_lottie("https://assets1.lottiefiles.com/packages/lf20_ofa3xwo7.json")
def add():
    st.write(10+20)
st.image("/home/sivayogan/Pictures/Screenshots/jira.png")

st.sidebar.header('huawei apps store：')
st.sidebar.subheader('1.please chose which app you want to operate')
# st.header(st.image("/home/sivayogan/Pictures/Screenshots/jira.png"))
st.sidebar.image("/home/sivayogan/Pictures/Screenshots/jira.png")


with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=['Jira']
    )
with st.container():
    st.header('My personal Assistant')

with st.container():
    if st.button('Click to Talk'):
        st.write('Please say something')
        res=gt.main()
        st.write(res)
        gt.talk(res)
    else:
        st.write('Click to talk')
    
