from django.shortcuts import render, redirect

from .models import Donate
from .forms import DonationForm


def indexView(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            donation = Donate(name=name, amount=amount, is_donated=True)
            donation.save()
            print(name, amount)
            return redirect('index')
        return redirect('index')

    context = {
        'form': DonationForm(),
        'client_id': "AQZpCOXVV5Ty1J2hwt42OxHE65xmV-jfFm2E1YmY2pLdKwSH1Ip2G_wci7BdqMH3HzmghSzXYdw1lrfb"
    }
    return render(request, 'index.html', context)
