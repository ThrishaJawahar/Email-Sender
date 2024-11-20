from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse

def send_email(request):
    if request.method == 'POST':
        try:
            subject = request.POST['subject']
            recipient = request.POST['recipient']
            message_body = request.POST['message']
            sender = request.POST['sender']

            html_message = loader.render_to_string(
                'Emailapp/message.html',  
                {
                    'name': sender,
                    'body': message_body,
                    'sign': sender,
                }
            )

            send_mail(
                subject,
                message_body,
                'lavanyaraja146@gmail.com',  
                ['ralphlauren251999@gmail.com'],  
                html_message=html_message,
                fail_silently=False,
            )

            return HttpResponse("Mail Sent!!")
        
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

return render(request, 'Emailapp/send_email.html')
