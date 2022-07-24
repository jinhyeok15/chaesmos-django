from django.test import TestCase
from django.utils import timezone

from .forms import TagForm, LetterCreateForm
from .models import Letter

from users.tests import user_factory

# Create your tests here.

def letter_factory(size):
    users = user_factory(size)
    
    letters = []
    for i in range(size):
        letters.append(Letter.objects.create(
            title=f'title{i}',
            main=f'main{i}',
            fk_writer=users[i],
            selected_date=timezone.now()
        ))
    return letters


class PostOfficeTestCase(TestCase):
    def test_tag_is_valid_exception(self):
        letters = letter_factory(1)
        form = TagForm({
            'letter': letters[0].id,
            'tags': 'tag1 tag2 tag3'
        })

        if form.is_valid():
            tag = form.save()
            self.assertEqual(tag[0].name, 'tag1')
        else:
            Exception('test failed - test_tag_id_valid_exception')
