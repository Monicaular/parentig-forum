from django import forms
from .models import Post, ContactRequest, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'age', 'tags', 'categories']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'photo', )
        widgets = {
            'parent_comment': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Comment'
        self.fields['content'].widget.attrs.update({'class': 'form-control form-control-sm'}) 
        self.fields['photo'].widget.attrs['accept'] = 'image/*' 
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('Content', placeholder='Write a comment...'),
            ButtonHolder(
                Submit('submit', 'Post', css_class='btn btn-primary mt-2 float-right')
            )
        )
        