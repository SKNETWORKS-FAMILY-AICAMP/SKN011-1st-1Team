import streamlit as st

st.title("❓자주 묻는 질문 FAQ")

faq_list = [

]

for question, answer in faq_list:
    with st.expander(question): #클릭하면 펼쳐짐
        st.write(answer)