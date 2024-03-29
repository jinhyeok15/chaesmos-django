from django import forms
from .models import *


class LetterCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'title-input',
        'placeholder': '제목'
    }))
    main = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'text-textarea',
        'placeholder': '고민이 무엇인가요?',
        'cols': '10',
        'rows': '10'
    }))
    selected_date = forms.DateField(label="날짜:", widget=forms.DateInput(
        attrs={
            'type': 'date',
            'id': 'choose',
        }
    ))

    class Meta:
        model = Letter
        fields = [
            'title', 'main', 'selected_date', 'fk_writer'
        ]


class TagForm(forms.Form):
    letter = forms.IntegerField()
    tags = forms.CharField()  # 하나의 string에 여러개의 tag를 붙이기 보다 getlist()를 하여 list로 불러오도록 바꾸기

    class Meta:
        model = Tag
        fields = [
            'letter', 'tags'
        ]
    
    def save(self):
        splited = self.data.get('tags', []).split(' ')
        letter_id = self.data.get('letter')

        return Tag.objects.bulk_create([Tag(name=t, fk_letter=letter_id) for t in splited])
    
    def is_valid(self):
        letter_id = self.data.get('letter')
        try:
            Letter.objects.get(pk=letter_id)
        except Letter.DoesNotExist:
            self.add_error('letter object does not exist')
