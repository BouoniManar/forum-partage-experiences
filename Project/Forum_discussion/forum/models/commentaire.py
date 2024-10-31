from django.db import models

from forum.models.sujet import Sujet
from forum.models.utilisateur import Utilisateur



class Commentaire(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, related_name='commentaires', on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet, related_name='commentaires', on_delete=models.CASCADE)

    """ def ajouter_commentaire(self):
        pass

    def modifier_commentaire(self):
        pass

    def supprimer(self):
        pass

    def __str__(self):
        return f"Commentaire de {self.utilisateur} sur {self.sujet}" """
