import flet as ft

def main(page: ft.Page):
    botao_1 = ft.ElevatedButton(
        text = "Clique aqui"
    )

    page.add(botao_1)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
