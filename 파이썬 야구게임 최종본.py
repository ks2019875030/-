import random
intlist=[]

for i in range(0,3):
    intlist.append(random.randrange(1,10))   #랜덤으로 1~10까지 다른숫자 3개를 무작위로 뽑을 수 있게 한다.


while True: 
    num1 = int(input("1번째 숫자를 입력하시오:"))  #숫자를 입력받는다.
    num2 = int(input("2번째 숫자를 입력하시오:"))
    num3 = int(input("3번째 숫자를 입력하시오:"))
    strike=0
    ball=0
    no_ball=0
    for i in range(3):                       #입력받은 수와 랜덤으로 뽑힌 숫자 3개를 각각 비교하는 조건문을 만든다.
        if i==0:
            if intlist[i]==num1:
                strike=strike+1
            elif intlist[i]==num2 or intlist[i]==num3:
                ball=ball+1
            else:
                no_ball = no_ball+1
        if i==1:
            if intlist[i]==num2:
                strike=strike+1
            elif intlist[i]==num1 or intlist[i]==num3:
                ball=ball+1
            else:
                no_ball = no_ball+1
        if i==2:
            if intlist[i]==num3:
                strike=strike+1
            elif intlist[i]==num1 or intlist[i]==num2:
                ball=ball+1
            else:
                no_ball = no_ball+1
    if strike==3:
        print("정답!!!!!")        #입력한 숫자와 뽑힌 숫자를 각각 비교한 것에 대한 결과를 출력한다.
        break
    elif no_ball==3:
        print("NO STRIKE!! NO BALL!!")
    else:
        print(strike, "S", ball, "B")
    



