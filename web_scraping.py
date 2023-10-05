import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
import pandas as pd
from time import sleep

# Variável global para rastrear a janela atual
current_window = None


def avancar_window(window):
    window.destroy()
    messagebox.showinfo('Mensagem', 'Você será redirecionado para "SITE".')


def open_analise_window():
    global current_window

    # Verifica se já existe uma janela secundária aberta e fecha-a
    if current_window:
        current_window.destroy()

    # Criando janela secundária para Análise de Mercado
    current_window = tk.Toplevel(janela)
    current_window.title('Análise de Mercado')
    current_window.geometry('300x250')

    # Adicionando orientação ao usuário
    orientacao_label = tk.Label(current_window, text='Selecione as opções desejadas:')
    orientacao_label.pack(pady=10)

    # Adicionando caixas de seleção
    checkbox1 = tk.Checkbutton(current_window, text='Apenas realizar download localmente.')
    checkbox1.pack()

    checkbox2 = tk.Checkbutton(current_window, text='Realizar download e vizualizar arquivo.')
    checkbox2.pack()

    # Criando um Frame para os botões de navegação
    button_frame = tk.Frame(current_window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Botão de Retroceder
    retroceder_button = tk.Button(button_frame, text='Retroceder para Principal', command=close_current_window)
    retroceder_button.pack(side=tk.LEFT)

    # Botão de Avançar (simétrico à direita)
    avancar_button = tk.Button(button_frame, text='Avançar', command=lambda: avancar_window(current_window))
    avancar_button.pack(side=tk.RIGHT)


def open_precos_window():
    global current_window
    # Verifica se já existe uma janela secundária aberta e fecha-a
    if current_window:
        current_window.destroy()
    # Criando janela secundária para Monitoramento de Preços
    current_window = tk.Toplevel(janela)
    current_window.title('Monitoramento de Preços')
    current_window.geometry('300x250')

    # Adicionando orientação ao usuário
    orientacao_label = tk.Label(current_window, text='Selecione as opções desejadas:')
    orientacao_label.pack(pady=10)

    # Adicionando caixas de seleção
    checkbox1 = tk.Checkbutton(current_window, text='Apenas realizar download localmente.')
    checkbox1.pack()

    checkbox2 = tk.Checkbutton(current_window, text='Realizar download e vizualizar arquivo.')
    checkbox2.pack()

    # Criando um Frame para os botões de navegação
    button_frame = tk.Frame(current_window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Botão de Retroceder
    retroceder_button = tk.Button(button_frame, text='Retroceder para Principal', command=close_current_window)
    retroceder_button.pack(side=tk.LEFT)

    # Botão de Avançar (simétrico à direita)
    avancar_button = tk.Button(button_frame, text='Avançar', command=lambda: avancar_window(current_window))
    avancar_button.pack(side=tk.RIGHT)


def open_cot_window():
    global current_window
    # Verifica se já existe uma janela secundária aberta e fecha-a
    if current_window:
        current_window.destroy()
    # Criando janela secundária para Pesquisar Cotações de Moeda
    current_window = tk.Toplevel(janela)
    current_window.title('Pesquisar Cotações de Moeda')
    current_window.geometry('300x250')

    # Adicionando orientação ao usuário
    orientacao_label = tk.Label(current_window, text='Selecione as opções desejadas:')
    orientacao_label.pack(pady=10)

    # Adicionando caixas de seleção
    checkbox1 = tk.Checkbutton(current_window, text='Apenas realizar download localmente.')
    checkbox1.pack()

    checkbox2 = tk.Checkbutton(current_window, text='Realizar download e vizualizar arquivo.')
    checkbox2.pack()

    # Criando um Frame para os botões de navegação
    button_frame = tk.Frame(current_window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Botão de Retroceder
    retroceder_button = tk.Button(button_frame, text='Retroceder para Principal', command=close_current_window)
    retroceder_button.pack(side=tk.LEFT)

    # Botão de Avançar (simétrico à direita)
    avancar_button = tk.Button(button_frame, text='Avançar', command=lambda: avancar_window(current_window))
    avancar_button.pack(side=tk.RIGHT)


def close_current_window():
    global current_window
    if current_window:
        current_window.destroy()
    current_window = None


# Criando Janela Principal
janela = tk.Tk()
janela.title('Web Scraping')
janela.geometry('360x400')

# Centralizando orientação de texto usando pack
texto_orientacao = tk.Label(janela, text='Escolha qual dado deseja buscar na Web:')
texto_orientacao.pack(pady=10)  # Adicionamos pady para espaçamento vertical

# Centralizando os botões usando pack
botao = tk.Button(janela, text='Análise de Mercado', command=open_analise_window)
botao.pack(pady=5)  # Adicionamos pady para espaçamento vertical

botao_2 = tk.Button(janela, text='Monitoramento de Preços', command=open_precos_window)
botao_2.pack(pady=5)  # Adicionamos pady para espaçamento vertical

botao_3 = tk.Button(janela, text='Pesquisar Cotações de Moeda', command=open_cot_window)
botao_3.pack(pady=5)  # Adicionamos pady para espaçamento vertical

janela.mainloop()
