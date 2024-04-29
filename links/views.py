from django.shortcuts import render, redirect
from .models import Link, Review
from .forms import ReviewForm
from statistics import median


def links_hub(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
    else:
        review_form = ReviewForm()

    links = Link.objects.all()

    links_names = list()
    for link in links:
        links_names.append(link.name)

    reviews_stars = list()
    for link_name in links_names:
        reviews = Review.objects.filter(name=link_name)

        for review in reviews:
            reviews_stars.append(review.stars)
        link = Link.objects.get(name=link_name)
        link.stars = median(reviews_stars)
        link.save(update_fields=["stars"])

    links = Link.objects.all()
    reviews = Review.objects.all()

    return render(request, 'links_hub.html', {
        'links': links,
        'review_form': review_form,
        'reviews': reviews,
    })


def main(request):
    if request.method == "POST":  # если пользователь отправил форму
        return redirect(links_hub)
    links = Link.objects.all()
    return render(request, 'main.html', {'links': links})
