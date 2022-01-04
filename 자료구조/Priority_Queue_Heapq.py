# 우선순위 큐 (=Priority Queue) , 시간복잡도 : O(log N)

# 2진트리에서 rootNode(=뿌리 처음시작)의 값이 가장 큰값이 오면 max-heap라 칭하고 가장 작은 값이 오면 mini-heap라 칭한다
# 파이썬은 2진트리 rootNode오는 수는 제일 작은 수이므로 mini-heap 이라한다.
# 파이썬은 우선순위 큐에서 값을 뺄 때에는 가장 작은 값이 먼저 빠지게 된다. 
# 또한 다른 언어에서 pop()함수를 통해서 빼기만 하지만 파이썬은 get()함수를 사용하며 빠지는 놈이 누구인지도 출력후 빠진다

# PriorityQueue의 느린속도의 대응책 heapq(=힙큐)
import heapq # 여기서 heapq로 쓰기 귀찮다 하면 ✨as hq로 줄여서 사용할 수 있다.

#✨사용법

pq = []                 # 1. 배열선언을 해준다
heapq.heappush(pq, 6)   # 2. heap.heappush를 통해 수를 넣어준다. 넣어줄때 선언한 배열을 쓰고, 원하는 수를 넣는다.
heapq.heappush(pq, 20)
heapq.heappush(pq, 80)
heapq.heappush(pq, -120)
heapq.heappush(pq, -70)

print(pq)               # 위에서 pq가 배열로 선어 되어있기 때문에 순서대로 들어가지 않을까 라고 생각하지만 heapq.heappush() 통해서 들어 가면 알아서 mini-heap순서로 바꿔준다
while pq:
    print(pq[0])        # 0번쨰는 최상단이므로 mini-heap인 제일 작은수가 오게 된다.
    heapq.heappop(pq)


#이방법 또한 안전한 스레드를 사용해서 하므로 연산 시간이 조금더 오래 걸리므로 코테에서 사용하지 않음
# from queue import Empty, PriorityQueue

# pq = PriorityQueue()
# pq.put(6)
# pq.put(5)
# pq.put(4)
# pq.put(10)
# pq.put(-6)

# while not pq.empty():
#     print(pq)
#     print(pq.get) # 파이썬에서는 get이 pop과 같다 