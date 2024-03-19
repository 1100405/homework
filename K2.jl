using CSV, DataFrames, PrettyTables, Clustering, Plots, StatsPlots, Random

df = CSV.read("dye.csv", DataFrame)

rng = MersenneTwister(405)

X = select(df, Not("class"))
features = Matrix(X)'
result = kmeans(features, 3; maxiter=20, display=:iter, rng)

cluster_df = DataFrame(class=result.assignments)
CSV.write("cluster3_jl.csv", cluster_df)

scatter(result.centers'[:, 1], result.centers'[:, 2],
        xlim=(0, 50), ylim=(0, 1),
        xlabel="d1", ylabel="c1", label="",
        color=:Gray, size=(800, 200))