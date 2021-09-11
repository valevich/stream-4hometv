import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import pygsheets
from pygsheets.datarange import DataRange
import datetime
from PIL import Image
import re
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie


def app():

    is_prod = os.environ.get('IS_HEROKU', None)

    #----------------------------------------------------------------------------------#
    #                                  DISPLAY HEADER                                  #
    #----------------------------------------------------------------------------------#
    def display_header():

        #---------------  HEADER ROW 1  -------------------
        col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
        with col1:
            img = Image.open("images/20130322-legenda1-post.jpg")
            st.image(img,width=188)
        with col2:
            img = Image.open("images/w1280x800_12789.jpg")
            st.image(img,width=200)
        with col3:
            img = Image.open("images/2063433_w1.jpg")
            st.image(img,width=223)
        with col4:
            img = Image.open("images/superhero.jpg")
            st.image(img,width=223)
        with col5:
            img = Image.open("images/goroskop-na-udahu2.jpg")
            st.image(img,width=223)
        with col6:
            img = Image.open("images/Anna-Karenina.jpg")
            st.image(img,width=188)
        st.write ('\n')


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    #----------------------------------------------------------------------------------#
    #                                  DISPLAY ABOUT                                   #
    #----------------------------------------------------------------------------------#
    def display_about():

        #---------------  ROW 1  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>The Best International TV</b></p>'
        st.markdown(row, unsafe_allow_html=True)

        #---------------  ROW 2  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Grey; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;"><b>RELIABLE, QUALITY, ​EASY TO USE SERVICE</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        # st.write ('\n')

        #---------------  ROW 3  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Blue; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 18px;"><b>News • Movies • Sports • TV Series • Shows • Kid\'s programs • 7 Days Archive</b></p>'
        st.markdown(row, unsafe_allow_html=True)


        #---------------  LOTTIE IMAGE  -------------------
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/datafiles/ZHlTlyhzTLf9ImW/data.json")
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                renderer="svg", # canvas
                height=250,
                width=250,
                key=None,
            )


        # st.write ('\n')
        # st.write ('\n')

        #---------------  ROW 4  -------------------
        col1, col2, col3 = st.columns([.5,1.3,3])
        with col2:
            st.image('https://a.d-cd.net/WqAAAgNd3-A-960.jpg',width=188)
        with col3:
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 16px;"> \
            Over 2000 Russian, Ukrainian, European, American and World TV HD Channels. Watch Live TV from many countries in the world, anytime on many platforms. \
            Best world channels and major sports events Live in FULL HD. Also available Archive for past 7 days.</p>'
            st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  ROW 5  -------------------
        col1, col2, col3, col4 = st.columns([2.5,2,.3,3])
        with col2:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 16px;"> \
            Available on many platforms from anywhere in the world</p>'
            st.markdown(row, unsafe_allow_html=True)
        with col4:
            img = Image.open("images/Image102.png")
            st.image(img,width=250)
        st.write ('\n')

        #---------------  ROW 6  -------------------
        col1, col2, col3 = st.columns([.5,1.3,3])
        with col2:
            st.image('images/nikulin.jpg',width=188)
        with col3:
            # st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 16px;"> \
            Любимые советские сериалы и фильмы представлены последними новинками киноиндустрии, авторскими фильмами, культовыми сериалами. \
            Телевизионные каналы Спорта отображены лучшими видами хоккея, футбола, тенниса, борьбы, бокса.</p>'
            st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  ROW 7  -------------------
        col1, col2, col3, col4 = st.columns([1,4,.3,3])
        with col2:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 16px;"> \
            All new subscribers receive free test period of 7 days. You\'ll be able to test service quality and make sure your local internet access is \
            sufficient to support IPTV streaming.</p>'
            st.write ('\n')
            st.write ('\n')
            st.markdown(row, unsafe_allow_html=True)
        with col4:
            st.write ('\n')
            st.image('images/freetrial.png',width=200)
        st.write ('\n')

        #---------------  ROW 8  -------------------
        col1, col2, col3 = st.columns([2,1.5,2])
        with col2:
            st.write ('\n')
            st.image('images/register.png',width=200)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 9  -------------------
        col1, col2, col3 = st.columns([2,1.2,1.8])
        with col1:
            st.image('https://i.ibb.co/NjSvDkZ/soccer2.jpg',width=300)
        with col3:
            st.image('https://i.ibb.co/LSjt23q/Olympiakos-Argentinian-midfielder-Alejandro-Dominguez-C-celebrates-with-teammates-after-scoring-a-go.jpg',width=350)
        st.write ('\n')


        #---------------  EMAIL US  -------------------
        col1, col2, col3 = st.columns([1.5,1,1])
        with col2:
            st.image('images/email.png',width=100)

        col1, col2, col3 = st.columns([.9,1,1])
        with col2:
            row = '<p style="text-align: center;font-family:sans-serif; color:Grey; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;"> \
                <b>4hometv10@gmail.com</b></p>'
            st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        

        st.markdown("---")
        st.write ('\n')



    #----------------------------------------------------------------------------------#
    #                                     REGISTER                                     #
    #----------------------------------------------------------------------------------#
    def register():

        st.write ('\n')
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Register</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        with st.form('Form'):

            #---------------  ROW 1  -------------------
            col1, col2, col3, col4 = st.columns([.8,1,1.4,.8])
            with col1:
                fname = st.text_input(label='First Name')
            with col2:
                lname = st.text_input(label='Last Name')
            with col3:
                email = st.text_input(label='Email Address')
            with col4:
                phone = st.text_input(label='Phone Number')            


            submitted = st.form_submit_button('Submit')
            if submitted:
                #---------------  Validate First Name  -------------------
                if len(fname) == 0:
                    st.write ('Error! Please enter your First Name!')

                #---------------  Validate Last Name  -------------------
                if len(lname) == 0:
                    st.write ('Error! Please enter your Last Name!')

                #---------------  Validate Email Address  -------------------
                if len(email) > 0:
                    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
                    if match:
                        st.write ("Email: ", match.group())
                    else:
                        st.write ("Email Address is not valid! Please re-enter!")
                else:
                    st.write ('Error! Please enter your Email Address!')

                #---------------  Validate Phone Number  -------------------
                if len(phone) > 9:
                    match = re.match(r"^\(*\+*[1-9]{0,3}\)*-*[1-9]{0,3}[-. /]*\(*[2-9]\d{2}\)*[-. /]*\d{3}[-. /]*\d{4} *e*x*t*\.* *\d{0,4}$", phone)
                    if match:
                        st.write ("Phone Number: ", phone)
                    else:
                        st.write ("Phone Number is not valid! Please re-enter!")
                else:
                    st.write ('Error! Please re-enter your Phone Number!')






    #----------------------------------------------------------------------------------#
    #                                       MAIN                                       #
    #----------------------------------------------------------------------------------#

    display_header()

    # xSelection = st.sidebar.radio("Select your List", ('Users','Devices','Admin')) 

    # if xSelection == 'Users':
    #     display_gsheet (xSelection)
    # elif xSelection == 'Devices': 
    #     display_gsheet (xSelection)
    # elif xSelection == 'Admin': 
    #     pwd = st.sidebar.empty()
    #     t = pwd.text_input("Enter Password")
    #     if t != "":
    #         if t == 'nella1':
    #             pwd.empty()
    #             display_gsheet (xSelection)


    st.sidebar.markdown('---')

    # if st.sidebar.checkbox("Register"):
    #     register()
    # else:
    #     display_about()

    display_about()


