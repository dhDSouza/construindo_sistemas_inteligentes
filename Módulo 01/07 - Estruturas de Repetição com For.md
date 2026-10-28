# Tópico 04 — Estruturas de Repetição com `for`

## Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender como o `for` percorre uma sequência de valores;
- utilizar `range()` para controlar início, fim e passo de uma contagem;
- construir contagens progressivas e regressivas;
- combinar repetições, entradas e estruturas condicionais;
- utilizar contadores, acumuladores, `break` e `continue`;
- escolher entre `for` e `while` de acordo com o problema.

**Pré-requisito:** [Tópico 03 — Estruturas de Repetição com `while`](05%20-%20Estruturas%20de%20Repetição%20com%20While.md).

---

# 1. Do `while` para o `for`

Na aula anterior, usamos um contador para mostrar os números de 1 a 5:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Podemos realizar a mesma tarefa com `for`:

```python
for numero in range(1, 6):
    print(numero)
```

Saída dos dois programas:

```text
1
2
3
4
5
```

O `for` recebe cada valor produzido por `range()` e executa o bloco uma vez para cada valor. Não precisamos escrever o incremento da variável.

---

# 2. Como funciona o `for`?

A palavra `for` pode ser entendida como **para cada**. O `in` indica de onde vêm os valores percorridos.

Estrutura geral:

```python
for variavel in sequencia:
    # Instruções executadas para cada valor
```

Neste tópico, utilizaremos principalmente `range()`, que representa uma sequência de números inteiros.

```python
for numero in range(1, 4):
    print("Número atual:", numero)

print("Contagem encerrada.")
```

| Repetição | Valor de `numero` | Mensagem do bloco |
| --- | --- | --- |
| 1ª | `1` | `Número atual: 1` |
| 2ª | `2` | `Número atual: 2` |
| 3ª | `3` | `Número atual: 3` |

Depois que os valores terminam, o programa mostra `Contagem encerrada.` uma única vez.

**Importante:** o cabeçalho termina com dois-pontos e as instruções do bloco ficam indentadas com quatro espaços.

---

# 3. `range()` com um argumento

Na forma `range(fim)`, a contagem começa em `0`, avança de um em um e termina **antes** de `fim`.

```python
for numero in range(5):
    print(numero)
```

Saída:

```text
0
1
2
3
4
```

O bloco executou cinco vezes, mas o número `5` não apareceu.

Podemos usar essa forma quando queremos repetir uma ação uma quantidade definida de vezes:

```python
for repeticao in range(3):
    print("Bem-vindo à aula de Python!")
```

A variável `repeticao` recebe `0`, `1` e `2`, mesmo que não seja utilizada dentro do bloco.

---

# 4. `range()` com início e fim

Na forma `range(inicio, fim)`, escolhemos o primeiro valor. O limite final continua sendo excluído.

```python
for numero in range(1, 6):
    print(numero)
```

Esse exemplo mostra de `1` até `5`.

Para incluir um limite inteiro informado pelo usuário em uma contagem crescente de um em um, somamos `1` ao limite final:

```python
limite = int(input("Contar até qual número positivo? "))

if limite > 0:
    for numero in range(1, limite + 1):
        print(numero)
else:
    print("O limite deve ser maior que zero.")
```

Se a entrada for `3`, `range(1, limite + 1)` será `range(1, 4)`, percorrendo `1`, `2` e `3`.

---

# 5. `range()` com início, fim e passo

O terceiro argumento indica quanto a contagem avança a cada repetição:

```python
for numero in range(2, 11, 2):
    print(numero)
```

Saída:

```text
2
4
6
8
10
```

Aqui, começamos em `2` e avançamos de dois em dois, sem atingir o limite `11`.

| Expressão | Valores percorridos |
| --- | --- |
| `range(4)` | `0, 1, 2, 3` |
| `range(1, 5)` | `1, 2, 3, 4` |
| `range(2, 11, 2)` | `2, 4, 6, 8, 10` |
| `range(1, 10, 3)` | `1, 4, 7` |

