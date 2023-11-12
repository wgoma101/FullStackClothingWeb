from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Feedback
from django.contrib import messages
from django.views import View

from .forms import FeedbackForm
#class based view
class IndexView(View):
    def get(self, request):
        user = "wilson"
        product_numb = 7
        products = Product.objects.all().order_by("id")[:4]#limit to 4 suits
        #handle request, renders home.html, passes in values
        return render(request,"products/home.html",{
            "name":user,
            "product_numb":product_numb,
            "products":products,  
        })
    def post(self, request):
        pass
# Create your views here.
#home page default is get request
def index(request):
    user = "wilson"
    product_numb = 7
    products = Product.objects.all().order_by("id")[:4]#limit to 4 suits
    #handle request, renders home.html, passes in values
    return render(request,"products/home.html",{
        "name":user,
        "product_numb":product_numb,
        "products":products,  
    })

#renders signup page
def signup(request):
    return render(request,"products/signup.html")

productArr = ["suits","dresses","shirts","shoes"]
def product_cat(request,product):
    if product in productArr:
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page you are looking for does not exsist")
#class based view
class ProductPageView(View):
    def get(self,product_brand,product_slug):
        product = Product.objects.get(slug=product_slug)
        my_feedback = Feedback.objects.get(product=product,id = 2)
        form = FeedbackForm(instance=my_feedback)
        reviews = Feedback.objects.filter(product=product)
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
       
    def post(self,product_brand,product_slug):
        product = Product.objects.get(slug=product_slug)
        my_feedback = Feedback.objects.get(product=product,id = 2)
        form = FeedbackForm(request.POST,instance=my_feedback)
        reviews = Feedback.objects.filter(product=product)
        if form.is_valid():
            form.save()
            #show success message
            messages.success(request,"Your feedback was submitted successfully")
            form = FeedbackForm()
            #return to product page and show all feedbacks
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
        


#create product page
def product_page(request,product_brand,product_slug):
    product = Product.objects.get(slug=product_slug)
    my_feedback = Feedback.objects.get(product=product,id = 2)
    form = FeedbackForm(instance=my_feedback)
    reviews = Feedback.objects.filter(product=product)
    #handles get requests
    if request.method == "GET":
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
    #hands post requests, in the case of feedback
    else:
        #adding instance to be able to edit
        form = FeedbackForm(request.POST,instance=my_feedback)
        if form.is_valid():
            form.save()
            #show success message
            messages.success(request,"Your feedback was submitted successfully")
            form = FeedbackForm()
            #return to product page and show all feedbacks
        return render(request,"products/product.html",{
            "product":product,  
            "form":form,
            "reviews":reviews,
        })
    
    