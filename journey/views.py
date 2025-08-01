from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JourneyForm
from .models import Journey, User


def journey_list(request):
    journey_list = Journey.published.all()
    paginator = Paginator(journey_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        journeys = paginator.page(page_number)
    except PageNotAnInteger:
        journeys = paginator.page(1)
    except EmptyPage:
        journeys = paginator.page(paginator.num_pages)
    return render(
        request,
        'journey/list.html',
        {
            'journeys': journeys,
            'section': 'journey_list'
        }
    )


def journey_detail(request, journey_id):
    journey = get_object_or_404(
        Journey,
        id=journey_id
    )
    return render(
        request,
        'journey/detail.html',
        {
            'journey': journey,
        }
    )


@login_required
def post_create(request):
    template = 'journey/create_journey.html'
    form = JourneyForm(request.POST or None)
    context = {
        'form': form,
        'section': 'create'
    }
    if form.is_valid():
        journey = form.save(commit=False)
        journey.author = request.user
        journey.save()
        return redirect(f'/journey/profile/{journey.author.username}/')
    return render(request, template, context)


def profile(request, username):
    template = 'journey/profile.html'
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all().order_by('author')
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_number = post_list.count()
    context = {
        'page_obj': page_obj,
        'post_number': post_number,
        'author': author,
    }
    return render(request, template, context)
