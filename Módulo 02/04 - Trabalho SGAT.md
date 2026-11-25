# Trabalho em Grupo – Sistema de Gerenciamento de Assistência Técnica (SGAT)

## 1. Situação-problema

Uma empresa de assistência técnica de informática realiza diariamente serviços de manutenção de computadores, notebooks e outros equipamentos eletrônicos.

Atualmente, a empresa registra seus atendimentos manualmente em cadernos e planilhas, ocasionando problemas como perda de informações, dificuldade de localização de serviços e falta de controle financeiro.

Diante desse cenário, a empresa contratou uma equipe de desenvolvedores para criar uma aplicação desktop que facilite o gerenciamento de suas ordens de serviço (OS).

**Vocês serão essa equipe de desenvolvimento!**

Cada grupo deverá criar um nome e uma identidade visual para sua assistência técnica.

## 2. Objetivos

Desenvolver uma aplicação desktop utilizando Python, Tkinter e Programação Orientada a Objetos (POO), aplicando os conhecimentos desenvolvidos em aula:

- Criação e utilização de ambientes virtuais;
- Gerenciamento de dependências com `pip`;
- Desenvolvimento de interfaces gráficas;
- Manipulação de componentes gráficos e gerenciadores de layout;
- Programação orientada a eventos;
- Classes, objetos, listas, funções e métodos;
- Estruturas condicionais e de repetição;
- Validação de informações e tratamento de erros;
- Trabalho em equipe.

## 3. Organização do trabalho

| Informação | Descrição |
| --- | --- |
| Modalidade | Trabalho em grupo |
| Integrantes | 3 a 4 alunos |
| Tempo de desenvolvimento | 9 horas (3 aulas) |
| Linguagem | Python |
| Biblioteca gráfica | Tkinter |
| Armazenamento | Listas e objetos |
| Entrega | Código-fonte e documentação |

## 4. Cadastro de ordens de serviço

Cada ordem de serviço deverá possuir as seguintes informações:

| Campo | Tipo de dado | Exemplo |
| --- | --- | --- |
| Número da OS | `int` | 001 |
| Nome do cliente | `str` | João Silva |
| Telefone | `str` | (51) 99999-9999 |
| Equipamento | `str` | Notebook |
| Marca e modelo | `str` | Dell Inspiron 15 |
| Descrição do problema | `str` | Equipamento não liga |
| Valor do serviço | `float` | R$ 150,00 |
| Situação | `str` | Pendente |

O número da OS deverá ser gerado automaticamente pelo sistema. O formato com zeros à esquerda é apenas uma sugestão de apresentação.

### 4.1. Situações de uma ordem de serviço

| Situação | Descrição |
| --- | --- |
| Pendente | Equipamento recebido pela assistência. |
| Em andamento | Equipamento em manutenção. |
| Concluído | Serviço finalizado. |
| Entregue | Equipamento devolvido ao cliente. |

Fluxo típico de atendimento:

```text
Pendente --> Em andamento --> Concluído --> Entregue
```

Toda nova ordem de serviço deverá iniciar com a situação **Pendente**.

## 5. Requisitos funcionais

| Código | Funcionalidade | Descrição |
| --- | --- | --- |
| RF01 | Cadastrar OS | Registrar uma nova ordem de serviço. |
| RF02 | Listar OS | Apresentar todas as ordens cadastradas na interface. |
| RF03 | Pesquisar OS | Buscar pelo número da OS ou pelo nome do cliente. |
| RF04 | Alterar situação | Localizar uma OS e atualizar sua situação. |
| RF05 | Remover OS | Localizar e excluir uma ordem de serviço. |
| RF06 | Limpar formulário | Limpar os campos de cadastro sem excluir registros. |
| RF07 | Validar informações | Impedir cadastros com informações inválidas. |
| RF08 | Indicadores | Apresentar um resumo das ordens cadastradas. |
| RF09 | Controle financeiro | Calcular e apresentar os valores dos serviços. |

## 6. Regras de negócio

- O número da OS deverá ser único e não deverá ser reutilizado após uma exclusão durante a execução do programa.
- Todos os campos de cadastro deverão ser preenchidos. O número e a situação inicial serão definidos automaticamente pelo sistema.
- O valor do serviço deverá ser numérico e não poderá ser negativo.
- Toda nova OS deverá iniciar como pendente.
- A situação da OS poderá ser alterada posteriormente para uma das quatro situações previstas.
- O sistema deverá apresentar mensagens de sucesso ou erro na própria interface gráfica.
- O sistema deverá informar quando uma pesquisa não encontrar resultados.
- Os indicadores deverão ser atualizados após o cadastro, a remoção ou a alteração de situação de uma OS.
- A aplicação não deverá encerrar inesperadamente quando o usuário informar dados inválidos.

## 7. Interface gráfica

Antes de iniciar a programação, cada grupo deverá planejar a organização da interface gráfica.

