from django import forms


class Press(forms.Form):
    choices_press = (
        ('lemondefr', 'Le monde'),
        ('20Minutes', '20 Minutes'),
        ('LesEchos', 'Les Echos'),
    )


    choice_press = forms.ChoiceField(choices = choices_press, label = 'Choose the press please!')