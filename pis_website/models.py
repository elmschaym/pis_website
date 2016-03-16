from django.db import models
from django.contrib.auth.models import User



''' WEBSITE MODEL '''

class Events(models.Model):
    news_event = (
                  ('N', 'News'),
                  ('E', 'Events')
                )

    subject = models.CharField(max_length = 850)
    description = models.TextField()
    category = models.CharField(max_length=2,choices=news_event)
    date_created = models.DateField( auto_now_add = True)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta():
        db_table = 'events'
 
    def __unicode__(self):
      return self.subject

class EventImages(models.Model):
    event = models.ForeignKey(Events)
    image_path = models.FileField(upload_to='event_image')


    class Meta():
        db_table = 'events_images'
 
    def __unicode__(self):
      return self.event
  
