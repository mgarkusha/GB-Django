from django.shortcuts import render_to_response
from .models import Work
import datetime


# Create your views here.
def main_page(request):
    birthday = datetime.date(day=25, month=11, year=1983)
    aboutme = [{'name': 'ФИО', 'value': 'Гаркуша Михаил Иванович'}, {'name': 'День рождения', 'value': birthday}, {
        'name': 'Специальность', 'value': 'Инженер связи'},
               {'name': 'Место рождения', 'value': 'Leningrad'},
               {'name': 'Интересы', 'value': 'Спорт, путешествия, развитие'}]
    return render_to_response('index.html', {'aboutme': aboutme})


def education(request):
    edu = [{'name': 'Школа №95', 'value': 'с 1 по 9 класс'}, {'name': 'Школа №137', 'value': 'с 9 по 11 класс'},
           {'name': 'ВУЗ',
            'value': 'Санкт-Петербургский университет телекоммуникций им. проф. Бонч-Бруевича, Профессия: инженер связи'},
           {'name': 'Курсы', 'value': 'Много разных, последний Geek Brains'}]
    return render_to_response('education.html', {'edu': edu})


def work(request):
    workplaces = [{'name': 'Телефонная компания', 'prof': 'продажа карточек связи'},
                  {'name': 'Веб-студия', 'prof': 'верстальщик'},
                  {'name': 'Тур-фирма', 'prof': 'системный администратор'},
                  {'name': 'Веб-студия', 'prof': 'вёрстка/программирование Perl'},
                  {'name': 'Завод', 'prof': 'системный админ'},
                  {'name': 'Курьерская компания', 'prof': 'системный админ'},
                  {'name': 'Завод', 'prof': 'системный админ'},
                  {'name': 'Таксомоторная компания', 'prof': 'системный админ'}]
    workplaces_bd = Work.objects.all()
    return render_to_response('work.html', {'workplaces': workplaces, 'workplaces_bd': workplaces_bd})
