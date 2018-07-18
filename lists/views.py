from django.shortcuts import render

def home_page(request):
  # render() automatically searches folders called 'templates' in any 
  # of your apps' directories
  return render(request, 'home.html')
