from django import forms


class LoginForms(forms.Form):
        nome_login=forms.CharField(
                label='Nome de Login (seu email)', 
                required=True, 
                max_length=100,
                 widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex.: seuemail@email.com',
                }
        )
        )
        senha=forms.CharField(
                label='Senha', 
                required=True, 
                max_length=70,
                widget=forms.PasswordInput(
                        attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
                }
                )
        )
# este item esta sendo manipulado por java script
# class FilhoForm(forms.Form):
#     nome_filho = forms.CharField(
#         label='Nome do Filho',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Filho'})
#     )
    
#     idade_filho = forms.IntegerField(
#         label='Idade do Filho',
#         min_value=0,
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade do Filho'})
#     )

class CadastroForms(forms.Form):
        nome_marido=forms.CharField(
        label='Nome Marido Completo*', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
                }
            )
        )
        nome_esposa=forms.CharField(
        label='Nome Esposa Completo*', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Maria Silva',
                }
            )
        )
        email=forms.EmailField(
        label='Digite seu Email - se existir (não obrigatório)',
        required=False,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
                }
            )
        )
        celular = forms.CharField(
        label='Celular*',
        required=True,
        max_length=15,  # Ajustar para incluir formatação
        widget=forms.TextInput(  # Alterado para TextInput para aceitar o formato
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: (99) 94444-5555',
                'data-mask': '(99) 99999-9999',  # Atributo para usar com a máscara
            }
        )
    )
        numero_parcelas=forms.ChoiceField(
        label='Numero de Parcelas*',
        required=True,
        choices=[
            ("", "Selecione o número de parcelas"),  # Adiciona a opção de escolha
            ("1", "PAGAMENTO EM 1 VEZ"),
            ("2", "PAGAMENTO EM 2 VEZES"),
            ("3", "PAGAMENTO EM 3 VEZES"),
            ("4", "PAGAMENTO EM 4 VEZES"),
            ("5", "PAGAMENTO EM 5 VEZES"),
            ("6", "PAGAMENTO EM 6 VEZES"),
            ("7", "PAGAMENTO EM 7 VEZES"),
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
            )
        )

        # levar_filhos = forms.BooleanField(
        # required=False,
        # label='Levará filhos?'
        # )
    
        # filhos = forms.CharField(widget=forms.HiddenInput())  # Placeholder for dynamic fields

        # para criacao de senha no forma [desativado]
        # senha_1=forms.CharField(
        # label='Senha', 
        # required=True, 
        # max_length=70,
        # widget=forms.PasswordInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Digite sua senha',
        #         }
        #     ),
        # )
        # senha_2=forms.CharField(
        # label='Senha', 
        # required=True, 
        # max_length=70,
        # widget=forms.PasswordInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Digite sua senha novamente',
        #         }
        #     ),
        # )