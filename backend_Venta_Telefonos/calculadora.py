import tkinter as tk
from tkinter import messagebox

# --------------------------- #
# Funciones de la calculadora
# --------------------------- #
def click(boton):
    actual = entrada.get()
    if boton == "C":
        entrada.delete(0, tk.END)
    elif boton == "=":
        try:
            expresion = entrada.get().replace("×", "*").replace("÷", "/")
            resultado = eval(expresion)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(round(resultado, 2)))
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        except Exception:
            messagebox.showerror("Error", "Entrada inválida")
    else:
        entrada.insert(tk.END, boton)

# --------------------------- #
# Función para cambiar tema
# --------------------------- #
modo_oscuro = False

def alternar_tema():
    global modo_oscuro
    modo_oscuro = not modo_oscuro

    if modo_oscuro:
        colores_tema.update({
            "fondo": "#212121",
            "entrada": "#424242",
            "texto": "white",
            "num": "#1e88e5",
            "op": "#43a047",
            "esp": "#fbc02d",
            "igual": "#f4511e",
            "boton_tema": "#616161",
            "fg_tema": "white"
        })
        boton_tema.config(text="🌞")
    else:
        colores_tema.update({
            "fondo": "#e8f0fe",
            "entrada": "white",
            "texto": "black",
            "num": "#1e88e5",
            "op": "#43a047",
            "esp": "#fbc02d",
            "igual": "#f4511e",
            "boton_tema": "#cfd8dc",
            "fg_tema": "black"
        })
        boton_tema.config(text="🌙")

    aplicar_tema()

def aplicar_tema():
    ventana.config(bg=colores_tema["fondo"])
    frame.config(bg=colores_tema["fondo"])
    entrada.config(bg=colores_tema["entrada"], fg=colores_tema["texto"])
    boton_tema.config(bg=colores_tema["boton_tema"], fg=colores_tema["fg_tema"])
    for boton in botones_gui:
        texto = boton["text"]
        if texto.isdigit() or texto == ".":
            boton.config(bg=colores_tema["num"], fg="white")
        elif texto in ["+", "-", "×", "÷"]:
            boton.config(bg=colores_tema["op"], fg="white")
        elif texto == "C":
            boton.config(bg=colores_tema["esp"], fg="black")
        else:
            boton.config(bg=colores_tema["igual"], fg="white")

# --------------------------- #
# Ventana principal
# --------------------------- #
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("350x520")
ventana.resizable(False, False)

# Centrar la ventana en la pantalla
ancho_ventana = 350
alto_ventana = 520
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Diccionario de colores
colores_tema = {
    "fondo": "#e8f0fe",
    "entrada": "white",
    "texto": "black",
    "num": "#1e88e5",
    "op": "#43a047",
    "esp": "#fbc02d",
    "igual": "#f4511e",
    "boton_tema": "#cfd8dc",
    "fg_tema": "black"
}

# --------------------------- #
# Pantalla de entrada
# --------------------------- #
entrada = tk.Entry(
    ventana,
    font=("Arial", 24),
    width=14,
    borderwidth=4,
    relief="ridge",
    justify="right",
    bg=colores_tema["entrada"],
    fg=colores_tema["texto"]
)
entrada.pack(pady=20)

# --------------------------- #
# Botones
# --------------------------- #
botones = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

frame = tk.Frame(ventana, bg=colores_tema["fondo"])
frame.pack()

botones_gui = []

for i, fila in enumerate(botones):
    for j, boton in enumerate(fila):
        if boton.isdigit() or boton == ".":
            color = colores_tema["num"]
            fg = "white"
        elif boton in ["+", "-", "×", "÷"]:
            color = colores_tema["op"]
            fg = "white"
        elif boton == "C":
            color = colores_tema["esp"]
            fg = "black"
        else:
            color = colores_tema["igual"]
            fg = "white"

        btn = tk.Button(
            frame,
            text=boton,
            font=("Arial", 16, "bold"),
            bg=color,
            fg=fg,
            width=5,
            height=2,
            relief="flat",
            command=lambda b=boton: click(b)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        botones_gui.append(btn)

# --------------------------- #
# Botón modo claro/oscuro (discreto)
# --------------------------- #
boton_tema = tk.Button(
    ventana,
    text="🌙",
    font=("Arial", 10, "bold"),
    bg=colores_tema["boton_tema"],
    fg=colores_tema["fg_tema"],
    width=4,
    height=1,
    relief="flat",
    command=alternar_tema
)
# Colocado al fondo a la derecha
boton_tema.place(x=285, y=480)

# --------------------------- #
# Aplicar tema inicial
# --------------------------- #
aplicar_tema()

# --------------------------- #
# Ejecutar aplicación
# --------------------------- #
ventana.mainloop()