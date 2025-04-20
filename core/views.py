from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import *
# def home_page(request):
#     partners = Partner.objects.all()
#     return render(request, 'landing.html',{'partners': partners})


def contact_view(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Başarılı mesajı için yönlendirme
    
    return render(request, 'contact.html', {'form': form})

def faq_list(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'faq.html', {'faqs': faqs})