Os argumentos de `range()` devem ser inteiros. Um passo igual a zero gera `ValueError`.

---

# 6. Contagem regressiva

Para diminuir os valores, utilizamos um passo negativo:

```python
for numero in range(5, -1, -1):
    print(numero)

print("Lançamento realizado!")
```

Saída:

```text
5
4
3
2
1
0
Lançamento realizado!
```

O limite final é `-1` para que o zero seja incluído. O valor `-1` não faz parte da contagem.

**A direção do passo precisa permitir chegar aos valores desejados.**

| Expressão | O que acontece? |
| --- | --- |
| `range(5, 0, -1)` | Percorre `5, 4, 3, 2, 1` |
| `range(5, 0)` | Não percorre nenhum valor: o passo padrão é positivo |
| `range(1, 5, -1)` | Não percorre nenhum valor: o passo aponta na direção contrária |
| `range(3, 3)` | Não percorre nenhum valor: início e fim são iguais |

Quando o intervalo é vazio, o bloco do `for` não executa nenhuma vez. Isso não gera erro.

---

# 7. Exemplo prático — Tabuada

```python
numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)
```

O número digitado permanece o mesmo. Quem muda a cada repetição é o `multiplicador`, que recebe os valores de `1` até `10`.

Por exemplo, para a entrada `3`, a primeira linha será `3 x 1 = 3` e a última será `3 x 10 = 30`.

---

# 8. Acumuladores e contadores no `for`

Vamos solicitar quatro notas válidas, calcular a média e contar quantas atingiram pelo menos `7`:

```python
soma = 0
notas_a_partir_de_sete = 0

for aluno in range(1, 5):
    print("Aluno:", aluno)
    nota = float(input("Digite uma nota de 0 a 10: "))

    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida. Digite uma nota de 0 a 10: "))

    soma += nota

    if nota >= 7:
        notas_a_partir_de_sete += 1

media = soma / 4

print("Média da turma:", media)
print("Quantidade de notas a partir de 7:", notas_a_partir_de_sete)
```

O `for` controla os quatro alunos. O `while` permite tentar novamente a nota do mesmo aluno enquanto ela estiver fora da faixa.

| Aluno | Nota válida | Soma acumulada | Notas a partir de 7 |
| --- | --- | --- | --- |
| 1 | `8` | `8` | `1` |
| 2 | `6` | `14` | `1` |
| 3 | `10` | `24` | `2` |
| 4 | `4` | `28` | `2` |

Ao final, a média será `7.0` e a quantidade será `2`.

**Os acumuladores e contadores devem ser inicializados antes do laço.** Se `soma = 0` estivesse dentro do `for`, o total seria reiniciado a cada aluno.

Considere entradas numéricas no formato correto; para notas decimais, utilize ponto. A validação de faixa não trata textos como `dez`.

---

# 9. Percorrendo um texto

O `for` também pode percorrer uma string, recebendo uma letra por vez:

```python
palavra = "ROBÔ"

for letra in palavra:
    print(letra)
```

Saída:

```text
R
O
B
Ô
```

Não precisamos de `range()` nesse caso: o próprio texto fornece os caracteres. Espaços também são percorridos. Se o texto estiver vazio, o bloco não executa.

---

# 10. Interrompendo com `break`

Assim como no `while`, `break` encerra o laço imediatamente:

```python
encontrado = False

for tentativa in range(1, 4):
    print("Tentativa:", tentativa)
    codigo = input("Digite o código de acesso: ")

    if codigo == "PYTHON":
        encontrado = True
        break

    print("Código incorreto.")

if encontrado:
    print("Acesso autorizado.")
else:
    print("Tentativas esgotadas.")
```

O usuário tem **no máximo três tentativas**. Se acertar na primeira, as outras duas não acontecem. A variável `encontrado` registra se houve acerto para escolher a mensagem final.

---

# 11. Pulando uma repetição com `continue`

O `continue` pula o restante do bloco da repetição atual e passa para o próximo valor:

