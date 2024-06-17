import streamlit as st 
import pandas as pd
import pyodbc 

st.set_page_config(page_title="CRUD APP",layout="wide")

st_hide_style = '''
<style>
#MainMenu {visibility: hidden}
header {visibility: hidden}
footer {visibility: hidden}
div.block-container {padding: 0.5rem 1rem}
</style>
'''
st.markdown(st_hide_style,unsafe_allow_html=True)

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=91017860-WWT;DATABASE=crud_project;UID=sa;PWD=ashishmita')

con_cursor = sql_conn.cursor()


st.title(":blue[CRUD APPLICATION]")

select_options = st.sidebar.selectbox("Select options for CRUD operations (CREATE,READ,UPDATE,DELETE)", options=["CREATE","READ","UPDATE","DELETE"])

if select_options == "CREATE":
    st.header("Insert details")
    name = st.text_input("Enter name for details",max_chars=50)
    email = st.text_input("Enter email for details",max_chars=50)
    if st.button("CREATE"):
        con_cursor.execute('Insert into users (name,email) values(?,?)',(name,email))
        con_cursor.commit()
        sql_conn.close()
        st.success("Insert details sucessfully")
elif select_options == "READ":
    st.header("Read data from applications")
    input_id= st.number_input("Enter ID for fetching data")
    if st.button('SEARCH'):
        output = con_cursor.execute('select * from users where id=?',input_id)
        display_output = output.fetchall()
        for ans in display_output:
            sqlname = ans.name
            sqlemail = ans.email
            sqlid = ans.id
            if sqlname==None:
                st.success("No data available")
            else:
                st.write(f'The name is {sqlname} and email is {sqlemail}')
        
elif select_options == "UPDATE":
    st.header("Update applications")
    update_id=st.text_input("Enter ID for updating")
    update_name=st.text_input("Enter name for updating")
    update_email=st.text_input("Enter email for updating")
    if st.button('UPDATE'):
        con_cursor.execute("update users set name=?,email=? where id=?",update_name,update_email,update_id)
        con_cursor.commit()
        st.success("Update details successfully")
elif select_options == "DELETE":
    st.header("Delete applications")
    delete_id = st.text_input("Enter id to delete")
    if st.button("DELETE"):
        con_cursor.execute("Delete users where id=?",delete_id)
        con_cursor.commit()
        st.warning("Delete details succussfully")