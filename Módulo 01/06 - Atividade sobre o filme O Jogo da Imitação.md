# Atividade — O Jogo da Imitação: da investigação ao código

**Base:** filme *O Jogo da Imitação* e conteúdos de introdução ao Python, `input()` e estruturas condicionais.

**Organização:** duplas, com reflexão individual ao final.  
**Tempo sugerido:** duas aulas de 50 minutos, após a exibição do filme.  
**Entrega:** respostas em um arquivo de texto e dois arquivos `.py`.

## Objetivo

Relacionar situações do filme à organização de um problema em entrada, processamento e saída. Construir programas que recebam dados, verifiquem condições e apresentem decisões justificadas.

Use apenas os recursos estudados: variáveis, `print()`, `input()`, `int()`, `float()`, operações aritméticas, comparações, `if`, `elif`, `else`, `and`, `or` e `not`. Não é necessário usar laços, listas, funções próprias ou bibliotecas.

> Os programas desta atividade são simulações didáticas inspiradas no filme. As regras e os valores foram criados para a aula; eles não reproduzem a Enigma nem seu processo de decifração.

<div align="center">
  <img src="https://imgs.search.brave.com/kUWlJK46rXYA1pZwPdFBTmquoHR4Iwdff4HJNlRryJQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zbnBj/dWx0dXJhLm9yZy9p/bWFnZW5zL29fam9n/b19kYV9pbWl0YWNh/b18yMDE1MDExNV9w/Zi5qcGc">
  <p>Filme: O Jogo da Imitação</p>
</div>

## Parte 1 - Laboratório de programação

Criem uma pasta chamada `atividade_jogo_imitacao`. Em cada arquivo, incluam comentários explicando a leitura dos dados, as condições utilizadas e o motivo da ordem dos testes.

Considerem entradas numéricas no formato correto, com ponto para decimais. Validem as opções solicitadas em cada exercício. Não é necessário tratar palavras digitadas no lugar de números.

### Missão 1 — Cadastro de uma mensagem

**Arquivo:** `01_cadastro_mensagem.py`

Antes de investigar uma mensagem, a equipe precisa organizar os dados disponíveis.

Recebam pelo teclado:

- o nome ou apelido do analista;
- a identificação da mensagem, como texto, por exemplo `MSG-007`;
- a quantidade de grupos de símbolos, como inteiro;
- o tempo estimado para analisar cada grupo, em minutos, como decimal.

Regras:

1. A quantidade de grupos e o tempo por grupo devem ser maiores que zero.
2. Se qualquer um desses valores for inválido, mostrem `Dados inválidos` e não calculem o tempo total.
3. Se os dados forem válidos, calculem o tempo total estimado: quantidade de grupos multiplicada pelo tempo por grupo.
4. Apresentem uma ficha com o analista, a identificação, a quantidade de grupos e o tempo total em minutos.
5. Se o total for menor ou igual a 60 minutos, mostrem `Análise dentro do prazo`; caso contrário, mostrem `Reorganizar o trabalho`.

**Para explicar:** por que a identificação é texto mesmo quando contém algarismos? Por que é adequado usar `float()` para o tempo por grupo?

### Missão 2 — Central de prioridades

**Arquivo:** `02_central_prioridades.py`

A equipe dispõe de tempo limitado para analisar uma mensagem. As prioridades abaixo são regras fictícias para praticar decisões em Python.

Recebam pelo teclado:

- a identificação da mensagem;
- o tempo disponível, em minutos, como decimal;
- o tempo necessário, em minutos, como decimal;
- a resposta à pergunta `A mensagem indica risco imediato? (sim/nao):`;
- a resposta à pergunta `A mensagem contém uma pista recorrente? (sim/nao):`.

Regras de validação:

1. Os dois tempos devem ser maiores que zero. Usem `or` para detectar um tempo inválido e mostrem `Tempo inválido`.
2. As duas respostas devem ser exatamente `sim` ou `nao`. Se alguma não for, mostrem `Resposta inválida`.
3. Não classifiquem a mensagem quando houver dados inválidos. Se houver erro nos tempos e nas respostas ao mesmo tempo, a mensagem de tempo inválido tem prioridade.

Com dados válidos, escolham apenas um resultado, nesta ordem:

| Condição | Resultado |
| --- | --- |
| Tempo necessário maior que o disponível | `Solicitar apoio: tempo insuficiente` |
| Há tempo suficiente e existe risco imediato | `Prioridade máxima` |
| Há tempo suficiente, não existe risco imediato e existe pista recorrente | `Prioridade alta` |
| Há tempo suficiente e nenhuma das duas indicações está presente | `Prioridade normal` |

Mostrem a identificação da mensagem e o resultado. Quando houver tempo suficiente, calculem e mostrem também quantos minutos restarão depois da análise.

**Atenção ao limite:** se o tempo necessário for igual ao disponível, a análise cabe no prazo e o tempo restante será zero.

**Para explicar:** se há risco imediato, mas falta tempo, qual resultado aparece? Justifiquem com a ordem das condições e discutam por que um programa real precisaria de regras definidas por pessoas responsáveis por esse contexto.

## Parte 2 — Teste de mesa e execução

Antes de executar, preencham o resultado esperado para cada caso. Depois executem o programa, registrem a saída obtida e indiquem se ela corresponde à previsão. Se houver diferença, expliquem a correção feita.

### Casos obrigatórios da missão 1

Usem um nome e uma identificação de sua escolha.

| Grupos | Minutos por grupo | Resultado esperado | Saída obtida |
| --- | --- | --- | --- |
| 10 | 5.0 | | |
| 12 | 5.0 | | |
| 13 | 5.0 | | |
| 0 | 5.0 | | |
| 10 | -1.0 | | |

### Casos obrigatórios da missão 2

Usem uma identificação de sua escolha.

| Tempo disponível | Tempo necessário | Risco | Pista | Resultado esperado | Saída obtida |
| --- | --- | --- | --- | --- | --- |
| 60 | 60 | sim | sim | | |
| 60 | 61 | sim | sim | | |
| 60 | 30 | nao | sim | | |
| 60 | 30 | nao | nao | | |
| 60 | 30 | sim | nao | | |
| 0 | 30 | nao | nao | | |
| 60 | 30 | talvez | nao | | |
| -1 | 30 | talvez | nao | | |

Acrescentem pelo menos um caso criado pela dupla para cada missão e expliquem o que ele verifica.

## Parte 3 — Reflexão individual

Cada integrante deve escrever um parágrafo de 5 a 8 linhas respondendo:

> Como o filme e os programas desta atividade ajudam a compreender a relação entre regras, testes e decisões humanas? Cite uma condição do seu código e explique um limite da simulação.

