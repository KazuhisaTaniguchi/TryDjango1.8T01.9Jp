from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import (
    SingUpForm,
    ContactForm,
)


def home(request):
    title = 'Wellcome'
    form = SingUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        # print request.POST['email'] not recommended
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'New full name'
        instance.full_name = full_name

        instance.save()
        context = {
            'title': 'Thank you'
        }
    return render(request, 'newsletter/home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = form_email
        contact_message = '%s: %s via %s' % (
            form_full_name, form_message, form_email)

        send_mail(
            subject,
            contact_message,
            from_email,
            [to_email],
            fail_silently=False,
        )

    context = {
        'form': form,
    }
    return render(request, 'newsletter/forms.html', context)
