from django.shortcuts import render, redirect


def links_hub(request):
    return render(request, 'links_hub.html')


def main(request):
    if request.method == "POST":  # если пользователь отправил форму
        return redirect(links_hub)
    print(request)
    return render(request, 'main.html')
