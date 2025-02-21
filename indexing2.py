import pandas as pd
import numpy as np

print("======= 문제 1: 특정 인덱스의 여러 값 선택 =======")
print("아래 Series에서 인덱스가 'b', 'd', 'f'인 값들만 선택하여 출력하시오.")

s1 = pd.Series([10, 20, 30, 40, 50, 60], index=['a', 'b', 'c', 'd', 'e', 'f'])
# 여기에 코드 작성
print(s1[['b', 'd', 'f']])

print("======= 문제 2: 특정 인덱스의 값 변경 =======")
print("아래 Series에서 인덱스 'c'의 값을 300으로 변경하고, 'e'의 값을 500으로 변경한 후 출력하시오.")

s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# 여기에 코드 작성
s2[['c', 'e']] = 300, 500
print(s2)

print("======= 문제 3: 특정 조건을 만족하는 값 선택 (불리언 인덱싱) =======")
print("아래 Series에서 값이 40 이상인 데이터만 선택하여 출력하시오.")

s3 = pd.Series([25, 35, 45, 20, 50, 10, 60])
# 여기에 코드 작성
print(s3[s3 >= 40])

print("======= 문제 4: 특정 조건을 만족하는 값 변경 =======")
print("아래 Series에서 값이 30 미만인 경우 'Low', 30 이상 50 미만이면 'Medium', 50 이상이면 'High'로 변환한 새로운 Series를 만드시오.")

s4 = pd.Series([10, 20, 35, 45, 55, 25, 50])
# 여기에 코드 작성
ns4 = s4.apply(lambda x: "Low" if x < 30 else "Medium" if x < 50 else "High")
print(ns4)


print("======= 문제 5: 인덱스 재정렬 (reindex 사용) =======")
print("아래 Series의 인덱스를 ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 순서로 변경하고, 없는 값은 NaN으로 채운 후 출력하시오.")

s5 = pd.Series([100, 200, 300, 400, 500], index=['a', 'c', 'e', 'g', 'b'])
# 여기에 코드 작성
ns5 = s5.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(ns5)

print("======= 문제 6: 인덱스 변경 및 설정 =======")
print("아래 DataFrame에서 'Category' 컬럼을 인덱스로 설정한 후 출력하시오.")

df6 = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})
# 여기에 코드 작성
df6.set_index('Category', inplace=True)
print(df6)

print("======= 문제 7: 다중 인덱스 생성 및 조회 =======")
print("아래 데이터를 MultiIndex를 사용하여 DataFrame을 생성하고, ('Seoul', 2020) 데이터만 선택하여 출력하시오.")

data = {
    'City': ['Seoul', 'Seoul', 'Busan', 'Busan'],
    'Year': [2020, 2021, 2020, 2021],
    'Population': [9.7, 9.6, 3.4, 3.3]
}

# 여기에 코드 작성
city = pd.Series(data['City'])
year = pd.Series(data['Year'])
population = pd.Series(data['Population'])

df7 = pd.DataFrame({'City': city, 'Year': year, 'Population': population})
print(df7)
print(df7.iloc[0, 0:2])

print("======= 문제 8: 다중 인덱스의 특정 레벨 선택 =======")
print("아래 MultiIndex DataFrame에서 'Busan' 데이터만 출력하시오.")

index = pd.MultiIndex.from_tuples([
    ('Seoul', 2020), ('Seoul', 2021),
    ('Busan', 2020), ('Busan', 2021)
], names=['City', 'Year'])

df8 = pd.DataFrame({'Population': [9.7, 9.6, 3.4, 3.3]}, index=index)
# 여기에 코드 작성
print(df8.loc['Busan'])

print("======= 문제 9: 두 개의 Series 인덱스를 기준으로 합 연산 수행 =======")
print("아래 두 개의 Series에서 동일한 인덱스끼리 더한 후, 없는 값은 0으로 처리하여 출력하시오.")

s9_1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s9_2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
# 여기에 코드 작성
s9_3 = s9_1.add(s9_2, fill_value=0)
print(s9_3)

print("======= 문제 10: 특정 인덱스가 포함된 행만 선택 =======")
print("아래 DataFrame에서 인덱스가 'b' 또는 'd'인 행만 선택하여 출력하시오.")

df10 = pd.DataFrame({
    'Value': [100, 200, 300, 400],
}, index=['a', 'b', 'c', 'd'])
# 여기에 코드 작성
print(df10.loc['b' or 'd'])
print(df10.loc[['b', 'd']])
