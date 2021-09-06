from django.http import HttpResponse

'''
单个固定路由
'''


def page1(request):
    h = 'page101'
    return HttpResponse(h)


def calculate_total(request, num1, calculate_method, num2):
    if calculate_method == 'add':
        return HttpResponse(num1 + num2)
    elif calculate_method == 'mul':
        return HttpResponse(num1 * num2)
    elif calculate_method == 'sub':
        return HttpResponse(num1 - num2)


def cal_view(request, x, op, y):
    if op == 'add':
        html = '%s,%s,%s' % (x, op, y)
        return HttpResponse(html)


def view_birthday1(request, year, month, day):
    html = '%s,%s,%s' % (year, month, day)
    return HttpResponse(html)


def view_birthday2(request, year, month, day):
    html = '%s,%s,%s' % (month, year, day)
    return HttpResponse(html)
