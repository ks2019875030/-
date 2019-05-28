import random

def P(Q,K) :
    B = 0 ; S = 0               #먼저 명령어 def로 함수의 정의를 내려줍니다.
    for i in range(3) :
        if int(Q[i]) == K[i] :
            S += 1
        elif int(Q[i]) in K :
            B += 1
    if S == 3 :
        return 0
    else :
        return [S,B]

while True :
    T = input('야구게임 시작을 원하시면 시작을 입력하세요.')
    if T == '시작' :
        Num = [i for i in range(1,10)]
        K = []
        for i in range(3) :
            m = len(Num)
            X = Num.pop(random.randrange(0,m-1))
            K.append(X)
        print('숫자는 다른 세 자리 숫자입니다.')
        while True :        
            while True :
                A = input('숫자는 무엇일까요? :')
                if 100<=int(A)<=999 and A[0] != A[1]and A[1]!=A[2]and A[0] != A[2] :
                    break
                else :
                    print('서로 다른 세 자리의 자연수를 입력하세요.')
            
            if P(A,K) == 0 :
                print(' 정답입니다!!')
                break
            print(P(A,K)[0], 'STRIKE', P(A,K)[1], 'BALL.')

    else :
        print('시작을 치라고했습니다 ㅎ.')
        continue



