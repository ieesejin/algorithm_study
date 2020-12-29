# algorithm_study
___
## 소수 확인
> 1보다 큰 정수 N에 대해서 1과 N으로만 나누어 지는 수.

|확인 범위|시간복잡도|
|:---:|:---:|
|2 ~ N|O(N)|
|2 ~ N/2|O(N)|
|2 ~ sqrt(N)|O(sqrt(N))|
___

## heapq
> 이진 트리 기반의 최소 힙 자료구조
>
> 원소들이 항상 정렬된 상태로 추가, 삭제
>
> 모든 원소(K)는 항상 자식 원소(2K+1, 2K+2) 보다 크기가 작거나 같음
```python
import heapq
heap = [3, 2, 5]
heapq.heapify(heap) # O(N)
heapq.heappop(heap) # O(log N)
heapq.heappush(heap, 1) # O(log N)
```
heap[0]으로 최소값을 가져올 수 있다.

최대 힙은 지원을 하지 않으므로 heap (-num, num)으로 최대값을 가져올 수 있다.
```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```
