import flet as ft

def main(page: ft.Page):
    dd = ft.Dropdown(
        label = "Selecione uma opção",
        options = [
            ft.dropdown.Option(text = "Opção 1", key = "1"),
            ft.dropdown.Option(text = "Opção 2", key = "2"),
            ft.dropdown.Option(text = "Opção 3", key = "3"),
            ft.dropdown.Option(text = "Opção 4", key = "4"),
            ft.dropdown.Option(text = "Opção 5", key = "5", disabled = True)
        ],
        value = "3" #Colocará a opção com a Key "3" como padrão
    )

    page.add(dd)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
