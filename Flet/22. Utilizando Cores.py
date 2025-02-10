import flet as ft

def main(page: ft.Page):
    containers = [
        ft.Container(height = 100, width = 200, bgcolor = ft.Colors.DEEP_ORANGE),
        ft.Container(height = 100, width = 200, bgcolor = "deeporange"),
        ft.Container(height = 100, width = 200, bgcolor = "#FC6238"),
        ft.Container(height = 100, width = 200, bgcolor = ft.Colors.with_opacity(0.5, ft.Colors.DEEP_ORANGE)),
        ft.Container(height = 100, width = 200, bgcolor = ft.Colors.with_opacity(0.2, "#FC6238")),
        ft.Container(height = 100, width = 200, bgcolor = ft.Colors.with_opacity(0.9, "#FC6238")),
    ]

    page.add(*containers)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
