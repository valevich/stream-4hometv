import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import pygsheets
from pygsheets.datarange import DataRange
import datetime
from PIL import Image
import re
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests
from csv import DictReader
from st_aggrid import AgGrid                                 
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode


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



    #----------------------------------------------------------------------------------#
    #                                     Signup                                       #
    #----------------------------------------------------------------------------------#
    def Signup ():

        st.title ('Get Started with IPTV in 4 Simple Steps')
        st.write ('You’ve probably heard a lot about IPTV streaming lately, but you may not know where to start. IPTVs are getting popular day by day. You can get thousands of live TV channels. Whereas, live TV platforms like Sling TV and fuboTV costs more than $30 per month for around 100+ channels. If you want a reliable IPTV service for your Firestick, read on...')
        st.write ('\n')


        #---------------  ROW 1  -------------------
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/Fire-TV.png")
            st.image(img,width=350)
        #---------------  ROW 2  -------------------
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            st.subheader ('Step 1:  Register and get 7 days Free Trial Subscription')
            st.subheader ('Step 2:  Buy a Fire TV, Google TV or any Android TV device')
            st.subheader ('Step 3:  Download and Install IPTV App')
            st.subheader ('Step 4:  Activate Device MAC Address')
        #---------------  ROW 3  -------------------
        col1, col2, col3 = st.columns([1.2,2,.8])
        with col2:
            img = Image.open("images/Google-TV.jpeg")
            st.image(img,width=300)

        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')


        st.title ('How to Renew your account')
        # st.write ('You can use Paypal to send payment as indicated below...')
        # st.write ('\n')
        #---------------  PAYPAL  -------------------

        col1, col2, col3 = st.columns([.5,2,3])
        with col2:
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20;"> \
                Send payments to account: <b>@4hometv</b></p>'
            st.markdown(row, unsafe_allow_html=True)
        with col3:
            lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_9l396Q.json")
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                renderer="svg", # canvas
                height=300,
                width=300,
                key=None,
            )

        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
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




    #----------------------------------------------------------------------------------#
    #                                 Install_IPTV_App                                 #
    #----------------------------------------------------------------------------------#
    def Install_IPTV_App():

        #---------------  Install_IPTV ROW 1  -------------------
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/watch_smartiptv.png")
            st.image(img,width=470)
        st.write ('\n')

        #---------------  Install_IPTV ROW 2  -------------------
        st.write('This is a step-by-step guide on how to install SmartIPTV on FireStick, Fire TV, and Fire TV Cube. \
            SmartIPTV is available on FireStick devices and works as an IPTV management service. \
            It also offers a 7 days free trial so that you can explore it well before paying for the subscription. \
            It costs about 5.49 EUR or $6.67 per each device.')
        st.write('Follow these steps to install Smart IPTV:')
        st.write ('\n')

        #---------------  Install_IPTV Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('From FireStick Home click on Settings')
        with col3:
            img = Image.open("images/Step1-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Go to “My Fire TV”')
        with col3:
            img = Image.open("images/Step2-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Access to the “Developer Options”')
        with col3:
            img = Image.open("images/Step3-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Click on “Apps from unknown sources”')
        with col3:
            img = Image.open("images/Step4-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('You will be prompted towards a message, Click “Turn ON”')
        with col3:
            img = Image.open("images/Step5-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Return to Home > then Click on the Search icon at the top > then search for “Downloader”')
        with col3:
            img = Image.open("images/Step6-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Select the Downloader app from the list')
        with col3:
            img = Image.open("images/Step7-install.png")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 8  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 8</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Click on "Get" or "Download"')
        with col3:
            img = Image.open("images/Step8-install.png")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 9  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 9</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once downloaded, click "Open"')
        with col3:
            img = Image.open("images/Step9-install.png")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 10  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 10</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('On Downloader Home menu, insert this URL "apk.siptv.app" and click "Go"')
        with col3:
            img = Image.open("images/Step10-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 11  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 11</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Wait until the Smart IPTV app is downloaded')
        with col3:
            img = Image.open("images/Step11-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 12  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 12</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Downloader application will prompt to install Smart IPTV. Click “Install”')
        with col3:
            img = Image.open("images/Step12-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 13  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 13</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once installed click “Done”')
        with col3:
            img = Image.open("images/Step13-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 14  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 14</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now press “Delete” to delete installation temp file.')
        with col3:
            img = Image.open("images/Step14-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Step 15  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 15</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('The “Delete” message will prompt again. So press "Delete" again')
        with col3:
            img = Image.open("images/Step15-install.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')

        #---------------  Install_IPTV Step Done  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Done</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now you have installed the Smart IPTV app on FireStick!')
        with col3:
            lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/temp/lf20_MqU2rh.json")
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                renderer="svg", # canvas
                height=150,
                width=150,
                key=None,
            )
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"> \
            <b>How to Access and Use Smart IPTV on FireStick</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')
        st.write ('Here are the steps you need to follow in order to access and use Smart IPTV on FireStick:')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  Install_IPTV Access 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press on the Home button in your FireStick remote and select Apps')
        with col3:
            img = Image.open("images/Access-Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Access 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Select Smart IPTV app from the list')
        with col3:
            img = Image.open("images/Access-Step2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Access 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Open the app and you will see this screen the first time you open Smart IPTV (Note down the Mac Address)')
        with col3:
            img = Image.open("images/Access-Step3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Install_IPTV Access 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now please Register, then Click on Account and Login. Then you can add your device type and MAC Address.')
        with col3:
            img = Image.open("images/Access-Step4.png")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  Install_IPTV Access 5  -------------------
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            # row = '<p style="text-align: left;color:Blue;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
            #     All set! Your account will be activated shortly and you will be notified by email!</p>'
            row = '<p style="text-align: center;font-family:sans-serif; color:Blue; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"> \
                <b>All set! Your account will be activated shortly and you will be notified by email!</b></p>'
            st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  Install_IPTV Access 6  -------------------
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
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')


        #---------------  Buy SmartIPTV App  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"> \
            <b>How to Purchase and Activate SmartIPTV app</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  SmartIPTV Purchase  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            # row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
            #     Visit https://siptv.app/activation/ to activate Smart IPTV and enter your Mac address</p>'
            # st.markdown(row, unsafe_allow_html=True)
            # st.write ('\n')
            st.write('Visit https://siptv.app/activation/ to activate Smart IPTV and enter your Mac address.')
            st.write('Now you need to enter your payment information. Smart IPTV costs 5.49 EUR or $6.67.')
        with col3:
            img = Image.open("images/SmartIPTV.png")
            st.image(img,width=500)
        st.write ('\n')




    #----------------------------------------------------------------------------------#
    #                                   Remote_Control                                 #
    #----------------------------------------------------------------------------------#
    def Remote_Control():

        #---------------  Remote_Control Image  -------------------
        st.write ('\n')
        st.write ('\n')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image('images/firestick_smartiptv1.png',width=300)
        with col3:
            st.write ('\n')
            st.write ('\n')
            lottie2 = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_cvMXoy.json")
            st_lottie(
                lottie2,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                renderer="svg", # canvas
                height=150,
                width=150,
                key=None,
            )
        st.write ('Here we have a quick guide on how to use the firestick remote with the smart IPTV app to make it easy for you to pick up the controls and be changing the channel like a pro in no time.')

        st.write ('\n')
        st.write ('\n')

        #---------------  Remote_Control Row 1  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to bring up channel list and choose another channel</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press OK center button')
        with col3:
            img = Image.open("images/remote1.jpeg")
            st.image(img,width=150)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 2a  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to add channel to Favorites</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press OK, then highlight a channel and long press OK button and choose Add Favorite')
        with col3:
            img = Image.open("images/remote2a.png")
            st.image(img,width=300)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 2b  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to bring channel groups up</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press ok, then press the Play button')
        with col3:
            img = Image.open("images/remote2b.png")
            st.image(img,width=300)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 3  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to go Up or Down a channel</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press Left or Right on the remote')
        with col3:
            img = Image.open("images/remote3.png")
            st.image(img,width=300)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 4  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to skip through the channel list faster</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press OK then press Left or Right')
        with col3:
            img = Image.open("images/remote4.png")
            st.image(img,width=350)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 5  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to bring up the TV Guide for certain channels</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press OK then go to the channel and press the Menu button')
        with col3:
            img = Image.open("images/remote5.png")
            st.image(img,width=300)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 5b  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to watch Archive up to 7 days.</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press Menu button to see Guide then select any program in the past. You may use Right or Left button to change the date which you can see in the top right corner.')
        with col3:
            img = Image.open("images/remote5b.png")
            st.image(img,width=350)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 6  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to bring up the last viewed channels</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press Down on the remote')
        with col3:
            img = Image.open("images/remote6.jpeg")
            st.image(img,width=150)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 7  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to change the picture size</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press the Fast Forward button')
        with col3:
            img = Image.open("images/remote7.jpeg")
            st.image(img,width=150)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 8  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to change the volume using the firestick remote</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Hold the Up or Down button on the remote')
        with col3:
            img = Image.open("images/remote8.png")
            st.image(img,width=300)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')

        #---------------  Remote_Control Row 9  -------------------
        col1, col2, col3 = st.columns([4,.5,2])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 24px;"> \
                How to Exit the Smart IPTV app</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Press the Home button')
        with col3:
            img = Image.open("images/remote9.jpeg")
            st.image(img,width=150)
        st.write ('\n')
        st.markdown("---")
        st.write ('\n')





    #----------------------------------------------------------------------------------#
    #                                Available_Channels                                #
    #----------------------------------------------------------------------------------#
    def Available_Channels():

        df = pd.read_csv('4hometv_channels.csv')
        xRows = df.shape[0] * 3

        st.write ('\n')
        st.write ('\n')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image('images/channels.png',width=500)

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.write ('\n')
            st.write ('\n')
            row = f'<p style="text-align: center;font-family:sans-serif; color:black; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 20px;">Total Channels Available: <b>{xRows}</b></p>'
            st.markdown(row, unsafe_allow_html=True)


        font_color = [['black'],['blue'],['black'],['blue'],['black'],['blue']]
        fig = go.Figure(data=[go.Table(
            columnwidth=[1.2,.8,1.2,.8,1.2,.8],
            header=dict(values=list(['Channel', 'Group', 'Channel', 'Group', 'Channel', 'Group']),
                        fill_color='paleturquoise',
                        font=dict(color='black', family='Arial, sans-serif', size=9),
                        align='center'),
            cells=dict(values=[df.Channel1, df.Group1, df.Channel2, df.Group1, df.Channel3, df.Group3],
                    fill_color='lavender',
                    font_color=font_color,
                    height=25,
                    font=dict(size=11),
                    align = ['left', 'center', 'left', 'center', 'left', 'center']
                )
            )
        ])
        fig.update_layout(margin=dict(l=0,r=0,b=5,t=5), width=1000,height=2000)
        st.write(fig)




    #----------------------------------------------------------------------------------#
    #                            Frequently_Asked_Questions                            #
    #----------------------------------------------------------------------------------#
    def Frequently_Asked_Questions():

        #---------------  ROW 1  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Frequently Asked Questions</b></p>'
        st.markdown(row, unsafe_allow_html=True)

        #---------------  IMAGE  -------------------
        st.write ('\n')
        col1, col2, col3 = st.columns([1,1,1])
        st.write ('\n')
        with col2:
            img = "https://i.ibb.co/bg5kkBR/faq.png"
            st.image(img,width=320)
        st.write ('\n')

        #---------------  FAQ 1  -------------------
        row = '<p style="text-align: left;font-family:sans-serif; color:Blue; margin-top: 100; margin-bottom: 0; line-height: 80px; font-size: 18px;"> \
            <b>1. Requirements for IPTV Service?</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        row = '<p style="text-align: left;font-family:sans-serif; color:Black; margin-top: 0; margin-bottom: 0; line-height: 0px; font-size: 14px;"> \
            In fact, to use IPTV you need to be equipped with a high speed broadband connection. Speed of the broadband connection should be at least 4Mbps.</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  FAQ 2  -------------------
        row = '<p style="text-align: left;font-family:sans-serif; color:Blue; margin-top: 100; margin-bottom: 0; line-height: 80px; font-size: 18px;"> \
            <b>2. Can I use the subscription on multiple devices?</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        row = '<p style="text-align: left;font-family:sans-serif; color:Black; margin-top: 0; margin-bottom: 0; line-height: 0px; font-size: 14px;"> \
            Well, you can use your IPTV subscription on multiple devices. However, you will only be able to watch the content on two devices at the same time.</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  FAQ 3  -------------------
        row = '<p style="text-align: left;font-family:sans-serif; color:Blue; margin-top: 100; margin-bottom: 0; line-height: 80px; font-size: 18px;"> \
            <b>3. Can you cancel a subscription?</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        row = '<p style="text-align: left;font-family:sans-serif; color:Black; margin-top: 0; margin-bottom: 0; line-height: 0px; font-size: 14px;"> \
            Your subscription will be automatically cancelled on expiration date.</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  FAQ 4  -------------------
        row = '<p style="text-align: left;font-family:sans-serif; color:Blue; margin-top: 100; margin-bottom: 0; line-height: 80px; font-size: 18px;"> \
            <b>4. Should we use Wi-Fi or Ethernet?</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        row = '<p style="text-align: left;font-family:sans-serif; color:Black; margin-top: 0; margin-bottom: 0; line-height: 0px; font-size: 14px;"> \
            We always recommend that you connect your device hardware (ethernet) but it works just fine with Wi-Fi.</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        #---------------  FAQ 5  -------------------
        row = '<p style="text-align: left;font-family:sans-serif; color:Blue; margin-top: 100; margin-bottom: 0; line-height: 80px; font-size: 18px;"> \
            <b>5. What happens when video keeps buffering?</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        row = '<p style="text-align: left;font-family:sans-serif; color:Black; margin-top: 0; margin-bottom: 0; line-height: 20px; font-size: 14px;"> \
            Most likely your internet connection is not reliable. You can check your internet speed. If the speed and connection is reliable and you still continue to have issues, please contact us below.</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')

        st.markdown("---")
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





    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    #----------------------------------------------------------------------------------#
    #                              MAIN - BEGIN SCRIPT                                 #
    #----------------------------------------------------------------------------------#
    display_header()

    xSelection = st.sidebar.radio("Select Below:", ('How to Sign-up or Renew','Install SmartIPTV App', 'Remote Control', 'Available Channels', 'Frequently Asked Questions')) 
    # xSelection = st.sidebar.radio("Select Below:", ('Install IPTV App', 'Activate Device', 'Remote Control', 'Available Channels', 'Frequently Asked Questions')) 

    if xSelection == 'How to Sign-up or Renew':
        Signup ()
    elif xSelection == 'Install SmartIPTV App': 
        Install_IPTV_App ()
    elif xSelection == 'Remote Control': 
        Remote_Control ()
    elif xSelection == 'Available Channels': 
        Available_Channels ()
    elif xSelection == 'Frequently Asked Questions': 
        Frequently_Asked_Questions ()


