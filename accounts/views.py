from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, LoginForm
from .models import User  # Importe seu modelo User

def signup(request):
    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':
        # Verificamos se o formulário foi enviado com os dados corretos
        form = UserForm(request.POST)
        if form.is_valid():
            # Salvar os dados do formulário no banco de dados
            form.save()
            # Redirecionar para a página de login após o cadastro
            return redirect('login')
    else:
        # Caso o formulário não tenha sido enviado com os dados corretos
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':
        # Verificamos se o formulário foi enviado com os dados corretos
        form = LoginForm(request.POST)
        if form.is_valid():
            # Recuperar os dados do formulário
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            # Autenticar o usuário com as credenciais enviadas pelo formulário
            #user = authenticate(request, email=email, password=password)

            # Verificar se o usuário existe no banco de dados
            #if user is not None:
            
            if user is not None and user.check_password(password):
                # Autentica o usuário
                # Caso a autenticação seja bem-sucedida, armazenar os dados do usuário na sessão do usuário
                login(request, user)  # Aqui está a correção
                # Redireciona para a página inicial ou outra página após o login bem-sucedido
                return redirect('home')
            else:
                # Caso as credenciais estejam incorretas
                form.add_error(None, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        # Caso o formulário não tenha sido enviado com os dados corretos
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



