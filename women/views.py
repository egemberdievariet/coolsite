from django.shortcuts import render, redirect
from women.models import Women
from women.forms import AddPostForm
menu = [
    {"name": "Главная страница", "url": "index"},
    {"name":"О нас", "url": "about"},
    {"name":"Наши контакты", "url": "contacts"},
    {"name":"Вопросы", "url": "questions"},
    {"name": "Добавить статью", "url": "add-post"}
]
def index(request):
    women = Women.objects.all()
    new_women = {"new_women": women, "menu": menu}
    return render(request, 'index.html', context=new_women)

def about(request):
    new_women = {"menu": menu}
    return render(request, "about.html", context=new_women)


def contacts(request):
    new_women = {"menu": menu}
    return render(request, "contacts.html",context=new_women)


def questions(request):
    new_women = {"menu": menu}
    return render(request, "questions.html", context=new_women)


def add_women(request):

    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPostForm()
    new_women = {"menu": menu, 'form': form}
    return render(request, "add_women.html", context=new_women)


def delete_women(request, women_id):
    if request.method == "POST":
        Women.objects.filter(id=women_id).delete()
        return redirect('index')


def detail_women(request, women_id):
    woman = Women.objects.filter(id=women_id).first()
    new_women = {'menu': menu, 'woman': woman}
    return render(request, 'women_detail.html', context=new_women)

