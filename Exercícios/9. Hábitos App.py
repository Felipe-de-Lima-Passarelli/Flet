import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = "Hábitos App"
    page.window.width = 450
    page.window.height = 800
    page.window.resizable = False
    page.window.maximizable = False

    texto1 = ft.Container()

    texto2 = ft.Container()

    quadro_evolucao = ft.Container()

    texto3 = ft.Container()

    tarefas = ft.Container()

    novas_tarefas = ft.Container()

    page.add(
        texto1,
        texto2,
        quadro_evolucao,
        texto3,
        tarefas,
        novas_tarefas
    )

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
