import streamlit as st
from streamlit import *
import pandas as pd

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

df = st.session_state.df

col_1, col_2 = st.columns(2)

is_plot = False

with col_1:
    type_select = st.selectbox('Тип топлива', ['Не важно'] + list(df['index_product'].unique()))
    region_select = st.selectbox('Регион', ['Не важно'] + list(df['index_place'].unique()))

with col_2:
    if st.sidebar.button('Обновить'):
        if type_select != 'Не важно':
            if region_select != 'Не важно':
                df_out = df[(df['index_place'] == region_select) & (df['index_product'] == type_select)]
            
            else:
                df_out = df[df['index_product'] == type_select]
        
        else:
            if region_select != 'Не важно':
                df_out = df[(df['index_place'] == region_select)]
            
            else:
                df_out = df



        st.write(df_out)
        is_plot = True

if is_plot:
    st.line_chart(df_out.set_index('index_date')['index_value'])
    is_plot = False