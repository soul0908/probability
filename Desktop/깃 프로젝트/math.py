# 수확적 확률과 통계적 확률

import random
import matplotlib.pyplot as plt 

def probability(num):
    랜덤숫자 = 0
    주사위횟수 = [ 0, 0, 0, 0, 0, 0, 0]

    for i in range(num):
        랜덤숫자 = random.randint(1, 6)
        주사위횟수[0] += 1 # 주사위 시행횟수 더하기

        if  1 == 랜덤숫자:
            주사위횟수[1] += 1
        elif 2 == 랜덤숫자:
            주사위횟수[2] += 1
        elif 3 == 랜덤숫자:
            주사위횟수[3] += 1
        elif 4 == 랜덤숫자:
            주사위횟수[4] += 1
        elif 5 == 랜덤숫자:
            주사위횟수[5] += 1
        else:
            주사위횟수[6] += 1
    print('시행을 {}번 했을때'.format(num))
    print('[ 횟수 1 2 3 4 5 6 ]')
    for i in 주사위횟수:
        print(i, end=' ')
    print()
    print('[ 확률 ]')
    for i in 주사위횟수:
        print(round((i/num)*100,2), end=' ')
    print()

    평균 = 0
    for i in range(1,7):
        평균 += i * 주사위횟수[i]

    print('평균 값은', 평균/num)

    편차제곱합 = 0
    for i in range(1,7):
        편차제곱합 += (평균-i)**2
    분산 = 편차제곱합 / 5
    print('분산값은', 분산)
    print('표준편차는', (분산)**(1/2))
    print('-----------------------------')
    
probability(10)
probability(100)
probability(200)
probability(300)
probability(400)