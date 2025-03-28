import flet as ft

def main(page: ft.Page):
    md = ft.Markdown(
        value = """
# Esse é o título
## Subtítulo 1
### Subtítulo 2
#### Subtítulo 3
"""
)

    page.add(md)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
