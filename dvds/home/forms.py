from django import forms
from .models import Support, GearBox, Promotion


class SupportForm(forms.ModelForm):
    """
        Support form 
    """

    class Meta():
        model = Support
        exclude = ('user',)
        fields = ('name', 'email', 'number', 'location',
                  'gearbox', 'information', 'message',)

    def __init__(self, *args, **kwargs):
        """
            Sets classes and autofocus
        """

        super().__init__(*args, **kwargs)
        gearbox = GearBox.objects.all()
        promotion = Promotion.objects.all()

        gears = [(c.id, c.get_friendly()) for c in gearbox]
        promotions = [(p.id, p.get_friendly()) for p in promotion]

        self.fields['name'].widget.attrs['autofocus'] = True

        self.fields['name'].widget.attrs['placeholder'] = 'John Smith'
        self.fields['number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'contact@dedhamvaledriving.com'
        self.fields['location'].widget.attrs['placeholder'] = 'Your Location - Colchester'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message here'

        for field in self.fields:
            self.fields['gearbox'].choices = gears
            self.fields['information'].choices = promotions
            self.fields[field].widget.attrs['class'] = 'rounded-0 mb-2'
            self.fields[field].label = False
