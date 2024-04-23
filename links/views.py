from django.shortcuts import render, redirect
from .models import Link, Review
from .forms import ReviewForm


def links_hub(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            name = review_form.cleaned_data.get('name')
            review = review_form.cleaned_data.get('review')
            link = Link.objects.filter(name=name).first()
            if link is not None:
                link.reviews.append(review)
                link.save()
    else:
        review_form = ReviewForm()
    links = Link.objects.all()
    return render(request, 'links_hub.html', {
        'links': links,
        'review_form': review_form,
    })


def main(request):
    if request.method == "POST":  # если пользователь отправил форму
        return redirect(links_hub)
    return render(request, 'main.html')
