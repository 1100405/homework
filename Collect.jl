using CSV, DataFrames, PrettyTables

df = CSV.read("data_with_classes.csv", DataFrame)

df = groupby(df, :Class)

matclass1 = df[1]
matclass1 = select(matclass1, Not(:Class))
matclass1 = Matrix(matclass1)

matclass2 = df[2]
matclass2 = select(matclass2, Not(:Class))
matclass2 = Matrix(matclass2)

matclass3 = df[3]
matclass3 = select(matclass3, Not(:Class))
matclass3 = Matrix(matclass3)

pretty_table(matclass1)
println(size(matclass1))
pretty_table(matclass2)
println(size(matclass2))
pretty_table(matclass3)
println(size(matclass3))