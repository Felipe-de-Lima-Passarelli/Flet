import flet as ft
from time import sleep

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    pb1 = ft.ProgressBar(
        value = 0,
        bar_height = 50,
        color = ft.Colors.GREEN,
        bgcolor = ft.Colors.CYAN_ACCENT,
        tooltip = "Barra de Progresso"
    )

    pb2 = ft.ProgressBar(
        bar_height = 50,
    )

    page.add(pb1, pb2)

    for i in range(0, 10):
        pb1.value += 0.1
        pb1.update()
        sleep(1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
