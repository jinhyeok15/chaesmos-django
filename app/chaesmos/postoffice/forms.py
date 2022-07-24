from django import forms
from .models import *


class LetterCreateForm(forms.ModelForm):

    class Meta:
        model = Letter
        fields = [
            'title', 'main', 'selected_date', 'fk_writer'
        ]


class TagForm(forms.Form):
    letter = forms.IntegerField()
    tags = forms.CharField()

    class Meta:
        model = Tag
        fields = [
            'letter', 'tags'
        ]
    
    def save(self):
        splited = self.data.get('tags').split(' ')
        letter_id = self.data.get('letter')

        return Tag.objects.bulk_create(Tag(name=t, fk_letter=letter_id) for t in splited)
    
    def is_valid(self):
        letter_id = self.data.get('letter')
        try:
            Letter.objects.get(pk=letter_id)
        except Letter.DoesNotExist:
            self.add_error('letter object does not exist')
