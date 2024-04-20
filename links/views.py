from django.shortcuts import render, redirect
from .models import Link


def links_hub(request):
    links = Link.objects.all()
    return render(request, 'links_hub.html', {'links': links})


def main(request):
    if request.method == "POST":  # если пользователь отправил форму
        return redirect(links_hub)
    print(request)
    return render(request, 'main.html')
