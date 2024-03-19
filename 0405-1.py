import random

data_point = [(2,5), (3,2), (3,3), (3,4), (4,3), (4,4), (6,3), (6,4),
            (6,6), (7,2), (7,5), (7,6), (7,7), (8,6), (8,7)]
#more_points = [(random.randint(0, 30), random.randint(0, 30)) for i in range(30)]
#data_point += more_points
clusters = [(2,2), (4,6), (6,5), (8,8)]
distance_avg = 0

def calculateDistance(point_1, point_2):
    x = point_1[0] - point_2[0]
    y = point_1[1] - point_2[1]
    return (x**2 + y**2)**0.5

def search():
    global distance_avg  #####
    distance_avg = 0 #####
    compare = []
    for i in data_point:
        for j in clusters:
            compare.append(calculateDistance(i, j))
        tmp = min(compare)
        groups[compare.index(tmp)].extend([i])
        distance_avg += tmp  #####
        compare = []
    distance_avg /= 15.0 #####

def update():
    for i in range(4):
        count, x, y = 0.0, 0, 0
        for j in groups[i]:
            x += j[0]
            y += j[1]
            count += 1
        x /= count
        y /= count
        clusters[i] = (x, y)

for i in range(10):
    groups = {0:[], 1:[], 2:[], 3:[]}
    search()
    update()
    print(str(i)+': ', distance_avg)
