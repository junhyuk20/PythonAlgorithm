# 파이썬 자료구조  큐, 디큐
#from queue import Queue # queue 는 선입 선출(맨처음 들어온놈 맨처음으로 나간다) 
# 또한 큐는 멀티 쓰레드를 제어하면서 사용하기 때문에 느리므로 코테에서는 사용하지 않는다. 밑에껄 사용

# 위와 같은 이유로 파이썬에서 큐 자료구조를 사용해야 될때에는 deque를 사용하면 된다.
from collections import deque # deque는 앞에서 추가 앞에서 삭제, 뒤에서 추가 뒤에서 삭제 양방향 가능한 자료구조

dq = deque()
dq.append(123) # 뒤에서부터 삽입
dq.appendleft(456) # 앞에서부터 삽입
dq.appendleft(789)

print(dq)

print(dq.pop()) # 뒤에서부터 삭제
print(dq.popleft()) # 앞에서부터 삭제
print(dq)