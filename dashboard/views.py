from django.shortcuts import render, redirect
from . models import * 

from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout


# To display authentication messages
from django.contrib import messages

# Create your views here.
def Login(request):
    if request.method == 'POST':
        uemail = request.POST['email']
        upassword = request.POST['password']

        user = authenticate(request, username=uemail, password=upassword)
        if user is not None :
            messages.info(request, f"You are now logged in as {uemail}.")
            login(request, user)
            return redirect('Dashboard')
        else:
            messages.warning(request, "User Not Found")
            return redirect('Login')

    return render(request, 'login.html')

def Profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Developed, Designed and Maintained by SEQTTO SOFTWARE SOLUTIONS \n If you trouble to login. mail: info@seqtto.com")
        return redirect('Login')
    
    context = {
        'username': request.user.username,
        'usermail': request.user.email,
    }
    
    return render(request, 'profile.html', context)

def Editprofile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')

    if request.method == 'POST':
        uname = request.POST['name']
        uemail = request.POST['email']
        upassword = request.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.info(request, "Username Already Exists")
            return redirect('Editprofile')

        elif User.objects.filter(email=uemail).exists():
            messages.info(request, "Email Already Exists")
            return redirect('register')

        else:
            user = User.objects.create_user(username=uname, email=uemail, password=upassword)
            return redirect('Login')

    return render(request, 'editdetails.html')

def Allevents(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    allevents = Events.objects.all()
    content = {'allevents': allevents}

    return render(request, 'events.html', content)

def AddEvent(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')

    if request.method == 'POST':
        cate = request.POST.get('category', 'dance')
        impp = request.POST.get('isImp', 'Not')
        name = request.POST.get('eventname', '').strip()
        url = request.POST.get('eventurl', '')
        des = request.POST.get('desc', '')
        event = request.POST.get('aboutevent', '')
        startdate = request.POST.get('start-date', None)
        if startdate == '':
            startdate = None

        starttime = request.POST.get('start-time', None)
        if starttime == '':
            starttime = None
        
        enddate = request.POST.get('end-date', None)
        if enddate == '':
            enddate = None
        
        endtime = request.POST.get('end-time', None)
        if endtime == '':
            endtime = None
            
        loc = request.POST.get('venue', '')
        imagess = request.FILES.get('images', None)

        record = Events.objects.create(
            Category = cate,
            Imp = impp,
            Eventname = name,
            Eventurl = url,
            Desc = des,
            Aboutevent = event,
            Start_date = startdate,
            Start_time = starttime,
            End_date = enddate,
            End_time = endtime,
            Venue = loc,
            Banner = imagess
        )

        record.save()
        messages.success(request, "Event created successfully!")
        
        return redirect('Allevents')

    return render(request, 'addevent.html')

def Editevents(request, id):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    val = Events.objects.get(id=id)
    
    return render(request, 'editevents.html', {'val': val})



def uprec(request, id):
    cate = request.POST.get('category', 'dance')
    impp = request.POST.get('isImp', 'Not')
    name = request.POST.get('eventname', '').strip()
    url = request.POST.get('eventurl', '')
    des = request.POST.get('desc', '')
    event = request.POST.get('aboutevent', '')
    startdate = request.POST.get('start-date', None)
    if startdate == '':
        startdate = None

    starttime = request.POST.get('start-time', None)
    if starttime == '':
        starttime = None
        
    enddate = request.POST.get('end-date', None)
    if enddate == '':
        enddate = None
        
    endtime = request.POST.get('end-time', None)
    if endtime == '':
        endtime = None
            
    loc = request.POST.get('venue', '')
    imagess = request.FILES.get('images', None)

    data = Events.objects.get(id=id)
    data.Category = cate
    data.Imp = impp
    data.Eventname = name
    data.Eventurl = url
    data.Desc = des
    data.Aboutevent = event
    data.Start_date = startdate
    data.Start_time = starttime
    data.End_date = enddate
    data.End_time = endtime
    data.Venue = loc
    data.Banner = imagess

    data.save()

    return redirect('Allevents')


def Delete(request, id):
    val = Events.objects.get(id=id)
    val.delete()

    return redirect('Allevents')

def Newss(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    if request.method == 'POST':
        news = request.POST['news']

        record = News.objects.create(New = news)
        record.save()

        return redirect('Home')

    return render(request, 'TrendingNews.html')

def Feedbacks(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        msg = request.POST['message']

        record = Feedback.objects.create(
            Name = name,
            Role = role,
            Message = msg,
        )
        
        record.save()

        return redirect('Dashboard')

    return render(request, 'feedback.html')

def Banners(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    banners = Banner.objects.all()
    content = {'banners': banners}
    
    return render(request, 'banners.html', content)

def Addbanner(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        image = request.FILES['images']

        record = Banner.objects.create(Title = title, Subtitle = subtitle, Image = image)
        record.save()

        return redirect('Banners')

    return render(request, 'addbaner.html')

def Addblog(request):
    if request.method == 'POST':
        name = request.POST['name']
        msg = request.POST['message']
        image = request.FILES.get('images', None)

        
        record = Blogs.objects.create(
            Name = name,
            Image = image,
            Message = msg
        )
        
        record.save()
        
        return redirect('Blog')
        
    return render(request, 'addblog.html')

def Blog(request):
    blogs = Blogs.objects.all()
    content = {'blogs': blogs}
    
    return render(request, 'blogs.html', content)



def Deleteblog(request, id):
    val = Blogs.objects.get(id=id)
    val.delete()

    return redirect('Blogs')

def Editbanner(request, id):
    val = Banner.objects.get(id=id)
    val.delete()

    return redirect('Banners')


def Dashboard(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Developed, Designed and Maintained by SEQTTO SOFTWARE SOLUTIONS \n If you trouble to login. mail: info@seqtto.com")
        return redirect('Login')
    
    return render(request, 'dboard.html')

def Useredit(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    return render(request, 'user edit.html')

def Mainusers(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey just login and use my website")
        return redirect('Login')
    
    users = User.objects.all()
    content = {'users': users}
    
    return render(request, 'users.html', content)



def Addgallery(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Hey, just login and use my website")
        return redirect('Login')
    
    if request.method == 'POST':
        # Get the uploaded images
        dancers_images = request.FILES.getlist('dancers')
        musicians_images = request.FILES.getlist('musics')

        # Create a new Gallery instance
        gallery = Gallery.objects.create()

        # Save Dancer images
        for image in dancers_images:
            Dancer.objects.create(gallery=gallery, image=image)

        # Save Musician images
        for image in musicians_images:
            Musician.objects.create(gallery=gallery, image=image)

        # Redirect to the Gallery page
        return redirect('Gallery')

    return render(request, 'addgallery.html')


def Newuser(request):
    return render(request, 'newuser.html')

def Logout(request):
    logout(request)
    return redirect('Home')