from django.shortcuts import render, redirect
from . import models, forms


def create_message(request):
    form_instance = forms.MessageForm()

    if request.method == 'Message':
        form_instance = forms.MessageForm(data=request.Message)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('selecao:home')

    return render(request, 'selecao/create_message.html', {
        'form':form_instance,
    })


def show_home(request):
    """
    This view will show home page
    """

    return render(
        request=request,
        context={
            'page_title': 'home'
        },
        template_name='selecao/show_home.html'
    )


def about(request):
    return render(
        request=request,
        context={
            'page_title': 'about'
        },
        template_name='selecao/about.html'
    )


def service(request):
    return render(
        request=request,
        context={
            'page_title': 'service'
        },
        template_name='selecao/service.html'
    )