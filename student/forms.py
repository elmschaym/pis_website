from django import forms

class Login_Form(forms.Form):
    username = forms.DecimalField(
        widget   = forms.NumberInput(
            attrs = {
                'placeholder' : 'Username',
                'class'       : 'form-control',
                'id'          : 'username',
                'required'    : 'True',
                'style'       : 'border-radius : 0px',
            }
        ),
    )
     
    password = forms.CharField(
        widget   = forms.PasswordInput(
            attrs = {                  
                'placeholder' : 'Password',
                'class'       : 'form-control',
                'id'          : 'password',
                'required'    : 'True',
                'style'       : 'border-radius : 0px',
            }
        ),
    )