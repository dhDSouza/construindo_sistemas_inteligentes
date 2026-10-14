# Tópico 02 — `input()` e estruturas condicionais

## Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- receber informações pelo teclado com `input()`;
- converter entradas para `int` e `float`;
- comparar valores e interpretar resultados booleanos;
- tomar decisões com `if`, `else` e `elif`;
- combinar condições com `and`, `or` e `not`;
- testar caminhos diferentes de um programa.

**Pré-requisito:** [Tópico 01 — Introdução ao Python](./01%20-%20Introdução%20ao%20Python.md).

---

# 1. De valores fixos para programas interativos

Na aula anterior, os dados eram escritos diretamente no código:

```python
nome = "Ana"
idade = 18

print("Nome:", nome)
print("Idade:", idade)
```

Para mudar o nome, precisávamos editar o arquivo. Agora vamos permitir que a pessoa informe os dados durante a execução.

Um programa pode ser organizado em três etapas:

```text
Entrada → Processamento → Saída
```

Por exemplo: receber duas notas, calcular a média e mostrar o resultado.

---

# 2. Recebendo dados com `input()`

A função `input()` mostra uma mensagem, espera a pessoa digitar e devolve o texto informado quando ela pressiona **Enter**.

```python
nome = input("Qual é o seu nome? ")

print("Olá,", nome)
```

Exemplo de interação no terminal:

```text
Qual é o seu nome? Beatriz
Olá, Beatriz
```

O texto entre aspas é a pergunta. A resposta é guardada na variável `nome`.

```python
nome = input("Nome: ")
cidade = input("Cidade: ")

print("=== CADASTRO ===")
print("Nome:", nome)
print("Cidade:", cidade)
```

Cada chamada de `input()` aguarda uma nova entrada.

---

# 3. `input()` sempre devolve uma string

Mesmo que a pessoa digite números, o resultado de `input()` é do tipo `str`.

```python
idade = input("Digite sua idade: ")

print(idade)
print(type(idade))
```

Se a pessoa digitar `18`, teremos:

```text
18
<class 'str'>
```

O valor guardado é `"18"`, e não o inteiro `18`.

Isso muda o significado de algumas operações:

```python
numero1 = input("Primeiro número: ")
numero2 = input("Segundo número: ")

print(numero1 + numero2)
```

Se as entradas forem `10` e `5`, a saída será `105`. O operador `+` juntou dois textos. Essa operação é chamada de **concatenação**.

Para realizar a soma numérica, precisamos converter os dados.

---

# 4. Convertendo entradas para números

## Números inteiros com `int()`

```python
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)

print("No próximo aniversário você terá", idade + 1, "anos.")
```

Também podemos escrever a leitura e a conversão na mesma linha:

```python
idade = int(input("Digite sua idade: "))
```

A execução ocorre de dentro para fora:

```text
input() recebe "18" → int() converte para 18 → idade recebe 18
```

## Números decimais com `float()`

```python
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print("Total da compra:", total)
```

Digite `19.90`, com ponto, para informar um valor decimal.

| Informação | Leitura sugerida | Exemplo de entrada |
| --- | --- | --- |
| Nome | `input()` | `Marina` |
| Quantidade de livros | `int(input())` | `4` |
| Temperatura | `float(input())` | `23.5` |

> [!NOTE]
> `int("dez")`, `int("2.5")` e `float("2,5")` geram `ValueError`. Nesta aula, considere que a pessoa digitará números no formato solicitado. O tratamento de entradas não numéricas será estudado depois.

---

# 5. Por que um programa precisa tomar decisões?

Até aqui, as instruções eram executadas em sequência. Mas muitas situações dependem de uma condição:

- se houver estoque, permitir uma compra;
- se a energia acabar, encerrar uma missão;
- se a média atingir o mínimo, informar aprovação.

Uma **condição** é uma expressão que pode ser avaliada como verdadeira ou falsa.

```python
idade = 20

print(idade >= 18)
```

Saída:

```text
True
```

