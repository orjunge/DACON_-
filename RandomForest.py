import pandas as pd
import numpy as np

# 데이터 로드
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sub = pd.read_csv("sample_submission.csv")

# 데이터 확인
print(train.shape, test.shape, sub.shape)
display(train.head(2), test.head(2), sub.head(2))
## 결측치 및 정보
train.isnull().sum()
train.describe()
train.info()

# 전처리
## 대출등급 값을 숫자로 변환
grade_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
train['대출등급'] = train['대출등급'].map(grade_mapping)

## 'object' dtype을 가진 컬럼 삭제
object_columns = train.select_dtypes(include=['object']).columns
train = train.drop(columns=object_columns)

# 모델 생성 및 예측
## 입력 특성과 타겟 변수 분리
X = train.iloc[:, :-1]
y = train.iloc[:, -1]

##  모델 생성
model = RandomForestRegressor()

## 모델 학습
model.fit(X, y)

## 'object' dtype을 가진 컬럼 삭제
object_columns = test.select_dtypes(include=['object']).columns
test = test.drop(columns=object_columns)

prediction = model.predict(test)

## 반올림하여 대출등급 변환 후 '대출등급' 컬럼에 추가
sub['대출등급'] = pd.Series(np.round(prediction)).astype(int).map(grade_mapping)


# 파일 생성
# sub.to_csv("240115_랜덤포레스트.csv", index=False)
