from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegForm,ProductForm,BrandForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Mobile,Brand
from django.contrib import messages
from django.views.generic.base import View
# Create your views here.


def home(request):
    brands=Brand.objects.all()
    return render(request,'index.html',{'brands':brands})



def register(request):
    if request.method == 'POST':
        
        form = RegForm(request.POST)
        name = form.data['username'] 
        subject = 'Welcome to BargainBuddy ... Your New Shopping Companion!'
        message = f"""
            Dear {name},
            
            Welcome to BargainBuddy, your go-to destination for the best deals, discounts, and savings on the products you love! We're thrilled to have you join our growing community of savvy shoppers.

            At BargainBuddy, we understand the thrill of finding great deals and getting the most value for your money. Whether you're on the lookout for the latest gadgets, fashion trends, or household essentials, we're here to make your shopping experience more exciting and budget-friendly.

            Here's what you can expect from BargainBuddy:

            Personalized Recommendations:
            Discover products tailored to your preferences and interests. Our smart algorithms analyze your shopping history to provide you with personalized recommendations that suit your taste.

            Real-time Price Comparisons:
            Compare prices from various retailers to ensure you're getting the best possible deal. We do the hard work for you, so you can shop confidently and save money.

            Exclusive Offers and Promotions:
            Be the first to know about exclusive discounts, limited-time offers, and special promotions from your favorite brands. BargainBuddy members enjoy access to deals that others might miss.

            Savings Alerts:
            Set up alerts for your desired products, and we'll notify you when prices drop. Never miss a bargain again!

            To get started, log in to your BargainBuddy account and start exploring the world of unbeatable deals. Don't forget to customize your profile to enhance your shopping experience.

            Thank you for choosing BargainBuddy as your shopping companion. We're here to help you shop smarter and save more.

            Happy shopping!

            Best Regards,
            The BargainBuddy Team
            """
        from_email = settings.EMAIL_HOST_USER
        to_mail = [form.data['email']]
        if form.is_valid():
            form.save()
            send_mail(subject,message,from_email,to_mail)
            messages.success(request,"User Registration Successfull")
            return redirect(home)
    else:
        form = RegForm()
    return render(request,'register.html',{'form':form})

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print("User Logged in")
            messages.success(request, 'Successfully logged in ')
            return redirect(home)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')
def logoutp(request):
    logout(request)
    messages.success(request,'User Logged out')
    return redirect(home)


def products(request):
    product= Mobile.objects.all()
    return render(request,'products.html',{'product':product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(products)
    else:
        form = ProductForm()
        
    return render(request, 'add_product.html', {'form': form})



def more_details(request, phone_id):
    Learn_more = Mobile.objects.filter(phone_id=phone_id)
    return render(request, 'details.html', {'Learn_more': Learn_more})


def delete_item(request,phone_id):
    demp = Mobile.objects.get(phone_id=phone_id)
    demp.delete()
    return redirect(products)


def edit_item(request,phone_id):
   
    item = get_object_or_404(Mobile, phone_id=phone_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=item)  
        if form.is_valid():
            form.save()
            return redirect(products) 
    else:
        form = ProductForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})

    

def compare(request):
    products=Mobile.objects.all()
    return render(request,'compare.html',{'products':products})

def comparison_result(request):
    if request.method == 'POST':
        product1_id = request.POST.get('product1')
        product2_id = request.POST.get('product2')

        
        product1 = get_object_or_404(Mobile, phone_id=product1_id)
        product2 = get_object_or_404(Mobile, phone_id=product2_id)

        
        price_difference = abs(product1.price - product2.price)

        context = {
            'product1': product1,
            'product2': product2,
            'price_difference': price_difference,
        }

        return render(request, 'comparison_result.html', context)
    else:
        
        pass
    
    


def search_results(request):
    query = request.GET.get('q', '') 
    results = Mobile.objects.filter(model_name__istartswith=query)  
    return render(request, 'search_results.html', {'query': query, 'results': results})



def user_list(request):
    users = User.objects.all()
    return render(request,'user.html',{'users':users})


def delete_user(request, username):
    del_user = get_object_or_404(User, username=username)
    del_user.delete()
    return redirect(user_list) 


def brand_list(request):
    brand=Brand.objects.all()
    return render(request,'brands.html',{'brand':brand})

def brand_items(request, brand_id):
    brand = get_object_or_404(Brand, brand_id=brand_id)
    items = Mobile.objects.filter(brand=brand)
    return render(request, 'branditems.html', {'brand': brand, 'items': items})


def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(brand_list)
    else:
        form = BrandForm()
        
    return render(request, 'add_brand.html', {'form': form})



def brand_details(request, brand_id):
    brand_det= get_object_or_404(Brand, brand_id=brand_id)
    return render(request, 'brand_details.html', {'brand_det': brand_det})


def edit_brand(request, brand_id):
    brand = get_object_or_404(Brand, brand_id=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            # Redirect to a suitable page after successful update
            return redirect('brand_details', brand_id=brand_id)
    else:
        form = BrandForm(instance=brand)

    return render(request, 'edit_brand.html', {'form': form, 'brand': brand})

def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, brand_id=brand_id)
    brand.delete()
    return redirect(brand_list)
