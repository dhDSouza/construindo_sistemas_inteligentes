# Tópico 03 — Estruturas de Repetição com `while`

## Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender o funcionamento das estruturas de repetição;
- utilizar `while` para repetir instruções;
- trabalhar com contadores e acumuladores;
- identificar e evitar loops infinitos;
- utilizar `while True` e `break`;
- desenvolver programas interativos utilizando repetições e condicionais.

**Pré-requisito:** Tópico 02 — `input()` e estruturas condicionais.

---

# 1. O que são estruturas de repetição?

Imagine que precisamos mostrar uma mensagem cinco vezes.

Poderíamos escrever:

```python
print("Olá!")
print("Olá!")
print("Olá!")
print("Olá!")
print("Olá!")
```

Mas e se precisássemos mostrar essa mensagem 100 vezes?

Para evitar escrever o mesmo código repetidamente, utilizamos uma **estrutura de repetição**, também chamada de *loop*.

Em Python, temos duas estruturas principais:

- `while`: repete instruções enquanto uma condição for verdadeira;
- `for`: permite percorrer sequências de valores (será estudado no próximo tópico).

---

# 2. Estrutura de repetição `while`

A palavra `while` significa **enquanto**.

Ela permite executar um bloco de código enquanto determinada condição for verdadeira (`True`).

Sintaxe:

```python
while condicao:
    # Instruções repetidas
```

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

print("Fim!")
```

Saída:

```text
1
2
3
4
5
Fim!
```

**Como funciona?**

1. Criamos um contador com valor inicial `1`.
2. O `while` verifica se o contador é menor ou igual a `5`.
3. Se a condição for verdadeira, apresenta o número.
4. `contador += 1` aumenta o contador em uma unidade.
5. O processo se repete até que a condição seja falsa.

Observe:

| Repetição | Contador | Condição `<= 5` |
| --- | --- | --- |
| 1ª | 1 | `True` |
| 2ª | 2 | `True` |
| 3ª | 3 | `True` |
| 4ª | 4 | `True` |
| 5ª | 5 | `True` |
| Final | 6 | `False` |

Quando o contador chega a `6`, o `while` termina.

**Importante:** assim como no `if`, a indentação determina quais instruções pertencem ao `while`.

---

# 3. Contadores e acumuladores

Durante uma repetição, frequentemente precisamos contar acontecimentos ou somar valores.

## Contador

Um **contador** registra quantas vezes alguma coisa aconteceu.

Podemos aumentar ou diminuir seu valor:

```python
contador += 1  # Aumenta em 1
contador -= 1  # Diminui em 1
```

Também podemos aumentar de dois em dois, por exemplo, utilizando `contador += 2`.

## Acumulador

Um **acumulador** guarda um resultado que vai sendo atualizado a cada repetição.

Exemplo: solicitar três números e calcular sua soma.

```python
contador = 1
soma = 0

while contador <= 3:
    numero = int(input("Digite um número: "))

    soma += numero
    contador += 1

print("Soma total:", soma)
```

Se o usuário informar `10`, `20` e `30`:

| Repetição | Número | Soma |
| --- | --- | --- |
| 1ª | 10 | 10 |
| 2ª | 20 | 30 |
| 3ª | 30 | 60 |

Resultado: `Soma total: 60`

Observe que utilizamos duas variáveis com finalidades diferentes:

- `contador`: controla a quantidade de repetições.
- `soma`: acumula os números informados.

---

# 4. Loops infinitos

Um **loop infinito** acontece quando a condição de repetição nunca se torna falsa.

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Nesse exemplo, o contador nunca aumenta. Portanto, a condição `contador <= 5` será sempre verdadeira.

O programa continuará mostrando `1` indefinidamente.

Para evitar isso, precisamos garantir que a condição possa se tornar falsa.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

> **Dica:** para interromper uma execução que ficou presa em um loop infinito, normalmente utilizamos `Ctrl + C` no terminal.

---

# 5. Repetição com `while True` e `break`

Em algumas situações, queremos manter um programa funcionando até que o usuário decida encerrá-lo.

Para isso, podemos utilizar:

- `while True`: mantém a repetição ativa;
- `break`: interrompe a repetição imediatamente.

Exemplo:

```python
while True:
    resposta = input("Deseja continuar? (sim/nao): ")

    if resposta == "nao":
        break

    print("Continuando...")

