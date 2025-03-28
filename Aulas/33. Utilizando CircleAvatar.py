import flet as ft

def main(page: ft.Page):
    av1 = ft.CircleAvatar(
        foreground_image_src = "https://felipe-de-lima-passarelli.github.io/DBD/Imagens/Personagens/10.png",
        radius = 150,
        tooltip = "Feng Min"
    )

    av2 = ft.CircleAvatar(
        bgcolor = ft.Colors.AMBER,
        color = ft.Colors.WHITE,
        content = ft.Text(value = "PA"),
        max_radius = 100,
        min_radius = 80,
        tooltip = "Usuário PA"
    )

    page.add(av1, av2)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
