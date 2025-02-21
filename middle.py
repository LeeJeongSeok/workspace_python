import pandas as pd
import numpy as np

print("======= 중급 문제 ======")

print("======= 문제 1: 특정 값 조건 처리 ======")
s1 = pd.Series([12, 25, 40, 55, 10, 10, 38, 19, 50])
for i in s1:
  if (i <= 20):
    print("Low")
  elif (i > 21 and i <= 40):
    print("Medium")
  else:
    print("High")

# 문제 1번 개선 코드
# 원본 데이터
# s1 = pd.Series([12, 25, 40, 55, 10, 10, 38, 19, 50])
#
# # apply()를 사용하여 벡터 연산 적용
# def categorize(value):
#     if value <= 20:
#         return "Low"
#     elif value <= 40:  # value > 21 조건은 필요 없음
#         return "Medium"
#     else:
#         return "High"
#
# # 변환된 Series 생성
# categorized_s1 = s1.apply(categorize)

# 결과 출력
# print(categorized_s1)
print("======= 문제 2: 결측값 처리 (평균값과 중간값 비교) ======")
s2 = pd.Series([10, 20, np.nan, 40, 50, np.nan, 70])
filled_s2 = s2.fillna(0).astype(int)

# 평균값 구하기
total = 0
for i in filled_s2:
  total += i

average = int(total / len(filled_s2))

# 평균값으로 덮어쓰기
averageFilledS2 = s2.fillna(average).astype(int)
print(averageFilledS2)


print("======= 문제 3: 정규화 (Normalization) ======")
s3 = pd.Series([12, 45, 78, 34, 89, 23, 56, 90])
X_min, X_max = s3.min(), s3.max()
Xnorm = (s3 - X_min) / (X_max - X_min)
print(s3)
print(Xnorm)


print("======= 문제 4: 특정 값 기준 정렬 (아래 Series에서 값이 NaN인 경우를 제외하고, 값이 50 이상인 데이터만 오름차순 정렬하시오.) ======")
s4 = pd.Series([np.nan, 60, 30, 80, 20, np.nan, 55, 70, 45])
ns = s4.dropna()
print(ns)
# 시리즈 값에 대한 특정 조건을 만족하는 데이터만 필터링할 때 사용하는 문법 (Boolean Indexing)
ns = ns[ns >= 50].sort_values()
print(ns)

print("======= 문제 5: 문자열 데이터 필터링 (아래 Series에서 길이가 6 이상인 문자열만 필터링하여 출력하시오.) ======")
s5 = pd.Series(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"])
# for i in s5:
#   if len(i) >= 6:
#     print(i)

print(s5[s5.str.len() >= 6]) # 불리언 인덱싱을 활용하여 길이가 6 이상인 문자열을 필터링


print("======= 문제 6: Series 연산 (값 조정): (다음 Series에서 모든 값이 홀수이면 그대로 두고, 짝수인 경우 +1을 하여 홀수로 변환하시오.) ======")
s6 = pd.Series([2, 7, 10, 13, 18, 21, 30])
ns6 = pd.Series()

for i in s6:
  if i % 2 == 0:
    ns6[i] = i
  else:
    ns6[i] = i + 1

# 짝수인 경우 +1 (홀수 변환)
s6_modified = s6.apply(lambda x: x if x % 2 != 0 else x + 1)

print(ns6)

print("======= 문제 7: 상위 N개 값 출력 (다음 Series에서 상위 3개의 값을 출력하시오.) ======")
s7 = pd.Series([100, 50, 20, 80, 60, 90, 30])
sort = s7.sort_values(ascending=False)
print(sort.head(3))

print(s7.nlargest(3))

print("======= 문제 8: 데이터 그룹화 (Binning) (다음 Series에서 값을 10 단위 구간으로 그룹화하여, 각 그룹의 개수를 출력하시오.) ======")
s8 = pd.Series([5, 12, 25, 37, 48, 52, 68, 75, 88, 95])

# 10 단위로 그룹화 (Binning)
bins = pd.cut(s8, bins=range(0, 101, 10))  # 0~100을 10 단위로 자름
grouped = s8.groupby(bins).count()  # 각 구간별 개수 계산

print(grouped)


