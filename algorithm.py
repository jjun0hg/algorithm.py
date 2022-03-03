"""array = [3,5,1,2,4]
summary = 0

for x in array:
  summary += x

print(summary)

a = 5
b = 7

print(a+b)

array = [3,5,1,2,4]

for i in array:
  for j in array:
    temp = i * j
    print(temp)

import time
start_time = time.time() # 측정시작

# 프로그램 소스코드
end_time = time.time()  #측정 종료
print("time :", end_time - start_time)  # 수행 시간 출력
"""
# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교

from random import randint
import time

array = []
for _ in range(10000):
  array.append(randint(1, 100)) # 1부터 100 사이의 랜덤한 정수

#선택 정렬프로그램 성능 측정
start_time = time.time()
for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i +1, len(array)):
    if array[min_index] >array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #스와프

end_time = time.time() # 측정종료
print("선택 정렬 성능 측정:", end_time - start_time)

array = []
for _ in range(10000):
  array.append(randint(1,100)) # 1부터 100 사이의 랜덤한 정수

start_time = time.time()
# 기본 정렬 라이브러리 사용

array.sort()
end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)#수행시간 출력



  







