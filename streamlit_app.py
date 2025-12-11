import streamlit as st
st.title(":green[Projek LPK 2025]")
st.header(":blue[Penentuan bilangan dan genap]")
number = st.number_input("Insert a number",min_value=0, max_value=10000)
if number%2==1:
    st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
    st.write("Bilangan",number,"termasuk bilangan genap")
