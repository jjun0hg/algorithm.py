#100명의 사람이 하나 이상의 테이블에 나누어 앉는 패턴.

sit_min =2 # 앉힐수있는최소사람수
sit_max = 10 # 앉힐수있는최대사람수
total = 6 # 전체사람의수
memo = {}
# A = 남은사람수, B = 앉힌사람수
def 문제(A, B):
    key = str([A, B])
    if key in memo:
        return memo[key]
    if A < 0:
        return 0
    if A ==0:
        return 1
    global count
    count = 0
    for i in range(B, sit_max +1):
        count += 문제(A - i, i)
    memo[key] = count
    return count
    
print(문제(total, sit_min))
    