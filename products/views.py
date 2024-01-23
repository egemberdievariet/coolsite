from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Animal

new_names =["Ariet", "Nurislam", "Aidar", "Asel", "Nurjamal", "Kasym", "Aman"]
def index(request):
    names = {"new_names": new_names}
    return render(request, "index.html", context=names)


hobby = ["Sleeping", "Programming", "Football", "Reading", "Volleyball"]
def about(request):
    hobbies = {"hobbies": hobby}
    return render(request, "about.html", context=hobbies)

def animal(request):
    animal = Animal.objects.all()
    new_animal = {"new_animal": animal}
    return render(request, "animal.html", context=new_animal)


def detail_animal(request, animal_id):
    animal = Animal.objects.filter(id= animal_id)
    new_animal = {"new_animal": animal}
    return render(request, "animal2.html", context=new_animal)

def delete_animal(request, animal_id):
    animal = Animal.objects.filter(id=animal_id)
    animal.delete()
    return redirect("animal")


def animal(request):
    animal = Animal.objects.all()
    new_animal = {"new_animal": animal}
    return render(request, "animal.html", context=new_animal)

def delete_animal_by_name(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    animal.delete()
    return redirect("animal2")

def create_animal(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        breed = request.POST.get("breed")
        animal = Animal.objects.create(
            name=name,
            age=age,
            breed=breed
        )
        animal.save()
        return render(request, "animal")
