# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, usando métodos HTTP, rotas, validação de dados e códigos de status para gerenciar uma coleção de livros.

## 📝 Tarefas

### 🛠️ Executar a API inicial

#### Descrição
Instale as dependências e execute o código inicial. Explore a documentação interativa do FastAPI para entender como a aplicação e suas rotas são apresentadas.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Iniciar a aplicação executando `python starter-code.py`.
- Responder a uma requisição `GET /` com uma mensagem sobre a API.
- Permitir que a documentação interativa seja acessada em `/docs`.

### 🛠️ Consultar livros

#### Descrição
Implemente as rotas para consultar todos os livros e buscar um livro pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Retornar a coleção de livros em `GET /books`.
- Retornar um livro específico em `GET /books/{book_id}`.
- Responder com o status HTTP `404` quando o identificador não corresponder a um livro existente.

### 🛠️ Cadastrar livros

#### Descrição
Implemente a criação de livros, recebendo título e autor no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Aceitar uma requisição `POST /books` com os campos `title` e `author`.
- Gerar um identificador para o novo livro e adicioná-lo à coleção em memória.
- Retornar o livro criado com o status HTTP `201`.
- Usar a validação de dados do FastAPI para rejeitar campos obrigatórios ausentes ou inválidos.

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações de atualização e remoção para que a API ofereça as operações básicas de CRUD.

#### Requisitos
O programa concluído deve:

- Atualizar título e autor com `PUT /books/{book_id}`.
- Remover um livro com `DELETE /books/{book_id}`.
- Responder com o status HTTP `404` ao tentar atualizar ou remover um livro inexistente.
- Demonstrar as operações e seus resultados pela documentação em `/docs`.