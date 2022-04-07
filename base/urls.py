from django.urls import path
from .views import BookList,BookDetails,BookAdd,BookUpdate,DeleteView,CustomLoginView,StudentView,Register

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',StudentView.as_view(), name='index' ),
    path('register/',Register.as_view(), name='register'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'), name='logout'),
    path('admin-panel/',BookList.as_view(), name ='admin-panel'),
    path('book/<int:pk>/', BookDetails.as_view(), name='book_details'),
    path('add-book/',BookAdd.as_view(), name ='add-book'),
    path('update-book/<int:pk>/',BookUpdate.as_view(), name ='update-book'),
    path('delete-book/<int:pk>/',DeleteView.as_view(), name ='delete-book'),

]