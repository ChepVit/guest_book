from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import GuestForm
from webapp.models import Guest


def guest(request, *args, **kwargs):
    guests = Guest.objects.all()
    return render(request, 'index.html', context={
        'guests': guests
    })

def guest_create(request, *args, **kwargs):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest = Guest.objects.create(
                email=form.cleaned_data['email'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            return redirect('guest')
        else:
            return render(request, 'create.html', context={'form': form})

def guest_update(request, pk):

    guest = get_object_or_404(Guest, pk=pk)

    if request.method == 'GET':

        form = GuestForm(data={

            'email': guest.email,

            'text': guest.text,

            'author': guest.author

        })

        return render(request, 'update.html', context={'form': form, 'guest': guest})

    elif request.method == 'POST':

        form = GuestForm(data=request.POST)

        if form.is_valid():

            guest.email = form.cleaned_data['email']

            guest.text = form.cleaned_data['text']

            guest.author = form.cleaned_data['author']

            guest.save()

            return redirect('guest')

        else:

            return render(request, 'update.html', context={'form': form, 'guest': guest})


def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')