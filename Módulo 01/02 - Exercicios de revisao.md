# Exercícios de revisão — Introdução ao Python

**Data: 08/10/2026**  
**Base: Aula 01 — Introdução ao Python, `print()` e variáveis.**

## Orientações

Crie um arquivo `.py` para cada exercício, utilizando os nomes sugeridos. Escreva os valores diretamente no código e utilize apenas os recursos estudados: variáveis, atribuições, `print()`, `type()`, comentários e as operações `+`, `-`, `*` e `/`.

Utilize nomes de variáveis em `snake_case`, ponto para os números decimais e `True` ou `False` para valores booleanos.

## 12 — Texto ou cálculo?

**Arquivo: `12_texto_ou_calculo.py`**

Antes de executar, escreva em comentários o que acredita que cada linha mostrará:

```python
print("12 + 3")
print(12 + 3)
print("Resultado:", 12 + 3)
print("12", "3")
```

Depois execute e compare suas previsões com a saída. Explique em um comentário por que as duas primeiras linhas produzem resultados diferentes.

## 13 — Cadastro de uma oficina

**Arquivo: `13_cadastro_oficina.py`**

Uma escola oferece uma oficina de robótica. Crie variáveis para armazenar:

- nome da oficina: `"Robótica para iniciantes"`;
- sala: `"Laboratório 2"`;
- quantidade de vagas: `24`;
- duração em horas: `2.5`;
- inscrições abertas: `True`.

Mostre uma ficha com um título e uma informação por linha. Em seguida, mostre o tipo de cada variável com `type()` e escreva comentários explicando o que `str`, `int`, `float` e `bool` representam nesse cadastro.

## 14 — Dividindo a conta

**Arquivo: `14_dividindo_conta.py`**

Quatro amigos compraram uma pizza de R$ 48.00 e uma bebida de R$ 12.00. A conta será dividida igualmente.

1. Crie variáveis para o preço da pizza, o preço da bebida e a quantidade de amigos.
2. Calcule o total da conta em uma nova variável.
3. Calcule quanto cada amigo deverá pagar.
4. Mostre o total e o valor por pessoa com descrições.
5. Use `type()` para mostrar o tipo do valor por pessoa.

**Para pensar:** o resultado da divisão é um `int` ou um `float`, mesmo quando não há centavos?

## 15 — Estoque da biblioteca

**Arquivo: `15_estoque_biblioteca.py`**

A biblioteca começa o dia com 40 livros disponíveis. Nesta ordem:

1. recebe 12 livros novos;
2. empresta 9 livros;
3. recebe a devolução de 4 livros;
4. empresta mais 6 livros.

Crie uma variável `livros_disponiveis` e atualize essa mesma variável após cada acontecimento. Mostre a quantidade inicial e a quantidade após cada atualização, identificando a etapa.

Antes de executar, anote em comentários suas previsões para cada etapa. Compare com o resultado do programa.

## 16 — Boletim de notas

**Arquivo: `16_boletim_notas.py`**

Um aluno recebeu as notas `7.5`, `8.0` e `9.5` em três atividades de mesmo peso.

1. Guarde o nome do aluno e cada nota em variáveis separadas.
2. Calcule a soma das notas em uma variável `soma_notas`.
3. Calcule a média dividindo a soma pela quantidade de atividades.
4. Mostre o nome, as três notas e a média.
5. Troque apenas a segunda nota por `6.5` no código e execute novamente.

O programa deve recalcular a média a partir das variáveis. Não escreva a média pronta no código. Não é necessário informar aprovação ou reprovação.

## 17 — Oficina de correção

**Arquivo: `17_corrigindo_codigo.py`**

O programa abaixo deveria mostrar o nome de um curso, o valor da mensalidade e se a matrícula está ativa, mas contém erros:

```python
nome curso = "Python básico"
mensalidade = 89,90
matricula_ativa = true

print("Curso:", nome_curso)
print("Mensalidade:", Mensalidade)
print("Matrícula ativa:", matricula_ativa)
```

