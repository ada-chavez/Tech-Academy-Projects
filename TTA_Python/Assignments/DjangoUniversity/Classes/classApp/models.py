from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=100)
    course_num = models.IntegerField()
    instructor_name = models.CharField(max_length=100, default="")
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title

o1 = djangoClasses.objects.update_or_create(title="Defence Against the Dark Arts", course_num=101, instructor_name="Gilderoy Lockhart", duration=1.0)
o2 = djangoClasses.objects.update_or_create(title="Care of Magical Creatures", course_num=440, instructor_name="Silvanus Kettleburn", duration=2.5)
o3 = djangoClasses.objects.update_or_create(title="Potions", course_num=666, instructor_name="Severus Snape", duration=1.5)