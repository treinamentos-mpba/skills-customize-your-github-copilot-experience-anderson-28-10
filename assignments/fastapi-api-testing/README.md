# 📘 Atividade: Testes Automatizados para APIs FastAPI

## 🎯 Objetivo

Pratique testes automatizados de APIs com `pytest` e o `TestClient` do FastAPI. Você irá verificar respostas, validação de dados e erros da API, mantendo os testes independentes entre si.

## 📝 Tarefas

### 🛠️ Preparar o ambiente de testes

#### Descrição
Instale as dependências, copie o código da API inicial para um módulo importável e prepare o arquivo onde os testes serão escritos.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx`.
- Copiar `starter-code.py` para `app.py` sem alterar as rotas fornecidas.
- Criar um arquivo chamado `test_api.py` que importe `app` e `books` de `app.py`.
- Criar uma fixture `client` usando `TestClient` para enviar requisições sem iniciar um servidor.

### 🛠️ Testar as rotas de consulta

#### Descrição
Escreva testes para consultar a coleção de livros, consultar um livro existente e solicitar um identificador inexistente.

#### Requisitos
O programa concluído deve:

- Verificar que `GET /books` retorna status `200` e a coleção esperada.
- Verificar que `GET /books/{book_id}` retorna status `200` e os dados do livro solicitado.
- Verificar que um identificador inexistente retorna status `404`.
- Usar asserções sobre status HTTP e conteúdo JSON, não apenas sobre o código de status.

### 🛠️ Testar operações de escrita

#### Descrição
Verifique a criação, a atualização e a remoção de livros e confirme que cada operação altera os dados conforme esperado.

#### Requisitos
O programa concluído deve:

- Testar `POST /books`, incluindo status `201`, identificador e dados do livro criado.
- Testar `PUT /books/{book_id}` e confirmar que os dados retornados foram atualizados.
- Testar `DELETE /books/{book_id}` e confirmar o status `204` e a remoção do livro.
- Fazer as verificações por meio das respostas da API e de consultas posteriores, quando aplicável.

### 🛠️ Testar erros e isolamento

#### Descrição
Cubra dados inválidos e operações sobre livros inexistentes. Garanta também que alterações feitas por um teste não afetem os demais.

#### Requisitos
O programa concluído deve:

- Verificar que campos obrigatórios ausentes em `POST /books` produzem status `422`.
- Verificar que atualizar ou remover um livro inexistente produz status `404`.
- Usar uma fixture que restaure a coleção de livros após cada teste.
- Usar `pytest.mark.parametrize` para testar mais de um payload inválido sem duplicar o teste.
- Executar a suíte com `python -m pytest -v` e obter aprovação em todos os testes.