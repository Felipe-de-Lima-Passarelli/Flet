import flet as ft

def main(page: ft.Page):
    def clicar(e):
        botao_6.data += 1 #Ou e.control.data += 1
        texto.value = f"Botão acionado {botao_6.data} vez(es)"
        texto.update()
        botao_6.update()

    page.spacing = 50

    estilo_botao = ft.ButtonStyle(
        color = {
            ft.ControlState.HOVERED: ft.Colors.WHITE,
            ft.ControlState.DEFAULT: ft.Colors.BLACK,
        },
        bgcolor = {
            ft.ControlState.HOVERED: ft.Colors.PINK,
            "": ft.Colors.AMBER
        },
        padding = {
            "": 10,
            ft.ControlState.HOVERED: 20
        },
        side = {
            ft.ControlState.HOVERED: ft.BorderSide(width = 2, color = ft.Colors.BLUE),
            "": ft.BorderSide(width = 2, color = ft.Colors.BLACK)
        },
        shape = {
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius = 10),
            "": ft.BeveledRectangleBorder(radius = 15)
        },
        animation_duration = 1000, #1000 = 1 segundo
    )

    botao_1 = ft.ElevatedButton(
        text = "Clique aqui",
    )

    botao_2 = ft.ElevatedButton(
        text = "Botão inativo",
        disabled = True,
    )

    botao_3 = ft.ElevatedButton(
        text = "Botão com icone",
        icon = ft.Icons.FAVORITE,
        icon_color = ft.Colors.PINK,
    )

    botao_4 = ft.ElevatedButton(
        text = "Demais propriedades",
        bgcolor = ft.Colors.RED,
        color = ft.Colors.WHITE,
        icon = ft.Icons.FAVORITE_BORDER,
        tooltip = "Olá, eu sou um botão",
        url = "https://www.google.com"
    )

    botao_5 = ft.ElevatedButton(
        text = "Botão com estilo personalizado",
        icon = ft.Icons.GIRL,
        icon_color = ft.Colors.BLACK,
        style = estilo_botao
    )

    botao_6 = ft.ElevatedButton(
        text = "Botão com contagem de cliques",
        on_click = clicar,
        data = 0
    )

    texto = ft.Text()

    page.add(botao_1, botao_2, botao_3, botao_4, botao_5, botao_6, texto)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
