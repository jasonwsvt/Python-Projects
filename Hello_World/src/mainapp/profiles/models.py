from django.db import models

TYPE_CHOICES = {
    ('----------','----------'),
	('Dame','Dame'),
	('Doctor','Doctor'),
	('Esquire','Esquire'),
	('Excellency','Excellency'),
	('Her Honour','Her Honour'),
	('His Honour','His Honour'),
	('Lady','Lady'),
	('Lord','Lord'),
	('Sir','Sir'),
	('Sire','Sire'),
	('The Honourable','The Honourable'),
	('The Right Honourable','The Right Honourable'),
}

# Create your models here.
class Profile(models.Model):
    prefix = models.CharField(max_length=20, default='----------',choices=TYPE_CHOICES)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=32)
    
    objects = models.Manager()
    
    def __str__(self):
        return self.prefix + " " + self.firstName + " " + self.lastName