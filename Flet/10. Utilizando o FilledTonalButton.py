import flet as ft

def main(page: ft.Page):
    botao_1 = ft.FilledTonalButton(
        text = "Botão secundário"
    )

    bota_2 = ft.FilledTonalButton(
        text = "Botão secundário"
    )

    page.add(
        botao_1,
        ft.FilledTonalButton(text="Botão secundário"),
        ft.FilledTonalButton(text="Botão secundário desabilitado", disabled = True),
        ft.FilledTonalButton(text="Botão secundário com icone", icon = ft.Icons.ADD),
        ft.FilledTonalButton(text="Botão secundário com icone colorido", icon = ft.Icons.ADD, icon_color = ft.Colors.GREEN),
        ft.FilledTonalButton(text="Botão secundário com tooltip", tooltip = "Ação não permitida", disabled = True),
        ft.FilledTonalButton(text = "Botão secundário com estilo", style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius = 0)))
    )

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
