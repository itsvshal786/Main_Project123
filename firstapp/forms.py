from django import forms
from firstapp.models import userData



class userDataForm(forms.ModelForm):
    class Meta():
        model=userData
        exclude=["userId",
                 "userName",
                 "userPassword",
                 "userEmail",
                 "userImage",
                 "isActive"

        ]