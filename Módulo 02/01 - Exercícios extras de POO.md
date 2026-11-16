# Tópico 01 — Exercícios extras de POO

Atividades complementares à [Introdução à Programação Orientada a Objetos](01%20-%20Introdução%20à%20POO.md).

**Objetivo:** praticar classes, objetos, `__init__`, `self`, atributos de instância, métodos, retornos, validações e listas de objetos em novos contextos.

## Orientações

- Resolva cada exercício em um arquivo Python separado, usando o nome sugerido.
- Utilize apenas os recursos estudados até o tópico 01. Não é necessário usar herança, propriedades, bibliotecas ou tratamento de exceções.
- Considere que os argumentos têm os tipos corretos e que os dados iniciais são válidos. Implemente as validações de valores descritas em cada exercício.
- Nos métodos de consulta, devolva o resultado com `return`. Faça a apresentação com `print()` fora da classe.
- Quando uma operação retornar `False`, os atributos devem permanecer como estavam antes da tentativa.
- Antes de executar, anote o resultado esperado. Depois, compare com a saída do programa.

## Exercício 01 — Do problema para a classe

**Arquivo: `extra_01_lampada.py`**

Uma sala possui duas lâmpadas que podem ser ligadas e desligadas separadamente.

1. Identifique a classe, dois atributos e dois comportamentos que representam esse problema.
2. Implemente a classe `Lampada`, recebendo `local` e iniciando o atributo `ligada` como `False`.
3. Crie `ligar()` e `desligar()`. Cada método deve retornar `True` se mudar o estado e `False` se a lâmpada já estiver no estado solicitado.
4. Crie uma lâmpada para a entrada e outra para o fundo da sala.
5. Na lâmpada da entrada, execute `ligar()`, `ligar()`, `desligar()` e `desligar()`, nessa ordem.

**Conferência:** os retornos são `True`, `False`, `True` e `False`. As duas lâmpadas terminam desligadas; a do fundo não sofre alterações durante as chamadas.

**Para explicar:** qual é a diferença entre o retorno de `desligar()` e o valor de `ligada` após uma operação bem-sucedida?

## Exercício 02 — Corrigindo o uso de `self`

**Arquivo: `extra_02_placar.py`**

O código abaixo deveria registrar os pontos de um jogador, mas contém erros:

```python
class Placar:
    def __init__(self, jogador):
        jogador = jogador
        pontos = 0

    def marcar(quantidade):
        pontos = pontos + quantidade


placar = Placar("Lia")
placar.marcar(3)
print(placar.jogador, placar.pontos)
```

1. Corrija a inicialização dos atributos e a definição do método.
2. Faça `marcar(quantidade)` aceitar apenas inteiros positivos, retornando `True` quando somar os pontos e `False` quando recusar o valor. Considere que o argumento já é inteiro.
3. Acrescente `consultar_pontos()`, que retorna a pontuação sem alterá-la.
4. Execute `marcar(3)`, `marcar(2)`, `marcar(0)` e `marcar(-1)`.
5. Guarde o retorno de `consultar_pontos()` em uma variável e mostre seu dobro.

**Conferência:** os retornos das marcações são `True`, `True`, `False` e `False`. A pontuação final é `5`, e seu dobro é `10`.

**Para explicar:** por que escrever apenas `pontos = 0` em `__init__` não cria um atributo do objeto?

## Exercício 03 — Reservatório de água

**Arquivo: `extra_03_reservatorio.py`**

Crie a classe `Reservatorio`, recebendo `capacidade` e iniciando `nivel` com zero. Considere a capacidade positiva e todas as medidas em litros inteiros.

Implemente:

- `adicionar(litros)`: aceita uma quantidade positiva apenas se ela couber integralmente no reservatório;
- `retirar(litros)`: aceita uma quantidade positiva apenas se houver água suficiente;
- `espaco_disponivel()`: retorna a diferença entre a capacidade e o nível atual.

Os dois primeiros métodos devem retornar booleanos. Não aceite uma operação parcialmente: se alguém tentar adicionar mais água do que cabe, recuse toda a quantidade.

