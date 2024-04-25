import math

# Noktaların temsili için tuple oluşturduk
points = [(2, 3), (5, 8), (10, 12), (15, 20)]

# Öklid mesafesi için fonksiyon tanımladık
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafelerin hesaplanması için bir döngü oluşturduk
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulduk
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
