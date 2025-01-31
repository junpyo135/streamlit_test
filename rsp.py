import random as rd
import streamlit as st
def rock():
    select=['가위','바위','보']

    computer=rd.choice(select)
    while True:
        user=st.text_input('가위, 바위, 보 중에서 하나 입력>>>',value='바위')
        if user in select:
            break
        st.write('잘못된 입력입니다. 다시 입력하세요.')

    st.write('컴퓨터는 ',computer,'를 냈습니다.')
    st.write('사용자는 ',user,'를 냈습니다.')

    if user =='가위' and computer =='보' or \
        user =='바위' and computer =='가위' or \
        user =='보' and computer =='바위':
        st.write('유저가 이겼습니다.')
    else:
        st.write('유저가 졌습니다.')

if __name__ == '__main__':
    rock()
