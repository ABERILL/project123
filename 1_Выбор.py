import streamlit as st
from streamlit import *
import pandas as pd




hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




d = st.sidebar.date_input("Дата")

def date(d):

    return date

add_selectbox_1 = st.sidebar.selectbox(
    "Регион",
    ("Все регионы", "Европейская часть РФ", "Урал и Сибирь", "Сибирь и Дальний Восток"))

add_selectbox_2 = st.sidebar.selectbox(
    "Топливо",
    ("ДТ", ""))

add_selectbox_3 = st.sidebar.selectbox(
    "Вид топлива",
    ("Летнее", "Межсезонное", "Зимнее"))

# vibor = st.radio(
#     "Какой тип графика предпочитаете?",
#     ('Линейный', 'Гистограмма'))


df = pd.read_csv('C:/rabota/project123/data5.csv')
st.session_state.df = df
# st.write(df)

# chart_data = pd.DataFrame(df)[['index_product', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_product')


# c = alt.Chart(chart_data).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

# st.line_chart(chart_data)

if st.sidebar.button("Поиск"):

    if add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Летнее" :
        data_Europlet = df[(df['index_place'] == 'EVR') & (df['index_product'] == 'DTL') & (df['index_date'] == str(d))] 
        chart_data = pd.DataFrame(data_Europlet)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europlet)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Межсезонное" :
        data_Europmiddle = df[(df['index_place'] == 'EVR') & (df['index_product'] == 'DTM') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Зимнее" :
        data_Europzim = df[(df['index_place'] == 'EVR') & (df['index_product'] == 'DTZ') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europzim)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europzim)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Все виды топливы" :
        data_Europmiddle = df[(df['index_place'] == 'EVR') & (df['index_product']) & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)


    if add_selectbox_1 ==  "Сибирь и Дальний Восток" and add_selectbox_3 == "Летнее" :
        data_Europlet = df[(df['index_place'] == 'DAL') & (df['index_product'] == 'DTL') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europlet)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europlet)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Сибирь и Дальний Восток" and add_selectbox_3 == "Межсезонное" :
        data_Europmiddle = df[(df['index_place'] == 'DAL') & (df['index_product'] == 'DTM') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Сибирь и Дальний Восток" and add_selectbox_3 == "Зимнее" :
        data_Europzim = df[(df['index_place'] == 'DAL') & (df['index_product'] == 'DTZ') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europzim)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europzim)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Все виды топлива" :
        data_Europmiddle = df[(df['index_place'] == 'EVR') & (df['index_product']) & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)


    if add_selectbox_1 ==  "Урал и Сибирь" and add_selectbox_3 == "Летнее" :
        data_Europlet = df[(df['index_place'] == 'SIB') & (df['index_product'] == 'DTL') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europlet)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europlet)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Урал и Сибирь" and add_selectbox_3 == "Межсезонное" :
        data_Europmiddle = df[(df['index_place'] == 'SIB') & (df['index_product'] == 'DTM') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Урал и Сибирь" and add_selectbox_3 == "Зимнее" :
        data_Europzim = df[(df['index_place'] == 'SIB') & (df['index_product'] == 'DTZ') & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europzim)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europzim)
        st.line_chart(chart_data)
    elif add_selectbox_1 ==  "Европейская часть РФ" and add_selectbox_3 == "Все виды топлива" :
        data_Europmiddle = df[(df['index_place'] == 'EVR') & (df['index_product']) & (df['index_date'] == str(d))]
        chart_data = pd.DataFrame(data_Europmiddle)[['index_date', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_date')
        st.write(data_Europmiddle)
        st.line_chart(chart_data)

    # if add_selectbox_1 ==  "Сибирь и Дальний Восток" :
    #    data_DAL = df[df['index_place'] == 'DAL']
    #    chart_data = pd.DataFrame(data_DAL)[['index_product', 'index_value']].reset_index().drop(columns = ['index']).set_index('index_product')
    #    st.write(data_DAL)
    #    st.line_chart(chart_data)


    if add_selectbox_1 ==  "Все регионы" :
        chart_data = pd.DataFrame(df)[['index_date', 'index_value']].reset_index().drop(columns = ['index'])[df['index_date'] == str(d)].set_index('index_date')
        st.write(df[df['index_date'] == str(d)])
        st.bar_chart(df[df['index_date'] == str(d)].set_index('index_product')['index_value'])


