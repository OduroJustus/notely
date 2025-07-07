from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'email', 'password1', 'password2', 'is_writer')

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control'}) 