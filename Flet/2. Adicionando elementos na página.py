import flet as ft

def main(page: ft.Page):
    page.title = "Início dos estudos em Flet" #Título do App

    mensagem = ft.Text(value = "Olá, Mundo!")
    page.add(mensagem) #Adicionar os elementos no App

ft.app(target = main) #Inicializar o App com a função Main
