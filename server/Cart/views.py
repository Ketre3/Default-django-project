from django.shortcuts import render

def cart_view(request):
    return render(request, 'basket.html')

def purchase_confirm_view(request):
    return render(request, 'basket_end.html')
