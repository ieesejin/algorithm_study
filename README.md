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

### 문자열 문자, 숫자 확인
> isalpha(), isdigit()
> 
> 문자열에서 문자와 숫자를 확인
>
> return: boolean
```python
num = '100'
str1 = 'abc'
str2 = '한글'

print(num.isalpha()) # False
print(str1.isalpha()) # True
print(str2. isalpha()) # True

print(num.isdigit()) # True
print(str1.isdigit()) # False
print(str2.isdigit()) # False

print('-_!@'.isdigit()) # False
print('-_!@'.isalpha()) # False
```

### 문자열 치환
> str = str.replace('치환 전 문자', '치환 후 문자', 치환 횟수)
>
> 치환 횟수는 생략가능 --> 생략하면 전부 치환
```python
str1 = 'abab'
atoc = str1.replace('a', 'c')
print(atoc) # 'cbcb'
atob = str1.replace('a', 'b', 1)
print(atob) # 'bbab'
```


### 이진탐색
> python 표준 라이브러리로 이진탐색 알고리즘으로 오름차순으로 정렬된 리스트에 x 값이 들어갈 위치를 탐색하거나 삽입할 수 있다.
>
> bisect(a, x), bisect_right(a, x) --> 리스트 a에 이미 x 값이 있을 때 뒤쪽 위치를 리턴
> 
> bisect_left(a, x) --> 리스트 a에 이미 x 값이 있을 때 왼쪽 위치를 리턴
>
> insort(a, x) --> 리스트 a에 x를 삽입한다.
```python
import bisect

a = [1, 3, 4, 5]
print(bisect.bisect_right(a, 3)) # 2
print(bisect.bisect_left(a, 3)) # 1

bisect.insort(a, 2)
print(a) # [1, 2, 3, 4, 5]
```


### 문자열 앞 자릿수 맞춰 0 채우기
> str.zfill(자릿 수) --> 자릿수가 될 때까지 앞에 0으로 채움
>
> str.rjust(자릿 수, 문자) --> 자릿수가 될 때까지 앞에 '문자'로 채움
```python
a = '2'
print(a.zfill(3)) # '003'
print(a.rjust(3, "0")) # '003'
print(a.rjust(3, "a")) # 'aa3'
```