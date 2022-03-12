# 큰수의 법칙( 가장 큰수를 k번 더하고, 두번째로 큰수를 한번 더하는 연산)
# n, m, k를 공백으로 구분하여 입력받기
n, m , k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

#입력받은 수 정렬
data.sort()
first = data[n -1]
second = data[n -2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m ==0:
        break
    result += second
    m -= 1

print(result) 