from django.shortcuts import render

# Create your views here.
def index(request):
  """ view to render homepage """
  return render(request, 'home/index.html')