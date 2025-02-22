import pandas as pd
import numpy as np

print("======= 문제 1: 점수에 따라 등급 및 패스 여부 추가 =======")
print("아래 DataFrame에서 점수(Score)에 따라 'Grade' 컬럼과 'Pass/Fail' 컬럼을 생성하시오.")
print("- 90 이상: 'A', 80 이상: 'B', 70 이상: 'C', 70 미만: 'F'")
print("- 점수가 70 이상이면 'Pass', 미만이면 'Fail'")

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Score': [65, 82, 95, 78, 68, 88, 91]
})
# 여기에 코드 작성
df1['Grade'] = df1.apply(lambda x: 'A' if x.Score >= 90 else 'B' if x.Score >= 80 else 'C' if x.Score >= 70 else 'F', axis=1)
df1['Pass/Fail'] = np.where(df1['Score'] >= 70, 'Pass', 'Fail')
print(df1)

print("======= 문제 2: 급여 기준 세금 부과 =======")
print("아래 DataFrame에서 급여(Salary)가 70000 이상이면 30%, 50000 이상이면 20%, 그 외에는 10%의 세율(Tax Rate)을 적용하시오.")

df2 = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [45000, 52000, 60000, 75000, 80000, 48000]
})
# 여기에 코드 작성
df2['Tax Rate'] = df2.apply(lambda x: x.Salary * 0.30 if x.Salary >= 70000 else x.Salary * 0.20 if x.Salary >= 50000 else x.Salary * 0.10, axis=1)
print(df2)

print("======= 문제 3: 이메일 도메인 추출 =======")
print("아래 DataFrame에서 이메일(Email)에서 도메인만 추출하여 'Domain' 컬럼을 생성하시오.")

df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Email': ['alice@example.com', 'bob@company.org', 'charlie@edu.net', 'david@enterprise.com', 'eve@startup.io']
})
# 여기에 코드 작성
df3['Domain'] = df3.apply(lambda x: x.Email.split('@')[1], axis=1)
print(df3)

print("======= 문제 4: 이름 길이에 따라 그룹화 =======")
print("아래 DataFrame에서 이름(Name)의 길이가 5자 이상이면 'Long', 그렇지 않으면 'Short'로 구분하는 새로운 컬럼을 생성하시오.")

df4 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
})
# 여기에 코드 작성
df4['Name Length'] = np.where(df4['Name'].str.len() >= 5, 'Long', 'Short')
print(df4)

print("======= 문제 5: 구매 등급 분류 =======")
print("아래 DataFrame에서 구매 금액(Purchase)이 200 이상이면 'Platinum', 150 이상이면 'Gold', 100 이상이면 'Silver', 100 미만이면 'Bronze'로 등급을 분류하시오.")

df5 = pd.DataFrame({
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Purchase': [50, 150, 250, 180, 90, 300]
})
# 여기에 코드 작성
df5['Grade'] = np.where(df5['Purchase'] >= 200, 'Platinum', np.where(df5['Purchase'] >= 150, 'Gold', np.where(df5['Purchase'] >= 100, 'Silver', 'Bronze')))
print(df5)


print("======= 문제 6: 재고 업데이트 =======")
print("아래 DataFrame에서 재고(Stock)가 20 미만인 경우 10을 추가하고, 그렇지 않으면 유지하시오.")

df6 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset', 'Webcam'],
    'Stock': [5, 15, 25, 30, 12, 18]
})
# 여기에 코드 작성
# df6['Stock'] = df6.apply(lambda x: x.Stock + 10 if x.Stock < 20 else x.Stock, axis=1)
df6['Stock'] = np.where(df6['Stock'] < 20, df6['Stock'] + 10, df6['Stock'])
print(df6)

print("======= 문제 7: 날짜 데이터 타입 변환 =======")
print("아래 DataFrame에서 'Date' 컬럼을 datetime 형식으로 변환하고, 해당 날짜가 주말인지 여부를 나타내는 'Is_Weekend' 컬럼을 추가하시오.")

df7 = pd.DataFrame({
    'Event': ['Conference', 'Workshop', 'Seminar', 'Webinar', 'Meeting'],
    'Date': ['2024-05-10', '2024-05-11', '2024-05-12', '2024-05-15', '2024-05-17']
})
# 여기에 코드 작성
df7['Is_Weekend'] = df7.apply(lambda x: 'Y' if (pd.to_datetime(x.Date).weekday == 5) or (pd.to_datetime(x.Date).weekday == 6) else 'N', axis=1)
print(df7)

# df7['Date'] = pd.to_datetime(df7['Date'])
# df7['Is_Weekend'] = df7['Date'].dt.weekday.apply(lambda x: 'Y' if x >= 5 else 'N')


print("======= 문제 8: 판매량 등급 구분 =======")
print("아래 DataFrame에서 판매량(Sales)이 상위 25% 이상이면 'Top', 하위 25% 이하면 'Low', 그 외에는 'Average'로 구분하는 새로운 컬럼을 생성하시오.")

df8 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset', 'Webcam', 'Printer', 'Tablet'],
    'Sales': [1500, 200, 500, 1200, 300, 400, 800, 1000]
})
# 여기에 코드 작성
df8['Rank'] = np.where(df8['Sales'] > df8['Sales'].quantile(.75), 'Top', np.where(df8['Sales'] < df8['Sales'].quantile(.25), 'Low', 'Average'))
print(df8)

