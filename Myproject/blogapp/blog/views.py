from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category, BlogCity, TripCity





def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()  
    }
    return render(request, "blog/index.html", context)



def blogs(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all() 
    }
    return render(request, "blog/blogs.html", context)


def blogs_city(request):
    context = {
        "blogs_city": BlogCity.objects.all(),
        "categories": Blog.objects.all() 
   }
    return render(request, "blog/blogs_city.html", context)



def blogs_details(request, slug):
    blog = TripCity.objects.get(slug=slug)
    
    return render(request, "blog/blogs_details.html", {
        "blog":blog
    })



def blogs_by_category(request, slug):
    c = Category.objects.get(slug=slug)   #Buradan sectigimiz tek bir kategori geldi
    context = {
        "blogs": c.blog_set.filter(),         #blog_set diyerek(model ismi + _set) sectigimiz kategorinin bloklarını almıs oluyoruz blogs demedik cünkü model icinde tanımlamadık categories i tanımladık
        # "blogs": Blog.objects.filter(is_active=True, category__slug=slug),  #iliskili olan kategori kaydına göre slug bilgisini alacagız sonra parametre olarak gelen slug bilgisine esitleyecegiz. Yani kategorısi slug olan bilgiler filtrelenmis olacak
        "categories": Category.objects.all(),
        "selected_category": slug, 
    }
    return render(request, "blog/blogs.html", context)


    
def city_by_blog(request, slug):
    
    context = {
        "blogs_city": BlogCity.objects.filter(is_active=True, category_ulke__slug=slug),  #iliskili olan kategori kaydına göre slug bilgisini alacagız sonra parametre olarak gelen slug bilgisine esitleyecegiz. Yani kategorısi slug olan bilgiler filtrelenmis olacak
        "category_ulke": Blog.objects.all(),
        "selected_category": slug, 
    }
    return render(request, "blog/blogs_city.html", context)




def trip_by_city(request, slug):
    
    context = {
        "trips_city": TripCity.objects.filter(is_active=True, category_city__slug=slug),  #iliskili olan kategori kaydına göre slug bilgisini alacagız sonra parametre olarak gelen slug bilgisine esitleyecegiz. Yani kategorısi slug olan bilgiler filtrelenmis olacak
        "category_city": BlogCity.objects.all(),
        "selected_category": slug, 
    }
    return render(request, "blog/blogs_city_trip.html", context)