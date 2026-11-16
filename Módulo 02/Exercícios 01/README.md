# Correções explicadas — Aula 01: Introdução à POO

Gabarito dos oito exercícios e do desafio extra da [aula 01](../01%20-%20Introdução%20à%20POO.md). Cada arquivo contém uma solução independente, com comentários. Como não há respostas de alunos nesta pasta, as correções apresentam soluções de referência e explicam as decisões.

As soluções seguem as premissas da aula: tipos corretos, quantidades inteiras, medidas positivas e dados iniciais válidos. Não é necessário usar herança, bibliotecas ou tratamento de exceções.

Para executar, abra o terminal nesta pasta e use, por exemplo:

```text
python 01_livros.py
```

Troque o nome pelo arquivo desejado. O arquivo `09_biblioteca.py` solicita entradas pelo terminal.

## 01 — Cadastro de livros

**Solução:** [01_livros.py](01_livros.py).

`Livro` é a classe. As duas chamadas a `Livro(...)` criam duas instâncias, referenciadas por `primeiro` e `segundo`. Os atributos são `titulo`, `autor` e `paginas`; `__init__` os inicializa usando `self`.

Antes da alteração, os livros têm 256 e 96 páginas. Depois de `primeiro.paginas = 280`, passam a ter 280 e 96. Apenas o primeiro muda, pois cada objeto guarda seus próprios atributos. Escrever `segundo = primeiro` faria as duas variáveis referenciarem o mesmo livro, em vez de criar outro.

## 02 — Área de um retângulo

**Solução:** [02_retangulo.py](02_retangulo.py).

`calcular_area()` acessa as medidas do objeto com `self` e devolve sua multiplicação. As áreas exibidas são `12` e `10`.

`return` entrega o resultado a quem chamou, permitindo armazená-lo ou utilizá-lo em outra conta. `print()` apenas apresenta o resultado. Se o método somente imprimisse a área e terminasse sem retornar um valor, uma atribuição como `area = primeiro.calcular_area()` guardaria `None`.

## 03 — Contador de atendimentos

**Solução:** [03_contador.py](03_contador.py).

Cada chamada a `Contador()` inicializa seu próprio `valor` com zero. `incrementar()` soma um ao valor atual; `zerar()` atribui zero somente à instância que recebe a chamada.

```text
Antes de zerar: 3 1
Depois de zerar: 0 1
```

Esses métodos alteram o estado e não precisam devolver um resultado pelo enunciado. Ao terminarem, retornam `None` implicitamente.

## 04 — Controle de estoque

**Solução:** [04_estoque.py](04_estoque.py).

As validações acontecem antes de alterar o estoque. Um `return False` encerra a chamada imediatamente quando a quantidade é inválida. Uma operação aceita altera o estado e retorna `True`.

| Operação | Retorno | Estoque após a chamada |
| --- | --- | --- |
| `vender(2)` | `True` | 2 |
| `vender(3)` | `False` | 2 |
| `repor(5)` | `True` | 7 |
| `repor(0)` | `False` | 7 |

O valor final é `5.0 * 7`, ou seja, `35.0`. O método de consulta não altera o estoque. A venda usa `quantidade > self.estoque` na recusa: vender exatamente o estoque disponível é permitido. Quantidades negativas e zero são recusadas tanto na venda quanto na reposição.

## 05 — Empréstimo de um livro

**Solução:** [05_emprestimo.py](05_emprestimo.py).

`emprestado` representa o estado atual; o retorno informa se a operação foi realizada. São informações diferentes: uma tentativa de empréstimo pode retornar `False` enquanto o atributo continua `True`.

| Operação | Retorno | `emprestado` após a chamada |
| --- | --- | --- |
| Primeiro empréstimo | `True` | `True` |
| Segundo empréstimo | `False` | `True` |
| Primeira devolução | `True` | `False` |
| Segunda devolução | `False` | `False` |

Verificar o estado antes de alterá-lo impede emprestar novamente um livro indisponível ou devolver um livro que já está disponível.

## 06 — Turmas independentes

**Solução:** [06_turmas.py](06_turmas.py).

