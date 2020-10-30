import base64
from django.shortcuts import render
from .models import Friends, Family, Lovelies, Video
from django.contrib.postgres.lookups import Unaccent
import playsound


# Create your views here.

def home(request):
    # playsound.playsound('myapp/static/myapp/media/H2.mp3', False)
    return render(request, "myapp/home.html")


def friends(request):
    model = Friends
    friendsData = []

    for f in Friends.objects.all().order_by('name'):
        image_url = f.image.url
        friendsData.append((f.name, image_url[7:], f.message))

    stuff_to_frontend = {
        'friends': friendsData,
    }
    return render(request, "myapp/friends.html", stuff_to_frontend)


def family(request):
    model = Family
    familyData = []

    for f in Family.objects.all().order_by('name'):
        image_url = f.image.url
        familyData.append((f.name, image_url[7:], f.message))
    stuff_to_frontend = {
        'family': familyData,
    }
    return render(request, "myapp/family.html", stuff_to_frontend)


def lovelies(request):
    model = Lovelies
    loveliesData = []

    for l in Lovelies.objects.all().order_by('name'):
        image_url = l.image.url
        loveliesData.append((l.name, image_url[7:], l.message))

    stuff_to_frontend = {
        'lovelies': loveliesData,
    }
    return render(request, "myapp/lovelies.html", stuff_to_frontend)


def searchFound(request):
    name = request.POST.get('searchwindow')
    print(name)
    data = []
    displaylist = []

    try:
        data.append((Friends.objects.get(name__startswith=name)))
    except:
        print("No Friends found")

    try:
        data.append((Family.objects.get(name__startswith=name)))
    except:
        print("No Family found")

    try:
        data.append((Lovelies.objects.get(name__startswith=name)))
    except:
        print("No Lovelies found")

    length = len(data)

    for i in range(length):
        displaylist.append((data[i].name, data[i].image.url[7:]))

    # if Friends.objects.filter(name=name):
    #     data = (Friends.objects.get(name=name))
    # elif Family.objects.filter(name=name):
    #     data = (Family.objects.get(name=name))
    # elif Lovelies.objects.filter(name=name):
    #     data = (Lovelies.objects.get(name=name))

    # if data:
    #     # if True:
    #     message = data.message
    #     image_path = data.image.url[1:]
    # else:
    #     message = "................."
    #     image_path = ('myapp/static/myapp/images/main.png')
    #     # image_path = ('/home/pi/PythonProg/Pbday/myapp/static/myapp/images/main.png')
    #
    # with open(image_path, "rb") as image_file:
    #     image_data = base64.b64encode(image_file.read()).decode('utf-8')

    # detail = {
    #     'name': name1,
    #     'photo': image_data,
    #     'message': message
    # }

    stuff_to_frontend = {
        'length': length,
        'displaylist': displaylist,
    }

    return render(request, "myapp/newsearchfound.html", stuff_to_frontend)


def detailView(request, name):
    data = []

    if Friends.objects.filter(name=name):
        data = (Friends.objects.get(name=name))
    elif Family.objects.filter(name=name):
        data = (Family.objects.get(name=name))
    elif Lovelies.objects.filter(name=name):
        data = (Lovelies.objects.get(name=name))

    if data:
        message = data.message
        image_path = data.image.url[1:]

    else:
        message = "................."
        image_path = ('myapp/static/myapp/images/main.png')

    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    # print(image_data)
    detail = {
        'name': name,
        'photo': image_data,
        'message': message
    }

    return render(request, "myapp/detail.html", detail)


