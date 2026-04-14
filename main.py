import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("hello world!")
st.write({'a':2, 'b':[2, 6, 'a']})

st.title('Demo')

uploaded_file = st.file_uploader('Upload your file please', type=('csv', 'py'))

if uploaded_file is not None:
    st.write('File uploaded...')
    df = pd.read_csv(uploaded_file)

    st.subheader("Data preview")
    st.write(df.head())

    st.subheader('Summary')
    st.write(df.describe())

    st.subheader('Filter')
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select col to filter by', columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox('Select value to filter by', unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader('Plot')
    x = st.selectbox('Select x values col', columns)
    y = st.selectbox('Select y values col', columns)

    if st.button('Generate plot'):
        st.line_chart(filtered_df.set_index(x)[y])
        print(filtered_df.set_index(x)[y])

else:
    st.write('Waiting on file upload...')