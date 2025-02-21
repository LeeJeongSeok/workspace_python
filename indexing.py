import pandas as pd
import numpy as np

print("Level 1: 기본 인덱싱 (기본적인 인덱스 다루기)")
print("======= 문제 1: 특정 위치(index)의 값 조회======")
print("======= 다음 Series에서 인덱스가 'b'인 값을 출력하시오. ======")
s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s1['b'])

print("======= 문제2: 정수 위치 기반 인덱싱(iloc[] 사용) ======")
print("======= 위 Series에서 두 번째(index=1) 값을 출력하시오. ======")
print(s1.iloc[1])

print("======= 문제 3: 여러 개의 특정 인덱스 값 조회 ======")
print("======= 위 Series에서 인덱스가 'a'와 'd'인 값들만 선택하여 출력하시오. ======")
print(s1['a'], s1['d'])
# 개선 코드
print(s1[['a', 'd']])

print("Level 2: 슬라이싱 (연속된 데이터 선택)")
print("======= 문제 4: 슬라이싱을 사용한 특정 범위 선택 (loc[] 사용) ======")
print("======= 위 Series에서 인덱스가 'b'부터 'd'까지의 값만 출력하시오. ======")
print(s1.loc['b':'d'])

print("======= 문제 5: 정수 위치 기반 슬라이싱 (iloc[] 사용) ======")
print("======= 위 Series에서 두 번째(index=1)부터 세 번째(index=2) 값만 출력하시오. ======")
print(s1.iloc[1:3])

print("Level 3: 조건을 활용한 인덱싱 (불리언 인덱싱)")
print("======= 문제 6: 특정 조건을 만족하는 값만 선택 ======")
print("======= 다음 Series에서 값이 50 이상인 데이터만 출력하시오. ======")
s2 = pd.Series([15, 45, 65, 30, 90, 10])
print(s2[s2 >= 50])

print("======= 문제 7: 특정 조건을 만족하는 값만 변경 ======")
print("======= 위 Series에서 값이 50 이상이면 High, 미만이면 Low로 변환하여 새로운 Series를 만드시오. ======")
def highAndLow(value):
  if value >= 50:
    return "High"
  else:
    return "Low"

ns = s2.apply(highAndLow)
print(ns)

print("Level 4: 인덱스 변경 및 설정")
print("======= 문제 8: 인덱스 재설정 (reset_index() 사용) ======")
print("======= 다음 Series에서 기존 인덱스를 삭제하고 새로운 숫자형 인덱스로 변경하시오. ======")
s3 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
ns3 = s3.reset_index(drop=True)
print(ns3)

print("======= 문제 9: 새로운 인덱스 설정 (set_index() 사용)======")
print("======= 다음 DataFrame에서 Name 컬럼을 인덱스로 설정하시오. ======")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
df.set_index('Name', drop=True, inplace=True)
print(df)

print("Level 5: 다중 인덱싱 (MultiIndex)")
print("======= 문제 10: 다중 인덱스 생성 ======")
print("======= 다음 데이터를 MultiIndex를 사용하여 DataFrame을 생성하시오. ======")
data = {
    'City': ['Seoul', 'Seoul', 'Busan', 'Busan'],
    'Year': [2020, 2021, 2020, 2021],
    'Population': [9.7, 9.6, 3.4, 3.3]
}

# 먼저 시리즈로 변환
city = pd.Series(data['City'])
year = pd.Series(data['Year'])
population = pd.Series(data['Population'])

# DataFrame으로 변환
df2 = pd.DataFrame({'City': city, 'Year': year, 'Population': population})
print(df2)

# MultiIndex 설정 --> 이렇게 하면 이전 인덱스가 덮어씌워진다.
# df2.set_index('City', drop=True, inplace=True)
# df2.set_index('Year', drop=True, inplace=True)

# Multiindex 개선코드
df2.set_index(['City', 'Year'], inplace=True)
print(df2)