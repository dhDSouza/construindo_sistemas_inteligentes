# Exercícios de Fixação — Estruturas Condicionais em Python

Conteúdo: `input()`, `int()`, `float()`, `if`, `elif`, `else`, `and`, `or`, `not` e condicionais aninhadas.

Objetivo: Reforçar a lógica de decisão por meio de situações práticas, trabalhando interpretação de regras, operadores relacionais e condições compostas.

## Orientações

- Crie um arquivo `.py` para cada exercício.
- Utilize apenas os conteúdos estudados até o momento.
- Não utilize estruturas de repetição (`while`, `for`), listas ou funções próprias.
- Todos os dados necessários devem ser solicitados com `input()`.
- Considere que o usuário digitará números no formato correto.
- Teste diferentes entradas para verificar o comportamento de cada condição.

## Exercício 01 — Sistema de estacionamento

### **`Fácil`**

Um estacionamento precisa calcular o valor cobrado de seus clientes de acordo com o tempo de permanência.

Desenvolva um programa que solicite a quantidade de horas que um veículo permaneceu estacionado.

As regras são:

| Tempo de permanência  | Valor    |
| --------------------- | -------- |
| Até 2 horas           | R$ 10,00 |
| Mais de 2 até 5 horas | R$ 20,00 |
| Mais de 5 horas       | R$ 30,00 |

Requisitos:

- A quantidade de horas deve ser maior que zero.
- Caso seja informado um valor inválido, apresente uma mensagem.
- Exiba o valor total a pagar.

## Exercício 02 — Classificação de personagem de RPG

### **`Fácil`**

Um jogo de RPG classifica seus aventureiros de acordo com o nível alcançado.

Solicite o nome e o nível de um personagem e determine sua classificação:

| Nível          | Classificação |
| -------------- | ------------- |
| 1 a 5          | Aprendiz      |
| 6 a 15         | Guerreiro     |
| 16 a 30        | Veterano      |
| 31 ou superior | Lendário      |

Requisitos:

- Não permita níveis menores que 1.
- Mostre o nome do personagem e sua classificação.
- Utilize `if`, `elif` e `else`.

## Exercício 03 — Sistema de autenticação

### **`Intermediário`**

Uma aplicação possui um sistema simples de autenticação.

Considere as credenciais cadastradas:

```
usuario_correto = "admin"senha_correta = "python123"
```

Solicite que a pessoa informe seu usuário e sua senha.

O programa deverá apresentar uma das seguintes mensagens:

- `Acesso autorizado!` — quando ambos estiverem corretos.
- `Senha incorreta!` — quando o usuário estiver correto, mas a senha errada.
- `Usuário não encontrado!` — quando o usuário não existir.

Desafio: Utilize condições aninhadas para verificar primeiro o usuário e depois a senha.

## Exercício 04 — Análise de empréstimo

### **`Intermediário`**

Um banco deseja automatizar a análise inicial de empréstimos.

Solicite as seguintes informações:

- Salário mensal do cliente.
- Valor solicitado para empréstimo.
- Quantidade de parcelas.

O empréstimo só poderá ser aprovado se todas as condições forem atendidas:

1. O salário deve ser de pelo menos R$ 2.000,00.
2. O valor solicitado não pode ultrapassar 10 vezes o salário.
3. O valor de cada parcela não pode ultrapassar 30% do salário.
4. A quantidade de parcelas deve estar entre 1 e 48.

Caso alguma condição não seja atendida, informe que o empréstimo foi recusado.

Desafio: Apresente o motivo da recusa.

Considere um empréstimo sem juros, apenas para fins de exercício.

## Exercício 05 — Sistema de combate RPG

### **`Intermediário`**

Durante uma aventura, um personagem encontra um inimigo e precisa decidir se consegue derrotá-lo.

Solicite:

- Nome do personagem.
- Vida atual.
- Pontos de ataque.
- Vida do inimigo.
- Pontos de defesa do inimigo.

Calcule o dano causado:

```
dano = ataque - defesa
```

Considere as seguintes regras:

- Se a vida do personagem for menor ou igual a zero, ele não poderá atacar.
- Se o dano for menor ou igual a zero, o ataque não causará dano.
- Se o dano for maior ou igual à vida do inimigo, o inimigo será derrotado.
- Caso contrário, o inimigo sobreviverá. Exiba a vida restante dele.

Desafio: Impedir que a vida restante do inimigo fique negativa.

## Exercício 06 — Controle de acesso a um laboratório

### **`Intermediário`**

Um laboratório de tecnologia possui equipamentos que só podem ser utilizados por pessoas autorizadas.

Solicite:

- Idade.
- Se a pessoa é aluno matriculado (`sim` ou `nao`).
- Se possui autorização do professor (`sim` ou `nao`).
- Se o laboratório está disponível (`sim` ou `nao`).

O acesso será permitido quando:

- O laboratório estiver disponível.
- A pessoa tiver pelo menos 16 anos.
- A pessoa for matriculada ou possuir autorização do professor.

Requisitos: Utilize `and` e `or` e apresente uma mensagem indicando se o acesso foi permitido ou negado.

## Exercício 07 — Sistema de frete

### **`Intermediário`**

Uma loja virtual deseja calcular o valor do frete com base na região do cliente e no valor da compra.

Solicite o valor da compra e a região de entrega:

| Região            | Frete    |
| ----------------- | -------- |
| Sul               | R$ 15,00 |
| Sudeste           | R$ 20,00 |
| Centro-Oeste      | R$ 25,00 |
| Norte ou Nordeste | R$ 35,00 |

Regras adicionais:

- Compras a partir de R$ 300,00 recebem frete grátis.
- Compras com valor menor ou igual a zero são inválidas.
- Regiões não reconhecidas devem apresentar `Região inválida`.
- Mostre o valor da compra, o frete e o total.

Atenção: Mesmo que a compra tenha frete grátis, a região informada deverá ser válida.

## Exercício 08 — Validação de triângulos

### **`Desafiador`**

Desenvolva um programa que receba três números representando os lados de um possível triângulo.

Para formar um triângulo, os três lados devem ser positivos e satisfazer:

> ### a+b>c E a+c>b E b+c>a

Caso seja possível formar um triângulo, classifique-o:

| Tipo       | Condição                     |
| ---------- | ---------------------------- |
| Equilátero | Três lados iguais            |
| Isósceles  | Exatamente dois lados iguais |
| Escaleno   | Três lados diferentes        |

Se os valores não formarem um triângulo, mostre `Triângulo inválido`.

Desafio: Realize primeiro a validação e somente depois a classificação.
