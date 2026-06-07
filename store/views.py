from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def offers_view(request):
    return render(request, 'offers.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def achievements_view(request):
    return render(request, 'achievements.html')

def teams_view(request):
    return render(request, 'teams.html')