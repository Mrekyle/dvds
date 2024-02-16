from django.db import models

# Create your models here.


class LessonPricing(models.Model):
    """
        Lesson pricing model
    """

    manual_hourly = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    manual_block = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    manual_refresher = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    automatic_hourly = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    automatic_block = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    automatic_refresher = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_ten = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_fifteen = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_twenty = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_twentyfive = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_thirty = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_thirtyfive = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_fourty = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)
    intensive_fourtyfive = models.DecimalField(
        decimal_places=2, max_digits=9, blank=True, null=True)

    class Meta():
        verbose_name = 'Lesson Pricing'
        verbose_name_plural = 'Lesson Pricing'

    def __str__(self):
        return self.id


class FranchiseFee(models.Model):
    """
        Setting franchise fee
    """

    franchise_fee = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta():
        verbose_name = 'Franchise Fee'

    def __str__(self):
        return self.id
