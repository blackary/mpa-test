import streamlit as st

"Page 2"

if st.button("Press to add query params"):
    st.experimental_set_query_params(foo="bar")

if st.button("Press to reset query params"):
    st.experimental_set_query_params()


"# Title 1"

for i in range(10):
    st.write("This is a paragraph")

"# Title 2"

for i in range(10):
    st.write("This is a paragraph")

"# Title 3"

for i in range(10):
    st.write("This is a paragraph")
