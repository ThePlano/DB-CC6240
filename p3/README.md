# Guia de Execução do Projeto com Neo4j e Python

Este guia descreve como criar as tabelas no banco de dados **Neo4j**, inserir os dados e executar as consultas utilizando o **main.py** e **querrys.py**.

---

## Estrutura do Projeto

- **querryCreate.cypher**: Contém os comandos Cypher para criar os nós e relacionamentos no banco Neo4j.
- **main.py**: Responsável por inserir os dados no banco após as tabelas terem sido criadas.
- **querrys.py**: Contém as consultas que devem ser executadas após a inserção dos dados.

---

## Passo a Passo para Execução

### Passo 1: Acesse o Neo4j

1. **Configure as credenciais no código**:
   - Verifique as configurações de conexão no **main.py** e **querrys.py**, incluindo **URI**, **usuário** e **senha**.

---

### Passo 2: Criar as Estruturas no Banco de Dados

1. **Abra a interface web do Neo4j**.
2. **Execute os comandos do arquivo `querryCreate.cypher`**:
   - Cole o conteúdo do arquivo no terminal Cypher do Neo4j e execute.
   - Isso criará os nós e relacionamentos necessários para o projeto.

---

### Passo 3: Inserir os Dados

1. **Execute o arquivo `main.py`**:
   - O script insere os dados no banco de dados Neo4j utilizando as tabelas criadas no passo anterior.
   - Para executar:
     ```bash
     python main.py
     ```

---

### Passo 4: Executar as Consultas

1. **Abra o arquivo `querrys.py`**.
2. **Execute as consultas com parâmetros no Python**:
   - As funções em `querrys.py` permitem enviar parâmetros para personalizar as consultas.

---

## Alunos:

- **Lucas Sombra do Nascimento** - RA: 221221120
- **Nathalia Saori Shimokawa** - RA: 221220528
- **Rafael Augusto Assembleia** - RA: 221221039

1. **Criar tabelas com `querryCreate.cypher`.**
2. **Inserir dados com `main.py`.**
3. **Executar consultas com `querrys.py` e enviar os parâmetros necessários.**

---
