from django import forms
import smtplib
from email.message import EmailMessage
from ecommerce.settings import EMAIL_HOST, EMAIL_HOST_PASSWORD

from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=120)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self) -> None:
        """
        Function to send email with smtlib, from Marvin email to "to_user_mail"
        inserting "body_content" in content of email

        :return:
        """
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]

        content = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        message = EmailMessage()
        message['subject'] = subject
        message['from'] = EMAIL_HOST
        message['to'] = EMAIL_HOST
        message.set_content(content)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_HOST, EMAIL_HOST_PASSWORD)
            smtp.send_message(message)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'amount', 'price', 'description']

