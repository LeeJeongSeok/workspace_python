from operator import concat

import pandas as pd
import numpy as np

print("======= 중급 문제 ======")
print("======= 주제 1: 객체 내의 연산 (Series 내부 값 변환 및 조작) ======")
# 문제 풀기전 궁금증
# 1. Series 내부 값을 변환하거나 조작하면 원본 데이터의 영향을 미치는건가?

print("======= 문제 1: 다음 Series에서 모든 값을 제곱한 후, 10을 더한 결과를 출력하시오. ======")
s1 = pd.Series([2, 4, 6, 8, 10])
ns1 = s1 * s1
print("제곱 전: ")
print(s1)
print("제곱 후: ")
print(ns1)

print("======= 문제 2: 아래 Series에서 각 값의 제곱근(sqrt)을 구한 후, 소수점 2자리까지 반올림하여 출력하시오. ======")
s2 = pd.Series([4, 9, 16, 25, 36])
ns2 = np.sqrt(s2).round(2)
print("제곱근 구하기 전: ")
print(s2)
print("제곱근 구한 후: ")
print(ns2)

print("======= 문제 3: 아래 Series에서 각 값의 로그(log) 를 구하고, NaN 값은 0으로 대체하여 출력하시오. ======")
s3 = pd.Series([1, 10, 100, np.nan, 1000, 0])
print("로그 구하기전")
ns3 = np.log(s3).round(2) # 여기서 먼저 log를 연산하면 음의 무한대(-inf)가 발생하기 때문에 NaN으로 처리를 먼저 진행
print("로그 구한 후")
print("nan값 0으로 바꾸기 전")
filled_s3 = ns3.fillna(0)
print("nan값 0으로 바꾼 후")
print(filled_s3)
# 개선 코드: replace로 nan을 0으로 바꾸고 연산
# replace(변경전 값, 변경될 값)
ns3 = np.log(s3.replace(0, np.nan)).round(2).fillna(0)


print("======= 주제 2: 객체 간의 연산 (Series 간의 연산) ======")
print("======= 문제 4: 아래 Series에서 각 값의 로그(log) 를 구하고, NaN 값은 0으로 대체하여 출력하시오. ======")
s4_1 = pd.Series([10, 20, 30, 40, 50])
s4_2 = pd.Series([5, 15, 25, 35, 45])
print("각 요소의 합")
s4_3 = s4_1 + s4_2
print(s4_3)

print("각 요소의 차")
s4_3 = s4_1 - s4_2
print(s4_3)

print("각 요소의 곱")
s4_3 = s4_1 * s4_2
print(s4_3)

print("각 요소의 나눗셈")
s4_3 = s4_1 / s4_2
print(s4_3)

print("======= 문제 5: 아래 두 개의 Series가 있을 때, 서로 다른 인덱스를 가진 요소들을 더할 경우 NaN 대신 0으로 처리하여 연산하시오. ======")
s5_1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s5_2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])

s5_3 = s5_1.add(s5_2, fill_value=0)
print(s5_3)

print("======= 문제 6: 아래 두 개의 Series에서 값이 더 큰 요소를 선택하여 새로운 Series를 만드시오. ======")
s6_1 = pd.Series([100, 200, 300, 400, 500])
s6_2 = pd.Series([150, 150, 350, 350, 600])

s6_3 = s6_1.where(s6_1 > s6_2, s6_2)
print(s6_3)
#개선안
"""
s6_3 = s6_1.combine(s6_2, max)
# 또는
s6_3 = np.maximum(s6_1, s6_2)
"""

print("======= 주제 3: 불리언 인덱싱 (조건을 활용한 데이터 필터링) ======")
print("======= 문제 7: 아래 Series에서 값이 50 이상인 요소만 출력하시오. ======")
s7 = pd.Series([10, 20, 50, 60, 70, 30, 90])
ns7 = s7[s7 >= 50]
print(ns7)

print("======= 문제 8: 아래 Series에서 값이 20 이상 80 이하인 데이터만 필터링하여 출력하시오. ======")
s8 = pd.Series([5, 15, 25, 35, 45, 85, 95, 75])
ns8 = s8[(s8 >= 20) & (s8 <= 80)] # ns8 = s8[s8.between(20, 80)] 로 대체 가능
print(ns8)

print("======= 문제 9: 아래 Series에서 짝수인 값만 선택하여 출력하시오. ======")
s9 = pd.Series([1, 3, 6, 9, 12, 15, 18])
ns9 = s9[s9 % 2 == 0]
print(ns9)

print("======= 문제 10: 아래 Series에서 값이 30 이상인 경우 Pass, 미만인 경우 Fail 로 변환한 새로운 Series를 만드시오. ======")
# 일단 람다식으로 바꾸기 전에 함수로 먼저 선언
def pass_or_fail(value):
  if value >= 30:
    return "Pass"
  else:
    return "Fail"

s10 = pd.Series([10, 25, 30, 45, 20, 35, 50])
ns10 = s10.apply(lambda x: "Pass" if x >= 30 else "Fail")
print(ns10)