print("Programa encerrado!")
```

**Como funciona?**

1. `while True` inicia uma repetição contínua.
2. O usuário informa uma resposta.
3. Se digitar `"nao"`, o `break` encerra a repetição.
4. Caso contrário, o programa continua executando.

O `break` interrompe apenas o laço de repetição em que está sendo executado, não necessariamente o programa inteiro.

---

# 6. Exemplo prático — Menu interativo

Vamos combinar os conteúdos anteriores para construir um menu que continua funcionando até que o usuário escolha sair.

```python
while True:
    print("\n=== MENU ===")
    print("1 - Dizer olá")
    print("2 - Calcular o dobro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Seja bem-vindo!")

    elif opcao == "2":
        numero = int(input("Digite um número: "))
        print("Dobro:", numero * 2)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
```

Observe que o menu será apresentado novamente após cada operação.

Isso acontece porque todas as instruções estão dentro do `while True`.

Somente a opção `0` encerra a repetição, por meio do `break`.

---

# 7. Exercícios

Crie um arquivo `.py` para cada exercício. Utilize apenas os conteúdos estudados até agora.

## Exercício 01 — Contagem progressiva

**Arquivo: `01_contagem.py`**

Solicite um número inteiro positivo e apresente todos os números de `1` até o valor informado.

Exemplo:

```text
Digite um número: 5

1
2
3
4
5
```

## Exercício 02 — Contagem regressiva

**Arquivo: `02_contagem_regressiva.py`**

Solicite um número inteiro positivo e faça uma contagem regressiva até zero.

Ao terminar, mostre `Lançamento realizado!`.

## Exercício 03 — Tabuada

**Arquivo: `03_tabuada.py`**

Solicite um número inteiro e apresente sua tabuada de multiplicação de 1 até 10 utilizando `while`.

## Exercício 04 — Somando números

**Arquivo: `04_somatorio.py`**

Solicite cinco números inteiros e apresente a soma de todos eles.

Utilize um contador para controlar as repetições e um acumulador para guardar a soma.

## Exercício 05 — Média da turma

**Arquivo: `05_media_turma.py`**

Solicite quantos alunos existem em uma turma.

Em seguida, leia a nota de cada aluno e calcule a média geral.

A quantidade de alunos deve ser maior que zero.

## Exercício 06 — Validando uma nota

**Arquivo: `06_validacao_nota.py`**

Solicite uma nota entre 0 e 10.

Enquanto o usuário informar um valor fora desse intervalo, apresente `Nota inválida` e solicite novamente.

Quando uma nota válida for informada, mostre `Nota registrada com sucesso!`.

## Exercício 07 — Menu de operações

**Arquivo: `07_menu.py`**

Crie um menu com as seguintes opções:

```text
=== MENU ===
1 - Somar dois números
2 - Verificar maioridade
0 - Sair
```

O menu deverá continuar aparecendo até o usuário escolher a opção `0`.

Utilize `while True`, condicionais e `break`.

---

# Desafio extra — Caixa eletrônico

**Arquivo: `08_caixa_eletronico.py`**

Desenvolva um caixa eletrônico simples com saldo inicial de R$ 500.00.

O programa deverá apresentar o seguinte menu:

```text
=== CAIXA ELETRÔNICO ===
1 - Consultar saldo
2 - Depositar dinheiro
3 - Sacar dinheiro
0 - Sair
```

**Regras:**

1. O menu deverá continuar funcionando até que o usuário escolha sair.
2. Depósitos e saques devem possuir valores maiores que zero.
3. Não será permitido sacar mais dinheiro do que existe na conta.
4. O saldo deverá ser atualizado após depósitos e saques válidos.
5. Opções inválidas devem apresentar uma mensagem de erro.

**Desafio adicional:** conte quantos depósitos e saques foram realizados durante a execução.

---

# Resumo do tópico

| Conceito | Finalidade |
| --- | --- |
| `while` | Repete instruções enquanto uma condição for verdadeira |
| Contador | Conta quantas vezes algo aconteceu |
| Acumulador | Guarda valores que são somados ou atualizados |
| `+=` | Incrementa uma variável |
| `-=` | Decrementa uma variável |
| `while True` | Cria uma repetição contínua |
| `break` | Interrompe uma repetição |

**Próximo tópico:** estrutura de repetição `for` e utilização de `range()`.