```python
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)
```

Saída:

```text
1
2
4
5
```

Quando `numero` vale `3`, o `print()` é pulado. O laço continua com `4` e `5`.

| Comando | Efeito |
| --- | --- |
| `break` | Encerra o laço em que está sendo executado |
| `continue` | Pula o restante da repetição atual desse laço |

---

# 12. Quando usar `for` ou `while`?

| Situação | Escolha sugerida | Motivo |
| --- | --- | --- |
| Ler cinco preços | `for` | A quantidade de leituras está definida |
| Mostrar uma tabuada de 1 a 10 | `for` | Há um intervalo de valores a percorrer |
| Percorrer as letras de um nome | `for` | Queremos visitar cada caractere |
| Repetir um menu até a opção de saída | `while` | A duração depende das escolhas do usuário |
| Pedir uma nota até receber um valor válido | `while` | Não sabemos quantas tentativas serão necessárias |

As duas estruturas podem resolver vários dos mesmos problemas. Escolha a que deixa mais claro o controle da repetição.

---

# 13. Erros comuns

| Problema | O que conferir |
| --- | --- |
| A contagem não mostrou o último número desejado | O limite final de `range()` é excluído |
| A contagem começou em zero | Com um argumento, `range()` começa em `0` |
| A contagem regressiva não executou | Foi informado um passo negativo? |
| O programa apresentou erro no `range()` | Os argumentos são inteiros e o passo é diferente de zero? |
| A soma guardou apenas o último valor | O acumulador foi inicializado antes do laço? |
| A mensagem final apareceu várias vezes | Ela ficou dentro do bloco por causa da indentação? |

Alterar a variável do `for` dentro do bloco não altera os valores que `range()` fornecerá nas próximas repetições:

```python
for numero in range(1, 4):
    print(numero)
    numero += 10
```

Esse código ainda mostra `1`, `2` e `3`. A cada nova repetição, `numero` recebe o próximo valor do intervalo. Não é necessário incrementá-lo manualmente.

---

# Desafio rápido em sala

Sem executar, escreva a saída e o valor final de `total`:

```python
total = 0

for numero in range(2, 9, 2):
    total += numero
    print(numero, total)

print("Total:", total)
```

Depois, troque o limite `9` por `8`. Qual repetição deixa de acontecer? Confira sua previsão no terminal.

---

# Exercícios

Crie um arquivo `.py` para cada exercício. Utilize `for` como estrutura principal e apenas os conteúdos estudados até aqui. Não é necessário usar listas, funções próprias ou tratamento de exceções.

Considere entradas numéricas no formato correto. Quando houver validação de faixa, utilize condicionais ou `while`, conforme o enunciado.

## Exercício 01 — Contagem progressiva

**Arquivo: `01_contagem_for.py`**

Leia um número inteiro positivo e mostre os números de `1` até ele, incluindo o limite. Se a entrada for menor ou igual a zero, mostre uma mensagem de valor inválido.

Teste com `1`, `5` e `0`.

## Exercício 02 — Contagem regressiva

**Arquivo: `02_contagem_regressiva_for.py`**

Leia um inteiro maior ou igual a zero. Mostre a contagem desse número até zero e, ao final, `Lançamento realizado!`. Para uma entrada negativa, apresente uma mensagem de valor inválido e não realize o lançamento.

Teste com `3`, `0` e `-1`.

## Exercício 03 — Números pares

**Arquivo: `03_pares_for.py`**

Leia um inteiro positivo e mostre os números pares de `2` até o limite, incluindo-o quando ele for par. Utilize o passo de `range()`.

Se o limite for `1`, informe que não há pares no intervalo. Para valores menores ou iguais a zero, informe que o limite é inválido.

Teste com `1`, `2`, `9` e `10`.

## Exercício 04 — Tabuada

**Arquivo: `04_tabuada_for.py`**

Leia um inteiro e apresente sua tabuada de multiplicação de `1` até `10`, utilizando `for`. Cada linha deve mostrar os dois fatores e o resultado.

