# from django import forms

# class PostForm(forms.Form):
#   title = forms.CharField(label='제목', max_length=20)
#   content = forms.CharField(label='내용', widget=forms.Textarea)

from second.models import Comment, Post
from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content']
    labels = {
      'title': _('제목'),
      'content': _('내용'),
    }
    help_texts = {
      'title': _('제목 입력'),
      'content': _('내용 입력')
    }
    error_messages = {
      'name': {
        'max_length': _('제목이 너무 깁니다 20자 이하로 해주세요')
      }
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    labels = {
      'content': _('댓글 내용'),
    }
    help_text = {
      'content': _('댓글을 입력해 주세요')
    }
