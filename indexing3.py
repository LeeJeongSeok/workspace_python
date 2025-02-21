import pandas as pd
import numpy as np

print("======= 문제 1: MultiIndex를 가진 DataFrame 생성 =======")
print("아래 데이터를 MultiIndex를 사용하여 DataFrame을 생성하고, 전체 출력하시오.")

data = {
    'Country': ['USA', 'USA', 'Canada', 'Canada', 'Germany', 'Germany'],
    'Year': [2020, 2021, 2020, 2021, 2020, 2021],
    'GDP': [21000, 22000, 1800, 1900, 4000, 4100]
}
# 여기에 코드 작성
df1 = pd.DataFrame(data).set_index(['Country', 'Year'])
print(df1)


print("======= 문제 2: 특정 MultiIndex 행 선택 =======")
print("위에서 만든 DataFrame에서 'Canada' 데이터만 선택하시오.")
# 여기에 코드 작성
print(df1.loc['Canada'])
print(df1.xs('Canada'))


print("======= 문제 3: MultiIndex 특정 레벨의 값 선택 =======")
print("위에서 만든 DataFrame에서 2021년 데이터만 선택하시오.")
# 여기에 코드 작성 (패스)
print(df1.loc[(slice(None), 2021), :])


print("======= 문제 4: 특정 조건을 만족하는 행 선택 =======")
print("아래 DataFrame에서 가격(Price)이 100 이상이고, 수량(Quantity)이 50 이상인 데이터만 출력하시오.")

df4 = pd.DataFrame({
    'Item': ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango'],
    'Price': [50, 120, 80, 200, 150],
    'Quantity': [40, 60, 30, 100, 20]
})
print(df4)
# 여기에 코드 작성
# 가격이 100 이상인 데이터 출력
print(df4[df4.get('Price') >= 100])
# 수량이 50 이상인 데이터 출력
print(df4[df4.get('Quantity') >= 50])
# 합치기
print(df4[(df4['Price'] >= 100) & (df4['Quantity'] >= 50)])
print(df4.query("Price >= 100 and Quantity >= 50"))


print("======= 문제 5: 특정 조건을 만족하는 값 변경 =======")
print("아래 DataFrame에서 가격(Price)이 100 이상이면 'Expensive', 미만이면 'Cheap'으로 변환한 새로운 컬럼을 추가하시오.")

df5 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset'],
    'Price': [1000, 50, 80, 300, 150]
})
# 여기에 코드 작성
print(df5)
def expensivAndCheap(value):
  if value < 100:
    return 'Cheap'
  else:
    return 'Expensive'


# df.assign(col2=lambda x : x.col1+2))
# 새로운 컬럼 생성
# ndf5 = df5.assign(col2 = lambda x : 'Expensive' if df5.get('Price') else 'Cheap')
ndf5 = df5.assign(col2=np.where(df5['Price'] >= 100, 'Expensive', 'Cheap'))
print(ndf5)


print("======= 문제 6: MultiIndex 레벨 교환 (swaplevel 사용) =======")
print("아래 MultiIndex DataFrame에서 인덱스 레벨을 교환하여 ('Year', 'Country') 순서로 변경하시오.")

index = pd.MultiIndex.from_tuples([
    ('USA', 2020), ('USA', 2021),
    ('Canada', 2020), ('Canada', 2021),
    ('Germany', 2020), ('Germany', 2021)
], names=['Country', 'Year'])

df6 = pd.DataFrame({'GDP': [21000, 22000, 1800, 1900, 4000, 4100]}, index=index)
# 여기에 코드 작성
print(df6.swaplevel())

print("======= 문제 7: 특정 인덱스 기준 정렬 =======")
print("위에서 만든 MultiIndex DataFrame에서 'Year'를 기준으로 정렬하시오.")
# 여기에 코드 작성
print(df6.sort_index(axis=0, level=1))


print("======= 문제 8: 두 개의 Series에서 공통된 인덱스만 출력 =======")
print("아래 두 개의 Series에서 공통된 인덱스만 선택하여 출력하시오.")

s8_1 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
s8_2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
# 여기에 코드 작성
print(pd.concat([s8_1, s8_2], axis=1).dropna())

print("======= 문제 9: 특정 인덱스 값 변경 =======")
print("아래 DataFrame에서 'd' 인덱스를 'z'로 변경하시오.")

df9 = pd.DataFrame({'Values': [10, 20, 30, 40]}, index=['a', 'b', 'c', 'd'])
# 여기에 코드 작성
print(df9.rename(mapper={'d':'z'}, axis=0))

print("======= 문제 10: 특정 인덱스가 포함된 행 삭제 =======")
print("아래 DataFrame에서 인덱스가 'b' 또는 'd'인 행을 삭제하시오.")

df10 = pd.DataFrame({'Values': [10, 20, 30, 40]}, index=['a', 'b', 'c', 'd'])
# 여기에 코드 작성
print(df10.drop(labels=['b', 'd'], axis=0))



df11 = pd.DataFrame(
            [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]],
            index=[1, 2, 3],
            columns=list('abcd'))

print(df11)
