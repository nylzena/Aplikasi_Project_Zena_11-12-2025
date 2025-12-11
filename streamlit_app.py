import streamlit as st
st.title(":purple[Projek LPK 2025]")
st.title(":blue[Penentuan bilangan dan genap]")
number = int(st.number_input("Masukkan angka",min_value=0, max_value=10000))
if number%2=1:
    st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
    st.write("Bilangan",number,"termasuk bilangan genap")
