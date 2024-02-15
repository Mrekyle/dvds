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
        self.fields['gearbox'].choices = gears
        self.fields['information'].choices = promotions
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'rounded-0 mb-2'
            self.fields[field].label = False