Crie um reservatório de capacidade `100` e execute as operações abaixo em sequência. Complete a tabela antes de rodar o programa.

| Operação | Retorno previsto | Nível depois |
| --- | --- | --- |
| `adicionar(60)` | | |
| `adicionar(50)` | | |
| `retirar(20)` | | |
| `adicionar(60)` | | |
| `retirar(100)` | | |
| `retirar(1)` | | |
| `adicionar(0)` | | |

**Conferência final:** nível `0` e espaço disponível `100`. Teste também uma retirada negativa e a adição exata da capacidade em um reservatório vazio.

## Exercício 04 — Acompanhar uma leitura

**Arquivo: `extra_04_leitura.py`**

Crie a classe `Leitura` com `titulo`, `total_paginas` e `paginas_lidas`. Receba os dois primeiros na criação e inicie o terceiro com zero. Considere `total_paginas` um inteiro positivo.

Implemente:

- `avancar(quantidade)`: aceita um inteiro positivo, desde que o total lido não ultrapasse o tamanho do livro; retorna `True` ou `False`;
- `paginas_restantes()`: retorna quantas páginas faltam;
- `concluida()`: retorna `True` se todas as páginas foram lidas e `False` caso contrário.

Crie duas leituras, uma de `120` páginas e outra de `80`. Na primeira, tente avançar `30`, depois `100` e depois `90` páginas.

**Conferência:** os retornos são `True`, `False` e `True`. A primeira leitura termina com `120` páginas lidas, zero restantes e `concluida()` igual a `True`. A segunda continua com zero páginas lidas.

**Para explicar:** chamar `concluida()` duas vezes deve alterar o progresso? Justifique.

## Exercício 05 — Listas próprias de cada objeto

**Arquivo: `extra_05_playlist.py`**

Crie a classe `Playlist`, recebendo `nome` e criando uma lista própria `musicas`, inicialmente vazia.

Implemente:

- `adicionar(titulo)`: recusa o texto vazio `""` e títulos já presentes na lista; adiciona os demais. Retorna `True` ou `False`;
- `quantidade_musicas()`: retorna o tamanho da lista.

Considere a comparação exata entre os textos: `"Sol"` e `"sol"` são títulos diferentes. Não é necessário remover espaços ou modificar letras.

1. Crie as playlists `Estudo` e `Viagem`.
2. Na primeira, adicione `"Chuva"`, `"Piano"`, novamente `"Chuva"` e, por último, `""`.
3. Na segunda, adicione apenas `"Estrada"`.
4. Mostre o nome, as músicas e a quantidade de cada playlist.
5. Percorra as músicas de `Estudo` com um `for`, mostrando um título por linha.

**Conferência:** as tentativas na primeira playlist retornam `True`, `True`, `False` e `False`. Ela contém `['Chuva', 'Piano']`; a segunda contém `['Estrada']`.

**Para explicar:** o que poderia acontecer se `musicas = []` fosse declarada diretamente no corpo da classe?

## Exercício 06 — Duas referências ou dois objetos?

**Arquivo: `extra_06_referencias.py`**

Sem executar, preveja as quatro linhas da saída:

```python
class Marcador:
    def __init__(self, valor):
        self.valor = valor

    def somar(self, quantidade):
        self.valor = self.valor + quantidade


primeiro = Marcador(10)
atalho = primeiro
segundo = Marcador(10)

atalho.somar(5)
segundo.somar(2)
print(primeiro.valor)
print(atalho.valor)
print(segundo.valor)

atalho = segundo
atalho.somar(3)
print(segundo.valor)
```

1. Execute o código e compare com sua previsão.
2. Desenhe setas ligando cada variável ao objeto correspondente antes e depois de `atalho = segundo`.
3. Explique quantos objetos foram criados e por que a atribuição não cria um terceiro.
4. Altere a criação inicial de `atalho` para que ele seja um objeto independente de valor `10`. Execute novamente e explique a mudança nas saídas.

## Exercício 07 — Relatório de inscrições

