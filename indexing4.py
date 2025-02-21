import pandas as pd
from pandas import Series

print("======= 문제 1: 특정 조건을 만족하는 데이터 선택 =======")
print("아래 DataFrame에서 가격(Price)이 150 이상인 제품만 선택하시오.")

df1 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset'],
    'Price': [1000, 50, 80, 300, 150],
    'Stock': [30, 200, 150, 50, 70]
})
# 여기에 코드 작성

print(df1[df1['Price'] > 150])