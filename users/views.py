from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from store.models import *
from store.utils import cookieCart, cartData, guestOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'items':items, 'order':order, 'cartItems':cartItems, 'form':form}
    return render(request, 'users/register.html', context)

@login_required
def my_account(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'users/my_account.html', context)
