from django.contrib import auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import Document, New, Block, License


def index(request):
    main_header = Block.objects.get(type='main_header')
    main_text = Block.objects.get(type='main_text')

    context = {
        'main_header': main_header.text,
        'main_text': main_text.text
    }

    return render(
        request,
        'index.html', context
    )


def news(request):
    news_list = New.objects.all()
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'news.html',
        {'news_page': page, 'paginator': paginator}
    )


def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            recepients = ['inood@yandex.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'it.asu@sts-strezh.ru', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form, 'username': auth.get_user(reguest).username})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})


def licenses(reguest):
    licenses = License.objects.all()
    return render(reguest, 'licenses.html', {'licenses': licenses})


def documents(request):
    docs = Document.objects.all()
    return render(request, 'documents.html', {'docs':docs })

def about(request):
    return render(request, 'about.html')
