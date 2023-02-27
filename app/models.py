from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Skill(models.Model):
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=200, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)
    type = models.CharField(max_length=200,
                            null=False,
                            choices=JOB_TYPE_CHOICES)

    # def save(self, *args, **kwargs):
    #   if not self.id:
    #     self.slug = slugify(self.title)
    #   return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
