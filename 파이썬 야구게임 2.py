import random

bg= random.sample(range(1,10),3)  #bg는 baseball game을 줄인것, 랜덤으로 1~9까지 다른숫자 3개를 무작위로 뽑는것을 나타낸다.

tr_cnt=0
st_cnt=0   #변수 설정 xx_cnt : 게임 수 , ss_cnt : 스트라이크 개수, bb_cnt : 볼 개수
bl_cnt=0

print("야구게임 시작!!")

while(st_cnt <3):
    num=input("숫자를 입력하시오 : ") #숫자 3개가 중복이 되지않도록 하기위해 조건문을 만든다.
if(num[0]==num[1]==num[2]):
    print("다른 숫자 3개를 입력하시오.")
    tr_cnt +=1
elif(num[0]==num[1]):
    print("다른 숫자 3개를 입력하시오.")
    tr_cnt +=1
elif(num[0]==num[2]):
    print("다른 숫자 3개를 입력하시오.")
    tr_cnt +=1
elif(num[1]==num[2]):
    print("다른 숫자 3개를 입력하시오.")
    tr_cnt+=1
else :
    pass
    



for i in range(0,3):
    for j in range(0,3):
        if(num[i]== str(bs[j])and i==j):    # 뽑은 3개 숫자와 내가 입력한 3개의 숫자를 비교하기 위한 소스이다.
            ss_cnt+=1
        elif(num[i]==str(bs[j])and i!=j):
            bb_cnt+=1

print(st_cnt,"STRIKE", bl_cnt,"BALL")
print(xx_cnt,"번째 정답입니다!")


