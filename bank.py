import streamlit as st
customers={'kim':[12345,'홍길동',300000],'lee':[67890,'파이썬',7890]}
class Bankaccount:
    # 속성
    def __init__(self,number,name,balance):
        self.account_number = number
        self.name = name
        self.balance = balance

    #기능, 메서드
    #입금
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    #출금
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
        else:
            # print('잔고가 부족해서 인출 불가합니다.')
            st.write('잔고가 부족해서 인출 불가합니다.')
        return self.balance
    def print_balance(self):
        st.write('잔고 :',self.balance)

def customerin():
    # name2=input('영어애칭>> ')
    # number=input('고객번호>> ')
    # name=input('고객이름>>')
    # balance = int(input('잔고>> '))
    name2=st.text_input('영어애칭>> ')
    number=st.text_input('고객번호>> ')
    name=st.text_input('고객이름>>')
    balance =st.number_input('잔고>> ')  
    customers[name2]=[number,name,balance]
def customermanage():
    for key,data in customers.items():
    # print(key,data[0])
    # # print('----')
        key = Bankaccount(data[0],data[1],data[2])
        st.write('고객번호',key.account_number)
        st.write('이름',key.name)
        st.write('잔금',key.balance)

        key.deposit(45000)
        key.print_balance()
        key.withdraw(30000)
        key.print_balance()




#   main
# 객체 생성
if __name__ == '__main__':          #bank.py에서만 쓸때(즉 만들어진 곳에서만 쓸때) 필요한 구문

    # customerin()
    customermanage(customers)


