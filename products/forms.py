from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(min_length=5,required=True,error_messages={"required": "You forgot to add your name"})
    rating = forms.IntegerField(min_value=1,max_value=5)
    text = forms.CharField(label="Your feedback",widget=forms.Textarea,max_length=200)