Vamos usar esse resultado para escolher quais instruções executar.

---

# 6. Operadores de comparação

| Operador | Significado | Exemplo | Resultado |
| --- | --- | --- | --- |
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 5` | `False` |
| `>` | Maior que | `8 > 3` | `True` |
| `<` | Menor que | `8 < 3` | `False` |
| `>=` | Maior ou igual a | `7 >= 7` | `True` |
| `<=` | Menor ou igual a | `4 <= 2` | `False` |

Compare:

```python
idade = 18          # Atribui um valor.
print(idade == 18)   # Compara o valor e mostra True.
```

**`=` atribui; `==` compara.**

Também podemos comparar textos:

```python
resposta = input("Deseja continuar? Digite sim ou nao: ")

print(resposta == "sim")
```

Essa comparação distingue maiúsculas de minúsculas: `"sim"` é diferente de `"Sim"`. Espaços digitados também fazem parte da entrada. Por enquanto, digite as opções exatamente como forem solicitadas.

---

# 7. Uma decisão simples com `if`

`if` significa **se**.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você atingiu a maioridade.")

print("Consulta encerrada.")
```

Se a condição for verdadeira, o bloco dentro do `if` será executado. Se for falsa, ele será pulado.

A última mensagem aparece nos dois casos, pois está fora do bloco.

| Entrada | Mensagens exibidas após a leitura |
| --- | --- |
| `18` | `Você atingiu a maioridade.` e `Consulta encerrada.` |
| `15` | Apenas `Consulta encerrada.` |

---

# 8. Dois-pontos e indentação

Em Python, a estrutura condicional termina sua primeira linha com `:`. As instruções pertencentes ao bloco ficam recuadas, normalmente com **quatro espaços**.

```python
energia = int(input("Energia do robô: "))

if energia < 20:
    print("Energia baixa.")
    print("Procure uma estação de recarga.")

print("Verificação concluída.")
```

As duas mensagens recuadas pertencem ao `if`. A última está fora dele.

> [!TIP]
> Mantenha o mesmo recuo dentro de cada bloco. O editor geralmente indenta a próxima linha automaticamente depois dos dois-pontos. Evite misturar tabulações e espaços.

---

# 9. Dois caminhos com `if` e `else`

`else` significa **senão**. Ele define o que acontece quando a condição do `if` é falsa.

```python
quantidade = int(input("Quantidade disponível em estoque: "))

if quantidade > 0:
    print("Produto disponível.")
else:
    print("Produto indisponível.")
```

Neste exemplo, considere uma quantidade não negativa. Apenas um dos dois blocos será executado.

```text
quantidade > 0?
    ├── Verdadeiro → Produto disponível.
    └── Falso      → Produto indisponível.
```

O `else` não recebe uma condição: ele cobre o caminho restante.

---

# 10. Mais de dois caminhos com `elif`

`elif` permite testar outra condição quando as anteriores forem falsas.

```python
media = float(input("Digite a média de 0 a 10: "))

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Em recuperação.")
else:
    print("Reprovado.")
```

Considere uma média válida entre 0 e 10. A regra deste exemplo é:

| Média | Situação |
| --- | --- |
| A partir de `7` | Aprovado |
| A partir de `5` e abaixo de `7` | Em recuperação |
| Abaixo de `5` | Reprovado |

Python testa de cima para baixo. Ao encontrar uma condição verdadeira, executa aquele bloco e pula os demais blocos da mesma cadeia.

Se a média for `8`, a condição `media >= 5` também seria verdadeira, mas ela nem será avaliada: o primeiro caminho já foi escolhido.

**A ordem das condições importa.** Se testássemos primeiro `media >= 5`, uma média `8` seria classificada como recuperação.

---

# 11. Vários `if` ou uma cadeia com `elif`?

Use `if` independentes quando mais de uma ação puder acontecer:

```python
temperatura = float(input("Temperatura: "))

if temperatura >= 30:
    print("Dia quente.")

if temperatura >= 35:
    print("Calor intenso.")
```

