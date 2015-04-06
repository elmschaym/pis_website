from django import forms

class LogInForm(forms.Form):
	userID = forms.CharField(
								label = '', 
								widget = forms.NumberInput(attrs = {'placeholder':'Employee ID Number'}), 
								required = True,
							)
	
	password = forms.CharField(
								label = '', 
								widget = forms.PasswordInput(attrs = {'placeholder':'Password'}), 
								required = True,
							)