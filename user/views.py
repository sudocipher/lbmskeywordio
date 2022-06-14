from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import BookUploadForm, UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'user/index.html', {'title':'index', 'name':'Library Management System'})

# register here
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                # mail system
                htmly = get_template('user/Email.html')
                d = {'username' : username}
                subject, from_email, to = 'welcome', '15jun20221000@gmail.com', email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                # ############
                messages.success(request, f'You account has been created! You are now able to log in!')
                return redirect('login')
        except:
            messages.info(request, 'Username already exists!')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form, 'title':'register here'})

# login form

def loginUser(request):
    if request.method == 'POST':

        # AuthenticationForm can also be used

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'welcome {username}!!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exist, plesae sign in!')
    
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

# TODO 4. Retrieve all the books.
def booksRender(request):
    context = {}
    books = Book.objects.all()
    context['books'] = books
    return render(request, 'user/books-render.html', context)

# TODO 3. Create an entry for a book
def bookInsert(request):
    if request.POST:
        form = BookUploadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('books-render')

    context = {'form':BookUploadForm}
    return render(request, 'user/book-insert.html', context)


# TODO 5. Update a book.
def bookUpdate(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookUploadForm(request.POST or None, instance=book)
    context = {'book':book, 'form':form}
    if form.is_valid():
        form.save()
        return redirect('books-render')
    return render(request, 'user/book-update.html', context)

# TODO 6. Delete a book.
def bookDelete(request, book_id):
    context = {}
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('books-render')
    # return render(request, 'user/book-delete.html', context)

