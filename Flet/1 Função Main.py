import flet as ft

def main(page: ft.Page):
    page.title = "Início dos estudos em Flet"
    page.add(ft.Text("Bem vindo ao começo"))

ft.app(target = main)
