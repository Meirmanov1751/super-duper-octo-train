from django.db import models


class Note(models.Model):

    note=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note[0:15]



class Notice(models.Model):
    title=models.CharField(max_length=50)
    note=models.CharField(max_length=300)
    note_created_date=models.ForeignKey(Note,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.title}|{self.note[0:15]}'




