from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def homePage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name': name,
            'subject': subject,
            'email': email,
            'message': message
        }
        message = '''
        new message: {}
        from: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message,'', ['prabeshuprety2@gmail.com'])
    return render(request, 'base/home.html')



def post(request):
    return render(request, 'base/post.html')