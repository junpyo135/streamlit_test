import streamlit as st
import bank
import rsp
#사이드바 화면
st.sidebar.header('로그인')
user_id=st.sidebar.text_input('아이디 입력',value='')
user_pw=st.sidebar.text_input('패스워드 입력',type='password')

if user_pw=='1234':
    st.sidebar.header("===junpyo's Portfolio ===")
    selectbox_options=['은행클래스','가위바위보게임']
    menu=st.sidebar.selectbox('메뉴선택',selectbox_options,index=None)

    if menu=='은행클래스':
        bank.customerin()
        bank.customermanage()
    elif menu == '가위바위보게임':
        rsp.rock()