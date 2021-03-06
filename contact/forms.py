"""Forms for Contact app """
from django import forms

class ContactForm(forms.Form):
    """
    Contact form that is rendered on contact.html and will
    let customer to send message
    """
    from_email = forms.EmailField(required=True,
                                  label="E-mail address:",
                                  widget=forms.TextInput(attrs={
                                      'placeholder': "Your Email Address",
                                      'autocomplete': "on"}))
    subject = forms.CharField(required=True,
                              label="Message subject:",
                              widget=forms.TextInput(attrs={
                                  'placeholder': "Enter Message Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Enter Your Message Here"}),
                              label="Message:",
                              required=True)

    class Meta:
        fields = ["subject", "from_email", "message"]
