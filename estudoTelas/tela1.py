from flet import Page,app,TextField,ElevatedButton,ResponsiveRow,WEB_BROWSER,MainAxisAlignment

btnsInputs={"":12,"sm":6,"md":4,"lg":2}

def minhaAplicacao(page:Page):
    page.title="Tela Cadastro"
    inputName=TextField(col=btnsInputs,label="Digite o seu nome")
    inputIdade=TextField(col={"sm":4,"md":2},label=" Digite a sua Idade")
    inputCPF = TextField( col=btnsInputs,label=" Digite a seu CPF")
    btnRegister=ElevatedButton("Cadastrar")

    responsiveLine=ResponsiveRow(controls=[inputName,inputIdade,inputCPF],alignment=MainAxisAlignment.CENTER)
    page.add(responsiveLine,btnRegister)

    page.update()


app(target=minhaAplicacao)