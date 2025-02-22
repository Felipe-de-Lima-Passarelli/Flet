import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = "Cálculadora"
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False

    def limpar(e):
        row1.value = "0"
        row1.update()

    def trocar_sinal(e):
        if not row1.value:
            return
        if row1.value[0] == "-":
            row1.value = row1.value[1:]
        else:
            row1.value = "-" + row1.value
        row1.update()

    def porcentagem(e):
        if "/" in row1.value:
            pos = row1.value.index("/")
            numero = str((int(row1.value[(pos + 1):]))/100)
            row1.value = row1.value[0:pos] + "/" + numero
            row1.update()
        elif "*" in row1.value:
            pos = row1.value.index("*")
            numero = str((int(row1.value[(pos + 1):])) / 100)
            row1.value = row1.value[0:pos] + "*" + numero
            row1.update()
        elif "+" in row1.value:
            pos = row1.value.index("+")
            row1.value = str(int(row1.value[0:pos])) + "+" + str(int(row1.value[0:pos]) * int(row1.value[pos:])/100)
            row1.update()
        else:
            pos = row1.value.index("-")
            row1.value = str(int(row1.value[0:pos])) + "-" + str(int(row1.value[0:pos]) * int(row1.value[pos:]) / 100)
            row1.update()

    def numero(e):
        if row1.value == "0":
            row1.value = ""
            row1.update()
        row1.value += e.control.content.content.value
        row1.update()

    def operador(e):
        if row1.value[-1] not in ("/", "*", "+", "-"):
            row1.value += e.control.content.content.value
            row1.update()
        else:
            row1.value = row1.value[0:-1] + e.control.content.content.value
            row1.update()

    def igual(e):
        row1.value = str(eval(row1.value))
        row1.update()

    row1 = ft.TextField(
        value = "0",
        disabled = True,
        text_size = 40,
        text_align = ft.TextAlign.RIGHT,
        expand = True,
        border = ft.InputBorder.NONE
    )

    row2 = ft.Row(
        controls = [
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "AC", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = limpar,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor=ft.Colors.BLUE_GREY_100,
                    radius=40,
                    content=ft.Text(value = "±", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = trocar_sinal,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor=ft.Colors.BLUE_GREY_100,
                    radius=40,
                    content=ft.Text(value = "%", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = porcentagem,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor=ft.Colors.ORANGE,
                    radius=40,
                    content=ft.Text(value = "/", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = operador,
                expand = True
            )
        ]
    )

    row3 = ft.Row(
        controls = [
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "7", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "8", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "9", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.ORANGE,
                    radius = 40,
                    content = ft.Text(value = "*", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = operador,
                expand = True
            )
        ]
    )

    row4 = ft.Row(
        controls = [
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "4", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "5", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "6", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.ORANGE,
                    radius = 40,
                    content = ft.Text(value = "-", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = operador,
                expand = True
            )
        ]
    )

    row5 = ft.Row(
        controls = [
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "1", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "2", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "3", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.ORANGE,
                    radius = 40,
                    content = ft.Text(value = "+", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = operador,
                expand = True
            )
        ]
    )

    row6 = ft.Row(
        controls = [
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLACK,
                    radius = 40,
                    disabled = True
                ),
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = "0", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.BLUE_GREY_100,
                    radius = 40,
                    content = ft.Text(value = ".", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = numero,
                expand = True
            ),
            ft.Container(
                ft.CircleAvatar(
                    bgcolor = ft.Colors.ORANGE,
                    radius = 40,
                    content = ft.Text(value = "=", size = 25, color = ft.Colors.BLACK)
                ),
                on_click = igual,
                expand = True
            )
        ]
    )

    page.add(
        row1,
        row2,
        row3,
        row4,
        row5,
        row6
    )

ft.app(target = main, assets_dir ="../Arquivos_Úteis") #Inicializar o App com a função Main
                                                     #view = ft.AppView.WEB_BROWSER (Inicializar no navegador)
