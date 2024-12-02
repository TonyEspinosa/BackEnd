from django.shortcuts import render

def v_cat(request):
	return render(request,'cat.html', {})