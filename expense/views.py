from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import expenses



def exp(request):
    expense = expenses()
    data = expenses.objects.all()
    total = 0
    for amount in data:
        total += amount.amount
    if request.POST.get('reason'):
        expense.reason = request.POST.get('reason')
        expense.amount = request.POST.get('amount')
        
        expense.save()
        return render(request, 'expense/expense.html', {'data': data, 'total': total})
    return render(request, 'expense/expense.html', {'data': data,'total': total})


def dele(request, id1):
    if request.method == 'POST':
        delete1 = expenses.objects.get(id=id1)
        delete1.delete()
        return redirect('expense')