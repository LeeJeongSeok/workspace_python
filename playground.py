import pandas as pd
import numpy as np

print("======= 문제 1: 특정 인덱스 행 선택 =======")
print("아래 DataFrame에서 인덱스가 2인 행을 선택하시오.")

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 40, 28],
    'Score': [85, 90, 95, 88, 76]
})
# 여기에 코드 작성
print(df1.iloc[2])

print("======= 문제 2: 슬라이싱으로 연속된 행 선택 =======")
print("아래 DataFrame에서 인덱스 1부터 3까지의 행을 선택하시오.")

# 여기에 코드 작성
print(df1.iloc[1:4])

print("======= 문제 3: 조건부 인덱싱 =======")
print("아래 DataFrame에서 점수(Score)가 85 이상인 행만 선택하시오.")

# 여기에 코드 작성
print(df1.loc[df1['Score'] >= 85])

print("======= 문제 4: 인덱스 변경 =======")
print("아래 DataFrame에서 'Name' 컬럼을 인덱스로 설정하시오.")

# 여기에 코드 작성
df1.set_index('Name', inplace=True)
print(df1)

print("======= 문제 5: 인덱스 재설정 =======")
print("문제 4에서 설정한 인덱스를 초기화하고, 기존 인덱스를 유지하시오.")

# 여기에 코드 작성
df1.reset_index('Name', inplace=True)
print(df1)

print("======= 문제 6: 인덱스 값 변경 =======")
print("아래 DataFrame에서 인덱스가 'd'인 행의 인덱스를 'z'로 변경하시오.")

df6 = pd.DataFrame({
    'Value': [100, 200, 300, 400],
}, index=['a', 'b', 'c', 'd'])
# 여기에 코드 작성
print(df6.rename(index = {'d': 'z'}))

print("======= 문제 7: 조건에 따라 값 변경 =======")
print("아래 DataFrame에서 점수(Score)가 90 이상이면 점수를 100으로 변경하시오.")

df7 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 22, 40, 28],
    'Score': [85, 90, 95, 88, 76]
})

# 여기에 코드 작성
df7.loc[df1['Score'] >= 90, 'Score'] = 100
print(df7)

print("======= 문제 8: 다중 조건 필터링 =======")
print("아래 DataFrame에서 나이가 25 이상이고 점수(Score)가 85 이상인 학생만 선택하시오.")

# 여기에 코드 작성
score_ = df1.loc[(df1['Age'] >= 25) & (df1['Score'] >= 85)]
print(score_)


print("======= 문제 9: 특정 인덱스 행 삭제 =======")
print("아래 DataFrame에서 인덱스가 'b' 또는 'd'인 행을 삭제하시오.")

df9 = pd.DataFrame({
    'Value': [100, 200, 300, 400],
}, index=['a', 'b', 'c', 'd'])
# 여기에 코드 작성
print(df9.drop(['b' or 'd']))

print("======= 문제 10: 조건에 따라 새 컬럼 추가 =======")
print("아래 DataFrame에서 점수(Score)가 90 이상이면 'Pass', 아니면 'Fail'로 표시된 새로운 컬럼을 추가하시오.")

# 여기에 코드 작성
print(df1)
assign = df1.assign(col=np.where(df1['Score'] >= 90, 'Pass', 'Fail'))
print(assign)
