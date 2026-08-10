# Painel de Controle de Tarefas — Flask

Projeto da atividade "Praticando" — Painel de Controle de Tarefas com Flask,
SQLite, autenticação, CRUD completo, API externa, filtro dinâmico, gráfico
de progresso e rotas REST (Desafio Avançado).

## Como rodar

```bash
# 1) Crie e ative um ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

# 2) Instale as dependências
pip install -r requirements.txt

# 3) Rode a aplicação
python app.py
```

Acesse http://127.0.0.1:5000 no navegador. O banco `painel.db` é criado
automaticamente na primeira execução.

Em produção, defina variáveis de ambiente em vez de usar os valores padrão:

```bash
export SECRET_KEY="uma-chave-bem-secreta-e-aleatoria"
export FLASK_DEBUG=False
```

## Estrutura

```
painel_tarefas/
├── app.py                  -> rotas, API JSON e lógica principal
├── database.py              -> conexão e criação das tabelas SQLite
├── requirements.txt
├── templates/
│   ├── base.html             -> layout, menu, Bootstrap, modo escuro
│   ├── login.html
│   ├── registro.html
│   ├── dashboard.html        -> filtro, cards por status e gráfico
│   ├── nova_tarefa.html
│   └── editar_tarefa.html
└── static/
    ├── css/style.css
    └── js/dashboard.js       -> fetch(), filtro, gráfico Chart.js
```

## Mapeamento completo dos objetivos do exercício

| # | Objetivo | Onde está implementado |
|---|----------|------|
| 1 | Rotas e templates | `app.py` (rotas) + `templates/base.html` (menu e área de conteúdo) |
| 2 | Banco SQLite | `database.py` — tabelas `usuarios (id, nome, email, senha)` e `tarefas (id, titulo, descricao, status, usuario_id)` |
| 3 | Autenticação | `/registro`, `/login`, `/logout`; hash com `werkzeug.security`; rotas protegidas com `session` via decorator `login_requerido` |
| 4/5 | CRUD de tarefas (rotas) | `/dashboard`, `/nova_tarefa`, `/editar/<id>`, `/excluir/<id>` |
| 6 | Interface e estilo | Bootstrap 5 + Bootstrap Icons em todos os templates; cards responsivos de tarefas |
| 7 | Segurança e boas práticas | `SECRET_KEY` via variável de ambiente; `FLASK_DEBUG` controla o modo debug; senha sempre em hash; validação de `título` e `status` no back-end |
| 8 | Filtro de tarefas por status | Dropdown no dashboard + rota `GET /api/tarefas?status=...` que retorna JSON; `static/js/dashboard.js` atualiza a lista via `fetch()` sem recarregar a página. Cards mudam de cor: Pendente=amarelo, Em andamento=azul, Concluída=verde |
| 9 | Modo escuro e personalização | Botão no menu (`base.html`), usa `data-bs-theme` do Bootstrap e salva a preferência em `localStorage` |
| 10 | Dashboard de progresso | Rota `GET /api/progresso` retorna a contagem por status em JSON; `dashboard.html` + `dashboard.js` montam um gráfico de pizza com **Chart.js** |
| Desafio Avançado | Versão REST completa | `GET/POST /api/tarefas`, `PUT/DELETE /api/tarefas/<id>` retornam e recebem JSON; consumidas via `fetch()` no `dashboard.js` para criar/editar status/excluir sem recarregar a página |

## Próximos passos sugeridos

- Adicionar paginação na lista de tarefas.
- Criar testes automatizados com `pytest` e `pytest-flask`.
- Mover a criação/edição completas (não só o "Concluir") também para modais AJAX.
