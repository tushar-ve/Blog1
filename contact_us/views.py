from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
from .models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings



# from .serializers import *
from django.contrib import messages
# from rest_framework.decorators import api_view
# from rest_framework.response import Response



def ContactUs(request):
    # serializer = contactserializer(data= request.data)
    # if not serializer.is_valid():    
    #         return Response({'status':403, 'errors': serializer.errors, 'message':'Not valid input'})
       
    # serializer.save()
    # return Response({'status':200, 'payload': serializer.data, 'message':'data save'})
    contactus = contactusModel.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        # if not serializer.is_valid():    
        #     return Response({'status':403, 'errors': serializer.errors, 'message':'Not valid input'})
       
        # serializer.save()
        # return Response({'status':200, 'payload': serializer.data, 'message':'data save'})
        h1='please check you input email <6'
       
        if len(email)<=6:
            data1={
                'h1':h1
            }
            messages.info(request, data1 )
        if email[0].isalpha():
             messages.info(request, 'please check you input is not aplha')
    
        if ("@" not  in email) and (email.count("@")==2):
            #  return redirect("/contact_us",custom_error="Try Again Later")
             messages.info(request, 'please check you input has invalid @')
        if (email[-4]!=".") ^ (email[-3]!="."):
            messages.info(request, 'please check your input')
        #               messages.info(request, 'please check you input')
                
                    
        en = contactusModel(name=name,email=email,message=message)
        en.save()
        data={
                        'en':en
                           }

        subject=" Regarding Registration"

        #htmly=get_template('email.html')

        from_email=settings.EMAIL_HOST_USER

        recipent_list=[email]

        context={'name':name,'email':email,'message':message}

        html=render_to_string('aboutus/email.html',context)

        #html_content=htmly.render(context)

        send_mail(

        subject,

        'message',

        from_email,

        recipent_list,

        html_message=html,

        

        )
                        
       
        messages.info(request, 'Your Message is Successfully send')
        return render(request, "aboutus/save.html", data)
    


           

    return render(request,"aboutus/about-us.html")

def thank(request):
    return render(request, "aboutus/email.html")

# @csrf_protect
