from django.shortcuts import render

def index(request):

    revenue = None
    vat = None

    if request.method == 'POST':

        price = float(request.POST.get('price'))
        quantity = float(request.POST.get('quantity'))

        revenue = price * quantity
        vat = revenue * 0.21

    return render(request, 'index.html', {
        'revenue': revenue,
        'vat': vat
    })