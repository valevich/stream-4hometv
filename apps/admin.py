import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import pygsheets
from pygsheets.datarange import DataRange
import datetime
from st_aggrid import AgGrid                                 
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from PIL import Image

# is_prod = os.environ.get('IS_HEROKU', None)

def app():

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
    #                        LOAD GOOGLE SHEET INTO DATAFRAME                          #
    #----------------------------------------------------------------------------------#
    # @st.cache
    def load_gsheet(gsheet):

            is_prod = os.environ.get('IS_HEROKU', None)
            if is_prod:
                gc = pygsheets.authorize(service_account_env_var = 'GDRIVE_API_CREDENTIALS') # use Heroku env
            else:    
                gc = pygsheets.authorize(service_file='client_secret_4hometv.json') # using local account credentials

            sheet = gc.open('4HomeTV')
            wks = sheet.worksheet_by_title(gsheet)
            df = wks.get_as_df()

            return df


    #----------------------------------------------------------------------------------#
    #                           DISPLAY USERS SHEET DATA                               #
    #----------------------------------------------------------------------------------#
    def display_users():
        with st.spinner('Loading Data...Please Wait...'):

            st.title('Users')
            df1 = load_gsheet('Users')           # LOAD GOOGLE SHEET
            df1.drop(df1.columns[[7,10,12,13,14,15,16,17,18,19,20,21]], axis = 1, inplace = True)
            df1 = df1.sort_values(by=['Status'], ascending=True)
            df1 = df1.reindex(columns=(['Status'] + list([a for a in df1.columns if a != 'Status']) ))

            style_negative = JsCode(
                """
                function(params) {
                    if (params.value.includes('Inactive')) {return {'backgroundColor': 'red', 'color': 'white'}} 
                    else {return {'color': 'green'}}
                };
                """
            )
            gb = GridOptionsBuilder.from_dataframe(df1)
            gb.configure_default_column(groupable=True, 
                                            value=True, 
                                            enableRowGroup=True, 
                                            editable=True,
                                            enableRangeSelection=True,
                                        )
            gb.configure_column("Status", cellStyle=style_negative, maxWidth=85)
            gb.configure_column("ExpirationDate", maxWidth=100)
            gridOptions = gb.build()
            data = AgGrid(
                df1,
                gridOptions=gridOptions,
                height=600,
                width='100%',
                theme='light',     # valid themes: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
                # defaultWidth=25,
                # fit_columns_on_grid_load=True, 
                enable_enterprise_modules=True,
                allow_unsafe_jscode=True
            )




    #----------------------------------------------------------------------------------#
    #                           DISPLAY DEVICES SHEET DATA                             #
    #----------------------------------------------------------------------------------#
    def display_devices():
        with st.spinner('Loading Data...Please Wait...'):

            st.title('Devices')    
            df1 = load_gsheet('Users')           # LOAD GOOGLE SHEET
            df1.drop(df1.columns[[0,1,3,4,5,6,7,8,10,11,12,19]], axis = 1, inplace = True)
            df1 = df1.sort_values(by=['Status'], ascending=True)
            df1 = df1.reindex(columns=(['Status'] + list([a for a in df1.columns if a != 'Status']) ))

            style_negative = JsCode(
                """
                function(params) {
                    if (params.value.includes('Inactive')) {return {'backgroundColor': 'red', 'color': 'white'}} 
                    else {return {'color': 'green'}}
                };
                """
            )
            gb = GridOptionsBuilder.from_dataframe(df1)
            gb.configure_default_column(groupable=True, 
                                            value=True, 
                                            enableRowGroup=True, 
                                            editable=True,
                                            enableRangeSelection=True,
                                        )
            gb.configure_column("Status", cellStyle=style_negative, maxWidth=85)
            gridOptions = gb.build()
            data = AgGrid(
                df1,
                gridOptions=gridOptions,
                height=600,
                width='100%',
                theme='light',     # valid themes: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
                # defaultWidth=25,
                # fit_columns_on_grid_load=True, 
                enable_enterprise_modules=True,
                allow_unsafe_jscode=True
            )





    #----------------------------------------------------------------------------------#
    #                                       MAIN                                       #
    #----------------------------------------------------------------------------------#

    display_header()

    pwd = st.sidebar.empty()
    t = pwd.text_input("Enter Password", type="password")
    if t != "":
        if t == 'nella1':
            pwd.empty()
            st.sidebar.markdown('---')
            xSelection = st.sidebar.radio("Select your List", ('Users','Devices')) 
            if xSelection == 'Users':
                display_users()
            elif xSelection == 'Devices': 
                display_devices ()
            pwd.empty()











    # # This is how you can get a Google Drive csv/excel share link to a Pandas DataFrame:
    # url = 'https://drive.google.com/file/d/1iHZZ7-8ht9Arwt2fFEdCNGGrcoq0CJ81/view?usp=sharing'
    # path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    # outlet_df = pd.read_csv(path)
    # st.write(outlet_df)


    #---------- Append
    # wks.clear()
    # values = [['aaa']]
    # wks.append_table(values, start='A1', end=None, dimension='ROWS', overwrite=True)  # Added

    ##---------- Get Column Names
    # all_values = wks.get_all_values()
    # cleaned_values = [[item for item in unique_list if item ]for unique_list in all_values]
    # st.write (cleaned_values[0])

    # #---------- Get 1st Column
    # first_column = wks.get_col(1)
    # first_column_data = first_column[1:] # We are doing a python slice here to avoid 
    #                                      # extracting the column names from the first row (keyword)
    # st.write (first_column_data)

    # #---------- Get every row
    # for row in wks:
    #     st.write (row)

    #---------- Replace all values
    # wks.replace("NaN", replacement="0")


    #---------- Update a single cell.
    # wks.update_value('B20', "Numbers on Stuff")

    #---------- Get last row
    # st.write (f"The last row is {wks.rows}")

    #---------- How To Bold Cells
    # model_cell = wks.cell('A1')
    # model_cell.set_text_format('bold', True)
    # DataRange('A1','F1', worksheet=wks).apply_format(model_cell)

    #---------- Export A Google Sheet To A .CSV
    # wks.export(filename='this_is_a_csv_file')

    #---------- Export A Google Sheet To Dataframe and then to JSON
    # st.write (wks.get_as_df().to_json())

    #---------- Export A Google Sheet To Dataframe





    # cells = wks.find("NaN", searchByRegex=False, matchCase=False, 
    #     matchEntireCell=False, includeFormulas=False, 
    #     cols=(3,6), rows=None, forceFetch=True)
    # wks.update_values(crange=None, values=None, cell_list=None, extend=False, majordim='ROWS', parse=None)
    # for cell in cells:
    #     cell.value = "Other"
    # wks.update_values(cell_list=cells)



    # # Read into dataframe
    # dataframe_two = wks.get_as_df()
    # dataframe_two.head(6)




    # news1, news2 = st.beta_columns([1,5])

    # with news1:
    #     st.image('https://cdn.pixabay.com/photo/2016/10/10/22/38/business-1730089_1280.jpg')

    # with news2: 
    #     st.markdown("***")






        # #---------------  gsheetsdb -------------
        # scope = ['https://spreadsheets.google.com/feeds',
        #         'https://www.googleapis.com/auth/drive']

        # credentials = service_account.Credentials.from_service_account_info(
        #     st.secrets["gcp_service_account"], scopes = scope)
        # client = Client(scope=scope, creds=credentials)
        # spreadsheetname = 'Research'
        # spread = Spread(spreadsheetname, client=client)

        # sh = client.open(spreadsheetname)
        # worksheet_list = sh.worksheets()

        # def worksheet_names():
        #     sheet_names = []
        #     for sheet in worksheet_list:
        #         sheet_names.append(sheet.title)
        #     return sheet_names

        # def load_the_spreadsheet(spreadsheetname):
        #     worksheet = sh.worksheet(spreadsheetname)
        #     df = DataFrame(worksheet.get_all_records())
        #     return df

        # def update_the_spreadsheet(spreadsheetname,dataframe):
        #     col = ['Date','Company']
        #     spread.df_to_sheet(dataframe[col],sheet = spreadsheetname,index = False)
        #     st.sidebar.info('Spreadsheet Updated')
            

        # #Load from Spreadsheet
        # what_sheets = worksheet_names()
        # ws_choice = st.radio('Available Worksheets', what_sheets)

        # #Create Select Box 
        # df = load_the_spreadsheet(ws_choice)

        # #Show Selection
        # select_CID = st.sidebar.selectbox('IPOs',list(df['Company'])) 


        # #Add Item to Spreadsheet
        # add = st.sidebar.checkbox('Add New Ticker')
        # if add:
        #     cid_entry = st.sidebar.text_input('New Ticker')
        #     confirm_input = st.sidebar.button('Confirm')

        #     if confirm_input:
        #         now = date.today()
        #         opt = {'IPOs': [cid_entry],
        #                 'Date': [now]}
        #         opt_df = DataFrame(opt)
        #         df = load_the_spreadsheet('IPOs')
        #         new_df = df.append(opt_df,ignore_index=True)
        #         update_the_spreadsheet('IPOs', new_df)
