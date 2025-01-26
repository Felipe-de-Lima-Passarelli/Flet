import flet as ft

def main(page: ft.Page):
    page.title = "Início dos estudos em Flet" #Título do App

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Centraliza horizontalmente
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER # Centraliza verticalmente

    #page.padding = 20 (Espaçamento igual para todas direções)
    page.padding = ft.padding.only(top = 30, right = 100, bottom = 50, left = 10)
    page.spacing = 10 #Espaçamento entre elementos

    mensagem = ft.Text(value="Olá, seja bem vindo, essa é minha primeira interface no FLET!", size = 30)

    page.add( #Adicionar os elementos no App
        mensagem,
        ft.Container(ft.Text(value="Nome: Felipe de Lima Passarelli")),
        ft.Text(value="Curso: Análise e Desenvolvimento de Sistemas"),
        ft.Text(value="Curso em Andamento")
    )

    page.update() #Atualizar as mudanças do App

ft.app(target=main) #Inicializar o App com a função Main