Reescreva o código corrigindo:

- o nome da variável que contém um espaço;
- a escrita do número decimal;
- a escrita do valor booleano;
- a diferença entre maiúsculas e minúsculas no nome da variável.

Para cada correção, escreva um comentário explicando a regra da aula que foi aplicada. Ao final, mostre também `type(mensalidade)` para verificar se o valor é um `float`.

## 18 — Guardando o valor anterior

**Arquivo: `18_valor_anterior.py`**

Leia o programa sem executá-lo:

```python
saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)
```

1. Anote em comentários os valores que serão mostrados.
2. Execute o código para conferir.
3. Explique por que `saldo_anterior` mantém o valor que recebeu na atribuição, mesmo depois das mudanças em `saldo`.
4. Acrescente uma despesa de 15 ao saldo atual e mostre novamente as duas variáveis.

## 19 — Orçamento do passeio

**Arquivo: `19_orcamento_passeio.py`**

Uma turma com 20 alunos fará um passeio. O ônibus custa R$ 600.00 para toda a turma. Cada ingresso custa R$ 15.00 e cada lanche custa R$ 10.00 por aluno.

Crie variáveis para os dados e calcule, em variáveis separadas:

- o custo de todos os ingressos;
- o custo de todos os lanches;
- o custo total do passeio, incluindo o ônibus uma única vez;
- o valor que cada aluno deverá pagar, dividindo o custo total igualmente.

Mostre um relatório com a quantidade de alunos e todos os custos. Depois altere a quantidade de alunos para 25 e execute novamente sem modificar as fórmulas.

**Para pensar:** por que o custo total aumenta, mas o valor por aluno diminui?

## 20 — Uma variável, diferentes tipos

**Arquivo: `20_mudando_tipos.py`**

Crie uma variável chamada `informacao`. Ela deverá receber, nesta ordem:

1. o texto `"42"`;
2. o número inteiro `42`;
3. o número decimal `42.0`;
4. o valor booleano `False`.

Após cada atribuição, mostre o valor e o resultado de `type(informacao)`.

Escreva um comentário explicando a diferença entre `"42"` e `42`. Ao final, explique se a variável guarda os quatro valores ao mesmo tempo ou apenas o último valor atribuído.

## 21 — Desafio: missão do robô explorador

**Arquivo: `21_missao_robo.py`**

Você vai simular uma missão utilizando apenas variáveis e operações sequenciais.

Crie o estado inicial do robô:

| Informação | Valor inicial |
| --- | --- |
| Nome | `"Atlas"` |
| Energia | `100` |
| Distância percorrida, em metros | `0` |
| Amostras coletadas | `0` |
| Missão em andamento | `True` |

Mostre uma ficha inicial. Depois simule os acontecimentos nesta ordem:

1. O robô percorre 120 metros e consome 20 pontos de energia.
2. Coleta 3 amostras e consome 15 pontos de energia.
3. Recarrega 10 pontos de energia.
4. Percorre mais 80 metros e consome 25 pontos de energia.
5. Coleta mais 2 amostras e consome 10 pontos de energia.
6. Encerra a missão: atribua `False` à variável que indica se a missão está em andamento.

Atualize as variáveis correspondentes em cada etapa. Mostre uma mensagem após cada acontecimento e, no final, apresente uma ficha com todos os valores atualizados.

**Parte extra:** considerando que a missão durou 4 minutos, calcule a distância média percorrida por minuto e mostre o resultado com a unidade `metros por minuto`.

## Conferência antes de entregar

- Cada arquivo executa sem erros?
- Os resultados são calculados usando variáveis, em vez de escritos prontos?
- As atualizações seguem a ordem indicada nos enunciados?
- As saídas têm descrições que permitem entender cada valor?
- Os exercícios de previsão e correção incluem os comentários solicitados?