Para `36`, as duas mensagens aparecem. Cada `if` faz seu próprio teste.

Use uma cadeia `if` / `elif` / `else` quando quiser escolher apenas um caminho entre as alternativas:

```python
temperatura = float(input("Temperatura: "))

if temperatura >= 35:
    print("Calor intenso.")
elif temperatura >= 30:
    print("Dia quente.")
else:
    print("Temperatura abaixo de 30 graus.")
```

Para `36`, apenas `Calor intenso.` aparece.

---

# 12. Combinando condições com `and`

`and` significa **e**: as duas condições precisam ser verdadeiras.

Uma oficina aceita pessoas a partir de 14 anos, desde que exista vaga:

```python
idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.")
```

Ter a idade mínima não basta se as vagas acabaram.

---

# 13. Alternativas com `or`

`or` significa **ou**: basta que pelo menos uma condição seja verdadeira.

Neste exemplo, estudantes ou professores recebem um desconto:

```python
categoria = input("Categoria (estudante, professor ou visitante): ")

if categoria == "estudante" or categoria == "professor":
    print("Desconto disponível.")
else:
    print("Sem desconto.")
```

Cada lado do `or` precisa representar a comparação desejada. Escreva `categoria == "professor"` por completo.

| Condição A | Condição B | `A and B` | `A or B` |
| --- | --- | --- | --- |
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

Ao misturar `and` e `or`, use parênteses para explicitar o agrupamento desejado:

```python
idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")
```

---

# 14. Invertendo uma condição com `not`

`not` significa **não**. Ele transforma `True` em `False` e `False` em `True`.

```python
resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")
```

Neste exemplo, considere somente as respostas `sim` e `nao`. A comparação cria um valor booleano, que é guardado em `em_manutencao`.

> [!NOTE]
> Não use `bool(input())` para interpretar respostas como `sim` e `nao`. Todo texto não vazio, incluindo `"nao"` e `"False"`, é convertido para `True`. Compare a resposta com o texto esperado.

---

# 15. Condicionais dentro de condicionais

Podemos fazer uma segunda decisão dentro da primeira. Isso é chamado de **aninhamento**.

```python
quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado.")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero.")
```

O primeiro teste verifica se a quantidade é positiva. O segundo só acontece quando o primeiro é verdadeiro.

Observe o recuo: o `else` se alinha ao `if` ao qual pertence.

---

# 16. Exemplo completo — Central de missões

Um robô só pode iniciar uma missão se tiver pelo menos 50 pontos de energia e não estiver em manutenção.

```python
nome = input("Nome do robô: ")
energia = int(input("Energia atual (0 a 100): "))
resposta = input("Está em manutenção? (sim/nao): ")

print("=== CENTRAL DE MISSÕES ===")
print("Robô:", nome)

if energia < 0 or energia > 100:
    print("Energia inválida. Informe um valor entre 0 e 100.")
elif resposta != "sim" and resposta != "nao":
    print("Resposta inválida. Use sim ou nao.")
else:
    em_manutencao = resposta == "sim"

    if energia >= 50 and not em_manutencao:
        print("Missão autorizada.")
        energia = energia - 30
        print("Energia após a missão:", energia)
    elif em_manutencao:
        print("Missão bloqueada: robô em manutenção.")
    else:
        print("Missão bloqueada: energia insuficiente.")

print("Atendimento encerrado.")
```

O programa primeiro verifica se os valores estão dentro das opções permitidas. Só depois decide sobre a missão. Se houver manutenção e pouca energia ao mesmo tempo, a mensagem exibida será a de manutenção, pela ordem dos testes.

Essa validação verifica a faixa de energia **depois da conversão**. Digitar `cinquenta` ainda causará um erro no `int()`.

## Teste de mesa

Antes de executar, acompanhe as condições usando alguns valores:

