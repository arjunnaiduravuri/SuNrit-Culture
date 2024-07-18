from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.
from django.db import models
  
class Events(models.Model):
    Category = models.CharField(max_length=50, default="dance", blank=True)
    Imp = models.CharField(max_length=10, default="Not", blank=True)
    Eventname = models.CharField(max_length=50, null=False)
    Eventurl = models.URLField(max_length=200, blank=True)
    Desc = models.TextField(blank=True)
    Aboutevent = models.TextField(blank=True)
    Start_date = models.DateField(blank=True, null=True)
    Start_time = models.TimeField(blank=True, null=True)
    End_date = models.DateField(blank=True, null=True)
    End_time = models.TimeField(blank=True, null=True)
    Venue = models.CharField(max_length=100, blank=True)
    Banner = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'events'

    def __str__(self):
        return f"Event: {self.Eventname}"


class Gallery(models.Model):
    class Meta:
        db_table = 'Gallery'

    def __str__(self):
        return 'New gallery'

class Dancer(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='dancers', on_delete=models.CASCADE)
    image = models.ImageField(null=False, upload_to='dancers/')

class Musician(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='musicians', on_delete=models.CASCADE)
    image = models.ImageField(null=False, upload_to='musicians/')


class News(models.Model):
    New = models.TextField(null = False)

    class Meta:
        db_table = "News"

class Feedback(models.Model):
    Name = models.CharField(max_length=10, null=False)
    Role = models.CharField(max_length=10, null=False)
    Message = models.TextField()

    class Meta:
        db_table = "Feedback"
        
    def __str__(self):
        return f"{self.Name}"

class Banner(models.Model):
    Title = models.CharField(max_length = 50, null=False )
    Subtitle = models.CharField(max_length=50, null=False)
    Image = models.ImageField(null= False, upload_to='images/')

    class Meta:
        db_table = "Banner"

class Subscribe(models.Model):
    email = models.EmailField(null=False)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Subs"

class Contact(models.Model):
    Name = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null = False)
    Subject = models.CharField(max_length=50, null = False)
    Message = models.TextField(null = False)

    class Meta:
        db_table = "Contactus"

    def __str__(self):
        return f"Message from {self.Name}"

class Blogs(models.Model):
    Name = models.CharField(max_length=50, null = False)
    Message = models.TextField()
    date = models.DateTimeField(default=now, blank=True)

    
    class Meta:
        db_table = "Blogs"

    def __str__(self):
        return f"{self.Name}"
    
    
        


