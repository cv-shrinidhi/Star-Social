from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2') # put in password1 and confirm it with password2
        model = get_user_model()

    # this is to display the labels against the form fields like username, password
    def __init__(self, *args, **kwargs):
        # super() gives access to methods of parent class (superclass) from child class (subclass)
        super().__init__(*args, **kwargs)
        # this is like setting up labels on html page except we do it from here
        # this is just for customization to display desired labels depending on the website
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
