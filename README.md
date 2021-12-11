# Teste de Estagio - Intuitive Care

Nome: Leonardo Gabriel Fusineli Silva

Repositório com os códigos dos testes de nivelamento relativos ao processo seletivo de estágio da empresa Intuitive Care.

# 1. Web Scraping:

## Objetivo
O objetivo era buscar a versão mais recente do Padrão TISS e baixar o componente organizacional.

## Como executar

Pelo terminal, vá para a pasta web_scrapping/:

```$ cd web_scraping/
```

Ative o ambiente virtual para o python:

```$ source bin/activate
```

Execute o programa:

```$ python web_scraping.py
```

Desative o ambiente virtual do python:

```$ deactivate```

## Saída
O arquivo pdf do Padrão TISS será baixado na pasta atual.


# 2. Transformação de Dados

## Objetivo
O objetivo era extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS), salvar os dados em tabelas estruturadas, em csvs e zipar todos os csvs num arquivo "Teste_{seu_nome}.zip".

## Como executar

Pelo terminal vá para a pasta data_transformation/:

```$ cd data_transformation/
```

Ative o ambiente virtual para o python:

```$ source bin/activate
```

Execute o programa :

```$ python data_transformation.py
```

Desative o ambiente virtual do python:

```$ deactivate```

## Saída
O arquivo zip será criado na pasta atual.

# 3. Banco de Dados MySQL

## Objetivo
O objetivo era criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação num banco MySQL ou Postgres e montar uma query analítica que traga a resposta para as seguintes perguntas:

"Quais as 10 operadoras que mais tiveram despesas com 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' no último trimestre?" e "Quais as 10 operadoras que mais tiveram despesas com 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' no último ano?"

## Como executar

Pelo terminal vá para a pasta banco_de_dados/:

```$ cd banco_de_dados/
```

Abra o arquivo database.py com um editor de texto e na linha 10 coloque a senha do banco de dados no campo senha, no lugar de "sql#123" (se o usuário do banco de dados não for o root, coloque também o usuario correto no campo usuario no lugar de "root") e salve as modificações.

Ative o ambiente virtual para o python:

```$ source bin/activate
```

Execute o programa :

```$ python database.py
```

Desative o ambiente virtual do python:

```$ deactivate```

## Saída
O programa imprimirá na tela as respostas das duas perguntas feitas.
