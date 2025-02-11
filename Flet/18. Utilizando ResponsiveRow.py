import flet as ft

#Breakpoint       Dimension
# xs               < 576px
# sm               >= 576px
# md               >= 768px
# lg               >= 992px
# xl               >= 1200px
# xxl              >= 1400px

def main(page: ft.Page):
    rrow_1 = ft.ResponsiveRow(
        columns = 12, #Tamanho padrão total da linha
        controls = [
            ft.ElevatedButton(
                col = 4, #Tamanho total de colunas do botão
                text = "1",
                bgcolor = ft.Colors.AMBER,
                color = ft.Colors.BLACK
            ),
            ft.ElevatedButton(
                col = {"sm": 4, "md" : 3}, #Utilizando os breakpoints
                text="1",
                bgcolor=ft.Colors.AMBER,
                color=ft.Colors.BLACK
            ),
            ft.ElevatedButton(
                col = 4,
                text="1",
                bgcolor=ft.Colors.AMBER,
                color=ft.Colors.BLACK
            ),
        ]
    )

    page.add(rrow_1)

ft.app(target = main, assets_dir = "../Arquivos_Úteis") #Inicializar o App com a função Main
