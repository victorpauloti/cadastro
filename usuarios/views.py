# insercao da logica de como sera o comportamento dos forms
# como o que validar, o que sera gravado no banco
from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
#from django.contrib.auth.models import User
from .models import Cadastro, Filho  # Importa os modelos

# backlog validacao se cadastro ja existe no banco de dados

def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            try:
                #print("Formulário é válido")
                # Captura os dados do formulário   
                nome_marido = form.cleaned_data.get('nome_marido')
                nome_esposa = form.cleaned_data.get('nome_esposa')
                email       = form.cleaned_data.get('email')
                celular     = form.cleaned_data.get('celular')
                numero_parcelas = form.cleaned_data.get('numero_parcelas')

                # Criação do objeto Cadastro e salvando no banco de dados
                cadastro = Cadastro.objects.create(
                nome_marido=nome_marido,
                nome_esposa=nome_esposa,
                email=email,
                celular=celular,
                numero_parcelas=numero_parcelas
                )
                #cadastro.save() # create ja salva os itens

                # Captura os dados dos filhos
                qtd_filhos = int(request.POST.get('qtdFilhos', 0))

                for i in range(1, qtd_filhos + 1):
                    nome_filho = request.POST.get(f'nomeFilho{i}')
                    idade_filho = request.POST.get(f'idadeFilho{i}')
                    
                    if nome_filho and idade_filho:
                        #try:
                            idade_filho = int(idade_filho)
                            Filho.objects.create(
                                cadastro=cadastro,
                                nome=nome_filho,
                                idade=idade_filho
                            )
                            #print(f"Filho {i} criado: {nome_filho}, {idade_filho} anos")
                        #except ValueError:
                            #print(f"Erro ao converter idade do filho {i}")
                #     else:
                #         print(f"Dados do filho {i} incompletos")

                # print("Cadastro criado com sucesso")

                return redirect('index')
            except Exception as e:
                print(f"Erro ao salvar: {str(e)}")

        else:
            print("Formulário inválido:", form.errors)
    else:
        form = CadastroForms()
    return render(request, "usuarios/cadastro.html",  {"form": form})




###### BACKLOG ##############################

    # valida se senhas sao iguais 
    #if form.is_valid():
    #     if form["senha_1"].value() != form["senha_2"].value():
    #         return redirect('cadastro')



    # cadastro para acesso ao djanto como usuario do sistema django
    # Extrai os últimos 4 dígitos do celular

    # senha = celular[-4:]  # Pega os últimos 4 caracteres

    # # verifica se o email ja esta cadastrado
    # if User.objects.filter(email=email).exists():
    #     return redirect('cadastro')

    # #criacao do usuario no django
    # usuario = User.objects.create_user(
    #     username=email,
    #     email=email,
    #     password=senha,
    # )
    # usuario.save()
    # return redirect('login')