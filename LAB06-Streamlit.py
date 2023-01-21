import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import time

st.title("ZADANIE PAD 06")

selected_card = st.selectbox("Wybierz wersję wyświetlania", ("Ankieta", "Staty"))
st.write("Wybrana wersja wyświetlania: ", selected_card)
if(selected_card == "Ankieta"):
    first_name = st.text_input("Wpisz swoje imie", "imie")
    second_name = st.text_input("Wpisz swoje nazwisko", "nazwisko")
    if st.button("Zapisz"):
        result = "Zapisano!"
        st.success(result)

elif(selected_card == "Staty"):

    data = st.file_uploader("Wczytaj swoje dane", type=['csv'])
    if data is not None:
        with st.spinner("Ładowanie..."):
            df = pd.read_csv(data)
            time.sleep(1) #tu sztucznie  spowalniam ładowanie o sekunde, żeby stestować czy działa, w rzeczywiscości ładowanie dzieje sie na tyle szybko ze nie jestem w stanie zauywazc kółeczka ładowania
            st.dataframe(df.head(10))
        st.success("Załadowano pomyślnie!")
        selected_plot = st.selectbox("Wybierz wykres, których chcesz wyświetlić", ("Line chart", "Count of values - Bar chart"))
        st.write("Wybrany wykres: ", selected_plot)
        if(selected_plot == "Line chart"):
            st.set_option('deprecation.showPyplotGlobalUse', False)
            all_columns_names = df.columns.to_list()
            selected_column_name_X = st.selectbox("Wybierz kolumnę na osi X:", all_columns_names)
            selected_column_name_Y = st.selectbox("Wybierz kolumnę na osi Y:", all_columns_names)
            chart_data = pd.DataFrame(
            df[selected_column_name_X],
            df[selected_column_name_Y])

            st.line_chart(chart_data)

        else:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            all_columns_names = df.columns.to_list()
            selected_column_name = st.selectbox("Wybierz kolumnę", all_columns_names)
            plot_data = df[selected_column_name].value_counts()
            st.bar_chart(plot_data)
else:
    st.write("Please select something")