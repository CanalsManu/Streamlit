import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

@st.dialog("Test dialog", dismissible=False)
def init_dialog():
    st.write('Hello')
    st.session_state['init dialog'] = 'Done'
    st.write(st.session_state)
    if st.button("Close"):
        st.rerun()

pg = st.navigation([
    st.Page('pages/page2.py'),
    st.Page('pages/page1.py')
])
pg.run()

st.error('Epa')
# st.sidebar()


st.title("Hola Nati :)")
st.write("hello world!")

st.title('Demo')

if "init dialog" not in st.session_state:
    init_dialog()

uploaded_file = st.file_uploader('Upload your file please', type=('csv', 'py'))



st.button('Empty button')

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