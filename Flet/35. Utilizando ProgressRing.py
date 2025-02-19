import flet as ft
from time import sleep

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    pr1 = ft.ProgressRing(
        value = 0.2,
        color = ft.Colors.GREEN,
        bgcolor = ft.Colors.GREEN_100,
        stroke_width = 20,
        tooltip = "Carregando..."
    )

    page.add(pr1)

    for i in range(0, 10):
        pr1.value += 0.1
        pr1.update()
        sleep(1)


ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
