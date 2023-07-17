from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse
from math import ceil
#
# from mycart.shop.models import Product


def index(request):
    allparams=[]
    product=Product.objects.all()
    # print(product)
    n=len(product)
    nSlides=n//4 + ceil((n/4)-(n//4))
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),"product":product}
    catprods=Product.objects.values('category')
    cats= {items['category'] for items in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allparams.append([prod,range(1,nSlides),nSlides])
    print(allparams)
    # allparams=[[product,range(1,nSlides),nSlides],[product,range(1,nSlides),nSlides]]
    params={'allprods':allparams}
    return  render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")


def contact(request):
    return render(request,"shop/carlease.html")


def tracker(request):
    return HttpResponse("this is tracker")


def search(request):
    return HttpResponse("this is search")


def prodView(request):
    return HttpResponse("this is product view")


def checkout(request):
    return HttpResponse('this is checkout')

# def getdata(request):
#     data=Product.objects.all()
#     return data[0].product_name
