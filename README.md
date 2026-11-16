# MAC0122-files

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Material teórico próprio e solução dos exercícios elaborados pelos docentes da disciplina MAC0122 (Princípios de
Desenvolvimento de Algoritmos), oferecida semestralmente pelo Departamento de Ciência da Computação do IME-USP.
Veja a ementa [aqui](https://portalservicos.usp.br/jupiterweb/obterDisciplina?nomdis=&sgldis=MAC0122).

Cursada no **segundo semestre de 2022**. Os temas vão de pilhas e filas a arrays 1D/2D, imagens com NumPy, recursão,
complexidade e algoritmos de ordenação (merge sort, quicksort, shaker sort).

### Estrutura

```
├── 01. 16 08/ ... 18. 22 11/   # uma pasta por aula (data), com pré-aula, aula e exercícios
├── classes/                    # estruturas implementadas ao longo do curso (Pilha, Fila, Array1D/2D/3D, NPImagem...)
├── provas/                     # resolução de prova antiga usada para estudo
└── images/                     # imagens usadas nos exercícios com NumPy
```

### Como usar

```bash
git clone https://github.com/tofolo17/MAC0122-files.git
cd MAC0122-files
pip install -r requirements.txt

pytest                                        # roda os testes das classes
PYTHONPATH=. python "06. 20 09/Aula/main.py"  # exercícios que usam classes/ devem rodar da raiz
```

No Windows (PowerShell), troque o `PYTHONPATH=.` por `$env:PYTHONPATH="."` antes do comando.

### Licença

[MIT](LICENSE)

---

## What will you find in this repository?

Theoretical material and solutions to the exercises prepared by the professors of MAC0122 (Principles of Algorithm
Design), offered every semester by the Computer Science Department at IME-USP.
Check the course outline [here](https://portalservicos.usp.br/jupiterweb/obterDisciplina?nomdis=&sgldis=MAC0122).

Taken in the **second semester of 2022**. Topics range from stacks and queues to 1D/2D arrays, images with NumPy,
recursion, complexity and sorting algorithms (merge sort, quicksort, shaker sort).

### Structure

```
├── 01. 16 08/ ... 18. 22 11/   # one folder per class (date), with pre-class, class and exercises
├── classes/                    # data structures built during the course (Stack, Queue, Array1D/2D/3D, NPImage...)
├── provas/                     # solution of a past exam used for study
└── images/                     # images used in the NumPy exercises
```

### How to use

```bash
git clone https://github.com/tofolo17/MAC0122-files.git
cd MAC0122-files
pip install -r requirements.txt

pytest                                        # runs the class tests
PYTHONPATH=. python "06. 20 09/Aula/main.py"  # exercises that use classes/ must run from the root
```

On Windows (PowerShell), replace `PYTHONPATH=.` with `$env:PYTHONPATH="."` before the command.

### License

[MIT](LICENSE)