**Arquivo: `extra_07_oficinas.py`**

Crie a classe `Oficina`, com `nome`, `capacidade` e `inscritos`. Receba nome e capacidade na criação; inicie inscritos com zero. Considere a capacidade um inteiro positivo.

Implemente:

- `inscrever()`: adiciona uma pessoa se houver vaga;
- `cancelar()`: remove uma pessoa se existir pelo menos uma inscrição;
- `vagas_disponiveis()`: retorna a quantidade de vagas restantes.

Os métodos que alteram o estado retornam `True` quando realizam a operação e `False` quando a recusam.

Crie uma lista com estas oficinas:

| Nome | Capacidade | Tentativas de inscrição |
| --- | --- | --- |
| Robótica | 2 | 3 |
| Desenho | 3 | 1 |
| Música | 1 | 0 |

Use os métodos para realizar as tentativas. Depois, percorra a lista e mostre:

- nome, inscritos e vagas disponíveis de cada oficina;
- total de pessoas inscritas;
- total de vagas disponíveis;
- quantidade de oficinas lotadas.

**Conferência:** Robótica tem `2` inscritos, Desenho tem `1` e Música tem `0`. O relatório apresenta `3` inscritos, `3` vagas disponíveis e `1` oficina lotada.

Repita o relatório com uma lista vazia: os três totais devem ser zero. Em um teste separado, cancele duas vezes uma oficina com apenas uma inscrição e confira que a segunda tentativa preserva zero inscritos.

## Desafio extra — Central de tarefas com menu

**Arquivo: `extra_08_tarefas.py`**

Crie a classe `Tarefa`, recebendo `descricao` e iniciando `concluida` com `False`.

- `concluir()` muda o estado para `True` se a tarefa estiver pendente.
- `reabrir()` muda o estado para `False` se a tarefa estiver concluída.
- Os dois métodos retornam `True` quando alteram o estado e `False` caso contrário.

Mantenha uma lista de objetos `Tarefa` e implemente o menu:

```text
1 - Cadastrar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Reabrir tarefa
5 - Mostrar resumo
0 - Sair
```

Regras:

1. Inicie com uma lista vazia.
2. No cadastro, recuse descrição vazia ou exatamente igual à de uma tarefa existente.
3. Na listagem, mostre descrição e situação de cada tarefa. Se não houver tarefas, informe isso.
4. Nas opções 3 e 4, procure a descrição exata com um `for`. Informe quando não encontrar a tarefa; quando encontrar, apresente uma mensagem de acordo com o retorno do método.
5. No resumo, mostre o total de tarefas, quantas estão pendentes e quantas estão concluídas. Percorra os objetos para calcular as contagens.
6. Informe opções desconhecidas e repita o menu até receber `0`.

O menu recebe entradas, procura objetos e apresenta resultados. As mudanças entre pendente e concluída ficam nos métodos da classe.

**Roteiro de conferência:** liste e consulte o resumo antes de cadastrar qualquer tarefa; cadastre `Estudar POO` e `Revisar listas`; tente repetir o primeiro cadastro; conclua `Estudar POO` duas vezes; procure uma descrição inexistente; reabra a primeira tarefa duas vezes; tente cadastrar `""` pressionando apenas Enter; informe uma opção desconhecida e encerre.

**Resultados de referência:** após concluir a primeira tarefa, o resumo deve indicar `2` tarefas, `1` pendente e `1` concluída. Após reabri-la, deve indicar `2` pendentes e `0` concluídas. Tentativas recusadas não alteram esses totais.

## Conferência antes de entregar

- Os atributos de cada objeto foram criados em `__init__` com `self`?
- As instâncias e suas listas permanecem independentes quando necessário?
- Os métodos de consulta retornam valores sem modificar o estado?
- As operações inválidas preservam todos os atributos?
- Você testou zero, valores negativos e limites exatos quando se aplicam?
- As listas vazias são tratadas sem acessar posições inexistentes?
- Você consegue explicar a diferença entre o estado do objeto e o retorno de um método?
