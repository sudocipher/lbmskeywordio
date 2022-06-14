from django.urls import path
from . import views as user_view
from django.contrib.auth import views as auth


urlpatterns = [    
    path('', user_view.index, name='index'),
    path('login/', user_view.loginUser, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name = 'user/index.html'), name='logout'),
    path('register/', user_view.register, name='register'),
    path('books-render/', user_view.booksRender, name='books-render'),
    path('book-insert/', user_view.bookInsert, name='book-insert'),
    path('book-update/<book_id>/', user_view.bookUpdate, name='book-update'),
    path('book-delete/<book_id>/', user_view.bookDelete, name='book-delete'),
]