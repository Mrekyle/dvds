from django import forms
from .models import LessonPricing


class PricingForm(forms.ModelForm):
    """
        Lesson Pricing Form
    """

    class Meta():
        model = LessonPricing
        fields = '__all__'
