from django.shortcuts import render
from .forms import SingUpForm


def home(request):
    title = 'Wellcome'
    if request.user.is_authenticated():
        title = "My Title %s" % (request.user)
    context = {
        'template_title': title,
    }
    return render(request, 'newsletter/home.html', context)
