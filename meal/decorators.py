from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home:home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('account:login')


	return wrapper_func
