from django.urls import path
from products import views
urlpatterns = [
    path("index/", views.index),
    path("about/", views.about),
    path("animal/", views.animal, name="animal"),
    path("animal/<int:animal_id>", views.detail_animal),
    path("delete-animal/<int:animal_id>", views.delete_animal),
    path("animal2/", views.animal, name="animal2"),
    path("delete_animal_by_name/<str:animal_name>", views.delete_animal_by_name),
    path("add-animal", views.create_animal)


]
