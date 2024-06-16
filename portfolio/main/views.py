from django.shortcuts import render, get_object_or_404


from .models import Projet, Tag


def home(request):
    projets = Projet.objects.all()
    tags = Tag.objects.all()

    return render(request, "home.html", 
                  {
                      "projets": projets,
                      "tags": tags })


def contact(request):
    return render(request, "contact.html")

def projet(request, id):
    projet = get_object_or_404(Projet, pk=id)
    return render(request, "projet.html", {"projet": projet})