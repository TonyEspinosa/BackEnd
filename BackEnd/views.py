from django.shortcuts import render

def v_home(request):
	return render(request,'inicio.html', {})