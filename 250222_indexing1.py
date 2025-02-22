import pandas as pd
import numpy as np

print("======= 문제 1: 조건에 따라 값 변경 =======")
print("아래 DataFrame에서 점수(Score)가 70 미만이면 'Fail', 70 이상 90 미만이면 'Pass', 90 이상이면 'Excellent'로 변경하시오.")

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Score': [65, 72, 85, 95, 68, 88, 91]
})
# 여기에 코드 작성
df1['Score'] = df1.apply(lambda x: 'Fail' if x.Score < 70 else 'Pass' if x.Score < 90 else 'Excellent',axis=1)
print(df1)

print("======= 문제 2: 새 컬럼 생성 (조건에 따라 등급 부여) =======")
print("위 DataFrame에서 'Grade'라는 새로운 컬럼을 추가하고, 점수에 따라 등급을 부여하시오.")
print("점수가 90 이상이면 'A', 80 이상 90 미만이면 'B', 70 이상 80 미만이면 'C', 70 미만이면 'F'.")

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Score': [65, 72, 85, 95, 68, 88, 91]
})
# 여기에 코드 작성
df2['Grade'] = df2.apply(lambda x: 'A' if x.Score >= 90 else 'B' if x.Score >= 80 else 'C' if x.Score >= 70 else 'F' , axis=1)
print(df2)

print("======= 문제 3: np.where()로 컬럼 값 변경 =======")
print("아래 DataFrame에서 연봉(Salary)이 60000 이상이면 'High', 그렇지 않으면 'Low'로 새 컬럼을 생성하시오.")

df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [55000, 75000, 62000, 80000, 58000]
})
# 여기에 코드 작성
print(df3['Salary'])
df3['Col'] = df3.apply(lambda x: 'High' if x.Salary >= 60000 else 'Low', axis=1)
print(df3)

print("======= 문제 4: apply()와 lambda로 복잡한 조건 처리 =======")
print("아래 DataFrame에서 나이(Age)가 30 이상이면 'Senior', 25 이상 30 미만이면 'Adult', 그 외에는 'Young'으로 구분하는 새 컬럼을 생성하시오.")

df4 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [22, 27, 35, 40, 29]
})
# 여기에 코드 작성
df4['Col'] = np.where(df4['Age'] >= 30, 'Senior', np.where((df4['Age'] >= 25) & (df4['Age'] < 30), 'Adult', 'Young'))
print(df4)

print("======= 문제 5: 다중 조건에 따라 값 변경 =======")
print("아래 DataFrame에서 구매금액(Purchase)이 100 이상이면 'Premium', 50 이상 100 미만이면 'Standard', 50 미만이면 'Basic'으로 변경하시오.")

df5 = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Purchase': [45, 85, 120, 30, 70, 200]
})
# 여기에 코드 작성
df5['Purchase'] = df5.apply(lambda x: 'Preminum' if x.Purchase >= 100 else 'Standard' if x.Purchase >= 50 & x.Purchase < 100 else 'Basic', axis=1)
print(df5)

print("======= 문제 6: 다중 조건으로 새 컬럼 생성 =======")
print("위 DataFrame에서 구매금액에 따라 할인율(Discount)을 부여하시오. 100 이상이면 20%, 50 이상이면 10%, 그 외는 5%.")
df6 = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Purchase': [45, 85, 120, 30, 70, 200]
})

# 여기에 코드 작성
df6['Discount_Percent'] = np.where(df6['Purchase'] >= 100, '20%', np.where(df6['Purchase'] >= 50, '10%', '5%'))
print(df6)

print("======= 문제 7: 기존 컬럼 기반으로 새로운 데이터 생성 =======")
print("아래 DataFrame에서 'First Name'과 'Last Name'을 합쳐서 'Full Name' 컬럼을 생성하시오.")

df7 = pd.DataFrame({
    'First Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Last Name': ['Smith', 'Brown', 'Johnson', 'Williams', 'Miller']
})
# 여기에 코드 작성
assign = df7.assign(Full_Name = df7['First Name'] + df7['Last Name'])
print(assign)

print("======= 문제 8: 조건에 따라 값 증가 =======")
print("아래 DataFrame에서 재고량(Stock)이 10 미만이면 5를 추가하고, 그렇지 않으면 그대로 유지하시오.")

df8 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset'],
    'Stock': [5, 15, 8, 20, 3]
})
# 여기에 코드 작성
df8['New Stock'] = np.where(df8['Stock'] < 10, df8['Stock'] + 5, df8['Stock'])
print(df8)