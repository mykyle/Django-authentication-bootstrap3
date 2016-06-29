from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from django import forms
from django.core.mail import send_mail

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
      error = False
      if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html',{'books': books, 'query': q})
      return render(request, 'books/search_form.html',{'error': error})


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20, label='Subject  here')
    email = forms.EmailField(required=False, label='Email here')
    message = forms.CharField(widget=forms.Textarea, label='Message Here')
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                 cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'books/contact_form.html', {'form': form})
