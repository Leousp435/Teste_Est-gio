import tabula
from zipfile import ZipFile

file_name = "padrao-tiss_componente-organizacional_202111.pdf"

table_1 = tabula.read_pdf(file_name, pages=114, output_format = "dataframe")

table_2 = tabula.read_pdf(file_name, pages = [115, 116, 117, 118, 119, 120], output_format = "dataframe", multiple_tables = False)

df1 = table_1[0]
df2 = table_2[0]

df1.columns = df1.iloc[0]
df1 = df1.iloc[1:]
df1["Código"] = df1["Código Descrição da categoria"].str.split(' ', expand=True)[0]
df1["Descrição da categoria"] = df1["Código Descrição da categoria"].str.split(' ', 1,expand=True)[1]
df1 = df1.set_index("Código")
df1 = df1.drop("Código Descrição da categoria", axis=1)

df2.columns = df2.iloc[0]
df3 = df2.iloc[140:]
df2 = df2.iloc[1:139]
df2 = df2.set_index("Código")

df3 = df3.drop("Descrição da categoria", axis=1)
df3 = df3.dropna(axis=0)
df3 = df3.drop([140, 141], axis=0)
df3["Descrição da categoria"] = df3["Código"].str.split(' ', expand=True)[1]
df3["Código"] = df3["Código"].str.split(' ', expand=True)[0]
df3 = df3.set_index("Código")

df1.to_csv("csv_1.csv")
df2.to_csv("csv_2.csv")
df3.to_csv("csv_3.csv")

zip_file = ZipFile("Teste_{Leonardo_Gabriel_Fusineli_Silva}.zip", "w")
zip_file.write("csv_1.csv")
zip_file.write("csv_2.csv")
zip_file.write("csv_3.csv")

zip_file.close()
