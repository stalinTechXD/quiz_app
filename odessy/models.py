from django.db import models

# Create your models here.
class ody(models.Model):
    eno1 = models.CharField(max_length = 30,)
    eno2 = models.CharField(max_length = 30)
    eno3 = models.CharField(max_length = 30)
    eno4 = models.CharField(max_length = 30)
    eno5 = models.CharField(max_length = 30)
    eno6 = models.CharField(max_length = 30)
    eno7 = models.CharField(max_length = 30)
    eno8 = models.CharField(max_length = 30)
    eno9 = models.CharField(max_length = 30)
    
    def __str__(self):
        return 'Employee Object with eno: +str(self.no)'


class hell(models.Model):
    en = models.CharField(max_length = 30,)

    def __str__(self):
        return 'Employee Object with eno: +str(self.no)'


class od(models.Model):
    en1 = models.CharField(max_length = 30,)
    en2 = models.CharField(max_length = 30)
    en3 = models.CharField(max_length = 30)
    en4 = models.CharField(max_length = 30)
    en5 = models.CharField(max_length = 30)
    en6 = models.CharField(max_length = 30)
    en7 = models.CharField(max_length = 30)
    en8 = models.CharField(max_length = 30)
    en9 = models.CharField(max_length = 30)
    en10 = models.CharField(max_length = 30)
    
    def __str__(self):
        return 'Employee Object with eno: +str(self.no)'        

