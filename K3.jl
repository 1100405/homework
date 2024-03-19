using CSV, DataFrames, PrettyTables, Clustering, Plots, StatsPlots, Random

df = CSV.read("dye.csv", DataFrame)
df_group = groupby(df, :class)

df_centers = DataFrame()
rng = MersenneTwister(405)

for class in df_group
    shuffled_class = shuffle(rng, class)
    first_50_rows = shuffled_class[1:50, :]
    
    global X = select(first_50_rows, Not("class"))
    global features = Matrix(X)'
    global result = kmeans(features, 2; maxiter=20, rng)
    df_what_ever = DataFrame(d1 = result.centers'[:, 1],
                             c1 = result.centers'[:, 2],
                             d2 = result.centers'[:, 3],
                             c2 = result.centers'[:, 4],
                             d3 = result.centers'[:, 5],
                             c3 = result.centers'[:, 6])
    append!(df_centers, df_what_ever)
end

pretty_table(Matrix(df_centers))