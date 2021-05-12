from django.db import models
from datetime import datetime



class Song(models.Model):

   # audio_file_type = (('song', 'Song'),
                #   ('postcard','Postcard'),
                 #  ('audiobook', 'Audiobook'),
                 #  )
    audiofile=models.CharField(max_length=10,null=False,default='Song')
    
    name = models.CharField(max_length=200,null=False)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name)
    
class Postcast(models.Model):
   # audio_file_type = (('song', 'Song'),
                  # ('postcard', 'Postcard'),
                   #('audiobook', 'Audiobook'),
                 #  )
    audiofile=models.CharField(max_length=10,null=False,default='Postcard')
    name = models.CharField(max_length=200,null=False)
    duration = models.PositiveIntegerField( null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True) 
    host=models.CharField(max_length=20,null=False)
    participants=models.PositiveIntegerField(max_length=100)

    
    def __str__(self):
        return str(self.name,self.host)
    

class Audiobook(models.Model):
   # audio_file_type = (('song', 'Song'),
            #       ('postcard', 'Postcard'),
            #       ('audiobook', 'Audiobook'),
             #      )
    audiofile=models.CharField(max_length=10,null=False,default='Audiobook')
    title = models.CharField(max_length=200,null=False)
    author_of_title = models.CharField(max_length=100, null=False)
    narrator=models.CharField(max_length=100,null=False)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time=models.DateTimeField(auto_now_add=True) 

    
    def __str__(self):
        return self.title
    
    