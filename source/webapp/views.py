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
#
#
# def guest_update(request, pk):
#     guest = get_object_or_404(Guest, pk=pk)
#     if request.method == 'GET':
#         form = GuestForm()
#         return render(request, 'update.html', context={'guest': guest, 'form': form})
#     elif request.method == 'POST':
#         guest.email = request.POST.get('email')
#         guest.author = request.POST.get('author')
#         guest.text = request.POST.get('text')
#
#         errors = {}
#         if not guest.email:
#             errors['email'] = 'Title should not be empty!'
#         elif len(guest.email) > 200:
#             errors['email'] = 'Title should be 200 symbols or less!'
#
#         if not guest.author:
#             errors['author'] = 'Author should not be empty!'
#         elif len(guest.author) > 40:
#             errors['author'] = 'Author should be 40 symbols or less!'
#
#         if not guest.text:
#             errors['text'] = 'Text should not be empty!'
#         elif len(guest.text) > 3000:
#             errors['text'] = 'Text should be 3000 symbols or less!'
#
#         if len(errors) > 0:
#             return render(request, 'update.html', context={
#                 'errors': errors,
#                 'guest': guest
#             })
#
#         guest.save()
#         return redirect('guest' )



#
#
# def article_delete_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'delete.html', context={'article': article})
#     elif request.method == 'POST':
#         article.delete()
#         return redirect('index')