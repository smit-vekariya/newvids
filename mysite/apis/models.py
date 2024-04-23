from django.db import models

# Create your models here.
class Poster(models.Model):
    cat_id = models.IntegerField(null=True, blank=True)
    cat_name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.cat_id)

class Template(models.Model):
    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE, null=True, blank=True)
    template_id = models.IntegerField(null=True, blank=True)
    template_type = models.IntegerField(null=True, blank=True)
    template_name = models.CharField(max_length=1000, null=True, blank=True)
    preview_image = models.CharField(max_length=1000, null=True, blank=True)
    preview_image_file = models.FileField(upload_to='preview_image_file/', null=True, blank=True)
    file_url = models.CharField(max_length=1000, null=True, blank=True)
    zip_file = models.FileField(upload_to='zip_file/', null=True, blank=True)
    is_paid = models.IntegerField(null=True, blank=True)
    is_favorite = models.IntegerField(null=True, blank=True)
    visit_count = models.CharField(max_length=1000, null=True, blank=True)
    is_new = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.template_id)