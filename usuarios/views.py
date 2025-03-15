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
                cpf_marido  = form.cleaned_data.get('cpf_marido')
                dt_nasc_marido = form.cleaned_data.get('dt_nasc_marido')
                nome_esposa = form.cleaned_data.get('nome_esposa')
                cpf_esposa  = form.cleaned_data.get('cpf_esposa')
                dt_nasc_esposa = form.cleaned_data.get('dt_nasc_esposa')
                email       = form.cleaned_data.get('email')
                celular     = form.cleaned_data.get('celular')
                numero_parcelas = form.cleaned_data.get('numero_parcelas')

                 # Criação do objeto Cadastro e salvando no banco
                cadastro = Cadastro.objects.create(
                    nome_marido=nome_marido,
                    cpf_marido=cpf_marido,
                    dt_nasc_marido=dt_nasc_marido,
                    nome_esposa=nome_esposa,
                    cpf_esposa=cpf_esposa,
                    dt_nasc_esposa=dt_nasc_esposa,
                    email=email,
                    celular=celular,
                    numero_parcelas=numero_parcelas
                )

                # Captura e conversão da quantidade de filhos
                qtd_filhos_str = request.POST.get('qtdFilhos', '0')
                try:
                    qtd_filhos = int(qtd_filhos_str)
                except ValueError:
                    qtd_filhos = 0

                # Itera para criar cada registro de Filho associado ao cadastro
                for i in range(1, qtd_filhos + 1):
                    # Obtém os campos dos filhos enviados através dos inputs nomeados dinamicamente
                    nome_filho = request.POST.get(f'nomeFilho{i}', '').strip()
                    idade_filho_str = request.POST.get(f'idadeFilho{i}', '').strip()

                    if nome_filho and idade_filho_str:
                        try:
                            idade_filho = int(idade_filho_str)
                        except ValueError:
                            print(f"Erro ao converter idade para o filho {i}: valor inválido")
                            continue  # Pula para o próximo filho se a conversão falhar

                        Filho.objects.create(
                            cadastro=cadastro,  # Associa o filho ao cadastro criado
                            nome=nome_filho,
                            idade=idade_filho
                        )

                return redirect('index')

            except Exception as e:
                print(f"Erro ao salvar: {str(e)}")
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})


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