from django.db import models

class Tag(models.Model):
    nom = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nom


class Projet(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projets")
    lien = models.URLField(max_length=200, blank=True)

    def __str__(self) :
        return self.titre


class ProjetImage(models.Model):
    projet = models.ForeignKey(Projet, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projet_images/")

    def __str__(self) -> str:
        return f"{self.projet.titre} Image"