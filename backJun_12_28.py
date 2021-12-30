# 백준 10950번 문제
# n = int(input())

# for i in range(1,n+1) :
#     a,b = map(int, input().split())
#     print(a+b)


#백준 10951번 문제
# while True :
#     try :
#         a,b = map(int, input().split())
#         print(a+b)

#     except :
#         break

#백준 10952번 문제 
# while True :
#     a,b = map(int, input().split())
#     if a != 0 and b != 0 : 
#         print(a+b)
#     else :
#         break

#백준 10953번 문제
# n = int(input())

# for i in range(1,n+1):
#     a,b = map(int, input().split(","))
#     print(a+b)
   
# 백준 11201번 문제
# n = int(input())

# for i in range(1,n+1) :
#     a,b = map(int, input().split())
#     print("Case #{}: {}".format(i,a+b))

# 백준 11022번 문제
# n = int(input())

# for i in range(1,n+1):
#     a,b = map(int,input().split())
#     print("Case #{}: {} + {} = {}".format(i,a,b,a+b))

#백준 11718번 문제
# while True:
#     try:
#         print(input())
#     except :
#         break

#백준 11719번 문제
# while True:
#     try:
#         print(input())
#     except :
#         break
    
#백준 11720번 문제
# n = input()
# print(sum(map(int, input())))

# n = input()
# nums = input()
# total = 0
# for i in nums :
#     total += int(i)  # total= total+int(i)
# print(total)

#백준 11721번 문제 
# 이문제는 python의 for문을 잘 알아야된다. 저는 for문을 배웠지만 증감하는 것을 까먹고 있어서 헤멨습니다.
# 또한 파이썬에서 문자열[인덱스 시작값,보여질값]을 넣으면 해당 문자열에 해당 인덱스 까지만 보여지게 됩니다.
# word = input()
# for i in range(0,len(word),10):
#     print(word[i:i+10])

#백준 2741번 문제
# n = int(input())

# for i in range(1,n+1) :
#     print(i)

# 백준 2742번 문제
# n = int(input())

# for i in range(1,n+1):
#     print((n+1)-i)

#백준 2739번 문제
# n = int(input())

# for i in range(1,10) :
#     print("{} * {} = {}".format(n,i,n*i))

#백준 443번 문제
#이번문제는 배열쓰는 것도 이렇게 푸는것도 생각을 하지 못했다. 구현하기 위해 생각할 시간이 좀 필요한 문제 였던것 같다.
#쉽지 않은 문제인것 같다..
# day =0
# month = [31,28,31,30,31,30,31,31,30,31,30,31]
# week = ["SUN","MON","TUE","WED","THU", "FRI" ,"SAT"]

# x,y = map(int, input().split())

# for i in range(x-1):
#     day += month[i]

# day = (day + y) % 7

# print(week[day])

# # 백준 8393번 문제
# n = int(input())
# temp = 0

# for i in range(1,n+1):
#     temp = temp + i
# print(temp)

# 백준 10818  첫번째 방법
# n = int(input())
# numbers = list(map(int, input().split()))
# maxNum = numbers[0]
# minNum = numbers[0]

    
# for i in range(n) :
#     if numbers[i] > maxNum :
#         maxNum = numbers[i]

# for i in range(n) :
#     if numbers[i] < minNum :
#         minNum = numbers[i]
# print(minNum, maxNum)

# # 백준 10818  두번쨰 방법
# n = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers),max(numbers))

