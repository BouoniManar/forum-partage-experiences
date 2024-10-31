from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Utilisateur(AbstractUser):
    role = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    email = models.EmailField(max_length=30)

    groups = models.ManyToManyField(Group, related_name='utilisateur_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='utilisateur_set', blank=True)

"""     def inscrire(self):
        # Logique d'inscription
        pass

    def se_connecter(self):
        # Logique de connexion
        pass

    def modifier_profil(self):
        # Logique de modification de profil
        pass

    def ajouter_favoris(self, produit):
        # Logique d'ajout de produit aux favoris """
        
