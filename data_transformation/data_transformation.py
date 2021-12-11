#Importamos as bibliotecas necessárias.
import tabula
from zipfile import ZipFile

file_name = "padrao-tiss_componente-organizacional_202111.pdf"


print("Lendo tabelas do arquivo", file_name)
#Lemos as tabelas do pdf e as colocamos em duas variáveis.
table_1 = tabula.read_pdf(file_name, pages=114, output_format = "dataframe")
table_2 = tabula.read_pdf(file_name, pages = [115, 116, 117, 118, 119, 120], output_format = "dataframe", multiple_tables = False)

#Transformamos essas listas de dataframes para somente dataframes
df1 = table_1[0]
df2 = table_2[0]

#Formatamos a primeira tabela para que ela fique igual à tabela do pdf.
df1.columns = df1.iloc[0]
df1 = df1.iloc[1:]
df1["Código"] = df1["Código Descrição da categoria"].str.split(' ', expand=True)[0]
df1["Descrição da categoria"] = df1["Código Descrição da categoria"].str.split(' ', 1,expand=True)[1]
df1 = df1.set_index("Código")
df1 = df1.drop("Código Descrição da categoria", axis=1)

#Setamos os nomes das colunas do segundo dataframe.
df2.columns = df2.iloc[0]

#Separamos o segundo dataframe em duas tabelas (Quadro 31 e 32). 
df3 = df2.iloc[140:]
df2 = df2.iloc[1:139]

#Setamos os index das linhas como a coluna "Código".
df2 = df2.set_index("Código")

#Formatamos a terceira tabela para que ela fique igual à do pdf.
df3 = df3.drop("Descrição da categoria", axis=1)
df3 = df3.dropna(axis=0)
df3 = df3.drop([140, 141], axis=0)
df3["Descrição da categoria"] = df3["Código"].str.split(' ', expand=True)[1]
df3["Código"] = df3["Código"].str.split(' ', expand=True)[0]
df3 = df3.set_index("Código")

print("Criando os arquivos csvs com as tabelas.")
#Escrevemos os dataframes para 3 arquivos csv.
df1.to_csv("csv_1.csv")
df2.to_csv("csv_2.csv")
df3.to_csv("csv_3.csv")

print("Criando arquivo zip")
#Criamos um arquivo zip e escrevemos os arquivos csv nele.
zip_file = ZipFile("Teste_{Leonardo_Gabriel_Fusineli_Silva}.zip", "w")
zip_file.write("csv_1.csv")
zip_file.write("csv_2.csv")
zip_file.write("csv_3.csv")

#Fechamos o arquivo zip.
zip_file.close()
print("Arquivo zip criado")
