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
        col1, col2, col3 = st.columns([.5,4,.5])
        with col2:
            st.subheader ('Step 1:  Buy a Fire TV, Google TV or any Android TV device.')
            st.subheader ('Step 2:  Register and get 7 days Free Trial Subscription.')
            st.subheader ('Step 3:  Download and Install IPTV App.')
            st.subheader ('Step 4:  Receive a Playlist link and add it to IPTV app.')
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


        st.title ('How to Activate or Renew your account')

        #---------------  PAYPAL  -------------------
        col1, col2, col3 = st.columns([.5,2,3])
        with col2:
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20;"> \
                Send payments to account: <b>@4hometv</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20;"> \
                or</p>'
            st.markdown(row, unsafe_allow_html=True)
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20;"> \
                <b>info@nellatech.com</b></p>'
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
    #                                 Install_IPTV_Apps                                #
    #----------------------------------------------------------------------------------#
    def Install_IPTV_Apps():

        #----------------------        Install_Downloader_App        ----------------------#
        col1, col2, col3 = st.columns([2,5,.5])
        with col1:
            img = Image.open("images/downloader1.png")
            st.image(img,width=200)
        with col2:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 20px; font-size: 22px;"> \
                <b>1. Install Downloader App on Firestick</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write ('The Downloader app is officially available on Amazon Store. You don’t have to side-load it onto your device. Here is how you can install the app:')
            result1 = st.button ("Read",1)
        st.write ('\n')

        #----------------------        Enable_ThirdParty_Apps        ----------------------#
        col1, col2, col3 = st.columns([2,5,.5])
        with col1:
            img = Image.open("images/firestick1.jpeg")
            st.image(img,width=200)
        with col2:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 20px; font-size: 22px;"> \
                <b>2. Enable Third-Party Apps on Firestick</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write ('For any apps not available on the Amazon App Store, you have to make a few adjustments to your device. Here’s how to enable third-party apps in Settings:')
            result2 = st.button ("Read",2)
        st.write ('\n')
        st.write ('\n')

        #----------------------        Install_IPTV_Player        ----------------------#
        col1, col2, col3 = st.columns([2,5,.5])
        with col1:
            img = Image.open("images/IPTV_Players.jpeg")
            st.image(img,width=200)
        with col2:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 20px; font-size: 22px;"> \
                <b>3. Install IPTV Player on Firestick</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write ("IPTV Player is required to play IPTV channels from your current subscription. You will find the installation and setup procedure in these guides below.  \
                       Choose one of our recommended IPTV players below and click 'Read' to see it's installation guide.")
 
        st.write ('\n')


        #---------------  IPTV Players  -------------------
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            img = Image.open("images/Tivimate.png")
            st.image(img,width=158)
            st.write('Price: Free or $24.99 for up to 5 devices')
            result3 = st.button ("Read",3)
        with col2:
            img = Image.open("images/SmartIPTV_Logo.png")
            st.image(img,width=150)
            st.write('Price: $6.00 per device')
            result4 = st.button ("Read",4)
        with col3:
            img = Image.open("images/Televizo.png")
            st.image(img,width=150)
            st.write('Price: Free')
            result5 = st.button ("Read",5)
        st.write ('\n')


        st.write ('\n')
        st.markdown("---")
        st.write ('\n')



        if result1:
            Install_Downloader_App()
        elif result2:
            Enable_ThirdParty_Apps()
        elif result3:
            Install_Tivimate()
        elif result4:
            Install_SmartIPTV()
        elif result5:
            Install_Televizo()






    #----------------------------------------------------------------------------------#
    #                              Install_Downloader_App                              #
    #----------------------------------------------------------------------------------#
    def Install_Downloader_App():

        st. title("Install Downloader App on Firestick")
        st.write ('\n')
        st.write ('\n')

        #---------------  Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Go to the home screen of Fire TV and then Use your remote to navigate to Find > Search on the menu bar in the middle of the screen.')
        with col3:
            img = Image.open("images/Downloader_Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now type in ‘Downloader’ (without the quotes of course) using the onscreen keypad (use the remote to navigate to the letters. \
                      \nYou should see the app suggestions on the list that show up as you begin typing. When you see ‘Downloader’ on the list, select and open it.')
        with col3:
            img = Image.open("images/Downloader_Step2.jpeg")
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
            st.write('You should now see ‘Downloader’ appear under the ‘APPS & GAMES’ section. Go ahead and click it.')
        with col3:
            img = Image.open("images/Downloader_Step3.jpeg")
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
            st.write("Now click the ‘Get’ or ‘Download‘ button to download and install the app. You should have the app in no more than a couple of minutes.")
        with col3:
            img = Image.open("images/Downloader_Step4.jpeg")
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
            st.write("Once the app is installed, click Open. You can always find it on the home screen among the recently installed apps or in Apps.\
                      When you open the app for the first time, you may see the ‘Update Notes for Downloader’ pop-up. Go ahead and read it if you want to, or simply click ‘OK’ to proceed.")
        with col3:
            img = Image.open("images/Downloader_Step5.png")
            st.image(img,width=500)
        st.write ('\n')

        st.write ("Now, before we get started with Downloader, there is one little tweak to the app I would suggest you make—Enable JavaScript.  If this option remains unchecked, some of the websites will not download properly in Downloader.")
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
            st.write("Here is how you can enable JavaScript: \
                    \n   1. Open Downloader \
                    \n   2. On the left sidebar you should see the option ‘Settings’; select it \
                    \n   3. Check the box next to Enable JavaScript in Settings.")
        with col3:
            img = Image.open("images/Downloader_Step6.jpeg")
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
            st.write("Click ‘Yes’ when you see the warning message. Again, don’t worry about the warning. \
                      Keep this option checked, most browsers keep JavaScript enabled by default")
        with col3:
            img = Image.open("images/Downloader_Step7.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        st.write ('Now you need to Enable Third-Party Apps on Firestick. Follow instructions in the next step.')





    #----------------------------------------------------------------------------------#
    #                            Enable_ThirdParty_Apps()                              #
    #----------------------------------------------------------------------------------#
    def Enable_ThirdParty_Apps():

        st. title("Enable Third-Party Apps on Firestick")
        st.write ('\n')
        
        #---------------  ROW 1  -------------------
        st.write('By default, FireStick doesn’t allow users to install third-party apps for security reasons. \
            Therefore, you won’t be able to sideload applications using Downloader until you make a few tweaks. \
            To install APKs via Downloader hassle-free, you’ll need to allow FireStick to install apps from unknown, or third-party, sources.')
        st.write('Follow these steps to install Smart IPTV:')
        st.write ('\n')

        #---------------  Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Launch your FireStick home screen and navigate to the settings icon.')
        with col3:
            img = Image.open("images/ThirdParty_Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Scroll down to the My Fire TV banner and click on it.')
        with col3:
            img = Image.open("images/ThirdParty_Step2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Click on Developer Options.')
        with col3:
            img = Image.open("images/ThirdParty_Step3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Select Install unknown apps.')
        with col3:
            img = Image.open("images/ThirdParty_Step4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Navigate to Downloader and select it to turn it ON.')
        with col3:
            img = Image.open("images/ThirdParty_Step5.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        st.write ('Press Home button and proceed to next step to Download IPTV app to Firestick.')





    #----------------------------------------------------------------------------------#
    #                                  Install_Tivimate                                #
    #----------------------------------------------------------------------------------#
    def Install_Tivimate():

        st. title("Install Tivimate Player")
        st.write ("TiviMate is an IPTV player that allows you to integrate third-party IPTV services with M3U links. \
                   So, first, we will download TiviMate on FireStick, and then we’ll use an IPTV service to enable the player’s capabilities. \
                   TiviMate offers a premium version as well. If you decide you’re going to use TiviMate regularly, I advise shelling out a few bucks for the advanced features.")
        st.write ('\n')
        st.write ('\n')

        #---------------  Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('From Home menu, select "Downloader" to open app. It can also be accessed from your Apps menu. ')
        with col3:
            img = Image.open("images/SmartIPTV_Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('On Downloader Home menu, insert this URL "https://is.gd/tivimate3" and click "Go"')
        with col3:
            img = Image.open("images/Tivimate_Step2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Wait until the Tivimate app is downloaded')
        with col3:
            img = Image.open("images/SmartIPTV_Step3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Downloader application will prompt to install Tivimate. Click “Install”')
        with col3:
            img = Image.open("images/Tivimate_Step4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once installed click “Done”')
        with col3:
            img = Image.open("images/SmartIPTV_Step5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now press “Delete” to delete installation temp file.')
        with col3:
            img = Image.open("images/Tivimate_Step6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('The “Delete” message will prompt again. So press "Delete" again')
        with col3:
            img = Image.open("images/SmartIPTV_Step7.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')


        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"> \
            <b>How to Access and Use Tivimate on FireStick</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')
        st.write ('Here are the steps you need to follow in order to access and use Tivimate on FireStick:')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  Tivimate Access 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('1. You may go to the Settings >> Applications >> Manage Installed Applications > Smart IPTV > Launch application OR \
                      \n2. You may hold down the Home button on the remote for a few seconds. A popup is displayed. Choose Apps OR \
                      \n3. Go ahead and click the 3-dot button on the FireStick home screen')
        st.write ('\n')
        with col3:
            img = Image.open("images/SmartIPTV_Access1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now, scroll, and on the bottom, you will find Tivimate.')
        with col3:
            img = Image.open("images/Tivimate_Access2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('You may also move this app on the home screen for quick and easy access. Simply press the menu button on the remote and click Move on the popup window on the TV. Now, place Tivimate in the first or second row.')
        with col3:
            img = Image.open("images/Tivimate_Access3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now you can comfortably access TiviMate Player from your FireStick home screen. There’s no need to go through a menu each time.')
        with col3:
            img = Image.open("images/Tivimate_Access4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Open the TiviMate app.')
        with col3:
            img = Image.open("images/Tivimate_Access5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Select Add playlist.')
        with col3:
            img = Image.open("images/Tivimate_Access6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('TiviMate will ask you to add a playlist using an M3U link, Xtream code, or Stalker Portal. \nSelect the M3U playlist. \
                      When you subscribe to an IPTV service, you will receive an email with relevant login information and an M3U link.')
        with col3:
            img = Image.open("images/Tivimate_Access7.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 8  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 8</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('TiviMate will ask you to type in your M3U link. Enter your M3U link and press Next.')
        with col3:
            img = Image.open("images/Tivimate_Access8.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 9  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 9</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('TiviMate will load the IPTV service and offer a peek at the number of channels and movies available in the IPTV package.')
        with col3:
            img = Image.open("images/Tivimate_Access9.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 10  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 10</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Add a Playlist name.')
        with col3:
            img = Image.open("images/Tivimate_Access10.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 11  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 11</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('If the playlist is finished processing, select Done.')
        with col3:
            img = Image.open("images/Tivimate_Access11.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Access 12  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 12</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('A minute or two later, you will see the IPTV service’s content appearing in the TiviMate app. \
                      Most IPTV services come with a dedicated EPG (electronic program guide), as shown here.')
        with col3:
            img = Image.open("images/Tivimate_Access12.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')

        st.title ('All Done!')
        st.write ('The major features of TiviMate are behind a paywall. You need to pay for the premium version to enjoy TiviMate at its greatest potential. \
                   When you try to access any premium feature without a premium account, TiviMate will ask you to upgrade to premium. For example, when you try \
                   to add a channel to your list of favorites, TiviMate will prompt you to upgrade the app. \
                   If you wish to continue with the free version, you can hit Cancel and keep using the free TiviMate app on FireStick.')

        st.write ('\n')
        st.write ('To purchase the premium version, you need to use the TiviMate Companion app from the Google Play Store. Here’s how to do it.')
        st.write ('\n')
        st.write ('\n')
        st.subheader ("Install 'TiviMate Companion' App From Google Play Store")

        st.write ('\n')
        st.write ('To purchase the premium version, you need to use the TiviMate Companion app from the Google Play Store. Here’s how to do it.')

        st.write ('\n')
        st.write ('Follow the steps below to purchase a TiviMate Premium subscription using the TiviMate Companion app.')

        st.write ('\n')
        st.write ('1. Open the Play Store on your Android device. \
                   \n2. Tap on the search bar at the top and search for TiviMate Companion. \
                   \n3. Download and install the TiviMate Companion app on your device. \
                   \n4. Open the app. It will ask you to create an account. Click the Account button. \
                   \n5. Click Sign up and follow the steps to create an account. \
                   \n6. Sign in using your account credentials. You may then pay for a one-year subscription using a credit or debit card.')

        st.write ('\n')
        st.write ('\n')
        st.subheader ("Unlock TiviMate Premium on FireStick")
        st.write ('Now that you have purchased TiviMate Premium using an Android device, it’s time to activate the premium subscription on your \
                   FireStick for a flawless IPTV experience. Go through the steps below.')
        st.write ('\n')


        #---------------  Tivimate Premium 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Open the TiviMate app on your FireStick.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Premium1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Premium 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('As soon as you try to use any of the premium features, TiviMate will ask you to unlock the feature by subscribing. \
                      Glance through all the Premium features and hit the Next button.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Premium2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Premium 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('The following screen will ask you to buy TiviMate Premium using the Android TiviMate Companion app. We have already done that. Click on the Account button.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Premium3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Premium 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Add your TiviMate account Email and Password and click on Log in.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Premium4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        st.write ('That’s it. You have successfully activated TiviMate Premium on FireStick. \
                   You can now enjoy all the features of the TiviMate IPTV player with your choice of IPTV provider.')


        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.subheader ("TiviMate Details and Features")
        st.write ('TiviMate is an IPTV player that allows you to have nonstop streaming. The app is compatible with many devices including FireStick. \
                   The interface of TiviMate is unique and specially designed for the big screens to give you the best streaming experience. \
                   It is user-friendly and works great on various devices including FireStick. Navigation of the app is easy and practical \
                   with all the necessary buttons and options.')
        st.write ('\n')
        st.write ('\n')


        #---------------  Tivimate Features1   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Record Content</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('TiviMate IPTV Player allows you to record content to view it later. If you don’t have time and want to watch something later, \
                      you can hit the Record button in the video player and view it later from the Recordings tab on the home screen of the TiviMate app.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features2   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Enable Subtitles</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('This one is quite useful when you’re watching content that’s not in your native language. From the player menu, \
                      simply hit the CC (closed captions) button and enable subtitles from the sliding menu.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features3   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Add to Favorites</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('There are multiple ways to add a channel to your favorites in the TiviMate Player app. \
                      Our go-to method is using the Add to Favorites button within the video player.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features4   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Multi-view Mode</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('If you want to view multiple channels at once, TiviMate has an option for that as well. From the player menu, \
                you can select Multi-view and select another channel to view two channels at the same time.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features5   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Sleep Timer</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('This is a must-have for any IPTV app. A sleep timer turns off the app after a set amount of time. \
                I’m glad to see the sleep timer built right into the player menu. Simply press the stopwatch icon on the video player screen and select the time from the right side menu.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features6   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Sleep Timer</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Users can automatically put the TiviMate app to sleep in anywhere from 15 minutes to 240 minutes. \
                This feature is useful, for example, when children are watching TV before bed. You can put a half-hour timer and shut down the app.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features7   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Check Video Details</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('By default, the TiviMate Player offers details on video quality, number of frames per second (FPS), and sound quality.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features7.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Tivimate Features8   -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 20px;"> \
                Change App Appearance</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Not a fan of the default look and theme of the TiviMate app? Go to Settings and you can easily change multiple aspects of the current \
                      look, such as the TV guide, font size, background color, and even selection color.')
        st.write ('\n')
        with col3:
            img = Image.open("images/Tivimate_Features8.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')

        st.write ('The list above is just the tip of the iceberg for the TiviMate app. Using the premium subscription, \
                   you can unlock dozens of useful features for the app. For more details, check out the TiviMate overview section in the article.')


        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')








    #----------------------------------------------------------------------------------#
    #                                  Install_SmartIPTV                               #
    #----------------------------------------------------------------------------------#
    def Install_SmartIPTV():

        st. title("Install SmartIPTV Player")
        st.write ("Smart IPTV is a paid service. However, there are NO recurring charges. You just need to pay a one-time activation fee of 5.49 EUR or about 6.00 USD. \
                   Use the MAC address in your Smart IPTV app to activate Smart IPTV paid service. \
                   There is a free 7-day trial as well, which you can explore before buying the paid subscription. You may start the trial with the same MAC address.")
        st.write ('\n')

        #---------------  Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('From Home menu, select "Downloader" to open app. It can also be accessed from your Apps menu. ')
        with col3:
            img = Image.open("images/SmartIPTV_Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('On Downloader Home menu, insert this URL "apk.siptv.app" and click "Go"')
        with col3:
            img = Image.open("images/SmartIPTV_Step2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Wait until the Smart IPTV app is downloaded')
        with col3:
            img = Image.open("images/SmartIPTV_Step3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Downloader application will prompt to install Smart IPTV. Click “Install”')
        with col3:
            img = Image.open("images/SmartIPTV_Step4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once installed click “Done”')
        with col3:
            img = Image.open("images/SmartIPTV_Step5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now press “Delete” to delete installation temp file.')
        with col3:
            img = Image.open("images/SmartIPTV_Step6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('The “Delete” message will prompt again. So press "Delete" again')
        with col3:
            img = Image.open("images/SmartIPTV_Step7.jpeg")
            st.image(img,width=500)
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

        #---------------  SmartIPTV Access 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('1. You may go to the Settings >> Applications >> Manage Installed Applications > Smart IPTV > Launch application OR \
                      \n2. You may hold down the Home button on the remote for a few seconds. A popup is displayed. Choose Apps OR \
                      \n3. Go ahead and click the 3-dot button on the FireStick home screen')
        st.write ('\n')
        with col3:
            img = Image.open("images/SmartIPTV_Access1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  SmartIPTV Access 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now, scroll, and on the bottom, you will find Smart IPTV. Click the app to run it.')
        with col3:
            img = Image.open("images/SmartIPTV_Access2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  SmartIPTV Access 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('You may also move this app on the home screen for quick and easy access. Simply press the menu button on the remote and click Move on the popup window on the TV. Now, place Smart IPTV in the first or second row.')
        with col3:
            img = Image.open("images/SmartIPTV_Access3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  SmartIPTV Access 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Open the app and you will see this screen the first time you open Smart IPTV (Note down the Mac Address)')
        with col3:
            img = Image.open("images/SmartIPTV_Access4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  SmartIPTV Access 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now please Register, then Click on Account and Login. Then you can add your device type and MAC Address. \
                      \nor send us an email with your Name and MAC Addess to 4hometv10@gmail.com')
        with col3:
            img = Image.open("images/SmartIPTV_Access5.png")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  SmartIPTV Access 6  -------------------
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

        #---------------  SmartIPTV Access 7  -------------------
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
            st.write('Now you need to enter your payment information. Smart IPTV costs 5.49 EUR or about $6.00.')
        with col3:
            img = Image.open("images/SmartIPTV.png")
            st.image(img,width=500)
        st.write ('\n')
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




    #----------------------------------------------------------------------------------#
    #                                  Install_Televizo                               #
    #----------------------------------------------------------------------------------#
    def Install_Televizo():

        st. title("Install Televizo Player")
        st.write ("Televizo IPTV is an IPTV player with which you can stream IPTV videos either with the M3U URL or Xtream Codes. It includes lots of \
                   features like live broadcasts and adding unlimited playlists. Moreover, it supports different streams like HLS, UDP, and RTMP. \
                   Other salient features include parental controls, sorting, searching, adding favorites, and subtitles.")
        st.write ('\n')

        #---------------  Step 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('From Home menu, select "Downloader" to open app. It can also be accessed from your Apps menu. ')
        with col3:
            img = Image.open("images/SmartIPTV_Step1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('On Downloader Home menu, insert this URL "https://is.gd/televizo3" and click "Go"')
        with col3:
            img = Image.open("images/Televizo_Step2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Wait until the Televizo app is downloaded')
        with col3:
            img = Image.open("images/SmartIPTV_Step3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Downloader application will prompt to install Televizo. Click “Install”')
        with col3:
            img = Image.open("images/SmartIPTV_Step4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once installed click “Done”')
        with col3:
            img = Image.open("images/Televizo_Step5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now press “Delete” to delete installation temp file.')
        with col3:
            img = Image.open("images/Televizo_Step6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Step 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('The “Delete” message will prompt again. So press "Delete" again')
        with col3:
            img = Image.open("images/Televizo_Step7.jpeg")
            st.image(img,width=500)
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')


        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"> \
            <b>How to Access and Use Televizo on FireStick</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')
        st.write ('\n')
        st.write ('Here are the steps you need to follow in order to access and use Televizo on FireStick:')
        st.write ('\n')
        st.write ('\n')
        st.write ('\n')

        #---------------  Televizo Access 1  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 1</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('1. You may go to the Settings >> Applications >> Manage Installed Applications > Televizo > Launch application OR \
                      \n2. You may hold down the Home button on the remote for a few seconds. A popup is displayed. Choose Apps OR \
                      \n3. Go ahead and click the 3-dot button on the FireStick home screen')
        st.write ('\n')
        with col3:
            img = Image.open("images/SmartIPTV_Access1.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 2  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 2</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Now, scroll, and on the bottom, you will find Televizo. Click the app to run it.')
        with col3:
            img = Image.open("images/Televizo_Access2.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 3  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 3</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('You may also move this app on the home screen for quick and easy access. Simply press the menu button on the remote and click Move on the popup window on the TV. Now, place Televizo in the first or second row.')
        with col3:
            img = Image.open("images/Televizo_Access3.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 4  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 4</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Once you open Televizo app, select Create Playlist.')
        with col3:
            img = Image.open("images/Televizo_Access4.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 5  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 5</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write('Give any name to your playlist and below type in M3U link which you received from your provider.')
        with col3:
            img = Image.open("images/Televizo_Access5.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 6  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 6</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("After Playlist is loaded, you can select all channels or you can select a group to see just this group's channels")
        with col3:
            img = Image.open("images/Televizo_Access6.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 7  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 7</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Now you can add EPG (Program Guide) by clicking and entering the Settings page.")
        with col3:
            img = Image.open("images/Televizo_Access7.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 8  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 8</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Select an Option 'Program guide'.")
        with col3:
            img = Image.open("images/Televizo_Access8.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 9  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 9</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Click '+' to add a new EPG link.")
        with col3:
            img = Image.open("images/Televizo_Access9.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 10  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 10</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Give any name to EPG Guide and enter the following link: http://epg.it999.ru/epg2.xml.gz.")
        with col3:
            img = Image.open("images/Televizo_Access10.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 11  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 11</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("You can also add any channel to your Favorites by long press OK button and select Add to Favorites.")
        with col3:
            img = Image.open("images/Televizo_Access11.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 12  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 12</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Also, you can block any group or channel and remove it from the group.")
        with col3:
            img = Image.open("images/Televizo_Access12.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 13  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 13</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("Channels can also be sorted as well as filter channels and change appearance as list, grid or tiles.")
        with col3:
            img = Image.open("images/Televizo_Access13.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 14  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 14</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("You may watch any channel in compact mode or as full screen.")
        with col3:
            img = Image.open("images/Televizo_Access14.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 15  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 15</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("To access TV Guide, you can long press Down button while watching your channel to it's schedule.")
        with col3:
            img = Image.open("images/Televizo_Access15.jpeg")
            st.image(img,width=500)
        st.write ('\n')

        #---------------  Televizo Access 16  -------------------
        col1, col2, col3 = st.columns([2,1,3])
        with col1:
            st.write ('\n')
            st.write ('\n')
            row = '<p style="text-align: left;font-family:sans-serif; color:Dark Grey; margin-top: 0; margin-bottom: 0; line-height: 24px; font-size: 30px;"> \
                Step 16</p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            st.write("You may customize the look and feel of the app in Additional Settings.")
        with col3:
            img = Image.open("images/Televizo_Access16.jpeg")
            st.image(img,width=500)
        st.write ('\n')
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
            st.write('Enjoy your Televizo app on FireStick!')
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

    xSelection = st.sidebar.radio("Select Below:", ('How to Sign-up or Renew',  
            'Available Channels', 'Premier League Channels','Setup & Install IPTV Apps', 
            'Remote Control SmartIPTV', 'Frequently Asked Questions', 'Add Storage to Fire TV')) 

    if xSelection == 'How to Sign-up or Renew':
        Signup ()
    elif xSelection == 'Available Channels': 
        Available_Channels ()
    elif xSelection == 'Premier League Channels': 
        Premier_League_Channels ()
    elif xSelection == 'Setup & Install IPTV Apps': 
        Install_IPTV_Apps ()
    elif xSelection == 'Remote Control SmartIPTV': 
        Remote_Control ()
    elif xSelection == 'Frequently Asked Questions': 
        Frequently_Asked_Questions ()
    elif xSelection == 'Add Storage to Fire TV': 
        Add_Storage_FireTV ()


