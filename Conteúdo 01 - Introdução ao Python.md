# Aula 01 — Introdução ao Python, `print()` e Variáveis

## Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

- compreender o que é uma linguagem de programação;
- entender o papel do Python;
- instalar e executar o Python;
- criar seu primeiro programa;
- utilizar a função `print()`;
- criar e modificar variáveis;
- reconhecer tipos básicos de dados;
- realizar operações simples utilizando variáveis.

---

# 1. Antes do Python: o que é programar?

Programar significa **criar instruções que um computador consegue executar**.

Imagine um computador como um funcionário extremamente obediente, rápido e completamente sem iniciativa.

Se você disser:

> Faça um café.

Para uma pessoa isso pode ser suficiente.

Para um computador, teríamos que detalhar algo semelhante a:

```text
Pegue uma xícara
Coloque café
Adicione água
Misture
Entregue a xícara
```

Um programa funciona da mesma maneira: é uma sequência de instruções.

Durante este curso aprenderemos inicialmente a construir essas instruções utilizando **Python**.

---

# 2. O que é Python?

Python é uma **linguagem de programação de propósito geral**.

Isso significa que ela não foi criada exclusivamente para uma única tarefa.

Com Python podemos desenvolver, por exemplo:

- automações;
- APIs e sistemas web;
- aplicações;
- análise de dados;
- inteligência artificial;
- machine learning;
- scripts;
- bots;
- jogos;
- aplicações científicas.

Uma característica importante é sua sintaxe relativamente simples.

Por exemplo, para mostrar uma mensagem na tela:

```python
print("Olá, mundo!")
```

Em Python não precisamos escrever uma grande quantidade de código para realizar operações simples.