A aplicação deverá possuir um formulário de cadastro, uma área de consulta e listagem, botões para executar as operações e uma área para apresentar os indicadores e as mensagens do sistema.

### 7.1. Exemplo de protótipo

```text
+------------------------------------------------------------------+
| TECHFIX INFORMATICA - GERENCIAMENTO DE ORDENS DE SERVICO           |
+------------------------------------------------------------------+
| NOVA ORDEM DE SERVICO                                            |
| Cliente:       [________________________]                        |
| Telefone:      [________________________]                        |
| Equipamento:   [________________________]                        |
| Marca/modelo:  [________________________]                        |
| Valor:         [________________________]                        |
| Problema:      [________________________]                        |
|                [________________________]                        |
| Situacao inicial: Pendente                                      |
|          [ Cadastrar OS ]  [ Limpar campos ]                     |
+------------------------------------------------------------------+
| CONSULTA                                                        |
| Nome ou numero da OS: [________________] [ Buscar ]              |
| [ Listar todas ]                                                |
|                                                                  |
| OS   | Cliente  | Equipamento | Situacao     | Valor             |
| 001  | Joao     | Notebook    | Pendente     | 150,00            |
| 002  | Maria    | Desktop     | Em andamento | 200,00           |
| 003  | Pedro    | Notebook    | Concluido    | 120,00            |
| 004  | Ana      | Impressora  | Entregue     |  80,00            |
|                                                                  |
| Numero da OS: [____] Nova situacao: [______________]             |
|          [ Alterar situacao ]  [ Remover OS ]                    |
+------------------------------------------------------------------+
| Total: 4 | Pendentes: 1 | Em andamento: 1                         |
| Concluidos: 1 | Entregues: 1                                    |
| Valor total: R$ 550,00                                          |
| Concluidos e entregues: R$ 200,00                                |
+------------------------------------------------------------------+
| Mensagem: Ordem de servico cadastrada com sucesso!                |
+------------------------------------------------------------------+
```

O protótipo é apenas uma referência. Cada grupo terá liberdade para definir cores, fontes, posicionamento e organização dos componentes.

Não é necessário utilizar componentes avançados de tabela. A listagem poderá ser apresentada utilizando `Label` ou `Text`. As operações de alteração e remoção poderão utilizar um campo para informar o número da OS.

## 8. Indicadores do sistema

O sistema deverá calcular automaticamente os seguintes indicadores com base nas ordens de serviço cadastradas:

| Indicador | Exemplo |
| --- | ---: |
| Total de ordens de serviço | 4 |
| Serviços pendentes | 1 |
| Serviços em andamento | 1 |
| Serviços concluídos | 1 |
| Equipamentos entregues | 1 |
| Valor total dos serviços cadastrados | R$ 550,00 |
| Valor dos serviços concluídos e entregues | R$ 200,00 |

O valor total corresponde à soma dos valores de todas as ordens cadastradas. O valor dos serviços concluídos e entregues corresponde à soma apenas das ordens nessas duas situações, sem representar necessariamente pagamentos recebidos.

Quando não existirem ordens cadastradas, os indicadores deverão apresentar zero.

## 9. Programação Orientada a Objetos

Os grupos deverão desenvolver uma classe chamada `OrdemServico`, responsável por representar as ordens de serviço do sistema.

A classe deverá possuir, no mínimo, a seguinte estrutura:

```text
+--------------------------------+
| OrdemServico                   |
+--------------------------------+
| numero: int                    |
| cliente: str                   |
| telefone: str                  |
| equipamento: str               |
| marca_modelo: str              |
| descricao: str                 |
| valor: float                   |
| situacao: str                  |
+--------------------------------+
| alterar_situacao()             |
| exibir_informacoes()           |
+--------------------------------+
```

Cada nova ordem de serviço deverá ser uma instância dessa classe e deverá ser armazenada em uma lista de objetos.

O método `alterar_situacao()` deverá permitir atualizar a situação da ordem. O método `exibir_informacoes()` deverá disponibilizar os dados para apresentação na interface gráfica.

> **Atenção:** não será necessário utilizar banco de dados nesta etapa. Os dados serão armazenados em memória e poderão ser perdidos quando a aplicação for encerrada.

## 10. Requisitos técnicos

- Utilizar Python e Tkinter;
- Criar e utilizar um ambiente virtual (`venv`);
- Gerar o arquivo `requirements.txt`;
- Utilizar classes e objetos para representar as ordens de serviço;
- Armazenar os registros em uma lista;
- Organizar as funcionalidades em funções e métodos;
- Utilizar estruturas condicionais e de repetição;
- Utilizar componentes gráficos como `Label`, `Entry`, `Button`, `Text` e `Frame`;
- Utilizar gerenciadores de layout para organizar a interface;
- Associar os botões às funcionalidades utilizando eventos;
- Validar os dados fornecidos pelo usuário;
- Realizar todas as interações com o usuário pela interface gráfica, sem depender de `input()` ou `print()` no terminal.

