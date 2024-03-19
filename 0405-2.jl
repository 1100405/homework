data_point = [(2,5), (3,2), (3,3), (3,4), (4,3), (4,4), (6,3), (6,4),
             (6,6), (7,2), (7,5), (7,6), (7,7), (8,6), (8,7)]
clusters = [(2.0,2.0), (4.0,6.0), (6.0,5.0), (8.0,8.0)]
distance_avg = 0.0

calculateDistance(point_1, point_2) =
    sqrt((point_1[1]-point_2[1])^2 + (point_1[2]-point_2[2])^2)

function search()
    global distance_avg
    distance_avg = 0.0
    compare = []
    for i in data_point
        for j in clusters
            push!(compare, calculateDistance(i, j))
        end
        tmp = minimum(compare)
        push!(groups[argmin(compare)], i)
        distance_avg += tmp
        compare = []
    end
    distance_avg /= 15.0
end

function update()
    for i in 1:4
        count, x, y = 0.0, 0, 0
        for j in groups[i]
            x += j[1]
            y += j[2]
            count += 1
        end
        x /= count
        y /= count
        clusters[i] = (x, y)
    end
end

for i in 0:9
    global groups = Dict(1 => [], 2 => [], 3 => [], 4 => [])
    search()
    update()
    println(string(i) * ": ", distance_avg)
end
