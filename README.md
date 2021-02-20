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
> heap[0]으로 최소값을 가져올 수 있다.
>
> 최대 힙은 지원을 하지 않으므로 heap (-num, num)으로 최대값을 가져올 수 있다.
```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```
### 접두사 확인
> str1.startswith(str2)
> 
> return type: boolean
```python
str1 = "helloworld"
str2 = "hel"
str1.startswith(str2)
# return True
```

### zip
> zip(list1, list2)
>
> return as list and element as tuple
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
zip(list1, list2)
# result: [(1, 4), (2, 5), (3, 6))
```

### Counter
> collections.Counter()
> 
> return as Dictionary
> 갯수가 많은 것 순으로 return 한다.
```python
import collections
list1 = ['a', 'b', 'c', 'a', 'b', 'e']
collections.Counter(list1)
# return: Counter({'a': 2, 'b': 2, 'c': 1, 'e': 1})

str1 = "ababc"
collections.Counter(str1)
# return: Counter({'a': 2, 'b': 2, 'c': 1})
>```

##### method
> update(): Counter 값을 갱신
```python
import collections
a = collections.Counter()
a.update("ababc")
```
> elements(): 요소들을 무작위 순서로 반환한다.

> most_common(): 요소들을 빈도수가 높은 순으로 (요소, 빈도수) 투플로 이루어진 list를 반환한다.
```python
import collections
a = collections.Counter("aaabcc")
a.most_common()
# return: [('a', 3), ('c', 2), ('b', 1)]
a.most_common(3)
# return: [('a', 3)]
```

### 순열, 조합
> 순열: itertools.permutations
>
> 중복을 허용하지 않고 n개에서 r개를 뽑아서 나열까지 방법
>
> 중복을 허용하진 않지만 뽑는 순서는 의미가 있다.
```python
import itertools
a = itertools.permutations([1, 2, 3, 4], 2)
# a: (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)
# 순서가 의미가 있기 때문에 (1, 2)와 (2, 1)은 다른 것으로 간주한다.
```

> 조합: itertools.combinations
>
> 중복을 허용하지 않고 n개에서 r개를 뽑는 방법
>
> 순서가 의미가 없기 때문에 순열과 다르게 (1, 2) (2, 1)은 같은 것이다.
```python
import itertools
a = itertools.combinations([1, 2, 3, 4], 2)
# a: (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
```