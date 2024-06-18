import streamlit as st 
import pandas as pd
import os
import pandas as pd


st.set_page_config(
    page_title='History Page',
    page_icon='🕰️',
    layout='wide'
)


def display_historic_predictions():

    csv_path = './Data/history.csv'
    csv_exist = os.path.exists(csv_path)

    if csv_exist:
        history = pd.read_csv(csv_path)
        st.dataframe(history)

    



if __name__ == '__main__':

    st.title("History Page")
    display_historic_predictions()



