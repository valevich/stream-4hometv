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
            if (wks[idx+1][4]) == email and (wks[idx+1][3]) == psw:
                xFound = 'Y'
                xRecord = wks[idx+1]
                st.session_state.row = idx+1

        return xRecord, xFound


    #----------------------------------------------------------------------------------#
    #                                  UPDATE_GSHEET                                   #
    #----------------------------------------------------------------------------------#
    def update_gsheet(xRecord, devType1, devMac1, devType2, devMac2, devType3, devMac3, devType4, devMac4):

        if is_prod:
            gc = pygsheets.authorize(service_account_env_var = 'GDRIVE_API_CREDENTIALS') # use Heroku env variable
        else:    
            gc = pygsheets.authorize(service_file='client_secret_4hometv.json') # using service account credentials
        sheet = gc.open('4HomeTV')
        wks = sheet.worksheet_by_title('Users')

        xUpdated = 'N'

        # if len(xRecord[12]) == 0 and len(xRecord[13]) == 0:
        #     wks.cell('M'+str(st.session_state.row)).value = devType
        #     wks.cell('N'+str(st.session_state.row)).value = devMac
        #     xUpdated = 'Y'
        # elif len(xRecord[14]) == 0 and len(xRecord[15]) == 0:
        #     wks.cell('O'+str(st.session_state.row)).value = devType
        #     wks.cell('P'+str(st.session_state.row)).value = devMac
        #     xUpdated = 'Y'
        # elif len(xRecord[16]) == 0 and len(xRecord[17]) == 0:
        #     wks.cell('Q'+str(st.session_state.row)).value = devType
        #     wks.cell('R'+str(st.session_state.row)).value = devMac
        #     xUpdated = 'Y'
        # elif len(xRecord[18]) == 0 and len(xRecord[19]) == 0:
        #     wks.cell('S'+str(st.session_state.row)).value = devType
        #     wks.cell('T'+str(st.session_state.row)).value = devMac
        #     xUpdated = 'Y'

        wks.cell('M'+str(st.session_state.row)).value = devType1
        wks.cell('N'+str(st.session_state.row)).value = devMac1
        xUpdated = 'Y'
        wks.cell('O'+str(st.session_state.row)).value = devType2
        wks.cell('P'+str(st.session_state.row)).value = devMac2
        xUpdated = 'Y'
        wks.cell('Q'+str(st.session_state.row)).value = devType3
        wks.cell('R'+str(st.session_state.row)).value = devMac3
        xUpdated = 'Y'
        wks.cell('S'+str(st.session_state.row)).value = devType4
        wks.cell('T'+str(st.session_state.row)).value = devMac4
        xUpdated = 'Y'

        return xRecord, xUpdated



    #----------------------------------------------------------------------------------#
    #                                     LOGIN                                        #
    #----------------------------------------------------------------------------------#
    def login(xUsername,xPassword):

        st.session_state.counter = 0
        xRecord = []

        xRecord, xFound = load_gsheet(xUsername, xPassword)
        if xFound != 'Y':
            xError = '5'
        else:
            xName = xRecord[0]
            xUsername = xRecord[2]
            xPassword = xRecord[3]
            st.session_state.counter += 1
            if "xRecord" not in st.session_state:
                st.session_state.xRecord = xRecord

        return xUsername, xPassword, xRecord, xFound




    #----------------------------------------------------------------------------------#
    #                                     ACCOUNT                                      #
    #----------------------------------------------------------------------------------#
    def account(xRec):

        st.sidebar.text ('Welcome' + ' ' + xRec[0])

        st.write ('\n')
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>My Account</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        if xRec[8] == 'Active':
            xColor = 'green'
        elif xRec[8] == 'Inactive': 
            xColor = 'red'
        elif xRec[8] == 'Admin': 
            xColor = 'blue'
        else : 
            xColor = 'black'

        x1 = xRec[8]
        x2 = xRec[9]
        x3 = xRec[10]


        col1, col2, col3, col4l5 = st.columns([2.5,1.5,2.5,.1])

        with col1:
            info_names = ["Name: ", "Username: ", "Phone: ", "Email: "]
            info_list = [xRec[0], xRec[2], xRec[7], xRec[4]]
            for name,infoValue in zip(info_names, info_list):
                row = \
                f"""<div> 
                        <span style='float: left;line-height: 5px; font-size:16px'><b>{name}</b></span>
                        <span style='float: right;line-height: 5px; font-size:16px'> {infoValue}</span>
                    </div>
                """
                st.markdown(row, unsafe_allow_html=True)
        with col3:
            row = \
            f"""<div> 
                    <span style='float: left; line-height: 5px; font-size:16px'><b>Status: </b></span>
                    <span style='float: right; color: {xColor}; line-height: 5px; font-size:16px'>{x1}</span>
                </div>
            """
            st.markdown(row, unsafe_allow_html=True)
            row = \
            f"""<div> 
                    <span style='float: left; line-height: 5px; font-size:16px'><b>Activation Date: </b></span>
                    <span style='float: right; line-height: 5px; font-size:16px'>{x2}</span>
                </div>
            """
            st.markdown(row, unsafe_allow_html=True)
            row = \
            f"""<div> 
                    <span style='float: left; line-height: 5px; font-size:16px'><b>Expiration Date: </b></span>
                    <span style='float: right; line-height: 5px; font-size:16px'>{x3}</span>
                </div>
            """
            st.markdown(row, unsafe_allow_html=True)



        st.write ('\n')
        row = '<p style="text-align: center;font-family:sans-serif; color:Red; margin-top: 20; margin-bottom: 5; line-height: 30px; font-size: 28px;"><b>My Devices</b></p>'
        st.markdown(row, unsafe_allow_html=True)
        st.write ('\n')

        with st.form(key='columns_in_form'):
            col1, col2, col3, col4 = st.columns([1,1,1,1])
            # with col1:
            devType1 = col1.selectbox('Device 1 Type', [xRec[12], 'Amazon FireTV', 'Google TV', 'Android TV', 'Samsung TV', 'LG TV', 'Other'], key=1)
            devMac1 = col1.text_input('MAC Address', xRec[13], key=2)
            # with col2:
            devType2 = col2.selectbox('Device 2 Type', [xRec[14], 'Amazon FireTV', 'Google TV', 'Android TV', 'Samsung TV', 'LG TV', 'Other'], key=3)
            devMac2 = col2.text_input('MAC Address', xRec[15], key=4)
            # with col3:
            devType3 = col3.selectbox('Device 3 Type', [xRec[16], 'Amazon FireTV', 'Google TV', 'Android TV', 'Samsung TV', 'LG TV', 'Other'], key=5)
            devMac3 = col3.text_input('MAC Address', xRec[17], key=6)
            # with col4:
            devType4 = col4.selectbox('Device 4 Type', [xRec[18], 'Amazon FireTV', 'Google TV', 'Android TV', 'Samsung TV', 'LG TV', 'Other'], key=7)
            devMac4 = col4.text_input('MAC Address', xRec[19], key=8)

            submit_button1 = st.form_submit_button('Submit')
            st.session_state.counter += 1
            if submit_button1:
                with st.spinner('Updating...Please Wait...'):
                    xUpdated = update_gsheet(st.session_state.xRecord, devType1, devMac1, devType2, devMac2, devType3, devMac3, devType4, devMac4)
                    if xUpdated[1] == 'Y':
                        st.write ('Device List Updated!')
                    else:
                        st.write ('Device Max is reached! Please contact support to add more devices!')


    #----------------------------------------------------------------------------------#
    #                                       MAIN                                       #
    #----------------------------------------------------------------------------------#
    def main(xRecord):

        display_header()

        if "counter" not in st.session_state:
            st.session_state.counter = 0

        if "first" not in st.session_state:
            st.session_state.first = 'Y'

        if "row" not in st.session_state:
            st.session_state.row = ''

        if st.session_state.counter == 1:
            account(xRecord)
            st.session_state.first = 'Y'
            st.session_state.counter += 1



    #----------------------------------------------------------------------------------#
    #                                 BEGIN SCRIPT                                     #
    #----------------------------------------------------------------------------------#

    if "username" not in st.session_state:
        st.session_state.username = ''
    if "password" not in st.session_state:
        st.session_state.password = ''

    usr = ''
    pwd = ''
    xUsername = ' '
    xPassword = ' '
    xFound = ''

    if "loggedin" not in st.session_state:
        st.session_state.loggedin = ''

    if "xRecord" not in st.session_state:
        st.session_state.xRecord = ''

    if st.session_state.loggedin != 'Y':
        if st.session_state.username != xUsername or st.session_state.password != xPassword:
            usr_placeholder = st.sidebar.empty()
            pwd_placeholder = st.sidebar.empty()
            usr = usr_placeholder.text_input("Email:", value="")
            pwd = pwd_placeholder.text_input("Password:", value="", type="password")
            st.session_state.username = usr
            st.session_state.password = pwd
            if len(st.session_state.username) > 0 and len(st.session_state.password) > 0:
                xUsername, xPassword, xRecord, xFound = login(usr,pwd)
            if xFound == 'Y':
                usr_placeholder.empty()
                pwd_placeholder.empty()
                main(xRecord)
                st.session_state.loggedin = 'Y'
                st.session_state.xRecord = xRecord
            elif st.session_state.username != '' and st.session_state.password != '':
                st.error("the username/password you entered is incorrect")
        else:
            xUsername, xPassword, xRecord, xFound = login(usr,pwd)
            if st.session_state.password != xPassword:
                pwd_placeholder = st.sidebar.empty()
                pwd = pwd_placeholder.text_input("Password:", value="", type="password")
                st.session_state.password = pwd
                if st.session_state.password == xPassword:
                    pwd_placeholder.empty()
                    main(xRecord)
                    st.session_state.loggedin = 'Y'
                    st.session_state.xRecord = xRecord
                elif st.session_state.password != '':
                    st.error("the password you entered is incorrect")
            else:
                main(xRecord)
                st.session_state.loggedin = 'Y'
                st.session_state.xRecord = xRecord
    else:
        st.session_state.counter = 1
        main(st.session_state.xRecord)








