from django import forms
from taggit.models import Tag

import datetime

# Important note: For each tuple in CHOICES for these filters, the two values must be the same!
# This is so that the form could fill its initial values from the query parameters in the URL

class TagForm(forms.Form):
    all_tags = Tag.objects.all()
    tag_choices = list(zip(all_tags, all_tags))

    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange':'form.submit();'}),
        choices=tag_choices,
        label=False
    )

class TimeForm(forms.Form):
    course_times = [datetime.datetime(2020, 4, 4, 10) + k*datetime.timedelta(hours=1) for k in range(6)]
    time_choices = [(time.strftime("%H:%M"), time.strftime("%H:%M")) for time in course_times]

    times = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange':'form.submit();'}),
        choices=time_choices,
        label=False
    )
