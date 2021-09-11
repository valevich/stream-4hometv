import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import pygsheets
from pygsheets.datarange import DataRange
import datetime
from PIL import Image
import re


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

        st.write ('\n')
        st.write ('\n')

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
        col1, col2, col3 = st.columns([2.1,1,2])
        with col1:
            st.image('https://i.ibb.co/NjSvDkZ/soccer2.jpg',width=300)
        with col2:
            st.image('images/email.png',width=130)
        with col3:
            st.image('https://i.ibb.co/LSjt23q/Olympiakos-Argentinian-midfielder-Alejandro-Dominguez-C-celebrates-with-teammates-after-scoring-a-go.jpg',width=350)
        st.write ('\n')

        #---------------  ROW 10  -------------------
        row = '<p style="text-align: center;font-family:sans-serif; color:Grey; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 16px;"> \
            <b>4hometv10@gmail.com</b></p>'
        st.markdown(row, unsafe_allow_html=True)


        st.markdown("---")
        st.write ('\n')


    #----------------------------------------------------------------------------------#
    #                                   LOAD_GSHEET                                    #
    #----------------------------------------------------------------------------------#
    def load_gsheet(email, psw):

        xFound = ''
        xRecord = []
        if is_prod:
            gc = pygsheets.authorize(service_account_env_var = 'GDRIVE_API_CREDENTIALS') # use Heroku env variable
        else:    
            gc = pygsheets.authorize(service_file='client_secret_4hometv.json') # using service account credentials
        sheet = gc.open('4HomeTV')
        wks = sheet.worksheet_by_title('Users')
        for idx, row in enumerate(wks):
            if (wks[idx+1][3]) == email and (wks[idx+1][2]) == psw:
                xFound = 'Y'
                xRecord = wks[idx+1]
                st.session_state.row = idx+1

        return xRecord, xFound


    #----------------------------------------------------------------------------------#
    #                                  UPDATE_GSHEET                                   #
    #----------------------------------------------------------------------------------#
    def update_gsheet(xRecord, devType, devMac):

        if is_prod:
            gc = pygsheets.authorize(service_account_env_var = 'GDRIVE_API_CREDENTIALS') # use Heroku env variable
        else:    
            gc = pygsheets.authorize(service_file='client_secret_4hometv.json') # using service account credentials
        sheet = gc.open('4HomeTV')
        wks = sheet.worksheet_by_title('Users')

        xUpdated = 'Y'
        if len(xRecord[11]) == 0 and len(xRecord[12]) == 0:
            wks.cell('L'+str(st.session_state.row)).value = devType
            wks.cell('M'+str(st.session_state.row)).value = devMac
        elif len(xRecord[13]) == 0 and len(xRecord[14]) == 0:
            wks.cell('N'+str(st.session_state.row)).value = devType
            wks.cell('O'+str(st.session_state.row)).value = devMac
        elif len(xRecord[15]) == 0 and len(xRecord[16]) == 0:
            wks.cell('P'+str(st.session_state.row)).value = devType
            wks.cell('Q'+str(st.session_state.row)).value = devMac
        elif len(xRecord[17]) == 0 and len(xRecord[18]) == 0:
            wks.cell('R'+str(st.session_state.row)).value = devType
            wks.cell('S'+str(st.session_state.row)).value = devMac
        else:
            xUpdated = 'N'

        return xRecord, xUpdated


    #----------------------------------------------------------------------------------#
    #                                     LOGIN                                        #
    #----------------------------------------------------------------------------------#
    def login():

        st.session_state.counter = 0
        xName = ''
        xError = 'N'
        xSubmitted = 'N'
        xRecord = []
        if xSubmitted == 'N':
        
            with st.sidebar.form(key ='Form1'):
                email = st.text_input(label='Email Address')
                psw = st.text_input("Enter a password", type="password")
                submitted1 = st.form_submit_button(label = 'Signin')
                if submitted1:
                    xSubmitted = 'Y'
                    #---------------  Validate Email Address  -------------------
                    if len(email) > 0:
                        match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
                        if not match:
                            xError = '1'
                    else:
                        xError = '2'
                    #---------------  Validate Passwords  -------------------
                    if len(psw) == 0:
                        xError = '3'
                    elif len(psw) < 8:
                        xError = '4'
                    if xError == 'N':
                        with st.spinner('Logging in...Please Wait...'):
                            xRecord, xFound = load_gsheet(email, psw)
                            if xFound != 'Y':
                                xError = '5'
                            else:
                                xName = xRecord[0]
                                st.session_state.counter += 1
                                if "xRecord" not in st.session_state:
                                    st.session_state.xRecord = xRecord


        return xName, xError, xRecord


    #----------------------------------------------------------------------------------#
    #                                     ACCOUNT                                      #
    #----------------------------------------------------------------------------------#
    def account(xRec):

        st.sidebar.text ('Welcome' + ' ' + xRec[0])

        col1, col2, col3, col4l5 = st.columns([2.5,.8,3.2,.1])

        with col1:
            st.write ('\n')
            row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Account</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')

            info_names = ["Name: ", "Username: ", "Phone: ", "Email: ", \
                        "Status: ", "Activation Date: ", "Expiration Date: "]
            info_list = [xRec[0], xRec[1], xRec[6], xRec[3], \
                        xRec[7],  xRec[8],  xRec[9]]
            for name,infoValue in zip(info_names, info_list):
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:14px'><b>{name}</b></span>
                        <span style='float: right;line-height: 5px; font-size:14px'> {infoValue}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)

        with col3:
            st.write ('\n')
            row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>Devices</b></p>'
            st.markdown(row, unsafe_allow_html=True)
            st.write ('\n')
            xDevices = 0
            #---------------  Device 1  -------------------
            xType = ''
            xMac = ''
            if len(xRec[11]) > 0:
                xType = xRec[11]
                xDevices = 1
            if len(xRec[12]) > 0:
                xMac = xRec[12]
                xDevices = 1
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:14px'><b>Device 1:</b>&nbsp;&nbsp;{xType}</span>
                        <span style='float: right;line-height: 5px; font-size:14px'><b>MAC Address:</b>&nbsp;&nbsp;{xMac}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)
            #---------------  Device 2  -------------------
            xType = ''
            xMac = ''
            if len(xRec[13]) > 0:
                xType = xRec[13]
                xDevices = 2
            if len(xRec[14]) > 0:
                xMac = xRec[14]
                xDevices = 2
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:14px'><b>Device 2:</b>&nbsp;&nbsp;{xType}</span>
                        <span style='float: right;line-height: 5px; font-size:14px'><b>MAC Address:</b>&nbsp;&nbsp;{xMac}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)
            #---------------  Device 3  -------------------
            xType = ''
            xMac = ''
            if len(xRec[15]) > 0:
                xType = xRec[15]
                xDevices = 3
            if len(xRec[16]) > 0:
                xMac = xRec[16]
                xDevices = 3
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:14px'><b>Device 3:</b>&nbsp;&nbsp;{xType}</span>
                        <span style='float: right;line-height: 5px; font-size:14px'><b>MAC Address:</b>&nbsp;&nbsp;{xMac}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)
            #---------------  Device 4  -------------------
            xType = ''
            xMac = ''
            if len(xRec[17]) > 0:
                xType = xRec[17]
                xDevices = 4
            if len(xRec[18]) > 0:
                xMac = xRec[18]
                xDevices = 4
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:14px'><b>Device 4:</b>&nbsp;&nbsp;{xType}</span>
                        <span style='float: right;line-height: 5px; font-size:14px'><b>MAC Address:</b>&nbsp;&nbsp;{xMac}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)




    #----------------------------------------------------------------------------------#
    #                                 BEGIN SCRIPT                                     #
    #----------------------------------------------------------------------------------#
    display_header()

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    if "first" not in st.session_state:
        st.session_state.first = 'Y'

    if "row" not in st.session_state:
        st.session_state.row = ''

    if st.session_state.counter == 0:
        xFullName, xError, xRecord = login()
        if xError == '1':
            st.error ("Email Address is not valid! Please re-enter!")
        elif xError == '2':
            st.error ('Error! Please enter your Email Address!')
        elif xError == '4':
            st.error ('Error! Password must be at least 8 characters!')
        elif xError == '3':
            st.error ('Error! Please enter Password!')
        elif xError == '5':
            st.error ('Email and/or Password not found!')
        elif xError == 'N':
            if len (xFullName) > 0:
                account(xRecord)

    if st.session_state.counter > 0:
        if st.session_state.first == 'Y':
            st.session_state.first = 'N'
            submit_button1 = st.button('Add Device')
            if submit_button1:
                st.session_state.counter += 1
        else:
            account(st.session_state.xRecord)
            devType = st.selectbox('Device Type', ['', 'Amazon FireTV', 'Google TV', 'Other'])
            devMac = st.text_input('MAC Address')
            submit_button2 = st.button('Submit')
            if submit_button2:
                with st.spinner('Updating...Please Wait...'):
                    xUpdated = update_gsheet(st.session_state.xRecord, devType, devMac)
                    if xUpdated == 'Y':
                        st.write ('Device Added!')
                    else:
                        st.write ('Device Max is reached! Please contact support to add more devices!')