A própria documentação oficial descreve Python como uma linguagem poderosa, com estruturas de dados de alto nível, sintaxe elegante, tipagem dinâmica e natureza interpretada. [Python documentation](https://docs.python.org/pt-br/3.14/tutorial/?utm_source=chatgpt.com)

---

# 3. De onde surgiu o Python?

Python começou a ser desenvolvido no início dos anos **1990**, por **Guido van Rossum**, no CWI, na Holanda. A linguagem recebeu influência de outra linguagem chamada **ABC**. [Python documentation](https://docs.python.org/pt-br/3/license.html?utm_source=chatgpt.com)

E não: o nome não surgiu por causa da cobra. 🐍

Guido estava lendo roteiros do programa humorístico britânico **Monty Python's Flying Circus** e decidiu utilizar o nome Python por ser curto e diferente. [Python documentation](https://docs.python.org/pt-br/2/faq/general.html?utm_source=chatgpt.com)

Então:

```text
Python 🐍 → não foi originalmente inspirado na cobra
Python 🎭 → veio de Monty Python
```

A cobra acabou virando a associação popular posteriormente.

---

# 4. Python é compilado ou interpretado?

Para uma primeira aula, podemos simplificar dizendo que Python é uma linguagem **interpretada**.

Nosso código:

```python
print("Olá!")
```

é executado por um programa chamado **interpretador Python**.

Podemos visualizar assim:

```text
Código Python
     ↓
Interpretador Python
     ↓
Computador
     ↓
Resultado
```

Por isso precisamos instalar Python na máquina antes de executar nossos arquivos.

---

# 5. Instalando Python

O local recomendado é o site oficial:

[Download oficial do Python](https://www.python.org/downloads/?utm_source=chatgpt.com)

Atualmente, no Windows, a própria documentação recomenda o uso do **Python Install Manager**, que pode ser instalado pelo site oficial ou pela Microsoft Store. [Python documentation](https://docs.python.org/pt-br/3.14/using/windows.html?utm_source=chatgpt.com)

## Windows

Depois da instalação, abra:

```text
Prompt de Comando
```

ou:

```text
PowerShell
```

e execute:

```bash
python --version
```

Também pode funcionar:

```bash
py --version
```

Se aparecer algo semelhante a:

```text
Python 3.14.7
```

está funcionando.

A documentação atual também permite iniciar o interpretador com comandos como `python` ou `py`. [Python documentation](https://docs.python.org/pt-br/3.14/tutorial/interpreter.html?utm_source=chatgpt.com)

---

# 6. IDE e editor de código

Apesar de Python poder ser utilizado diretamente pelo terminal, durante o curso podemos utilizar um editor como o **Visual Studio Code**.

Uma estrutura comum seria:

```text
VS Code
   ↓
Arquivo .py
   ↓
Interpretador Python
   ↓
Execução
```

Crie uma pasta:

```text
logica-python
```

Depois crie o arquivo:

```text
aula01.py
```

> [!TIP]
> Arquivos Python normalmente possuem a extensão `.py`.

Exemplos:

```text
calculadora.py
cadastro.py
atividade01.py
jogo.py
```

---

# 7. Nosso primeiro programa

Dentro de `aula01.py`:

```python
print("Olá, mundo!")
```

Execute o arquivo.

O resultado será:

```text
Olá, mundo!
```

Pronto.

Tecnicamente, você acabou de escrever um programa.

O famoso:

```python
print("Hello, World!")
```

é tradicionalmente utilizado como primeiro programa ao aprender uma linguagem.

---

# 8. A função `print()`

A função:

```python
print()
```

serve para mostrar informações na tela.

Por exemplo:

```python
print("Curso de Python")
```

Resultado:

```text
Curso de Python
```

Podemos executar vários `print()`:

```python
print("Python")
print("Lógica de Programação")
print("Estrutura de Dados")
```

Resultado:

```text
Python
Lógica de Programação
Estrutura de Dados
```

Cada `print()` adiciona uma quebra de linha por padrão.

---

# 9. Texto precisa estar entre aspas

Se queremos representar texto, utilizamos aspas.

Por exemplo:

```python
print("Daniel")
```

ou:

```python
print('Daniel')
```

Os dois funcionam.

Mas isto:

```python
print(Daniel)
```

não representa um texto.

Python irá interpretar `Daniel` como o nome de alguma coisa que deveria existir no programa.

---

# 10. Podemos imprimir números

Números não precisam de aspas.

```python
print(10)
print(25)
print(100)
```

Também podemos fazer operações:

```python
print(10 + 5)
```

Resultado:

```text
15
```

Observe a diferença:

```python
print(10 + 5)
```

Resultado:

```text
15
```

Enquanto:

```python
print("10 + 5")
```

Resultado:

```text
10 + 5
```

Por quê?

Porque:

```python
10 + 5
```

é uma expressão matemática.

Enquanto:

```python
"10 + 5"
```

é apenas texto.

---

# 11. Variáveis

Variável é um dos conceitos mais importantes da programação.

Uma variável permite **guardar um valor para utilizar posteriormente**.

Podemos imaginar uma variável como uma caixa.

```text
┌──────────────┐
│ idade        │
│              │
│     30       │
└──────────────┘
```

Em Python:

```python
idade = 30
```

Agora existe uma variável chamada:

```text
idade
```

contendo o valor:

```text
30
```

---

# 12. Criando variáveis

Exemplo:

```python
nome = "Arthur"
idade = 18
```

Temos:

```text
nome  → "Arthur"
idade → 18
```

Podemos mostrar essas informações:

```python
print(nome)
print(idade)
```

Resultado:

```text
Arthur
18
```

---

# 13. O sinal `=` não significa igualdade

Essa é uma observação importante para quem está começando.

Em matemática:

```text
x = 10
```

normalmente significa:

> x é igual a 10.

Em programação podemos pensar:

> coloque o valor `10` dentro da variável `x`.

Então:

```python
x = 10
```

é uma **atribuição**.

Podemos visualizar:

```text
10
 ↓
x
```

---

# 14. Uma variável pode mudar

É justamente por isso que ela se chama **variável**.

```python
pontuacao = 10

print(pontuacao)

pontuacao = 20

print(pontuacao)
```

Resultado:

```text
10
20
```

O valor anterior foi substituído.

Podemos pensar como um inventário de jogo:

```text
vida = 100
```

Depois de levar dano:

```python
vida = 75
```

A variável continua sendo `vida`, mas seu valor mudou.

---

# 15. Usando variáveis dentro do `print()`

Podemos imprimir vários valores:

```python
nome = "Ana"
idade = 17

print("Nome:", nome)
print("Idade:", idade)
```

Resultado:

```text
Nome: Ana
Idade: 17
```

Podemos colocar vários elementos:

```python
nome = "Ana"
idade = 17
curso = "Programação"

print(nome, idade, curso)
```

Resultado:

```text
Ana 17 Programação
```

---

# 16. Tipos de dados

Variáveis podem armazenar diferentes tipos de informação.

Inicialmente trabalharemos principalmente com quatro.

## Texto — `str`

```python
nome = "Gandalf"
```

`str` vem de **string**.

Representa texto.

---

## Número inteiro — `int`

```python
nivel = 10
```

Exemplos:

```python
idade = 18
quantidade = 50
vidas = 3
```

---

## Número decimal — `float`

```python
altura = 1.75
```

Exemplos:

```python
preco = 29.90
temperatura = 24.5
nota = 8.7
```

> [!NOTE]
> Em Python utilizamos `.` e não `,` para representar casas decimais.

Correto:

```python
preco = 19.90
```

---

## Booleano — `bool`

Representa verdadeiro ou falso.

```python
jogo_ativo = True
```

ou:

```python
jogo_ativo = False
```

Existem apenas dois valores booleanos:

```python
True
False
```

Eles serão extremamente importantes quando estudarmos estruturas como `if`.

---

# 17. Descobrindo o tipo de uma variável

Python possui a função:

```python
type()
```

Exemplo:

```python
nome = "Legolas"
idade = 2931
altura = 1.80
vivo = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(vivo))
```

Teremos algo semelhante a:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Neste momento basta compreender:

```text
str   → texto
int   → inteiro
float → decimal
bool  → verdadeiro/falso
```

---

# 18. Operações com variáveis

Variáveis numéricas podem participar de cálculos.

```python
numero1 = 10
numero2 = 5

resultado = numero1 + numero2

print(resultado)
```

Resultado:

```text
15
```

Observe:

```python
resultado = numero1 + numero2
```

Primeiro Python calcula:

```text
10 + 5
```

Depois armazena:

```text
15
```

na variável:

```text
resultado
```

---

# 19. Operadores matemáticos básicos

Vamos utilizar inicialmente:

```text
+    soma
-    subtração
*    multiplicação
/    divisão
```

Exemplo:

```python
a = 20
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Resultado:

```text
24
16
80
5.0
```

Observe que a divisão normalmente produz um `float`.

---

# 20. Atualizando uma variável utilizando ela mesma

Considere:

```python
moedas = 10
```

O jogador encontrou mais 5 moedas.

Podemos fazer:

```python
moedas = moedas + 5
```

Vamos interpretar:

```text
valor atual de moedas
       ↓
      10
       +
       5
       ↓
      15
       ↓
guardar novamente em moedas
```

Resultado:

```python
moedas = 15
```

Código:

```python
moedas = 10

moedas = moedas + 5

print(moedas)
```

Resultado:

```text
15
```

Esse padrão aparecerá muitas vezes daqui para frente.

---

# 21. Nomes de variáveis

Utilize nomes que expliquem o que a variável representa.

Evite:

```python
x = 150
y = 3
z = x * y
```

Prefira:

```python
preco = 150
quantidade = 3
total = preco * quantidade
```

O computador entende os dois.

Quem agradece pelo segundo código é o ser humano que precisar lê-lo depois. 😅

---

# 22. Algumas regras

Podemos utilizar:

```python
nome
idade
nome_aluno
nota_final
quantidade_produtos
```

Não podemos iniciar o nome com número:

```python
2nota = 10
```

Isso é inválido.

Prefira:

```python
nota2 = 10
```

Também não utilizamos espaços:

```python
nome aluno = "Carlos"
```

Errado.

Use:

```python
nome_aluno = "Carlos"
```

Essa forma é chamada de **snake_case**.

Coincidentemente bastante apropriada para Python. 🐍

---

# 23. Python diferencia maiúsculas de minúsculas

Observe:

```python
nome = "Ana"
Nome = "Carlos"
```

São duas variáveis diferentes.

Python é **case-sensitive**.

Portanto:

```text
nome
Nome
NOME
```

podem representar três variáveis diferentes.

Por padrão, prefira nomes minúsculos:

```python
nome_aluno
nota_final
quantidade
```

---

# 24. Comentários

Podemos escrever comentários no código utilizando:

```python
#
```

Exemplo:

```python
# Nome do personagem
nome = "Aragorn"

# Quantidade inicial de pontos
pontos = 100
```

Comentários são ignorados pelo interpretador.

Eles existem para ajudar humanos a entender o código.

---

# 25. Exemplo completo

Imagine um pequeno sistema de cadastro de personagem:

```python
nome = "Kael"
classe = "Guerreiro"
nivel = 5
vida = 120
mana = 30
vivo = True

print("=== PERSONAGEM ===")

print("Nome:", nome)
print("Classe:", classe)
print("Nível:", nivel)
print("Vida:", vida)
print("Mana:", mana)
print("Está vivo:", vivo)
```

Saída:

```text
=== PERSONAGEM ===
Nome: Kael
Classe: Guerreiro
Nível: 5
Vida: 120
Mana: 30
Está vivo: True
```

Mesmo conhecendo apenas `print()` e variáveis, já conseguimos organizar informações dentro de um programa.

E essa ideia será extremamente importante quando chegarmos em **Estruturas de Dados**.

---

# Desafio rápido em sala

Antes dos exercícios, você pode escrever no quadro:

```python
energia = 100

energia = energia - 25
energia = energia + 10

print(energia)
```

E perguntar:

**Qual será o resultado?**

Resposta:

```text
85
```

O interessante aqui não é apenas acertar.

Peça para os alunos explicarem **passo a passo o estado da variável**:

```text
energia = 100

energia = 75

energia = 85
```

Isso começa a desenvolver uma habilidade importantíssima em lógica: **simular mentalmente a execução do programa**.

---

# Exercícios

Os exercícios abaixo trabalham os conceitos da aula, mas não repetem os exemplos utilizados anteriormente.

## Exercício 01 — Apresentação

Crie um programa que armazene em variáveis:

- seu nome;
- sua cidade;
- sua idade;
- uma tecnologia que gostaria de aprender.

Depois apresente as informações utilizando `print()`.

Saída esperada semelhante a:

```text
===== MEU PERFIL =====
Nome: ...
Cidade: ...
Idade: ...
Tecnologia: ...
```

---

## Exercício 02 — Ficha de produto

Crie variáveis que representem um produto:

```text
nome
preço
quantidade em estoque
disponível
```

Depois mostre todas as informações na tela.

Utilize tipos de dados adequados para cada informação.

---

## Exercício 03 — Pontuação de um jogador

Um jogador inicia uma partida com:

```text
250 pontos
```

Durante a partida:

```text
ganha 120 pontos
perde 50 pontos
ganha 30 pontos
```

Crie uma variável chamada `pontos` e atualize seu valor a cada acontecimento.

Ao final mostre:

```text
Pontuação final: ...
```

Não realize o cálculo manualmente antes.

O programa deverá fazer todas as alterações.

---

## Exercício 04 — Carrinho de compras

Uma pessoa comprou:

```text
4 produtos
```

Cada produto custa:

```text
R$ 18.50
```

Crie variáveis para armazenar:

```text
preco
quantidade
total
```

Calcule o valor total da compra e apresente:

```text
Valor da compra: ...
```

---

## Exercício 05 — Conversão de horas

Considere:

```text
1 hora = 60 minutos
```

Crie uma variável:

```python
horas = 7
```

Calcule através do programa quantos minutos existem nesse período.

Resultado esperado:

```text
7 horas equivalem a 420 minutos
```

---

## Exercício 06 — Vida do personagem

Um personagem possui inicialmente:

```text
200 pontos de vida
```

Durante uma batalha:

```text
recebe 45 de dano
recebe 30 de dano
recupera 20 pontos de vida
```

Crie uma variável `vida` e atualize seu valor depois de cada acontecimento.

Mostre somente a quantidade final de vida.

---

## Exercício 07 — Salário

Uma pessoa recebe:

```text
R$ 2800
```

e receberá um bônus de:

```text
R$ 450
```

Crie:

```text
salario
bonus
salario_final
```

Calcule e apresente o salário final.

---

## Exercício 08 — Área de um retângulo

Crie duas variáveis:

```text
largura
altura
```

Calcule:

```text
área = largura × altura
```

Apresente largura, altura e área.

---

## Exercício 09 — Descobrindo os tipos

Crie as seguintes variáveis:

```python
titulo = "Python"
versao = 3
nota = 9.5
finalizado = False
```

Utilize `type()` para descobrir e mostrar o tipo de cada variável.

Depois, escreva como comentário ao lado de cada uma o que aquele tipo representa.

---

## Exercício 10 — Mini ficha de jogo

Crie um personagem contendo pelo menos:

```text
nome
classe
nivel
vida
ataque
defesa
possui_magia
```

Depois calcule uma variável:

```text
poder_total
```

utilizando:

```text
ataque + defesa
```

Mostre uma ficha organizada no terminal.

Exemplo de formato:

```text
========================
      PERSONAGEM
========================
Nome:
Classe:
Nível:
Vida:
Ataque:
Defesa:
Poder Total:
Possui magia:
========================
```

Aqui eles já começam a perceber que **programar é representar alguma coisa do mundo através de dados**.

---

# Desafio extra

Sem utilizar nenhum recurso além do que foi visto na aula, crie um pequeno sistema representando um personagem de RPG.

O personagem deve possuir:

```text
nome
vida
ouro
nivel
```

Durante a aventura:

```text
ganha ouro
recebe dano
gasta ouro
recupera vida
sobe de nível
```

Cada acontecimento deve alterar a variável correspondente.

No final, apresente o estado atualizado do personagem.

---
