from django.shortcuts import render, redirect
from .forms import ApplicationsForm
from django.views import View
import telebot

bot = telebot.TeleBot("1452235806:AAHnKq6WKiGaMb5Y-6bgH17WrEaJSJ7ULFM")


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'assassinaltair@bk.ru'
            to_email = ['aitofullstackdev@gmail.com', 'aitolivelive@gmail.com']
            message = 'Новая заявка на обратный звонок!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + '\r\n' + 'Номер телефона: ' + phone + '\r\n' + '\r\n' + 'Интересующий вопрос :' + comment
            # send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(-404000259, message)
        return redirect('contact')