A lista `self.alunos = []` é criada dentro de `__init__`, uma vez para cada objeto. `matricular()` adiciona um nome à lista daquela turma; `quantidade_alunos()` devolve seu tamanho com `len()`.

| Turma | Alunos | Quantidade |
| --- | --- | --- |
| Manhã | `['Ana', 'Bruno']` | 2 |
| Noite | `['Carla']` | 1 |

Se escrevêssemos `alunos = []` diretamente no corpo da classe, a lista seria um atributo de classe e as alterações com `append` seriam compartilhadas entre as instâncias. Não há bloqueio de nomes repetidos, conforme o enunciado.

## 07 — Relatório de produtos

**Solução:** [07_relatorio.py](07_relatorio.py).

O `for` percorre objetos completos. Para cada produto, o relatório consulta seu valor em estoque, acumula esse valor em `total` e incrementa `sem_estoque` apenas quando o estoque é exatamente zero.

| Produto | Estoque | Valor em estoque |
| --- | --- | --- |
| Caderno | 2 | 20.0 |
| Caneta | 0 | 0.0 |
| Borracha | 5 | 10.0 |

O total é `30.0` e há `1` produto sem estoque. A função `mostrar_relatorio` permite repetir o mesmo procedimento com outra lista. Os acumuladores são inicializados dentro dela, antes do laço. Com `[]`, o laço não executa e os resultados permanecem `0` e `0`; não há tentativa de acessar uma posição inexistente.

## 08 — Conta com operações validadas

**Solução:** [08_conta.py](08_conta.py).

Cada conta começa com saldo zero. Depósitos exigem valor positivo; saques exigem valor positivo e saldo suficiente. Uma recusa retorna antes de qualquer alteração.

| Operação na primeira conta | Retorno | Saldo após a chamada |
| --- | --- | --- |
| `depositar(50)` | `True` | 50 |
| `sacar(20)` | `True` | 30 |
| `sacar(40)` | `False` | 30 |
| `depositar(-10)` | `False` | 30 |

A segunda conta permanece com `0`, pois foi criada separadamente. Valores zero também são recusados nos dois métodos; sacar exatamente o saldo é permitido e deixa a conta zerada.

## 09 — Desafio extra: biblioteca com menu

**Solução:** [09_biblioteca.py](09_biblioteca.py).

A lista guarda três objetos `Livro`, inicialmente disponíveis. O `while` repete o menu até a opção `0`. As opções são comparadas como textos, pois `input()` devolve `str`.

Nas opções `2` e `3`, `encontrado` começa como `None`. O `for` procura um título exatamente igual ao digitado e, quando o encontra, guarda a referência ao objeto e encerra a busca com `break`. Esse `break` encerra somente a busca; o da opção `0` encerra o laço do menu.

O menu chama `emprestar()` ou `devolver()` e apresenta a mensagem de acordo com o retorno. As regras ficam nos métodos, permitindo reutilizá-las sem depender do menu. Um título ausente gera `Livro não encontrado`; outras opções geram `Opção desconhecida.`.

Roteiro para conferir no terminal:

| Entradas, em sequência | Resultado esperado |
| --- | --- |
| `1` | Os três títulos aparecem disponíveis |
| `2`, depois `Dom Casmurro` | `Empréstimo realizado.` |
| `2`, depois `Dom Casmurro` | `Livro já emprestado.` |
| `1` | Dom Casmurro aparece emprestado; os demais continuam disponíveis |
| `3`, depois `Dom Casmurro` | `Devolução realizada.` |
| `3`, depois `Dom Casmurro` | `Livro já disponível.` |
| `2`, depois `Título inexistente` | `Livro não encontrado` |
| `9` | `Opção desconhecida.` |
| `0` | `Biblioteca encerrada.` e fim do programa |

## Resposta ao desafio rápido em sala

As saídas são `3`, `6` e `3`, nessa ordem. Há dois objetos: `primeiro` e `referencia` apontam para o mesmo produto, que perde uma unidade; `segundo` aponta para outro produto, que recebe duas unidades. A atribuição `referencia = primeiro` não cria uma cópia.
