# from: https://github.com/upraneelnihar/streamlit-multiapps
#app.py
import streamlit as st
from multiapp import MultiApp
from apps import home, support, register, account, admin     # import your app modules here
from PIL import Image


st.set_page_config(
    page_title="4HomeTV",
    page_icon=":tv:",  # cinema satellite
    layout="wide",
)

#---------- Hide Streamlit Hamburger Menu -----------
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Support", support.app)
app.add_app("Register", register.app)
app.add_app("Account", account.app)
app.add_app("Admin", admin.app)

# img = Image.open("images/4hometv_logo2wide.png")
# st.sidebar.image(img,width=200)
img = Image.open("images/4HomeTV Logo.png")
st.sidebar.image(img,width=100)

# The main app
app.run()

