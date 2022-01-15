# 파이썬 자료구조  큐, 디큐
#from queue import Queue # queue 는 선입 선출(맨처음 들어온놈 맨처음으로 나간다) 
# 또한 큐는 멀티 쓰레드를 제어하면서 사용하기 때문에 느리므로 코테에서는 사용하지 않는다. 밑에껄 사용

# 위와 같은 이유로 파이썬에서 큐 자료구조를 사용해야 될때에는 deque를 사용하면 된다.
from collections import deque # deque는 앞에서 추가 앞에서 삭제, 뒤에서 추가 뒤에서 삭제 양방향 가능한 자료구조

# dq = deque()
# dq.append(123) # 뒤에서부터 삽입
# dq.appendleft(456) # 앞에서부터 삽입
# dq.appendleft(789)

# print(dq)

# print(dq.pop()) # 뒤에서부터 삭제
# print(dq.popleft()) # 앞에서부터 삭제
# print(dq)

#✨ 이문제의 핵심은 2초안에 푸는 것이다. 그러므로 시간 복잡도를 이제 항상 생각하면서 풀어야 되는게 핵심인 문제이다. 
# # 백준 2164번 카드2 문제  
# N =int(input())
# dq = deque() 
# for i in range(1, N+1): 
#     dq.append(i)

# #print(dq)
# while len(dq) > 1: # 마지막 하나만 찾아야 하니깐 길이가 1일때 멈춰라
#     dq.popleft()   # 맨앞에 놈을 삭제 
#     dq.append(dq.popleft()) # 그다음 맨앞을 삭제하고 추가를해주면 문제에서 봤던 맨아래에 넣는 형식이 된다. 굿

# print(dq.popleft()) 

#✨ 이문제를 배열로 풀게 된다면 시간복잡도는 O(N^2) 이 되므로 최대 50만인 수가 왔을 떄는 벌써 2초를 넘겨 버린다 그러므로 사용할 수없는 방법이다.
# 백준 2164번 카드2 문제  배열로 풀기 
N =int(input())
arr = []
for i in range(1, N+1) :
    arr.append(i)
    
#print(dq)
while len(arr) > 1: # 마지막 하나만 찾아야 하니깐 길이가 1일때 멈춰라
    arr.pop(0)   # 맨앞에 놈을 삭제 
    arr.append(arr.pop(0)) # 그다음 맨앞을 삭제하고 추가를해주면 문제에서 봤던 맨아래에 넣는 형식이 된다. 굿

print(arr.pop()) 