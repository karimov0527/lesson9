from django.urls import path
from .views import Books_list,Book_create,Book_update,Book_delete

urlpatterns = [
    path("",Books_list.as_view(),name="books-list"),
    path("create/",Book_create.as_view(),name="books-create"),
    path("update/<int:pk>",Book_update.as_view(),name='books-update'),
    path('delete/<int:pk>',Book_delete.as_view(),name="books-delete"),
]
