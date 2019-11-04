from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']
    
    # check if user has made inquiry already 
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contected:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listing/'+listing_id)

    contacts = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

    contacts.save()

    # send mail
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiy for'+ listing + '. Sign admin panel for more info',
    #   'ali.hamza4010424@gmail.com',
    #   [realtor_email, 'ali.hamza6625643@gmail.com'],
    #   fail_silently=False
    # )
    
    messages.success(request, 'Your request has been submiited, and get back to you soon')

    return redirect('/listing/'+listing_id)



