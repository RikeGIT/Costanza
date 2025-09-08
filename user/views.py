
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.shortcuts import render
import json

User = get_user_model()


@csrf_exempt
def register(request):

	
	if request.method == 'POST':
		if request.content_type == 'application/json':
			data = json.loads(request.body)
			email = data.get('email')
			password = data.get('password')
		else:
			email = request.POST.get('email')
			password = request.POST.get('password')
		if not email or not password:
			return render(request, 'register.html', {'error': 'Email e senha são obrigatórios.'})
		if User.objects.filter(email=email).exists():
			return render(request, 'register.html', {'error': 'Email já cadastrado.'})
		user = User.objects.create_user(email=email, password=password)
		return render(request, 'register.html', {'success': 'Usuário registrado com sucesso.'})
	return render(request, 'register.html')


@csrf_exempt
def user_login(request):
	if request.method == 'POST':
		if request.content_type == 'application/json':
			data = json.loads(request.body)
			email = data.get('email')
			password = data.get('password')
		else:
			email = request.POST.get('email')
			password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'login.html', {'success': 'Login realizado com sucesso.'})
		else:
			return render(request, 'login.html', {'error': 'Credenciais inválidas.'})
	return render(request, 'login.html')
