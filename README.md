# Coordinate-Plane-Ranging-Algorithm
Python implementation of an algorithm to find the distance between coordinate planes 

코드 개요:

### data 딕셔너리
 좌표 데이터를 저장하는 딕셔너리입니다. 키는 데이터 그룹을 나타내는 문자열이며, 값은 각 그룹의 좌표 쌍 목록입니다.

`calculate_distance` 함수: 두 좌표 간의 거리를 계산하는 함수입니다. 피타고라스 정리를 사용하여 x축 거리와 y축 거리의 제곱을 더하고 제곱근을 취합니다.

`find_max_distance` 함수: 특정 데이터 그룹의 최대 거리를 계산하는 함수입니다. 각 그룹의 좌표 쌍 사이 거리를 계산하고 그 중 최대값을 반환합니다.

예시 실행: 두 데이터 그룹 `"joint1"`과 `"joint2"`에 대한 최대 거리를 계산하고 결과를 출력합니다.

### 코드 사용 방법
data 딕셔너리를 수정하여 사용자 데이터를 입력합니다. 각 키는 데이터 그룹을 나타내는 문자열이고, 값은 각 그룹의 좌표 쌍 목록입니다. 좌표 쌍은 튜플 형식으로 (x, y) 값을 포함해야 합니다.
코드를 실행하여 각 데이터 그룹의 최대 거리를 계산합니다. 출력 결과는 다음과 같습니다.
```
joint1 최대 거리: 14.14
joint2 최대 거리: 17.32
```