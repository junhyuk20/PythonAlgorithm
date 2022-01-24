from itertools import permutations
from re import I
# ✨순열 : 모든 경우의수를 순서대로 뽑아서 확인 하는 기능이다.
# ✨모든 경우의 수를 순서대로 살펴볼 때 용이하다

# v = [0,1,2,3,4]

# for i in permutations(v,4):
#     print(i)


#백준 4690번 완전 세제곱 

#문제를 이해하지 못해서 답안지를 보게 됬음 ...
#문제에서 말하는 대로 a는 a<=100 범위안의 수까지 이며
# a = b+c+d 을 만족하는데 1보다 큰 자연수 라는 것을 통해 for문의 시작값을 2부터 시작 하며
# b,c,d또한 순차적으로 증가 한다는것을 토대로 c는 -> b+1값부터 시작 , d는 -> c+1값부터 시작 해서 3개 모두 101까지 진행하면 된다. b는 처음 시작하는 수이니 증가 해줄 필요가 없음
# 마지막으로 a의 세제곱 값이 b,c,d의 세제곱의 합과 같으면 문제에서 원하는 스타일로 보여주면 되고
# for a in range(2,101) :
#     for b in range(2,101):
#         for c in range(b+1,101):
#             for d in range(c+1, 101):
#                 if a ** 3 == b ** 3 + c ** 3 + d ** 3 :
#                     print("Cube = {}, Triple = ({},{},{})".format(a,b,c,d))





# 백준 9094 수학적 호기심 

# 문제 : 두 정수 n과 m이 주어졌을 때, 0 < a < b < n인 정수 쌍 (a, b) 중에서 (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, n과 m이 주어진다. 두 수는 0보다 크고, 100보다 작거나 같다.
# 출력 : 각 테스트 케이스마다 문제의 조건을 만족하는 (a, b)쌍의 개수를 출력한다.

# 이문제는 for문을 언제 까지 돌려야 되나를 감이 잡히지 않았다. 그래서 정답을 보게되었다... 
# 문제의가 원하는 조건 등 이런건 알았지만 for문을 언제까지 돌리는냐가 이상하게 감이 안잡히는 문제였다 무엇이 끝의 기준이 되어야 되는지... 
# 또한 두번째 a for문 안에 b for문이 있는데 a for문은 현재 1부터 9까지 총 9번을 돌고 b for문은 a+1 부터 9까지 도는데 처음은 8번돈다 그럼 만약 a가 9라고하면 b는 10이 되므로 for문을 돌수가 없다.
# 그렇다면 오류가 나지 않을까? 하는데 나지 않는다... 왜인지 모르겠다... 왜 내가 오류가 나지 않을까라고 생각한건 a는 9번을 돌아야 되는데 8번을 돌고 끝난다고 생각해서이다. 
# 그래서 확인 해보니 a랑 b는 별개이다 말그대로 a가 돌때 무조건 b가 돌아야 된다라는 조건이 없으니 b 는 b인거고 난 a이니깐 a할것 하고 끝낸다 라는 식이다.

# for _ in range(int(input())):
#     n,m = map(int, input().split())
#     cnt = 0
#     for a in range(1,n):
#         #print(a)
#         for b in range(a+1,n):
#             #print("현재 a는 {} b는 {}".format(a,b))
#             if (a **2 + b**2 + m) % (a*b) == 0 :
#                 cnt = cnt +1 
#     print(cnt)


# 백준 20410번 추첨상 사수 대작전

# 입력 : 한 줄에 걸쳐 준표가 좋아하는 소수 m, 참가자들이 정한 Seed, 시연으로 공개된 X1, X2 이 주어진다. 항상 가능한 상황만 입력으로 주어진다.
# 출력 : 준표가 비밀리에 선정한 정수 a, c를 출력한다. 가능한 답이 여러 개라면, 그중 아무거나 출력한다.
# 제한 : m ≤ 100 (m은 소수)  //  0 < Seed, X1, X2 < m  //  0 ≤ a, c < m
   
# 이 문제를 풀때 겁나 쫄았다. 하지만 시간을 들여 자세히 읽어보고 이해하니 어떻게 만들지 그려진 문제였다. 처음으로 답지 안보고 풀어서 기쁘다..ㅠ
# 이 문제의 핵심인  a,c만을 알아내면 된다. 아래의 두가지 공식을 이용해서 문제를 풀면 간단하게 풀린다! 
# X1 = (a × Seed + c) % m   
# X2 = (a × X1 + c) % m

# 13 5 2 9
# m,Seed,X1,X2 = map(int, input().split()) 
# #arr = []
# aNum =0
# cNum =0
# for a in range(m):
#     for c in range(m):
#         if (a*Seed+c)%m == X1:
#             if (a*X1+c)%m == X2:
#                 aNum = a
#                 cNum = c
#                 # arr.append(aNum)
#                 # arr.append(cNum)

# print(aNum,cNum)                
#print(arr[0],arr[1])

# 백준 1813 
# 이문제는 문제를 이해를 못하겠다.. 
# 답지를 봐도 
n = int(input())
arr = list(map(int, input().split()))
temp = [0] * 51
cnt = 0
checker = 0
for i in range(n):
    temp[arr[i]] += 1 # temp[0] = 1 , 
    print("temp[arr[{}]] : {}".format(i,temp[i]))
for i in range(len(temp)):
    if temp[i] == i :
        cnt = i;
        checker = 1
        print("temp[{}]일 때 값 : {}, cnt 값: {} , checker 값:{}".format(i,temp[i],cnt,checker))
if checker == 0 :
    print(-1);
    exit()
else: print(cnt)



               