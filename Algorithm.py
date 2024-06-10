import math

# 좌표 데이터 (예시)
data = {
  "joint1": [(5, 10), (10, 20)],  # (x1, y1), (x2, y2) 형식
  "joint2": [(20, 30), (30, 40)],
}

# 거리 계산 함수 (피타고라스 정리 사용)
def calculate_distance(point1, point2):
  x_diff = point2[0] - point1[0]
  y_diff = point2[1] - point1[1]
  distance = math.sqrt(x_diff**2 + y_diff**2)
  return distance

# 최대 거리 계산 함수
def find_max_distance(points):
  distances = [calculate_distance(points[i], points[i+1]) for i in range(len(points) - 1)]
  maximum_distance = max(distances)
  return maximum_distance

# 예시 실행
joint1_range = find_max_distance(data["joint1"])
joint2_range = find_max_distance(data["joint2"])

print(f"joint1 최대 거리: {joint1_range:.2f}")
print(f"joint2 최대 거리: {joint2_range:.2f}")
