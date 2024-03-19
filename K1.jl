using CSV, DataFrames, PrettyTables, Clustering, Plots, StatsPlots

df = CSV.read("dye.csv", DataFrame)

df_group = groupby(df, :class)
array = []
for class in df_group
    append!(array, size(class)[1])
end
barPlot = bar(1:16, array, color=:White, xticks=(1:16, 1:16), label="", title="barplot for n class")

c1 = select(df, "c1")
c1 = Array(c1)
c2 = select(df, "c2")
c2 = Array(c2)
c3 = select(df, "c3")
c3 = Array(c3)
histogramPlot = histogram(c1, color=:White, label="", title="Histogram of dye c1")

boxPlot = boxplot([c1, c2, c3], color=:White, xticks=(1:3, 1:3), label="", title="boxplot for c1, c2 and c3")

c3Array = []
for class in df_group
    c3 = select(class, "c3")
    c3 = Array(c3)
    push!(c3Array, [c3])
end
c3BoxPlot = boxplot(c3Array, color=:White, xticks=(1:16, 1:16), label="", title="boxplot c3 for each class")

plot(barPlot, histogramPlot, boxPlot, c3BoxPlot, size=(1000, 600))