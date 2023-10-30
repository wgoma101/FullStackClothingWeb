from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Feedback
from django.contrib import messages

from .forms import FeedbackForm

# Create your views here.

def index(request):
    user = "wilson"
    product_numb = 7
    products = Product.objects.all().order_by("id")[:4]
    return render(request,"products/home.html",{
        "name":user,
        "product_numb":product_numb,
        "products":products,  
    })

def signup(request):
    return render(request,"products/signup.html")

productArr = ["suits","dresses","shirts","shoes"]
def product_cat(request,product):
    if product in productArr:
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page you are looking for does not exsist")

def product_page(request,product_brand,product_slug):
    product = Product.objects.get(slug=product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(product=product)
    if request.method == "GET":
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
    
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name = form.cleaned_data["name"],
                rating = form.cleaned_data["rating"],
                product = product,
                text = form.cleaned_data["text"],
            )
            feedback.save()
            messages.success(request,"Your feedback was submitted successfully")
            form = FeedbackForm()
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
    
    