from django.urls import path
from women import views
urlpatterns = [
    path("index/", views.index, name = 'index'),
    path("about/", views.about, name = 'about'),
    path("contacts/", views.contacts, name = 'contacts'),
    path("questions/", views.questions, name = 'questions'),
    path("add-post/", views.add_women, name = 'add-post'),
    path("delete-post/<int:women_id>/", views.delete_women, name = 'delete-women'),
    path("detail-women/<int:women_id>/", views.detail_women, name = 'detail-women')


]
