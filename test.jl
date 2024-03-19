groups = Dict(1 => [], 2 => [], 3 => [], 4 => [])
compare = [2, 5, 8, 0, 4, 1]
tmp = minimum(compare)
t = argmin(compare)
i = (2, 1)
j = (2, 1)
push!(groups[argmin(compare)], i)
push!(groups[argmin(compare)], j)
println(groups)