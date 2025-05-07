from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    context = {
        'team': ['Алексей', 'Мария', 'Иван']
    }
    return render(request, 'global/contacts.html', context)
