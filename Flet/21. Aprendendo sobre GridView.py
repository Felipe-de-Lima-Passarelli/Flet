import flet as ft

#Aspect Radio
#9:16 -> 0.56
#2:3 -> 0.66
#1:1 -> 1.0
#16:9 -> 1.77

def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 1000
    grid = ft.GridView(
        controls = [
            ft.Image(src = f"https://picsum.photos/250/300?{num}", fit = ft.ImageFit.COVER) for num in range(0, 20)
        ],
        runs_count = 3,
        padding = 20,
        spacing = 20, #Espaço entre linhas
        run_spacing = 20, #Espaço entre as imagens na mesma linha
        #max_extent = 100, #Máxima largura será 100 pxs
        expand = True, #Para ativar o scroll
        #height = 300, #Outra forma de ativar o scroll
        child_aspect_ratio = 0.56
    )

    page.add(grid)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