| Energia | Manutenção | Resultado esperado |
| --- | --- | --- |
| `80` | `nao` | Missão autorizada; energia final `50` |
| `50` | `nao` | Missão autorizada; energia final `20` |
| `49` | `nao` | Energia insuficiente |
| `80` | `sim` | Robô em manutenção |
| `20` | `sim` | Robô em manutenção |
| `101` | `nao` | Energia inválida |
| `80` | `talvez` | Resposta inválida |

Testar exatamente o limite (`50`), um valor abaixo (`49`) e um acima (`51`) ajuda a perceber diferenças entre `>` e `>=`.

---

# 17. Erros comuns

| Problema | O que conferir |
| --- | --- |
| A soma de `10` e `5` mostrou `105` | As entradas foram convertidas para números? |
| Erro ao comparar idade com `18` | A idade ainda é uma string? |
| Erro na linha do `if` | Faltam os dois-pontos? Foi usado `=` no lugar de `==`? |
| Erro de indentação | As instruções do bloco estão recuadas corretamente? |
| Uma mensagem aparece sempre | Ela ficou fora do bloco por causa do recuo? |
| Uma nota alta caiu em recuperação | As condições foram organizadas na ordem correta? |
| `Sim` não foi reconhecido | O programa espera exatamente `sim`? |

Ao investigar um resultado inesperado, mostre temporariamente o valor e seu tipo:

```python
entrada = input("Digite um valor: ")
print("Valor recebido:", entrada)
print("Tipo:", type(entrada))
```

---

# Desafio rápido em sala

Sem executar, diga quais mensagens serão exibidas para uma entrada igual a `7`:

```python
nota = float(input("Nota: "))

if nota >= 5:
    print("Primeira condição atendida.")

if nota >= 7:
    print("Segunda condição atendida.")
else:
    print("Segunda condição não atendida.")

print("Fim.")
```

Depois, troque o segundo `if` por `elif`. O que muda? Explique a diferença antes de conferir no terminal.

---

# Exercícios

Crie um arquivo `.py` para cada exercício. Leia os dados com `input()` e faça as conversões necessárias. Utilize apenas os recursos estudados até aqui; não é necessário usar laços, funções próprias ou tratamento de exceções.

Considere entradas numéricas no formato correto. Quando o enunciado pedir validação, verifique a faixa ou as opções com condicionais. Execute cada programa mais de uma vez para testar caminhos diferentes.

## Exercício 01 — Apresentação interativa

**Arquivo: `01_apresentacao_interativa.py`**

Peça o nome, a cidade e a idade da pessoa. Mostre uma ficha e calcule quantos anos ela terá no próximo aniversário.

## Exercício 02 — Conta da lanchonete

**Arquivo: `02_conta_lanchonete.py`**

Leia o preço de um lanche e a quantidade comprada. Calcule o total. Considere preço e quantidade positivos. Se o total for a partir de R$ 50.00, aplique 10% de desconto; caso contrário, mantenha o valor original.

Mostre o total antes do desconto, o desconto e o valor final. Para calcular 10%, multiplique o total por `0.10`. Teste totais abaixo de 50, iguais a 50 e acima de 50.

## Exercício 03 — Comparando números

**Arquivo: `03_comparando_numeros.py`**

Leia dois números inteiros. Informe se o primeiro é maior, se o segundo é maior ou se os dois são iguais. Use uma cadeia `if` / `elif` / `else`.

## Exercício 04 — Termômetro da sala

**Arquivo: `04_termometro.py`**

Leia uma temperatura e mostre apenas uma classificação:

- abaixo de 18: `Ambiente frio`;
- a partir de 18 e abaixo de 26: `Ambiente agradável`;
- a partir de 26: `Ambiente quente`.

Teste especialmente os valores `18` e `26`.

## Exercício 05 — Boletim com decisão

**Arquivo: `05_boletim_condicional.py`**

Leia duas notas de mesmo peso. Se alguma nota estiver fora da faixa de 0 a 10, mostre `Nota inválida` e não calcule a média. Caso ambas sejam válidas, calcule e mostre a média e a situação:

- média a partir de 7: aprovado;
- média a partir de 5 e abaixo de 7: recuperação;
- média abaixo de 5: reprovado.

