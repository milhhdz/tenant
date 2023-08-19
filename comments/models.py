from django.db.models import Model, CharField

# Create your models here.
class Comment(Model):
    tweet = CharField(max_length=100)