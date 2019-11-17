from django.shortcuts import render
from GraffersID.company.models import CompanyInfoModel

def home_view(request):
    records_holder = CompanyInfoModel.objects.all()
    context={
        'records':records_holder
    }
    return render(request,'home.html',context)
