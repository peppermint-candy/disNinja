from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("No ninjas here!")

def ninjas(request):
	return render(request, "index.html")

def turtle(request, tt):
	context = {
		"turtle" : tt
	}
	
	return render(request, "turtle.html" , context)