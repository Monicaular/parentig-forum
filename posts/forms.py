from django import forms
from .models import Post, ContactRequest, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder

class PostForm(forms.ModelForm):
    """
    A form for creating and updating Post instances.

    This form maps to the Post model and specifies fields that should be exposed in the form interface,
    allowing users to submit post data.

    Attributes:
        model: The model associated with the form, Post.
        fields (list): Specifies which fields should be included in the form, making other fields not accessible.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'age', 'tags', 'categories']

class ContactForm(forms.ModelForm):
    """
    A form for creating ContactRequest instances.

    This form is used for users to send contact requests via the website, providing fields for name, email, and message.

    Attributes:
        model: The model associated with the form, ContactRequest.
        fields (tuple): Specifies the fields that are included in the form.
    """
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message')

class CommentForm(forms.ModelForm):
    """
    A form for creating and updating Comment instances.

    This form allows users to submit comments, optionally with a photo. The form utilizes Crispy Forms for layout
    and styling, ensuring a structured and stylized presentation.

    Attributes:
        model: The model associated with the form, Comment.
        fields (tuple): Specifies the fields to include in the form.
        widgets (dict): Defines specific widgets or properties for certain form fields.
    """
    class Meta:
        model = Comment
        fields = ('content', 'photo', )
        widgets = {
            'parent_comment': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Initializes the form, sets custom labels, and configures the Crispy Form helper for layout and design.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
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
        