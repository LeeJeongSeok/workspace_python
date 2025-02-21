import numpy as np
import pandas as pd

print("======= 문제 1: 특정 조건 필터링 =======")
print("아래 DataFrame에서 나이가 30 이상이면서 점수(Score)가 80 이상인 학생들만 선택하시오.")

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [24, 30, 22, 40, 28, 35, 29],
    'Score': [85, 90, 95, 88, 76, 82, 91]
})
# 여기에 코드 작성
score_age = df1.loc[(df1['Age'] >= 30) & (df1['Score'] >= 80)]
print(score_age)

print("======= 문제 2: 조건에 따라 값 변경 =======")
print("위 DataFrame에서 점수(Score)가 90 이상인 학생들의 나이를 99로 변경하시오.")

# 여기에 코드 작성
df1.loc[df1['Score'] >= 90, 'Age'] = 99
print(df1)

print("======= 문제 3: 특정 인덱스 삭제 =======")
print("아래 DataFrame에서 인덱스가 'b'와 'd'인 행을 삭제하시오.")

df2 = pd.DataFrame({
    'Value': [100, 200, 300, 400, 500, 600],
}, index=['a', 'b', 'c', 'd', 'e', 'f'])
# 여기에 코드 작성
print(df2.drop(['b', 'd']))

print("======= 문제 4: 인덱스 재설정 =======")
print("위에서 삭제한 후, 인덱스를 초기화하고 기존 인덱스를 삭제하시오.")

# 여기에 코드 작성
drop_b_d = df2.drop(['b', 'd'])
print(drop_b_d.reset_index().drop('index', axis=1))

print("======= 문제 5: 조건에 따라 값 변경 =======")
print("아래 DataFrame에서 점수(Score)가 80 미만이면 'Low', 80 이상 90 미만이면 'Medium', 90 이상이면 'High'로 점수를 수정하시오.")

df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Score': [70, 82, 95, 78, 88, 91]
})
# 여기에 코드 작성
df3['Score'] = np.where(df3['Score'] < 80, "Low",np.where(df3['Score'] < 90, "Medium", "High"))
print(df3)

print("======= 문제 6: 조건에 따라 새로운 컬럼 추가 =======")
print("위 DataFrame에서 이름(Name)이 5글자 이상이면 'Long', 아니면 'Short'로 새로운 컬럼을 추가하시오.")

# 여기에 코드 작성
df3['Col'] = df3['Name'].apply(lambda x: "Long" if len(x) >= 5 else "Short")
print(df3)

print("======= 문제 7: 복합 조건 필터링 후 값 수정 =======")
print("아래 DataFrame에서 나이가 25 이상이면서 점수(Score)가 85 이상인 경우, 점수를 100으로 변경하시오.")

df4 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [24, 30, 22, 40, 28, 35, 29],
    'Score': [85, 90, 95, 88, 76, 82, 91]
})
# 여기에 코드 작성
# df4[(df4['Age'] >= 25) & (df4['Score'] >= 85), 'Score'] = 100
df4.loc[(df4['Age'] >= 25) & (df4['Score'] >= 85), 'Score'] = 100
print(df4)

print("======= 문제 8: 조건에 따라 행 삭제 =======")
print("위 DataFrame에서 나이가 30 미만이면서 점수(Score)가 80 미만인 행을 삭제하시오.")

# 여기에 코드 작성
drop_score = df4.loc[(df4['Age'] < 30) & (df4['Score'] < 80)]
df4.drop(drop_score.index, inplace=True)
print(df4)


print("======= 문제 9: 인덱스 변경 =======")
print("아래 DataFrame에서 'Name' 컬럼을 인덱스로 설정하시오.")

df5 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 75000, 62000]
})
# 여기에 코드 작성
df5.set_index('Name', inplace=True)
print(df5)

print("======= 문제 10: 인덱스 값 변경 =======")
print("위 DataFrame에서 인덱스가 'David'인 행의 인덱스를 'Daniel'로 변경하시오.")

# 여기에 코드 작성
df5.rename(index={'David': 'Daniel'})
print(df5)



