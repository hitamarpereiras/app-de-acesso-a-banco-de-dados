import flet as ft
from utilils import modulo_2 as mm2
from time import sleep

def main(page: ft.Page):
    page.title= 'Login'
    page.window_width= 620
    page.window_height= 620
    page.theme_mode= ft.ThemeMode.DARK
    page.bgcolor= '#000000'
    page.horizontal_alignment= 'center'
    page.vertical_alignment= 'center'
    page.icon= './assets/user_icon.png'
    page.padding= 14

    # Adicionar cliente
    def adicionar_client(e):
        icon.visible= True
        h1.value= f'Sitema de Cadastro'
        h1.size= 28
        page.update()

        ########### FUNCAO DE ADICIONAR NOVO CLIENTE ###########
        def cadastrar(self):
            if c_name.value == '' or c_email.value == '':
                h2.visible= True
                h2.value = 'Por favor preencha os campos!'
                page.update()
                sleep(3)
                h2.visible= False
                page.update()
            elif c_senha.value == '' or c_tell.value == '':
                h2.visible= True
                h2.value = 'Por favor preencha os campos!'
                page.update()
                sleep(3)
                h2.visible= False
                page.update()
            else:
                load.width= 50
                load.src= './assets/loading.gif'
                load.visible = True
                page.update()
                sleep(5)
                load.visible = False
                cliente = mm2.Cliente(c_name.value.capitalize(), c_email.value, c_senha.value, c_tell.value)
                addc = mm2.Cliente.add_cliente(cliente)
                h2.visible= True
                h2.value = f'{addc}'
                c_name.value = ''
                c_email.value = ''
                c_senha.value = ''
                c_tell.value = ''
                page.update()
                sleep(5)
                h2.visible= False
                page.update()

        ########### LIMPAR INPUTS ###########
        def limpar_inputs(e):
            c_name.value= ''
            c_email.value= ''
            c_senha.value= ''
            c_tell.value= ''
            page.update()

        ########### MUDAR A COR DOS INPUTS P/ VERMELHO ###########
        def mudar_cor_inputs_V(e):
            c_name.color= '#e6324b'
            c_senha.color= '#e6324b'
            c_email.color= '#e6324b'
            c_tell.color= '#e6324b'
            c_name.border_color= '#e6324b'
            c_senha.border_color= '#e6324b'
            c_email.border_color= '#e6324b'
            c_tell.border_color= '#e6324b'
            page.update()

        ########### MUDAR A COR DOS INPUTS P/ NORMAL ###########
        def mudar_cor_inputs_N(e):
            c_name.color= '#ffffff'
            c_senha.color= '#ffffff'
            c_email.color= '#ffffff'
            c_tell.color= '#ffffff'
            c_name.border_color= '#17ffee'
            c_senha.border_color= '#17ffee'
            c_email.border_color= '#17ffee'
            c_tell.border_color= '#17ffee'
            page.update()

        ########### MUDAR A COR DOS INPUTS P/ VERDE ###########
        def mudar_cor_inputs_Verdes(e):
            c_name.color= '#17ffee'
            c_senha.color= '#17ffee'
            c_email.color= '#17ffee'
            c_tell.color= '#17ffee'
            page.update()

        ########### MENU EDITAR ###########
        def menu_editar_cliente(e):
            c_id.visible= True
            btn3.visible= True
            btn4.visible= True
            btn5.visible= True
            page.update()

        ########### PROCUAR CLIENTE POR ID ###########
        def procurar(e):
            client = mm2.procuar_clientes(c_id.value)
            if client:
                c_name.value= f'{client[1]}'
                c_email.value= f'{client[2]}'
                c_senha.value= f'{client[3]}'
                c_tell.value= f'{client[4]}'
                page.update()
            else:
                h2.value= 'Nenhum cliente com esse ID foi encontrado!'
                h2.visible= True
                page.update()
                sleep(5)
                limpar_inputs(e)
                h2.value= ''
                h2.visible= False
                page.update()

        ########### EXCLUIR CLIENTE POR ID ###########
        def excluir(e):
            if c_id.value == '':
                h2.value = 'Por favor preencha o campo com o ID!'
                page.update()
                sleep(3)
            else:
                delete = mm2.deletar_cliente(c_id.value)
                sleep(2)
                if delete == True:
                    mudar_cor_inputs_V(e)
                    h2.value = f'Esse Cliente foi DELETADO!'
                    h2.visible = True
                    page.update()
                    sleep(3)
                    mudar_cor_inputs_N(e)
                    limpar_inputs(e)
                    h2.visible = False
                    page.update()
                else:
                    h2.value= f'{delete}'
                    page.update()

        ########### ATUALIZAR CLIENTE POR ID ###########
        def editar_cliente(e):
            up = mm2.atualizar_cliente(c_id.value, c_name.value, c_email.value, c_senha.value, c_tell.value)
            if up:
                icon_all.src= './assets/confirme.gif'
                icon_all.visible= True
                h2.value= 'Dados atualizados com sucesso!'
                h2.color= '#17ffee'
                h2.visible= True
                mudar_cor_inputs_Verdes(e)
                page.update()
                sleep(6)
                h2.visible= False
                h2.color= '#ffffff'
                icon_all.visible= False
                mudar_cor_inputs_N(e)
                page.update()
            else:
                h2.value= 'Ops! Algo deu ERRADO.'
                h2.visible= True
                page.update()
                sleep(5)
                h2.visible= False
                page.update()

        ########### INPUT ID ###########
        c_id = ft.TextField(
            label= 'ID',
            visible= False,
            width= 60,
            height= 40,
            color= '#e6324b',
            cursor_height= 15,
            cursor_color= '#e6324b',
            border_width= 2,
            border_radius= 24,
            border_color= '#17ffee',
            focused_border_color= '#e6324b'
        )

        ########### INPUT NAME ###########
        c_name = ft.TextField(
                width= 230,
                height= 80,
                color= '#ffffff',
                border_width= 2,
                border_radius= 24,
                border_color= '#17ffee',
                focused_border_color= '#e6324b',
                visible= True
                )
        
        ########### INPUT EMAIL ###########
        c_email = ft.TextField(
                width= 230,
                height= 80,
                color= '#ffffff',
                border_width= 2,
                border_radius= 24,
                border_color= '#17ffee',
                focused_border_color= '#e6324b',
                visible= True
                )
        
        ########### INPUT SENHA ###########
        c_senha = ft.TextField(
                width= 230,
                height= 80,
                color= '#ffffff',
                border_width= 2,
                border_radius= 24,
                password= True,
                can_reveal_password= True,
                border_color= '#17ffee',
                focused_border_color= '#e6324b',
                visible= True
                )
        
        ########### INPUT TELEFONE ###########
        c_tell = ft.TextField(
                width= 230,
                height= 80,
                color= '#ffffff',
                border_width= 2,
                border_radius= 24,
                border_color= '#17ffee',
                focused_border_color= '#e6324b',
                visible= True
                )
        
        ########### BOTOES ###########
        btn = ft.ElevatedButton(
                text= 'CADASTRAR',
                width= 140,
                height= 40,
                bgcolor= '#17ffee',
                color= '#3d423c',
                on_click= cadastrar,
                visible= True
                )
        btn2 = ft.ElevatedButton(
                text= 'EDITAR',
                width= 100,
                height= 40,
                bgcolor= '#bdbdbd',
                color= '#404040',
                on_click= menu_editar_cliente,
                visible= True
                )
        btn3 = ft.ElevatedButton(
                text= 'PROCURA',
                width= 115,
                height= 40,
                bgcolor= '#bdbdbd',
                color= '#404040',
                on_click= procurar,
                visible= False
                )
        btn4 = ft.ElevatedButton(
                text= 'EXCLUIR',
                width= 115,
                height= 40,
                bgcolor= '#e6324b',
                color= '#404040',
                on_click= excluir,
                visible= False
                )
        btn5 = ft.ElevatedButton(
                text= 'ATUALIZAR',
                width= 122,
                height= 40,
                bgcolor= '#17ffee',
                color= '#404040',
                on_click= editar_cliente,
                visible= False
                )
        
        page.add(
            ft.ResponsiveRow([
                ######### AQUI E ONDE APARECE O MENU EDITAR ########
                ft.Row([
                    c_id,
                    btn3,
                    btn4,
                    btn5
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column(
                    spacing=4,
                    col={"sm": 4, "md": 5, "xl": 3},
                    controls=[
                        ft.Text('Nome', text_align='left', color='#17ffee'),
                        c_name,
                        ft.Text('Email', text_align='left', color='#17ffee'),
                        c_email,
                        btn
                        ]
                ),
                ft.Column(
                    spacing=4,
                    col={"sm": 4, "md": 5, "xl": 3},
                    controls=[
                        ft.Text('Senha', text_align='left', color='#17ffee'),
                        c_senha,
                        ft.Text('Telefone', text_align='left', color='#17ffee'),
                        c_tell,
                        btn2
                        ]
                ),

            ],alignment=ft.MainAxisAlignment.CENTER)

        )

    # Login do usuario
    def login_user(e):
        if user.value == '' or passw.value == '':
            h2.visible= True
            h2.value = 'Por favor preencha os campos!'
            page.update()
            sleep(3)
            h2.visible= False
            page.update()
        elif user.value and passw.value:
            res = mm2.acesso_ao_sistema(user.value.capitalize(), passw.value)
            if res == True:
                user.visible= False
                passw.visible= False
                icon.visible= False
                load.visible= True
                btn_confirm.visible= False
                page.update()
                sleep(5)
                load.visible= False
                h1.value= f'{user.value.capitalize()} Seja bem vindo(a)'
                page.update()
                sleep(3)
                icon.visible= True
                adicionar_client(e)
                page.update()
                teste_de_conexao(e)
                mm2.pegar_hora(user.value)
            elif res == False:
                h2.visible= True
                h2.value= f'NOME OU SENHA INCORETO!'
                page.update()
                sleep(3)
                h2.visible= False
                page.update()
    
    # Teste de conexao
    def teste_de_conexao(e):
        if mm2.teste_conect():
            icon.width = 50
            icon.src = f'./assets/on_bd.png'
            page.update()
        else:
            icon.width = 50
            icon.src = f'./assets/off_bd.png'
            page.update()
            
    icon = ft.Image(
        src= f'./assets/load_verde.gif',
        width= 60,
        visible= True
    )

    icon_all = ft.Image(
        src= './assets/user_icon.png',
        width= 50,
        visible= False
    )

    load = ft.Image(
        src= f'./assets/load_verde.gif',
        width= 100,
        visible= False
    )

    h1 = ft.Text(
        value='L O G I N',
        size=22,
        color= '#17ffee'
    )

    h2 = ft.Text(
        value='Informações de comfirmção!',
        size=15,
        bgcolor= '',
        color= '',
        visible= False
    )

    user = ft.TextField(
        label= 'Name',
        width= 200,
        height= 90,
        color= '#ffffff',
        border_width= 2,
        border_radius= 24,
        border_color= '#17ffee',
        focused_border_color= '#17ffee',
        visible= True
    )

    passw = ft.TextField(
        label= 'Password',
        width= 200,
        height= 90,
        color= '#ffffff',
        border_radius= 24,
        border_width= 2,
        password= True,
        border_color= '#17ffee',
        focused_border_color= '#17ffee',
        can_reveal_password=True,
        visible= True
    )

    btn_confirm = ft.ElevatedButton(
        text= 'E N T E R',
        width= 200,
        height= 40,
        bgcolor= '#17ffee',
        color= '#3d423c',
        on_click= login_user,
        visible= True
    )

    page.add(
        ft.Row([
            h1, 
            icon
        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        load,
        ft.Row([
            h2,
            icon_all
        ], ft.MainAxisAlignment.CENTER),
        user,
        passw,
        btn_confirm,
    )

ft.app(target=main)