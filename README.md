# DACON_고객대출등급분류
데이콘 주최의 [고객대출등급분류 대회](https://dacon.io/competitions/official/236214/overview/description)에 참여했던 코드입니다.

## 진행기간
2024.01.15 ~ 2024.02.05

## 최종순위
165등/1,650명 (Private 순위)  
정확도 0.82

## 활용 모델
RandomForest

## 대회 요약
### 목표
고객 정보와 대출 현황 데이터를 바탕으로 고객의 대출등급을 예측하는 AI 알고리즘 개발

### 과정
- 데이터 크기: train(96294, 15), test(64197, 14)
- 모델선정: 과적합(Overfitting)을 줄이고 예측 정확도를 높이기 위해 **RandomForest 모델** 선정
- 액션:
  1. 'A, B, C' 등의 값으로 되어 있는 '대출등급' 컬럼 값을 숫자로 매핑
  2. 데이터 타입 중 'object'인 컬럼 삭제 (삭제를 했을 때 정확도가 더 올라갔음)
  3. 모델 생성 및 예측한 결과를 반올림하여 다시 'A, B, C'의 문자 등급으로 변환  
     ```sub['대출등급'] = pd.Series(np.round(prediction)).astype(int).map(grade_mapping)```
