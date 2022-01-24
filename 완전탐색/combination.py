from itertools import combinations
# ✨조합 : 순서와 상관없이 뽑는 과정이다.
# ✨배열안에 수를 뽑는데 2개씩 이나 n개씩 뽑을떄의 경우의수를 쉽게 알 수 있따

# v = [0,1,2,3,4]

# # 콤비네이션스 함수에 첫번째 파라메터로는 배열 , 두번쨰는 몇개씩 뽑을 것이냐를 선택 할 수 있다. 
# for i in combinations(v,2) :
#     print(i)


        
#백준 2309일곱 난쟁이 
# heights = [int(input()) for _ in range(9)]
# for i in combinations(heights,7):
#     if sum(i) == 100:
#         for height  in sorted(i) :
#             print(height)

        #break # 여기에 break문을 걸어주지 않는다면 계속 for문을 돌아서 또 다른 합이 100이 되는 놈을 찾아서 또 보여주고 또 보여 주게 된다. 
              # 우리가 원하는건 값이 여러개면 하나만 뽑아서 7자리 수만 보여주면 된다.


#조합을 이용하지 않고 for만 사용한 문제 풀이 

# heights = [int(input()) for _ in range(9)]
# heights.sort()
# tot = sum(heights)

# def f() :
#     for i in range(8) : # 8번 돌고
#         for j in range(i+1, 9): # i = 0 이면 8번 , i = 1 이면 7번, i=2 이면 6번, i=3 이면 5번, i=4 이면 4번, i=5 이면 3번, i=6 이면 2번, i=7 이면 1번 돌고 끝 
#             if tot - heights[i] - heights[j] == 100:
#                 for k in range(9):
#                     if i != k and j != k :
#                         print(heights[k])

#                 return
# f()