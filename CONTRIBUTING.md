# Guia de contribuição

Obrigado por ajudar no desenvolvimento da API da Ótica Support! Este guia explica como trabalhar no repositório.

## Fluxo de trabalho

1. Crie uma branch a partir da `main`, com um nome que descreva a tarefa:
   - `feat/agendamento-de-consultas`
   - `fix/calculo-do-frete`
   - `docs/atualiza-readme`
2. Faça commits pequenos, cada um com uma única mudança lógica.
3. Abra um Pull Request para a `main` preenchendo o template.
4. Aguarde a revisão antes de fazer o merge.

## Padrão de commits

Usamos o formato **Conventional Commits**, com mensagens em português:

```
tipo: descrição curta no imperativo
```

| Tipo | Quando usar |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção de bug |
| `docs` | documentação |
| `chore` | configuração, dependências, tarefas de manutenção |
| `refactor` | melhoria de código sem mudar o comportamento |
| `test` | criação ou ajuste de testes |

Exemplos:

```
feat: adiciona endpoint de listagem de produtos
fix: corrige conflito de horários no agendamento
```

## Ambiente de desenvolvimento

1. Copie `.env.example` para `.env` e ajuste os valores.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências (instruções completas serão adicionadas ao README com o código inicial).

## Qualidade do código

- Siga o `.editorconfig` do repositório.
- Escreva testes para regras de negócio novas (agendamentos, estoque, pedidos).
- Nunca envie segredos, senhas ou chaves de API. Use sempre o `.env`.

## Dúvidas e problemas

Abra uma issue usando um dos templates disponíveis.