> **Dica:** não utilize `pack()` e `grid()` simultaneamente dentro de um mesmo contêiner. É possível utilizar gerenciadores diferentes em contêineres distintos, como os `Frame`.

## 11. Estrutura do projeto

Sugestão de organização dos arquivos:

```text
SGAT/
├── .venv/
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

| Arquivo | Finalidade |
| --- | --- |
| `main.py` | Interface gráfica e funcionalidades do sistema. |
| `models.py` | Classe que representa a ordem de serviço. |
| `requirements.txt` | Dependências do projeto. |
| `README.md` | Documentação e instruções de execução. |
| `.gitignore` | Arquivos e pastas ignorados pelo Git, caso seja utilizado. |

O Tkinter faz parte da biblioteca padrão do Python. Portanto, o arquivo `requirements.txt` poderá estar vazio caso nenhuma biblioteca externa seja utilizada.

## 12. Cronograma de desenvolvimento

| Aula | Atividades |
| --- | --- |
| Aula 01 – 3h | Planejamento, prototipação, configuração do ambiente, criação da classe e início da interface. |
| Aula 02 – 3h | Implementação das funcionalidades e integração com a interface gráfica. |
| Aula 03 – 3h | Finalização, testes, correção de erros e apresentação. |

Todos os integrantes deverão contribuir com a programação e compreender o funcionamento do sistema completo.

## 13. Testes da aplicação

Antes da entrega, verifiquem se o sistema se comporta corretamente nos seguintes cenários:

| Teste | Resultado esperado |
| --- | --- |
| Cadastrar uma OS com dados válidos | Registro adicionado à lista com número único e situação pendente. |
| Cadastrar com campos vazios | Mensagem de erro e nenhum registro adicionado. |
| Informar um valor negativo ou não numérico | Mensagem de erro e nenhum registro adicionado. |
| Pesquisar uma OS existente | Dados da OS apresentados na interface. |
| Pesquisar uma OS inexistente | Mensagem informando que não foram encontrados resultados. |
| Alterar a situação de uma OS | Situação e indicadores atualizados. |
| Remover uma OS existente | Registro removido e indicadores atualizados. |
| Alterar ou remover uma OS inexistente | Mensagem de erro, sem encerrar a aplicação. |
| Limpar o formulário | Campos limpos, sem excluir registros. |
| Listar sem registros cadastrados | Listagem vazia e indicadores zerados. |

## 14. Critérios de avaliação

| Critério | Peso |
| --- | ---: |
| Atendimento aos requisitos funcionais | 30% |
| Aplicação da POO | 15% |
| Organização da interface gráfica | 15% |
| Validação de dados | 15% |
| Organização do código | 10% |
| Trabalho em equipe | 10% |
| Apresentação e documentação | 5% |
| **Total** | **100%** |

## 15. Desafios extras (opcionais)

Para os grupos que concluírem os requisitos obrigatórios antes do prazo:

- Edição completa de uma ordem de serviço;
- Cadastro separado de clientes;
- Cadastro de técnicos responsáveis pela manutenção;
- Registro da data de entrada e saída do equipamento;
- Filtro de ordens de serviço por situação;
- Exportação de ordens de serviço para CSV;
- Armazenamento permanente utilizando JSON;
- Tela de login;
- Personalização adicional da identidade visual da empresa.

Os desafios extras não substituem os requisitos obrigatórios.

## 16. Entrega e apresentação

Cada grupo deverá entregar o código-fonte completo e um arquivo `README.md` contendo:

- Nome do sistema;
- Nome dos integrantes da equipe;
- Breve descrição do projeto;
- Funcionalidades implementadas;
- Instruções para configurar o ambiente e executar a aplicação.

Não é necessário enviar a pasta `.venv`.

Durante a apresentação, todos os integrantes deverão participar da demonstração e explicar como o sistema foi desenvolvido, como os dados são armazenados, como os eventos dos botões funcionam e como as validações e os indicadores foram implementados.

## 17. Checklist de entrega

- [ ] Ambiente virtual configurado.
- [ ] Interface gráfica funcional e organizada.
- [ ] Classe `OrdemServico` implementada.
- [ ] Ordens de serviço armazenadas em uma lista de objetos.
- [ ] Cadastro com numeração automática.
- [ ] Listagem e pesquisa de ordens de serviço.
- [ ] Alteração de situação e remoção de ordens.
- [ ] Limpeza do formulário.
- [ ] Validação de informações e mensagens na interface.
- [ ] Indicadores e controle financeiro funcionando.
- [ ] Testes realizados.
- [ ] Arquivo `requirements.txt` gerado.
- [ ] Arquivo `README.md` com identificação dos integrantes e instruções de execução.
- [ ] Código-fonte completo entregue.

---

**Bom trabalho a todos!**
