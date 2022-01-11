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
    #                                  DISPLAY HEADER                                  #
    #----------------------------------------------------------------------------------#
    def display_header2():

        #---------------  HEADER ROW 1  -------------------
        col1, col2, col3 = st.columns([.1,5,0.1])
        with col2:
            img = Image.open("images/premier-league-0.png")
            st.image(img,width=900)

        st.write ('\n')



    #----------------------------------------------------------------------------------#
    #                                     Signup                                       #
    #----------------------------------------------------------------------------------#
    def Signup ():

        display_header()

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

        display_header()

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

        display_header()

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

        display_header()

        df = pd.read_csv('4hometv_channels.csv')
        xAllRows = df.shape[0]
        xRows = 0

        st.write ('\n')
        st.write ('\n')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image('images/channels.png',width=500)


        st.write ('\n')
        col1, col2, col3, col4 = st.columns([1,.2,1.2,.8])
        with col1:
            xSelection = st.radio("Select Channel Groups to Display:", ('All Groups','Select a Group')) 
        with col3:
            if xSelection == 'Select a Group':
                xGroup = df['Group'].unique().tolist()
                # xGroup.insert(0,'All')
                xGroupChoice = st.selectbox('Select Group:', xGroup)
                # st.title('Channel Group: ' + xGroupChoice)
                st.write ('\n')

                # if xGroupChoice != 'All':
                df = df.loc[(df['Group'] == xGroupChoice)]
                xRows = df.shape[0]


        st.write ('\n')
        st.write ('\n')
        col1, col2, col3 = st.columns([2,1,2])
        with col1:
            row = f'<p style="text-align: left;font-family:sans-serif; color:black; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;">Total Channels Available: <b>{xAllRows}</b></p>'
            st.markdown(row, unsafe_allow_html=True)
        with col3:
            if xRows > 0:
                row = f'<p style="text-align: right;font-family:sans-serif; color:black; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;">Group: {xGroupChoice} Available Channels: <b>{xRows}</b></p>'
                st.markdown(row, unsafe_allow_html=True)


        xList1 = []
        xList2 = []
        xItem = 0

        for index, row in df.iterrows():
            xItem += 1
            xList1.append (str(row["ChannelNo"]) + '. ' + row["Channel"])
            xList1.append (row["Group"])
            if xItem > 2:
                xList2.append (xList1)
                xList1 = []
                xItem = 0
        xList2.append (xList1)

        df2 = pd.DataFrame(xList2)
        df2.rename(columns = 
            {0: 'Channel1',
             1: 'Group1',
             2: 'Channel2',
             3: 'Group2',
             4: 'Channel3',
             5: 'Group3'},
             inplace=True)

        # AgGrid(df2)

        style_group = JsCode(
            """
            function(params) {return {'color': 'blue'}};
            """
        )
        gb = GridOptionsBuilder.from_dataframe(df2)
        gb.configure_default_column(groupable=True, 
                                        value=True, 
                                        enableRowGroup=True, 
                                        editable=True,
                                        enableRangeSelection=True,
                                    )
        gb.configure_column("Group1", cellStyle=style_group, maxWidth=130)
        gb.configure_column("Group2", cellStyle=style_group, maxWidth=130)
        gb.configure_column("Group3", cellStyle=style_group, maxWidth=130)
        gridOptions = gb.build()
        data = AgGrid(
            df2,
            gridOptions=gridOptions,
            height=850,
            width='100%',
            theme='light',     # valid themes: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
            defaultWidth=25,
            fit_columns_on_grid_load=True, 
            enable_enterprise_modules=True,
            allow_unsafe_jscode=True
        )





    #----------------------------------------------------------------------------------#
    #                            Premier_League_Channels                               #
    #----------------------------------------------------------------------------------#
    def Premier_League_Channels():

        display_header2()

        #---------------  ROW 1  -------------------
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Channels that carry Premier League games</b></p>'
        st.markdown(row, unsafe_allow_html=True)

        #---------------  ROW 2  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Grey; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;"><b>Check all channels as some games may be on different channels</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')


        with st.spinner('Loading Data...Please Wait...'):

            df1 = pd.read_csv('4hometv_EPL.csv')

            gb = GridOptionsBuilder.from_dataframe(df1)
            gb.configure_default_column(groupable=True, 
                                            value=True, 
                                            enableRowGroup=True, 
                                            editable=True,
                                            enableRangeSelection=True,
                                        )
            gb.configure_column("ChannelNo", maxWidth=120)
            gb.configure_column("Channel", maxWidth=320)
            gb.configure_column("Group", maxWidth=500)
            gridOptions = gb.build()
            data = AgGrid(
                df1,
                gridOptions=gridOptions,
                # columnSize="sizeToFit",
                height=1000,
                # width=720,
                theme='fresh',     # valid themes: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
                # defaultWidth=25,
                fit_columns_on_grid_load=True, 
                enable_enterprise_modules=True,
                allow_unsafe_jscode=True
            )

        st.write ('\n')
        st.write ('\n')
        st.write ('\n')





    #----------------------------------------------------------------------------------#
    #                            Premier_League_Channels 0                              #
    #----------------------------------------------------------------------------------#
    def Premier_League_Channels0():

        display_header2()

        #---------------  ROW 1  -------------------
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Channels that carry Premier League games</b></p>'
        st.markdown(row, unsafe_allow_html=True)

        #---------------  ROW 2  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Grey; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;"><b>Check all channels as some games may be on different channels</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')


        with st.spinner('Loading Data...Please Wait...'):

            is_prod = os.environ.get('IS_HEROKU', None)
            if is_prod:
                gc = pygsheets.authorize(service_account_env_var = 'GDRIVE_API_CREDENTIALS') # use Heroku env
            else:    
                gc = pygsheets.authorize(service_file='client_secret_4hometv.json') # using local account credentials

            sheet = gc.open('4HomeTV')
            wks = sheet.worksheet_by_title('EPL')
            df1 = wks.get_as_df()

            gb = GridOptionsBuilder.from_dataframe(df1)
            gb.configure_default_column(groupable=True, 
                                            value=True, 
                                            enableRowGroup=True, 
                                            editable=True,
                                            enableRangeSelection=True,
                                        )
            gb.configure_column("ChannelNo", maxWidth=120)
            gb.configure_column("Channel", maxWidth=320)
            gb.configure_column("Group", maxWidth=500)
            gridOptions = gb.build()
            data = AgGrid(
                df1,
                gridOptions=gridOptions,
                # columnSize="sizeToFit",
                height=800,
                # width=720,
                theme='fresh',     # valid themes: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
                # defaultWidth=25,
                fit_columns_on_grid_load=True, 
                enable_enterprise_modules=True,
                allow_unsafe_jscode=True
            )

        st.write ('\n')
        st.write ('\n')
        st.write ('\n')







    #----------------------------------------------------------------------------------#
    #                            Frequently_Asked_Questions                            #
    #----------------------------------------------------------------------------------#
    def Frequently_Asked_Questions():

        display_header()

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





    #----------------------------------------------------------------------------------#
    #                               Add_Storage_FireTV                                 #
    #----------------------------------------------------------------------------------#
    def Add_Storage_FireTV ():

        display_header()

        #---------------  ROW 1  -------------------
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand1.png")
            st.image(img,width=470)
        st.write ('\n')

        #---------------  ROW 2  -------------------
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
            How to Add USB Flash Storage to Your Amazon Fire TV</p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 3  -------------------
        st.write('In Amazon’s current lineup of Fire TV models, the Fire TV Stick Lite, Fire TV Stick, and the Fire TV Cube support expanding their internal storage through the use of an external USB drive. Doing so allows you to move supported apps onto the external storage device to free up space on the Fire TV Stick and Fire TV Cube’s internal storage space. The Fire TV Stick 4K, while it does support external USB devices to some extent, does not currently support moving apps to external storage. Here are what accessories you need for external storage, instucritions for how to configure your Fire TV device correctly, and how to move apps off of the internal storage.')
        st.write ('\n')
        st.write ('\n')

        st.header('Requirments:')
        st.write ('\n')

        #---------------  ROW 4  -------------------
        st.subheader('USB Drive:')
        link = f'[Link](https://www.amazon.com/Samsung-BAR-Plus-128GB-MUF-128BE4/dp/B07BPG9YX9/ref=sr_1_5?dchild=1&keywords=flash+drive+128gb&qid=1635882803&qsid=139-6605085-6797824&s=electronics&sprefix=flash+drive+1%2Celectronics%2C78&sr=1-5&sres=B00TKFCYP0%2CB097MJK1XZ%2CB07BPG9YX9%2CB07Q5HMXTN%2CB00P8XQPY4%2CB015CH1PJU%2CB07D7PDLXC%2CB08CGXYNKV%2CB07T5XGWZY%2CB07855LJ99%2CB08XQGX99K%2CB007YX9OGW%2CB07TFCQ945%2CB082FGS7Q7%2CB01EZ0X55C%2CB07YYJRXQR%2CB07VQR5MPN%2CB077BGMX8C%2CB075X12NKG%2CB08GYM5F8G&srpt=FLASH_DRIVE)'
        st.markdown(link, unsafe_allow_html=True)
        st.write('Even though the Fire TV Stick and Fire TV Cube’s USB ports are only USB 2.0 ports, it is recommended that you use a USB drive capable of USB 3.0/3.1 speeds. This is because USB 3.0/3.1 drives tend to perform better than USB 2.0 drives, even when connected to USB 2.0 ports. Connecting a poorly performing USB drive to your Fire TV will result in very slow load times for apps that are stored on the drive. It’s best to use a USB 3.0/3.1 Flash Drive from a reputable brand, such as this compact Samsung drive or compact SanDisk drive. The storage capacity of the drive is up to you.')
        st.write ('\n')

        #---------------  ROW 5  -------------------
        st.subheader('OTG Cable:')
        link = f'[Link](https://www.amazon.com/ANDTOBO-Micro-Adapter-Power-Devices/dp/B083M1S6QT/ref=asc_df_B083M1S6QT/?tag=hyprod-20&linkCode=df0&hvadid=459410835726&hvpos=&hvnetw=g&hvrand=12648465173518764459&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9003687&hvtargid=pla-944808289663&th=1)'
        st.markdown(link, unsafe_allow_html=True)
        st.write('To connect the USB drive to the Fire TV, you will need a micro USB OTG cable. For use with a Fire TV Stick, you will need a “Y” cable that includes a power cable, such as this DSYJ OTG Cable or this 2-Pack of AuviPal OTG Cables. For the Fire TV Cube, you can use either a “Y” cable and ignore the extra power cable portion or you can use a straight micro USB OTG cable, like this Monoprice Straight OTG Cable or this 2-Pack of UGREEN Straight OTG Cables.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand2.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 6  -------------------
        st.subheader('Prepare USB Drive:')
        st.write('1. First, connect your OTG cable to your Fire TV Stick or Fire TV Cube and power on the device WITHOUT the USB drive connected.')
        st.write ('\n')
        st.write('2. Once the Fire TV is powered on and at the Home screen, plug the USB drive into the USB OTG cable. You do not need to format the USB drive to a specific file system format ahead of time. The Fire TV will be formatting the drive for you.')
        st.write ('\n')
        st.write('3. If your USB drive was not formatted with the FAT32 file system, you will be asked what you would like to do with the drive. If you want to use the drive for storing apps, you need to select the “Device Storage” option. Your drive will then be erased and formatted to store apps. Note that this means you will not be able to use the drive for anything else unless you later erase/format the drive.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand3.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 7  -------------------
        st.write('If your USB drive was formatted with the FAT32 file system, you will not see the above prompt. Instead, you need to navigate to Settings > My Fire TV > USB Drive and then select the “Format to Internal Storage” option.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand4.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 8  -------------------
        st.write('4. Confirm that you want to format the dirve by selecting “Yes” on the prompt. Once formatted, all files on the drive will be erased. This also means the drive cannot be used to store anything else while it is formatted for Fire TV app storage.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand5.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 9  -------------------
        st.write('5. Depending on the size and speed of the drive, formatting it can take several minutes. Just be patient.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand6.jpeg")
            st.image(img,width=470)
        with col2:
            img = Image.open("images/expand7.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 10  -------------------
        st.header('You can also move Apps to USB:')
        st.write ('\n')
        st.write('1. If you’d like, you can verify that your USB drive is prepared to accept apps by navigating to Settings > My Fire TV > USB Drive. If the option to “Format to External Storage” is present, then the drive is prepared correctly. If not, repeat the prepare steps above.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand8.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 11  -------------------
        st.write('2. To move apps to USB storage, navigate to Settings > Applications > Manage Installed Applications and be sure that the option at the top is set to “Show All Applications.”')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand9.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 12  -------------------
        st.write('3. Scroll down and select the app that you want to move to external storage. To free up the most internal storage space, select an app that has a large “Application:” value. The portion of the app listed under “Data:” or “Cache:” will not be moved to external storage.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand10.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 13  -------------------
        st.write('4. If the app can be moved, the option “Move to USB Storage” will be present. If the option is not there, then the app cannot be moved and must remain on the device’s internal storage. Not all apps can be moved. Select “Move to USB Storage” to begin moving the app.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand11.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 14  -------------------
        st.write('5. The app may take several minutes to move depending on the size of the app and the speed of your USB drive. Just be patient.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand12.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')

        #---------------  ROW 15  -------------------
        st.write('6. Once moved to USB Storage, pressing back to return to the app list will show a USB icon next to the app name, indicating that it is now on external storage. If you install a new app that can be moved to external storage while you have your USB drive connected, the new app will automatically be installed to your external USB drive. Ejecting or removing the USB drive while apps are installed on it will cause those apps to disappear from your Fire TV. When you reconnect the drive, those apps will automatically return. If you need to move the app back to internal storage, repeat this guide but select “Move to internal Storage” during step 4.')
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            img = Image.open("images/expand13.jpeg")
            st.image(img,width=470)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')





    #----------------------------------------------------------------------------------#
    #                                                                                  #
    #----------------------------------------------------------------------------------#
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    #----------------------------------------------------------------------------------#
    #                              MAIN - BEGIN SCRIPT                                 #
    #----------------------------------------------------------------------------------#
    # if "first" not in st.session_state:
    #     st.session_state.first = 'Y'
    
    # if st.session_state.first == 'Y':
    #     st.session_state.first = 'N'
    #     display_header()

    xSelection = st.sidebar.radio("Select Below:", ('How to Sign-up or Renew','Install SmartIPTV App', 
            'Remote Control', 'Available Channels', 'Premier League Channels', 'Frequently Asked Questions', 
            'Add Storage to Fire TV')) 

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
    elif xSelection == 'Add Storage to Fire TV': 
        Add_Storage_FireTV ()
    elif xSelection == 'Premier League Channels': 
        Premier_League_Channels ()


