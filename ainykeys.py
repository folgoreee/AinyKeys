from tkinter import *
from tkinter import messagebox
import secrets
import string
import math

# ============================ 
# CONFIGURAÇÕES 
# ============================
TAMANHO_MIN = 8
TAMANHO_MAX = 128

janela = Tk()
janela.title("AinyKeys")
janela.geometry("700x750")
cor_fundo = "#360b41"
janela.configure(bg=cor_fundo)

# ============================ 
# FUNÇÕES 
# ============================

def classificar_forca(bits):
    if bits < 28:
        return "Muito fraca", "#ff4d4d"
    elif bits < 36:
        return "Fraca", "#ff944d"
    elif bits < 60:
        return "Razoável", "#ffd24d"
    elif bits < 128:
        return "Forte", "#9be15d"
    else:
        return "Muito forte", "#2ecc71"


def calcular_entropia(tamanho, pool_size):
    if pool_size == 0:
        return 0
    return tamanho * math.log2(pool_size)


# Tira Caracteres que se parecem: 1, l, I, 0, O
def remover_ambiguos(conjunto):
    ambiguos = "1lI0O"
    return "".join(c for c in conjunto if c not in ambiguos)


def gerar_senha():
    try:
        tamanho = int(caixa_tamanho.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho.")
        return

    if tamanho < TAMANHO_MIN or tamanho > TAMANHO_MAX:
        messagebox.showerror("Erro",
                             f"O tamanho deve estar entre {TAMANHO_MIN} e {TAMANHO_MAX} caracteres.")
        return

    conjunto = ""
    if var_maiusculas.get():
        conjunto += string.ascii_uppercase
    if var_minusculas.get():
        conjunto += string.ascii_lowercase
    if var_numeros.get():
        conjunto += string.digits
    if var_simbolos.get():
        conjunto += string.punctuation

    if conjunto == "":
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
        return

    if var_remover_ambiguos.get():
        conjunto = remover_ambiguos(conjunto)
        if len(conjunto) < 2:
            messagebox.showerror("Erro",
                                 "Poucos caracteres após remover os ambíguos.\n"
                                 "Marque mais tipos de caractere.")
            return

    senha = "".join(secrets.choice(conjunto) for _ in range(tamanho))

    bits = calcular_entropia(tamanho, len(conjunto))
    forca, cor = classificar_forca(bits)

    caixa_senha.config(state="normal")
    caixa_senha.delete(0, END)
    caixa_senha.insert(0, senha)
    caixa_senha.config(state="readonly")

    label_entropia.config(text=f"Entropia: {bits:.1f} bits   |   Força: {forca}", fg=cor)

    print("=" * 50)
    print(f"Senha: {senha}")
    print(f"Tamanho: {tamanho}  |  Conjunto: {len(conjunto)} símbolos")
    print(f"Entropia: {bits:.2f} bits  |  Força: {forca}")
    if var_remover_ambiguos.get():
        print("Ambíguos removidos")
    print("=" * 50)


def copiar_senha():
    senha = caixa_senha.get()
    if senha == "":
        messagebox.showwarning("Aviso", "Gere uma senha antes de copiar.")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    janela.update()
    label_copiado.config(text="Senha copiada!")
    janela.after(2000, lambda: label_copiado.config(text=""))


# ====================== 
# INTERFACE 
# ======================

titulo = Label(janela, text="AinyKeys", font="Arial 30 bold", fg="white", bg=cor_fundo)
titulo.place(relx=0.5, y=40, anchor=CENTER)

subtitulo = Label(janela, text="Gere suas próprias senhas", font="Arial 14",
                  fg="#cfa6d6", bg=cor_fundo)
subtitulo.place(relx=0.5, y=80, anchor=CENTER)

# TAMANHO
label_tamanho = Label(janela, text="Tamanho da senha:", font="Arial 16", fg="white", bg=cor_fundo)
label_tamanho.place(x=50, y=140)

caixa_tamanho = Entry(janela, font="Arial 16", width=6, justify="center")
caixa_tamanho.insert(0, "16")
caixa_tamanho.place(x=320, y=140)

label_intervalo = Label(janela, text=f"(entre {TAMANHO_MIN} e {TAMANHO_MAX})",
                        font="Arial 11", fg="#cfa6d6", bg=cor_fundo)
label_intervalo.place(x=420, y=145)

# ============================ 
# OPÇÕES DE CARACTERES 
# ============================

var_maiusculas = BooleanVar(value=True)
var_minusculas = BooleanVar(value=True)
var_numeros = BooleanVar(value=True)
var_simbolos = BooleanVar(value=True)
var_remover_ambiguos = BooleanVar(value=False)

check_style = {
    "font": "Arial 14",
    "fg": "white",
    "bg": cor_fundo,
    "selectcolor": cor_fundo,
    "activebackground": cor_fundo,
    "activeforeground": "white"
}

check_maiusculas = Checkbutton(janela, text="Letras maiúsculas (A-Z)", variable=var_maiusculas, **check_style)
check_maiusculas.place(x=50, y=200)

check_minusculas = Checkbutton(janela, text="Letras minúsculas (a-z)", variable=var_minusculas, **check_style)
check_minusculas.place(x=50, y=240)

check_numeros = Checkbutton(janela, text="Números (0-9)", variable=var_numeros, **check_style)
check_numeros.place(x=50, y=280)

check_simbolos = Checkbutton(janela, text="Símbolos (!@#$%...)", variable=var_simbolos, **check_style)
check_simbolos.place(x=50, y=320)

check_remover_ambiguos = Checkbutton(janela, text="Remover caracteres ambíguos (1, l, I, 0, O)",
                                     variable=var_remover_ambiguos, **check_style)
check_remover_ambiguos.place(x=50, y=360)

# ============================ 
# GERAÇÃO E EXIBIÇÃO 
# ============================

botao_gerar = Button(janela, text="GERAR SENHA", font="Arial 14 bold",
                     bg="white", fg="#7d677e", width=18,
                     command=gerar_senha)
botao_gerar.place(x=50, y=420)

label_senha_titulo = Label(janela, text="Senha gerada:", font="Arial 16", fg="white", bg=cor_fundo)
label_senha_titulo.place(x=50, y=490)

caixa_senha = Entry(janela, font="Arial 16", width=30, justify="center", state="readonly")
caixa_senha.place(x=50, y=530)

botao_copiar = Button(janela, text="COPIAR", font="Arial 12 bold",
                      bg="white", fg="#7d677e", width=10,
                      command=copiar_senha)
botao_copiar.place(x=480, y=527)

label_copiado = Label(janela, text="", font="Arial 11 italic", fg="#2ecc71", bg=cor_fundo)
label_copiado.place(x=50, y=565)

# ============================ 
# FORÇA DA SENHA 
# ============================

label_entropia = Label(janela, text="Entropia: --", font="Arial 14 bold", fg="white", bg=cor_fundo)
label_entropia.place(x=50, y=610)

# ============================
# FIM 
# ============================

janela.mainloop()
