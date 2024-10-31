from django.db import models

from forum.models.produit import Produit
from forum.models.utilisateur import Utilisateur


class Note(models.Model):
    rating = models.PositiveIntegerField()
    utilisateur = models.ForeignKey(Utilisateur, related_name='notes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='notes', on_delete=models.CASCADE)

"""     def ajouter_note(self):
        pass

    def __str__(self):
        return f"Note de {self.utilisateur} pour {self.produit} : {self.rating}"
 """