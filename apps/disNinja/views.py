from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("No ninjas here!")

def ninjas(request):
	return render(request, "index.html")

def turtle(request, tt):
	tpic = {
		"red" : "{% static 'images/red.jpg' %}",
		"blue" : "{% static 'images/blue.jpg' %}",
		"purple" : "{% static 'images/purple.jpg' %}",
		"orange" : "{% static 'images/orange.jpg' %}"
	}

	try:
		context = { "images": tpic[tt] }
	except:
		context = { "images": "{% static 'images/megan.jpeg' %}" }

	return render(request, "turtle.html" , context)