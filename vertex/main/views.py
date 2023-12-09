from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import (
    Blog, OurServices, Gallery , HomeBG, AboutUs, Icons
)
from .forms import ContactUsForm
from django.core.mail import send_mail
from vertex.settings import EMAIL_HOST_USER


class HomeListView(ListView):
    template_name = 'index.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        blogs = Blog.objects.all()
        service = OurServices.objects.get()
        galleries = Gallery.objects.all()
        home_bgs = HomeBG.objects.get()
        about_us = AboutUs.objects.get()
        icons = Icons.objects.all()  

        context = {
            "blogs":blogs,
            "service":service,
            "galleries":galleries,
            "home_bgs":home_bgs,
            "about_us" : about_us,
            "icons":icons,
        }

        return render(request , self.template_name , context=context)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            send_mail(
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                subject="Verification Letter",
                message="Thx For Review",
            )

        else:
            form = ContactUsForm()
        
        return redirect('home')