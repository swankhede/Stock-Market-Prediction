from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from mainApp.models import Companies
from lstm.RunModel import RunModel

# Create your views here.


def index(request):
    companies = Companies.objects.all()
    context = {
        'companies':companies
    }

    if request.method=="POST":
        pk = request.POST['option']
        company = Companies.get_company_by_id(pk)
        print(company.name)

        print(company.symbol)
        obj = RunModel(company)
        predicted = obj.predictPrice()
        print(predicted[0][0])
        context['pred_price'] = predicted[0][0]
    return render(request,'index.html',context=context)