## Exercício 05 — Soma e contagem de positivos

**Arquivo: `05_soma_positivos_for.py`**

Leia seis números inteiros. Ao final, mostre a soma de todos os números e quantos deles são maiores que zero.

Use um acumulador para a soma e um contador para os positivos. O zero participa da soma, mas não deve ser contado como positivo.

Teste com números positivos, negativos e zero na mesma execução.

## Exercício 06 — Média da turma

**Arquivo: `06_media_turma_for.py`**

Leia a quantidade de alunos. Se ela for menor ou igual a zero, informe que a quantidade é inválida e não calcule a média.

Para uma quantidade válida, utilize `for` para ler a nota de cada aluno. Use `while` para solicitar novamente qualquer nota fora da faixa de `0` a `10`, sem avançar para o próximo aluno.

Mostre a média da turma e quantos alunos obtiveram nota a partir de `7`. Teste com apenas um aluno e com uma nota inválida seguida de uma válida.

## Exercício 07 — Contando uma letra

**Arquivo: `07_contando_letra.py`**

Leia uma palavra e, depois, uma única letra. Percorra a palavra diretamente com `for` e conte quantas vezes a letra aparece.

Considere que o usuário informará exatamente um caractere na segunda entrada. Diferencie maiúsculas e minúsculas: `a` e `A` são valores distintos.

Teste com `banana` e `a` (resultado `3`), com uma letra ausente e com uma palavra vazia.

## Exercício 08 — Tentativas limitadas

**Arquivo: `08_tentativas_for.py`**

Defina o código fictício `"ROBO123"`. Dê ao usuário no máximo três tentativas para acertá-lo.

Mostre o número da tentativa antes de cada leitura. Se acertar, encerre o laço com `break` e informe o sucesso. Se errar todas, informe que as tentativas acabaram.

Teste um acerto na primeira tentativa, um acerto na terceira e três erros.

---

# Desafio extra — Relatório de missões do robô

**Arquivo: `09_relatorio_missoes.py`**

Um robô pode realizar até cinco missões. Ele começa com `100` pontos de energia, e cada missão custa `25` pontos.

1. Utilize `for` para percorrer as missões de `1` até `5`.
2. Antes de pedir o resultado da missão, verifique se existe energia suficiente. Se não houver, mostre `Energia insuficiente` e encerre o laço com `break`.
3. Para cada missão que puder ser realizada, solicite uma pontuação inteira entre `0` e `100`. Utilize `while` para repetir a leitura enquanto a pontuação estiver fora da faixa.
4. Após receber uma pontuação válida, desconte a energia, acumule os pontos e conte a missão realizada.
5. Ao final, mostre a quantidade de missões realizadas, a pontuação total, a média de pontos por missão realizada e a energia restante. Só calcule a média se houver pelo menos uma missão realizada.

**Teste de mesa:** com pontuações `80`, `60`, `100` e `40`, o robô deve completar quatro missões, somar `280` pontos, obter média `70.0` e terminar com energia `0`. A quinta missão não deve solicitar pontuação.

**Desafio adicional:** altere a energia inicial para `20`. O programa deve encerrar sem realizar missões e sem tentar dividir por zero.

---

# Resumo do tópico

| Conceito | Finalidade |
| --- | --- |
| `for` | Executa um bloco para cada valor percorrido |
| `range(fim)` | Percorre inteiros de zero até antes de `fim` |
| `range(inicio, fim)` | Define o início e o limite final exclusivo |
| `range(inicio, fim, passo)` | Define também o avanço da contagem |
| Passo negativo | Permite construir contagens regressivas |
| Acumulador | Guarda um total atualizado durante o laço |
| Contador | Registra quantas vezes um evento aconteceu |
| `break` | Encerra o laço atual |
| `continue` | Passa para a próxima repetição do laço atual |

Antes de entregar, confira os limites de `range()`, a direção do passo, a inicialização dos acumuladores e a indentação. Execute os programas com os casos de teste indicados nos enunciados.
