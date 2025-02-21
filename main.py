import pandas as pd
import numpy as np

print("===========================================")
s = pd.Series([5, 15, 25, 35, 45], index=['A', 'B', 'C', 'D', 'E'])
print(s['B'])
print(s['D'])

print("=======값 수정======")
s['B'] = 100
s['E'] = 500

print(s)

print("======= 연산 ======")
s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s1 + s2)

print("======= 연산 ======")
s3 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s4 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])  # 'e' 인덱스 없음

result = s3.add(s4, fill_value = 0)  # s2에 없는 값은 0으로 처리
print("s3 + s4 결과 (fill_value 사용):\n", result)


print("======= 문제 6: 결측값 처리 ======")
s6 = pd.Series([1, np.nan, 3, np.nan, 5])
s6_filled = s6.fillna(0).astype(int)
print(s6_filled)

print("======= 문제 7: 데이터 정렬 ======")
s7 = pd.Series([15, 3, 40, 22, 8])
sorted_s7 = s7.sort_values(ascending=False)
print(s7)
print(sorted_s7)

print("======= 문제 8: 유니크 값과 개수 ======")
s8 = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(s8.unique())
print(s8.value_counts())
print("유니크 값 (정렬됨):", sorted(s8.unique()))  # 정렬된 유니크 값 출력
print("\n값 별 개수 (내림차순 정렬):\n", s8.value_counts().sort_index())  # 인덱스 기준 정렬


print("======= 문제 9: 특정 값 존재 여부 확인 ======")
s9 = pd.Series([5, 15, 25, 35, 45])
for value in s9.values:
  if(value == 30):
    print("30이 존재합니다.")
print("30이 존재하지 않습니다.")

# 개선안: in 연산자를 활용
if 30 in s9.values:
    print("30이 존재합니다.")
else:
    print("30이 존재하지 않습니다.")

print("======= 문제 10: 문자열 처리 ======")
s10 = pd.Series(["apple", "banana", "cherry", "date"])
# for value10 in s10.values:
#   upper = value10.upper()
#   print(upper)

# 개선안: 벡터 연산을 활용한 대문자 변환
print(s10.str.upper())


