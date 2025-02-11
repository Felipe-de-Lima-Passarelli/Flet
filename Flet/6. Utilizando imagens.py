import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        #src = "https://marquesfernandes.com/wp-content/uploads/2020/08/kwi4bvgzths31.jpg",
        src = "Imagens/Python.png",
        border_radius = 20,
        height = 200,
        width = 400,
        fit = ft.ImageFit.CONTAIN,
        tooltip = "Logo do Python"
        #repeat = ft.ImageRepeat.REPEAT -> Serve para repetir a imagem caso tenha espaço suficiente
    )

    page.add(img)

ft.app(target = main, assets_dir = "Arquivos_Úteis") #Inicializar o App com a função Main
