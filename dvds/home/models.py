from django.db import models

# Create your models here.


class Support(models.Model):
    """
        Contact form model.
    """

    name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(
        max_length=50, null=True, blank=True)
    gearbox = models.ForeignKey(
        'GearBox', max_length=25, blank=True, null=True, on_delete=models.SET_NULL)
    information = models.ForeignKey(
        'Promotion', max_length=50, blank=True, null=True, on_delete=models.SET_NULL)
    message = models.TextField()

    class Meta():
        verbose_name_plural = 'Support History'
        verbose_name = 'Support History'

    def __str__(self):
        return self.name


class GearBox(models.Model):
    """
        Student gearbox preference
    """

    gearbox = models.CharField(max_length=40, blank=True, null=True)
    friendly_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta():
        verbose_name = 'Gearbox Preference'
        verbose_name_plural = 'Gearbox Preference'

    def __str__(self):
        return self.gearbox

    def get_friendly(self):
        return self.friendly_name


class Promotion(models.Model):
    """
        How did the student hear about the school 
    """

    promotion = models.CharField(max_length=40, blank=True, null=True)
    friendly_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta():
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotion'

    def __str__(self):
        return self.promotion

    def get_friendly(self):
        return self.friendly_name
