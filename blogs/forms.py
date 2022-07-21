from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Article, Comment

class Articleform(ModelForm):
    class Meta:
        model = Article
        fields = ['heading', 'discription', 'featured_image', 'text_field', 'category', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(Articleform, self).__init__(*args, **kwargs)

        self.fields['heading'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Heading'})
        self.fields['discription'].widget.attrs.update({'class': 'form-control'})
        self.fields['featured_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['text_field'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})


# Comment form using modelform for blog post
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({'class': 'form-group form-control input-mf', 'placeholder': 'Comment*'})


# Edit article form and some fields are excluded
class EditArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['owner', 'comment_total', 'tags']
        
    def __init__(self, *args, **kwargs):
        super(EditArticleForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['readonly'] = True

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})