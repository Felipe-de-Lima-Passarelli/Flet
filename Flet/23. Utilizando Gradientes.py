import flet as ft
from math import radians

def main(page: ft.Page):
    containers = [
        ft.Container(
            expand = True,
            gradient = ft.LinearGradient(
                colors = [ft.Colors.CYAN, ft.Colors.PURPLE],
                begin = ft.Alignment(0, -1), #Centro é (0, 0)
                end = ft.Alignment(0, 1), #Centro é (0, 0)
                stops = [0, 0.5], #Onde as cores começam
                #rotation = radians(90)
            )
        ),
        ft.Container(
            expand = True,
            gradient = ft.RadialGradient(
                colors = [ft.Colors.AMBER, ft.Colors.DEEP_ORANGE, ft.Colors.PINK],
                stops = [0, 0.5, 1],
                center = ft.Alignment(x = 0, y = -1) #Centro é (0, 0)
            )
        ),
        ft.Container(
            expand = True,
            gradient = ft.SweepGradient(
                colors = [ft.Colors.RED, ft.Colors.BLACK, ft.Colors.PINK],
                stops = [0, 0.5, 1],
                center = ft.Alignment(x = 0, y = 0),
                rotation = radians(180)
            )
        )
    ]

    page.add(*containers)

ft.app(target = main, assets_dir = "Arquivos Úteis") #Inicializar o App com a função Main
