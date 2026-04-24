# map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 반환
# map 함수는 map 객체를 반환한다.
# 리스트를 입력받아 각 요소에 2를 곱해 반환하는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result) # [2,4,6,8]

def two_times(x):
    return x * 2

print(list(map(two_times, [1, 2, 3, 4]))) # [2, 4, 6, 8]

# lambda 사용
print(list(map(lambda a: a*2, [1, 2, 3, 4])))