## Exercício 06 — Acesso à oficina

**Arquivo: `06_acesso_oficina.py`**

Leia a idade e pergunte se a pessoa possui inscrição (`sim/nao`). Considere idade não negativa e uma das duas respostas indicadas. A entrada só será permitida para quem tiver pelo menos 14 anos **e** inscrição confirmada.

Use `and`. Teste uma pessoa que atende aos dois critérios, outra que atende a apenas um e outra que não atende a nenhum.

## Exercício 07 — Benefício no museu

**Arquivo: `07_beneficio_museu.py`**

Leia uma idade não negativa. Neste museu fictício, pessoas com menos de 12 anos **ou** a partir de 60 anos têm entrada gratuita. As demais pagam R$ 20.00.

Use `or` e teste as idades `11`, `12`, `59` e `60`.

## Exercício 08 — Pedido de livros

**Arquivo: `08_pedido_livros.py`**

A biblioteca tem 8 exemplares disponíveis. Leia a quantidade que a pessoa deseja retirar.

- Se a quantidade for menor ou igual a zero, informe que o pedido é inválido.
- Se for maior que o estoque, informe que não há exemplares suficientes.
- Caso contrário, confirme o pedido, atualize o estoque e mostre a quantidade restante.

O estoque só deve diminuir quando o pedido for confirmado.

## Exercício 09 — Calculadora com menu

**Arquivo: `09_calculadora_menu.py`**

Leia dois números decimais. Mostre um menu com as opções `1` para somar, `2` para subtrair, `3` para multiplicar e `4` para dividir. Leia a opção como texto.

Execute somente a operação escolhida. Se a opção não existir, mostre `Opção inválida`. Na divisão, verifique se o segundo número é zero antes de calcular; nesse caso, mostre `Não é possível dividir por zero`.

## Exercício 10 — Corrigindo decisões

**Arquivo: `10_corrigindo_decisoes.py`**

O programa deveria permitir a participação de pessoas a partir de 16 anos que tenham autorização, mas contém erros:

```text
idade = input("Idade: ")
autorizacao = input("Possui autorização? (sim/nao): ")

if idade >= 16 and autorizacao = "sim"
print("Participação permitida.")
else:
    print("Participação não permitida.")
```

Reescreva o código corrigindo a conversão da idade, o operador de comparação, os dois-pontos e a indentação. Explique cada correção em um comentário. Considere uma idade não negativa e as respostas `sim` ou `nao`.

---

# Desafio extra — Loja do aventureiro

**Arquivo: `11_loja_aventureiro.py`**

Crie uma loja com atendimento de uma única compra por execução.

1. Leia o nome do aventureiro e sua quantidade de ouro, como número inteiro.
2. Se o ouro for negativo, mostre `Quantidade de ouro inválida` e não prossiga com a compra.
3. Caso contrário, mostre um menu: `1` para poção de vida (25 moedas), `2` para escudo (60 moedas) e `3` para espada (100 moedas).
4. Leia a opção como texto e verifique se ela existe.
5. Para uma opção válida, verifique se o ouro é suficiente. Se for, desconte o preço e mostre o item adquirido e o saldo restante. Caso contrário, informe quantas moedas faltam.
6. Se a opção não existir, mostre `Item inválido`.

O ouro só pode ser descontado quando a compra for confirmada. Teste uma compra com sobra de ouro, uma com o valor exato, outra com saldo insuficiente, uma opção inválida e um saldo inicial negativo.

---

# Conferência antes de entregar

- As entradas numéricas foram convertidas para os tipos adequados?
- Os blocos estão indentados e as condições terminam com `:`?
- Foi usado `==` para comparar e `=` para atribuir?
- Os limites das regras foram respeitados, incluindo os casos de igualdade?
- Cada programa foi executado com entradas que percorrem caminhos diferentes?
- Estoques e saldos só são alterados quando a operação é permitida?
- As mensagens deixam claro o resultado de cada decisão?
