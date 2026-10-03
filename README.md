# Curva de Bézier Cúbica

Trabalho da disciplina de Computação Gráfica.

## O que o programa faz

Programa em Python com interface grafica (Tkinter) que desenha uma curva de Bezier cúbica.
O usuario informa 4 pontos:

- P0 e P3: pontos de inicio e fim da curva;
- P1 e P2: pontos de controle.

E também informa quantos valores de t serão usados para calcular a curva (quanto maior, mais suave fica).

Depois de preencher os campos e clicar em "Plotar Curva", o programa calcula os pontos da curva usando a fórmula da Bézier cúbica e desenha no canvas, junto com as linhas de controle (tracejadas) e os pontos marcados.

## Como rodar

Precisa ter Python instalado (o Tkinter já vem junto na instalação padrão).

No terminal, dentro da pasta do projeto:

```
python bezier.py
```

## Arquivos

- bezier.py - código do programa

## Autor

Rafael Ienne de Morais
