from django.shortcuts import render, redirect
from .utils import send_mail_to_user
from .models import Contact


from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMessage
from django.conf import settings
from softwarechamber.settings import EMAIL_HOST_USER







# Create your views here.

def send_email_form_contact():
    subject="Thank you for reaching out!"
    message = "Dear [Name]," + " " + "data"
    email="data['cost_email']"
    recipient_list =[email]
    send_mail(subject, message,EMAIL_HOST_USER, recipient_list, fail_silently=True)
    return redirect('/booking_success')


def home(request):
    return render(request, 'custom/base.html')



def contact_us(request):
    return render(request, 'custom/contact-us.html')



def about_us(request):
    return render(request, 'custom/about-us.html')




def booking_success(request):
    return render(request, 'custom/booking-success.html')




def contac_form_view(request):
    print("Welcome")
    if request.method == "POST":
 
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        subject = request.POST.get("subject", None)
        message = request.POST.get("message", None)
        contac_data = Contact.objects.create(name=name,email=email,subject=subject,message=message)
        contac_data.save()
        print("Contact created successfully: ")
        subject="Thank you for reaching out!"
        message = f"""Dear {name},
Thank you for contacting us. It's our joy to have the opportunity to collaborate.

Your message has been received, and we appreciate you taking the time to reach out to us. We understand the importance of your inquiry and would like to assure you that we are working diligently to address it.

Please expect to hear back from us within the next 24-48 hours. Our team will carefully review your message and provide a thoughtful response as soon as possible.

Once again, thank you for reaching out to us. We look forward to connecting with you soon. 


Best regards,

Software chamber
mbhmishu@gmail.com
+880 1832344599
"""
        email=contac_data.email
        recipient_list =[email]
        send_mail(subject, message,EMAIL_HOST_USER, recipient_list, fail_silently=True)
        print("Please check your email address and try again later to contact us.########################")
        return redirect('/booking_success')
    return render(request, 'custom/base.html')
