from django.db import models


# Cateqory model 
class Cateqory(models.Model):
    name = models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Client model 
class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    Cateqory = models.ForeignKey(Cateqory,on_delete=models.CASCADE)
    phone = models.IntegerField()
    tall = models.IntegerField()
    wedight = models.IntegerField()
    address = models.CharField(max_length=500)
    cteated_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name + " " + self.last_name
    
    # class Meta:
    #     ordering = ['-cteated_at']


