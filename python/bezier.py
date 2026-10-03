import tkinter as tk
largura = 800
altura = 550

janela = tk.Tk()
janela.title("Curva de Bezier Cubica")

label1 = tk.Label(janela, text="P0 (x, y):")
label1.grid(row=0, column=0)
p0x = tk.Entry(janela, width=5)
p0x.grid(row=0, column=1)
p0x.insert(0, "100")
p0y = tk.Entry(janela, width=5)
p0y.grid(row=0, column=2)
p0y.insert(0, "450")

label2 = tk.Label(janela, text="P1 (x, y) - controle:")
label2.grid(row=1, column=0)
p1x = tk.Entry(janela, width=5)
p1x.grid(row=1, column=1)
p1x.insert(0, "150")
p1y = tk.Entry(janela, width=5)
p1y.grid(row=1, column=2)
p1y.insert(0, "100")

label3 = tk.Label(janela, text="P2 (x, y) - controle:")
label3.grid(row=2, column=0)
p2x = tk.Entry(janela, width=5)
p2x.grid(row=2, column=1)
p2x.insert(0, "650")
p2y = tk.Entry(janela, width=5)
p2y.grid(row=2, column=2)
p2y.insert(0, "100")

label4 = tk.Label(janela, text="P3 (x, y):")
label4.grid(row=3, column=0)
p3x = tk.Entry(janela, width=5)
p3x.grid(row=3, column=1)
p3x.insert(0, "700")
p3y = tk.Entry(janela, width=5)
p3y.grid(row=3, column=2)
p3y.insert(0, "450")

label5 = tk.Label(janela, text="Numero de pontos t:")
label5.grid(row=4, column=0)
campo_t = tk.Entry(janela, width=5)
campo_t.grid(row=4, column=1)
campo_t.insert(0, "100")

canvas = tk.Canvas(janela, width=largura, height=altura, bg="white")
canvas.grid(row=5, column=0, columnspan=3, pady=10)

def desenhar():
    canvas.delete("all")

    x0 = float(p0x.get())
    y0 = float(p0y.get())
    x1 = float(p1x.get())
    y1 = float(p1y.get())
    x2 = float(p2x.get())
    y2 = float(p2y.get())
    x3 = float(p3x.get())
    y3 = float(p3y.get())

    qtd_t = int(campo_t.get())

    # calcula os pontos da curva usando a formula da bezier cubica
    pontos_x = []
    pontos_y = []
    t = 0
    while t <= qtd_t:
        t_norm = t / qtd_t

        x = ((1 - t_norm) ** 3) * x0 + 3 * ((1 - t_norm) ** 2) * t_norm * x1 + 3 * (1 - t_norm) * (t_norm ** 2) * x2 + (t_norm ** 3) * x3
        y = ((1 - t_norm) ** 3) * y0 + 3 * ((1 - t_norm) ** 2) * t_norm * y1 + 3 * (1 - t_norm) * (t_norm ** 2) * y2 + (t_norm ** 3) * y3

        pontos_x.append(x)
        pontos_y.append(y)

        t = t + 1

    # liga os pontos calculados com linhas pra formar a curva
    i = 0
    while i < len(pontos_x) - 1:
        canvas.create_line(pontos_x[i], pontos_y[i], pontos_x[i + 1], pontos_y[i + 1], fill="blue", width=2)
        i = i + 1

    # desenha os pontos de inicio/fim em vermelho
    canvas.create_oval(x0 - 4, y0 - 4, x0 + 4, y0 + 4, fill="red")
    canvas.create_oval(x3 - 4, y3 - 4, x3 + 4, y3 + 4, fill="red")

    # desenha os pontos de controle em verde
    canvas.create_oval(x1 - 4, y1 - 4, x1 + 4, y1 + 4, fill="green")
    canvas.create_oval(x2 - 4, y2 - 4, x2 + 4, y2 + 4, fill="green")

botao = tk.Button(janela, text="Plotar Curva", command=desenhar)
botao.grid(row=6, column=0, columnspan=3, pady=5)

desenhar()

janela.mainloop()
