from django.urls import path

from BookStore import views

urlpatterns = [
    path("",views.home, name = "home"),

    path("addauthor",views.add_author, name = "addauthor"),

    path("displayauthor",views.display_author, name = "displayauthor"),

    path('deleteauthor/<int:id>',views.delete_author, name = 'deleteauthor'),

    path('editauthor/<int:id>',views.edit_author, name = 'editauthor'),

    path("addbook",views.add_book, name = "addbook"),

    path("displaybook", views.display_book, name="displaybook"),

    path('deletebook/<int:id>', views.delete_book, name='deletebook'),

    path('editbook/<int:id>', views.edit_book, name='editbook')

]