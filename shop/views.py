from datetime import datetime, timezone
import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Create your views here.
from django.contrib.auth.models import User as Person, Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password

<<<<<<< HEAD
from . models import AssignTable, Cart, ChatTable, ComplaintTable, DeliveryStaff, FarmerTable, Feedback, Login, OrderMain, OrderSub, Payment, ProductTable, UserTable
=======
from . models import AssignTable, ChatTable, ComplaintTable, DeliveryStaff, FarmerTable, Feedback, Login, OrderMain, Payment, ProductTable, UserTable
>>>>>>> 3528a25 (Add requirements.txt)


def home(request):
    return render(request,'home.html')

<<<<<<< HEAD

def logout1(request):
    return render(request, "home.html")


def loginpage(request):
    if 'submit' in request.POST:
     a = request.POST['username']
     b=request.POST['pwd']
     l=Login(username= a,password=b)
     l.save()
    return HttpResponse("<script>alert('login successfully!');window.location='/login'</script>")
    return render(request,'login.html')

=======
>>>>>>> 3528a25 (Add requirements.txt)
def adminhome(request):
    return render(request,'ad/adminhome.html')

def userhome(request):
    return render(request,'User/home.html')

def user(request):
    if 'submit' in request.POST:
        a = request.POST['username']
        b = request.POST['password']
<<<<<<< HEAD
        print(a,b)
        try:
            p = authenticate(request,username=a, password=b)
            login(request,p)
            if p.groups.filter(name='admin').exists():
                print("kkkkkkkkkkkkk")

                return HttpResponse("<script>alert('Admin was Logged successfully!');window.location='/shop/adminhome'</script>")
        except:
            return HttpResponse("<script>alert('invalid username and password!');window.location='/login'</script>")

=======
        try:
            o = authenticate(request,username=a, password=b)
            login(request, o)
        except:
            return HttpResponse("<script>alert('invalid username and password!');window.location='/login'</script>")
        try:
            o=Person.objects.get(username=a,password=b)
            if o.groups.filter(name='admin').exists():
                return HttpResponse("<script>alert('Admin was Logged successfully!');window.location='/adminhome'</script>")
            elif o.groups.filter(name='user').exists():
                request.session['uid'] = o.id
                farmer=UserTable.objects.get(user_id=o.id)
                request.session['fid'] = farmer.id
                return HttpResponse("<script>alert('Logged in successfully!');window.location='/userhome'</script>")
    
            else:
               return HttpResponse("<script>alert('Invalid username or password');window.location='/login';</script>")
        except Person.DoesNotExist:
            return render(request,'login.html',{'error':'Invalid Username or password'})
>>>>>>> 3528a25 (Add requirements.txt)
            
    return render(request, 'login.html')

def userlogin(request):
    username = request.POST.get('uname')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({'status': 'error', 'message': 'Username and password required'})

    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse({'status': "error", 'message': 'Invalid username or password'})

    login(request, user)
    
    data=[]
    
    if user.groups.filter(name='user').exists():
        data.append({
            'status': 'success',
            'message': 'Login successful',
            'usertype': 'user',
            'login_id': user.id,

        })
    else:
         data.append({
            'status': 'success',
            'message': 'Login successful',
            'usertype': 'other',
            'login_id': user.id
        })

    return JsonResponse(response = {'data':data})


<<<<<<< HEAD

def slogin(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')

    user = authenticate(username=uname, password=pwd)
    print("Ssssssssssss",user)
    if user is not None:  
        login(request, user)
        print(user, 'ggggggggggg')

        if user.groups.filter(name='user').exists():
            s = UserTable.objects.get(login_id=user.id)
            response = {
                'type': 'user',
                'lid': user.id,
                'uid':s.id,
            }

        elif user.groups.filter(name='farmer').exists():
            print("sssssssssssshjbdjknjkas")
            p = FarmerTable.objects.get(login_id=user.id)
            response = {
                'type': 'farmer',
                'lid': user.id,
                'uid':p.id


            }

        elif user.groups.filter(name='deliverystaff').exists():
            d = DeliveryStaff.objects.get(login_id=user.id)
            response = {
                'type': 'deliverystaff',
                'lid': user.id,
                'uid':d.id
            }
        else:
            response = {'status': 'No group assigned'}

    else:  # ✅ invalid login
        response = {'status': 'Invalid Username or Password'}

    return JsonResponse(response)

=======
def applogin(request):
 uname=request.POST['uname']
 pwd=request.POST['pwd']
 try:
    user=authenticate(username=uname, password=pwd)
    login(request, user)
    if user.groups.filter(name='user').exists():
        s=UserTable.objects.get(user_id=user.id)
        response={
            'type':'user',
            'uid':s.id,
            'uimg':s.image.name,

        }
                
    elif user.groups.filter(name='farmer').exists():
        p=FarmerTable.objects.get(user_id=user.id)

        response={
            'type':'farmer',
            'uid':p.id,
        }  
    elif user.groups.filter(name='delivery staff').exists():
        p=DeliveryStaff.objects.get(user_id=user.id)

        response={
            'type':'deliverystaff',
            'uid':p.id,
        }  
 except:
    response={
        'status':'Invalid Username or Password',
    }  
 print(response)
 return JsonResponse(response)
>>>>>>> 3528a25 (Add requirements.txt)

def userregistration(request):

        name = request.POST['name']
<<<<<<< HEAD
        dob = request.POST['dob']
        gender = request.POST['gender']
        photo = request.FILES['photo']
=======
        dob = request.POST['date']
        gender = request.POST['gender']
        photo = request.FILES['image']
>>>>>>> 3528a25 (Add requirements.txt)
        phone = request.POST['phone']
        email = request.POST['email']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        district = request.POST['district']
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        fs = FileSystemStorage()
        img_path = fs.save(photo.name, photo)


        r= User.objects.create( username=uname, password=make_password(pwd))



        r.groups.add(Group.objects.get(name='user'))
        print(r,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')


        ud = UserTable(
            name=name,
            dob=dob,
            gender=gender,
            photo=img_path,
            place=place,
            post=post,
            pin=pin,
            district=district,
            phone=phone,
            email=email,
            login_id=r.pk,
        )
        ud.save()
<<<<<<< HEAD
        response = ({'status': 'success', 'message': 'Account created', 'usertype': 'user', 'login_id':r.pk})
        return JsonResponse(response)



def deliverystaffregister(request):
    
      
            name = request.POST['name']
            dob = request.POST['dob']         
            gender = request.POST['gender']
            phone = request.POST['phone']
            email = request.POST['email']
            place = request.POST['place']
            post = request.POST['post']
            pin = request.POST['pin']
            district = request.POST['district']
            drivinglicense = request.POST['drivinglicense']
            username = request.POST['username']
            password = request.POST['password']
            print(name,'iiiiiiiiiiiiiiiiiiii')
            

            u=User.objects.create(username=username,password=make_password(password))
            u.groups.add(Group.objects.get(name='deliverystaff'))
            staff = DeliveryStaff(
                name=name,
                dob=dob,
                gender=gender,
                email=email,
                phone=phone,
                place=place,
                post=post,
                pin=pin,
                district=district,
                drivinglicense=drivinglicense,
                username=username,
                password=password,
                login_id=u.pk
            )
            staff.save()
            return JsonResponse({"status": "success", "message": "Delivery staff registered successfully"})
        
 
=======
        return JsonResponse({'status': 'success', 'message': 'Account created', 'usertype': 'user', 'login_id':r.pk})
>>>>>>> 3528a25 (Add requirements.txt)



def viewusers(request):
    users = UserTable.objects.all()
    return render(request, 'ad/viewuser.html', {'users': users})


def viewreport(request):
    reports = OrderMain.objects.all().select_related('user', 'farmer')
    return render(request, 'ad/viewreport.html', {'reports': reports})

def viewfeedback(request):
    feedbacks = Feedback.objects.select_related('product', 'user').all()
    return render(request, 'ad/viewfeedback.html', {'feedbacks': feedbacks})

def viewrating(request):
    ratings = Feedback.objects.select_related('product', 'user').all()
    return render(request, 'ad/viewrating.html', {'ratings': ratings})

def view_complaints(request):
    complaints = ComplaintTable.objects.select_related('login').all()
    return render(request, 'ad/viewcomplaints.html', {'complaints': complaints})


<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from .models import ComplaintTable

def viewcomplaints(request):
    if request.method == "POST" and 'submit' in request.POST:
        cid = request.POST.get('cid')  
        reply = request.POST.get('reply')
=======
def viewcomplaints(request):
    if 'submit' in request.POST:
        cid = request.POST['cid']
        reply = request.POST['reply']
>>>>>>> 3528a25 (Add requirements.txt)

        try:
            c = ComplaintTable.objects.get(id=cid)
            c.reply = reply
            c.status = "Replied"
            c.save()
<<<<<<< HEAD
            return HttpResponse("<script>alert('Reply sent');window.location='/shop/viewcomplaints/';</script>")
        except ComplaintTable.DoesNotExist:
            return HttpResponse("<script>alert('Error sending reply');window.location='/shop/viewcomplaints/';</script>")
=======
            return HttpResponse("<script>alert('Reply sent');window.location='/view_complaints';</script>")
        except:
            return HttpResponse("<script>alert('Error sending reply');window.location='/view_complaints';</script>")
>>>>>>> 3528a25 (Add requirements.txt)

    complaints = ComplaintTable.objects.select_related('login').all()
    return render(request, 'ad/viewcomplaints.html', {'complaints': complaints})

<<<<<<< HEAD

=======
>>>>>>> 3528a25 (Add requirements.txt)
def verifyusers(request):
    users = UserTable.objects.all()
    return render(request, 'ad/verifyuser.html', {'users': users})
    
<<<<<<< HEAD
from django.shortcuts import redirect, get_object_or_404
from .models import UserTable  # replace with your actual user model

def uaccepted(request,id):
    user = get_object_or_404(UserTable, id=id)
    user.status = "accepted"
    user.save()
    return redirect('/shop/viewusers/')   # change redirect path to your user listing page

def urejected(request,id):
    user = get_object_or_404(UserTable, id=id)
    user.status = "rejected"
    user.save()
    return redirect('/shop/viewusers/')   # change redirect path to your user listing page
=======

def acceptuser(request, id):
    s=UserTable.objects.all()
    u = UserTable.objects.get(id=id)
    u.status = 'accepted'
    u.save()
    return HttpResponse("<script>alert('Rejected');window.location='/ad/verifyuser'</script>")

def rejectuser(request,id):
    s=UserTable.objects.all()
    u = UserTable.objects.get(id=id)
    u.status = 'rejected'
    u.save()
    return HttpResponse("<script>alert('Rejected');window.location='/ad/verifyuser'</script>")
>>>>>>> 3528a25 (Add requirements.txt)


def verifydelivery(request):
    staff = DeliveryStaff.objects.all()
    return render(request, 'ad/verifydstaff.html', {'staff': staff})

def acceptdelivery(request,id):
    d = DeliveryStaff.objects.get(id=id)
    d.status = 'accepted'
    d.save()
    return HttpResponse("<script>alert('Accepted');window.location='/ad/verifydstaff'</script>")

def rejectdelivery(request,id):
    d = DeliveryStaff.objects.get(id=id)
    d.status = 'rejected'
    d.save()
    return HttpResponse("<script>alert('Rejected');window.location='/ad/verifydstaff'</script>")



def usercheck(request):
    users = UserTable.objects.all()
    return render(request, 'ad/usercheck.html', {'users': users})


def blockdelivery(request,id):
    d = UserTable.objects.get(id=id)
    d.blocked = True
    d.save()
    return HttpResponse("<script>alert('Blocked');window.location='/ad/usercheck'</script>")

def unblockdelivery(request, id):
    d = UserTable.objects.get(id=id)
    d.blocked = False
    d.save()
    return HttpResponse("<script>alert('Unblocked');window.location='/ad/usercheck'</script>")


def verifyfarmers(request):
    farmers = FarmerTable.objects.all()
    return render(request, 'ad/farmercheck.html', {'farmers': farmers})


def blockfarmer(request,id):
        farmer = FarmerTable.objects.get(id=id)
        farmer.blocked = True
        farmer.status = 'blocked' 
        farmer.save()
        return HttpResponse("<script>alert('Farmer Blocked');window.location='/ad/farmercheck'</script>")



def unblockfarmer(request,id):

        farmer = FarmerTable.objects.get(id=id)
        farmer.blocked = False
        farmer.status = 'unblocked'  
        farmer.save()
        return HttpResponse("<script>alert('Farmer Unblocked');window.location='/ad/farmercheck'</script>")

def verifydeliverystaff(request):
    staff = DeliveryStaff.objects.all()
    return render(request, 'ad/staff.html', {'staff': staff})

def blockdeliverystaff(request,id):
    staff = DeliveryStaff(id=id)
    staff.blocked = True
    staff.status = 'blocked'
    staff.save()
    return HttpResponse("<script>alert('Delivery Staff Blocked');window.location='/ad/staff'</script>")


def unblockdeliverystaff(request, id):
    staff = DeliveryStaff(id=id)
    staff.blocked = False
    staff.status = 'unblocked'
    staff.save()
    return HttpResponse("<script>alert('Delivery Staff Unblocked');window.location='/ad/staff'</script>")

<<<<<<< HEAD
# def view_feedback(request):
#         feedbacks = Feedback.objects.all().order_by('-date')
#         data = []
#         for fb in feedbacks

#             {
#                 'user': fb.user.username if fb.user else None,
#                 'message': fb.message,
#                 'date': fb.date.strftime('%Y-%m-%d %H:%M:%S'),
#             }
#         ]
#         return JsonResponse({'status': 'success', 'feedbacks': data})
=======
# `#user module
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage
# from .models import UserTable
# from django.http import JsonResponse

# @csrf_exempt
# def updateprofile(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')

#         try:
#             user = UserTable.objects.get(login_id=user_id)
#             user.name = request.POST.get('name')
#             user.email = request.POST.get('email')
#             user.phone = request.POST.get('phone')
#             user.place = request.POST.get('place')
#             user.post = request.POST.get('post')
#             user.pin = request.POST.get('pin')
#             user.district = request.POST.get('district')

#             if 'photo' in request.FILES:
#                 image = request.FILES['photo']
#                 fs = FileSystemStorage()
#                 saved_path = fs.save(image.name, image)
#                 user.photo = saved_path

#             user.save()
#             return JsonResponse({'status': 'success'})
#         except UserTable.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'User not found'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid method'})

# def updateprofile(request):
#     data=[]
#     f=request.POST['uid']
#     d=UserTable.objects.all()
#     for i in d:
#         data.append([
            
#         ])

#         user_id = request.POST.get('user_id')
#         user = UserTable.objects.get(login_id=user_id)
#         user.name = request.POST.get('name')
#         user.email = request.POST.get('email')
#         user.phone = request.POST.get('phone')
#         user.place = request.POST.get('place')
#         user.post = request.POST.get('post')
#         user.pin = request.POST.get('pin')
#         user.district = request.POST.get('district')

#         image = request.FILES['photo']
#         fs = FileSystemStorage()
#         saved_path = fs.save(image.name, image)
#         user.photo = saved_path

#         user.save()
#         return JsonResponse({'status': 'success'})
        
# def submit_review(request):
    
#             user_id = request.POST['user_id']
#             product_id = request.POST['product_id']
#             review_text = request.POST['review']
#             rating = request.POST['rating']

#             user = UserTable.objects.get(id=user_id)
#             product = ProductTable.objects.get(id=product_id)

#             Feedback.objects.create(
#                 user=user,
#                 product=product,
#                 review=review_text,
#                 rating=rating
#             )

#             return JsonResponse({'status': 'success', 'message': 'Review submitted successfully'})




# def send_user_complaint(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             user_id = data['user_id']
#             subject = data['subject']
#             message = data['message']

#             user = UserTable.objects.get(id=user_id)  # or UserTable
#             ComplaintTable.objects.create(
#                 user=user,
#                 subject=subject,
#                 message=message
#             )

#             return JsonResponse({'status': 'success', 'message': 'Complaint submitted successfully'})

# def edituserprofile(request, user_id):
#     try:
#         user = UserTable.objects.get(id=user_id)
#     except UserTable.DoesNotExist:
#         return render(request, 'user/error.html', {'error': 'User not found'})

#     if request.method == 'POST':
#         user.name = request.POST['name']
#         user.email = request.POST['email']
#         user.phone = request.POST['phone']
#         user.place = request.POST['place']
#         user.post = request.POST['post']
#         user.pin = request.POST['pin']
#         user.district = request.POST['district']
#         user.dob = request.POST['dob']
#         user.gender = request.POST['gender']
#         user.username = request.POST['uname']
#         user.password=request.POST['pwd']


#         if 'photo' in request.FILES:
#             photo_file = request.FILES['photo']
#             fs = FileSystemStorage()
#             filename = fs.save(photo_file.name, photo_file)
#             user.photo = filename
#             user.save()
#         return render(request, 'user/profilesuccess.html', {'message': 'Profile updated successfully'})

#     return render(request, 'user/editprofile.html', {'user': user})

def user_chat_with_farmer(request):
    data = []

    from_id = request.POST.get('from_id')       # User/Farmer login ID
    to_id = request.POST.get('to_id')           # Farmer/User login ID
    message = request.POST.get('message')
    sender = request.POST.get('sender')         # "user" or "farmer"
    receiver = request.POST.get('receiver')     # "user" or "farmer"


    c = ChatTable(
        date=datetime.now(),
        message=message,
        FROMID=from_id,
        TOID=to_id,
        sender_type=sender,
        reciever_type=receiver,
    )
    c.save()

    # Retrieve full chat history between both parties
    messages = ChatTable.objects.filter(
        FROMID_id__in=[from_id, to_id],
        TOID_id__in=[from_id, to_id],
        sender_type__in=[sender, receiver],
        reciever_type__in=[sender, receiver]
    ).order_by('date')

    # Format messages
    for i in messages:
        data.append({
            'message': i.message,
            'date': i.date.strftime("%Y-%m-%d %H:%M:%S"),
            'sender': i.sender_type,
            'receiver': i.reciever_type,
            'from_id': i.FROMID_id,
            'to_id': i.TOID_id,
        })

    return JsonResponse({'status': 'success', 'chat': data})

# def user_chat_with_delivery(request):
#         data=[]
#         from_id = request.POST.get('from_id')  # User login ID
#         message = request.POST.get('message')
#         to_id = request.POST.get('to_id')  # User login ID
#         sender = request.POST.get('sender')  # User login ID
#         reciever = request.POST.get('reciever')  # User login ID



#         c=ChatTable(
#                 date=datetime.now(),
#                 message=message,
#                 FROMID=from_id,
#                 TOID=to_id,
#                 sender_type = sender,
#                 reciever_type=reciever,

#             )
#         c.save()

#         messages = ChatTable.objects.filter(
#         FROMID_id__in=[from_id, to_id],
#         TOID_id__in=[from_id, to_id],
#         sender_type__in=[sender,reciever],
#         reciever_type__in=[sender,reciever]

#         ).order_by('date')
#         for i in messages:
#             data.append({
#             'messages': messages,
#             'from_id': from_id,
#             'to_id': to_id,
#             'sender':i.sender_type,
#             'reciever':i.reciever_type,
#         })
    

# def get_user_profile(request, user_id):
#     try:
#         user = UserTable.objects.get(id=user_id)
#         profile = UserTable.objects.get(user=user)

#         data = {
#             'username': user.username,
#             'email': user.email,
#             'phone': profile.phone,
#             'place': profile.place,
#             'photo': profile.photo.url if profile.photo else None,
#         }
#         return JsonResponse({'status': 'success', 'profile': data})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})



# def update_user_profile(request):
    
#             data = json.loads(request.body)
#             user_id = data['user_id']

#             user = user.objects.get(id=user_id)
#             profile = UserTable.objects.get(user=user)

         
#             user.email = data.get('email', user.email)
#             profile.phone = data.get('phone', profile.phone)
#             profile.place = data.get('place', profile.place)

#             user.save()
#             profile.save()

#             return JsonResponse({'status': 'success', 'message': 'Profile updated successfully'})

   

# def farmer_register(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             name = data.get('name')
#             dob = data.get('dob')
#             gender = data.get('gender')
#             email = data.get('email')
#             phone = data.get('phone')
#             place = data.get('place')
#             post = data.get('post')
#             pin = data.get('pin')
#             district = data.get('district')
#             username = data.get('username')
#             password = data.get('password')

           
#             if FarmerTable.objects.filter(username=username).exists():
#                 return JsonResponse({'status': 'error', 'message': 'Username already exists'})
#             if FarmerTable.objects.filter(email=email).exists():
#                 return JsonResponse({'status': 'error', 'message': 'Email already exists'})

#             FarmerTable.objects.create(
#                 name=name,
#                 dob=dob,
#                 gender=gender,
#                 email=email,
#                 phone=phone,
#                 place=place,
#                 post=post,
#                 pin=pin,
#                 district=district,
#                 username=username,
#                 password=password,  
#                 status='pending'
#             )
#             return JsonResponse({'status': 'success', 'message': 'Farmer registered successfully'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

# def update_farmer_profile(request, id):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

            
#             farmer = FarmerTable.objects.get(id=id)

#             # Update fields (default to existing if not provided)
#             farmer.name = data.get('name', farmer.name)
#             farmer.dob = data.get('dob', farmer.dob)
#             farmer.gender = data.get('gender', farmer.gender)
#             farmer.email = data.get('email', farmer.email)
#             farmer.phone = data.get('phone', farmer.phone)
#             farmer.place = data.get('place', farmer.place)
#             farmer.post = data.get('post', farmer.post)
#             farmer.pin = data.get('pin', farmer.pin)
#             farmer.district = data.get('district', farmer.district)

#             # Optional: update password only if provided
#             if 'password' in data and data['password']:
#                 farmer.password = data['password']  # hash if needed

#             # Save changes
#             farmer.save()

#             return JsonResponse({'status': 'success', 'message': 'Profile updated successfully'})

#         except FarmerTable.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Farmer not found'})
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

 
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import FarmerTable  # Adjust as needed


# def farmer_login(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             username = data.get('username')
#             password = data.get('password')

#             # Check credentials
#             farmer = FarmerTable.objects.filter(username=username, password=password, blocked=False).first()

#             if farmer:
#                 return JsonResponse({
#                     'status': 'success',
#                     'message': 'Login successful',
#                     'data': {
#                         'id': farmer.id,
#                         'name': farmer.name,
#                         'email': farmer.email,
#                         'phone': farmer.phone,
#                         'district': farmer.district,
#                         'status': farmer.status,
#                     }
#                 })
#             else:
#                 return JsonResponse({
#                     'status': 'error',
#                     'message': 'Invalid credentials or account is blocked'
#                 })

#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': f'Exception: {str(e)}'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
# def edit_product(request,id):
   
#         try:
#             product = ProductTable.objects.get(id=id)
#             data = request.POST

#             product.name = data.get('name')
#             product.description = data.get('description')
#             product.quantity = data.get('quantity')
#             product.price = data.get('price')

#             if 'image' in request.FILES:
#                 product.image = request.FILES['image']

#             product.save()
#             return JsonResponse({'status': 'success', 'message': 'Product updated successfully'})
#         except ProductTable.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Product not found'})
  


# def delete_product(request, id):
#     try:
#         product = ProductTable.objects.get(id=id)
#         product.delete()
#         return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
#     except ProductTable.DoesNotExist:
#         return JsonResponse({'status': 'error', 'message': 'Product not found'})
    

# from django.shortcuts import get_object_or_404

# def view_orders(request):
#     orders = OrderMain.objects.all().order_by('-order_date')
#     data = []

#     for order in orders:
#         items = order.items.all()
#         item_list = [{
#             'product': item.product.name,
#             'quantity': item.quantity
#         } for item in items]

#         data.append({
#             'order_id': order.id,
#             'user': order.user.username,
#             'status': order.status,
#             'order_date': order.order_date.strftime('%Y-%m-%d %H:%M'),
#             'items': item_list,
#         })

#     return JsonResponse({'status': 'success', 'orders': data})



# def verify_order(request,id):
#         data=[]
#         u=request.POST['uid']
#         order = OrderMain.objects.get(id=id)
#         order.status = 'verified'
#         order.save()
#         return JsonResponse({'status': 'success', 'message': 'Order verified'})
#
#
# def view_feedback(request):
#     feedbacks = Feedback.objects.all().order_by('-date')
#     data = []
#
#     for fb in feedbacks:
#         data.append({
#             'user': fb.user.username,
#             'message': fb.message,
#             'date': fb.date.strftime('%Y-%m-%d %H:%M:%S'),
#         })
#
#     return JsonResponse({'status': 'success', 'feedbacks': data})

# def send_chat_message(request):
   
#         data = json.loads(request.body)
#         sender_id = data.get('sender_id')
#         receiver_id = data.get('receiver_id')
#         message = data.get('message')

#         try:
#             sender = UserTable.objects.get(id=sender_id)
#             receiver = UserTable.objects.get(id=receiver_id)
#             ChatTable.objects.create(sender=sender, receiver=receiver, message=message)
#             return JsonResponse({'status': 'success', 'message': 'Message sent'})
#         except UserTable.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Invalid user ID'})
 
# def get_chat_messages(request):
  
#         data = json.loads(request.body)
#         user1_id = data.get('user1_id')
#         user2_id = data.get('user2_id')

#         messages = ChatTable.objects.filter(
#             sender_id__in=[user1_id, user2_id],
#             receiver_id__in=[user1_id, user2_id]
#         ).order_by('timestamp')

#         result = [{
#             'sender': m.sender.username,
#             'receiver': m.receiver.username,
#             'message': m.message,
#             'timestamp': m.timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         } for m in messages]

#         return JsonResponse({'status': 'success', 'messages': result})

    
# def send_complaint(request):
#     data=[]
#     w=request.POST['uid']
#     data = json.loads(request.body)
#     user_id = data.get('user_id')
#     subject = data.get('subject')
#     message = data.get('message')

#     try:
#         user = UserTable.objects.get(id=user_id)
#         ComplaintTable.objects.create(user=user, subject=subject, message=message)
#         return JsonResponse({'status': 'success', 'message': 'Complaint submitted'})
#     except UserTable.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'User not found'})


# def view_reply(request):
#     data=[]
#     q=request.POST['uid']  
#     data = json.loads(request.body)
#     complaint_id = data.get('complaint_id')
#     complaint = ComplaintTable.objects.get(id=complaint_id)

#     return JsonResponse({
#                 'status': 'success',
#                 'complaint_id': complaint.id,
#                 'complaint': complaint.complaint_text,
#                 'reply': complaint.reply if complaint.reply else 'No reply yet'
#             })
    
  
# def view_farmer_payments(request):

#             data = json.loads(request.body)
#             farmer_id = data.get('farmer_id')

#             farmer = FarmerTable.objects.get(id=farmer_id)
#             payments = Payment.objects.filter(farmer=farmer).order_by('-payment_date')

#             payment_list = []
#             for payment in payments:
#                 payment_list.append({
#                     'payment_id': payment.id,
#                     'amount': str(payment.amount),
#                     'date': payment.payment_date.strftime("%Y-%m-%d %H:%M:%S"),
#                     'status': payment.status,
#                     'method': payment.method,
#                     'purpose': payment.purpose or ''
#                 })

#             return JsonResponse({'status': 'success', 'payments': payment_list})

def view_feedback(request):
        feedbacks = Feedback.objects.all().order_by('-date')
        data = [
            {
                'user': fb.user.username if fb.user else None,
                'message': fb.message,
                'date': fb.date.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for fb in feedbacks
        ]
        return JsonResponse({'status': 'success', 'feedbacks': data})
>>>>>>> 3528a25 (Add requirements.txt)


def register(request):
    if 'submit' in request.POST:
        name = request.POST['name']
        dob = request.POST['date']
        gender = request.POST['gender']
        photo = request.FILES['image']
        phone = request.POST['phone']
        email = request.POST['email']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        district = request.POST['district']
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        fs = FileSystemStorage()
        img_path = fs.save(photo.name, photo)


        r = User.objects.create(username=uname, password=pwd)
        r.groups.add(Group.objects.get(name='user'))

        # Save additional details
        ud = UserTable(
            name=name,
            dob=dob,
            gender=gender,
            photo=img_path,
            place=place,
            post=post,
            pin=pin,    
            district=district,
            phone=phone,
            email=email,
            login_id=r.pk
        )
        ud.save()

        return HttpResponse("<script>alert('successfully registered');window.location='/register'</script>")
    return render(request,"register.html")


<<<<<<< HEAD
# def manageuser(request):
#     uid = request.POST['uid']
#     i = UserTable.objects.get(id=uid)
#     i.name = request.POST.get('name')
#     i.dob = request.POST.get('dob')
#     i.gender = request.POST.get('gender')
#     i.email = request.POST.get('email')
#     i.phone = request.POST.get('phone')
#     i.place = request.POST.get('place')
#     i.post = request.POST.get('post')
#     i.pin = request.POST.get('pin')
#     i.district = request.POST.get('district')
#     i.photo = request.POST.get('photo')
#     i.username = request.POST.get('uname')
#     i.password = request.POST.get('pwd')
#
#     i.save()
#     return JsonResponse({"status": "success", "message": "Delivery staff edited successfully"})
#

=======
>>>>>>> 3528a25 (Add requirements.txt)
def text(request):
    a=request.POST["a"]
    b=request.POST["b"]
    print(a,b,'i')
    response = {'status':'success'}
    return JsonResponse(response)

def send_feedback(request):
<<<<<<< HEAD
    uid=request.POST["lid"]
    pid=request.POST["pid"]
    fb=request.POST["review"]
    rating=request.POST["rating"]
    print("bbbbbbbbbbb",pid,uid)
    f=Feedback(user_id=uid,product_id=pid,feedback=fb,date=datetime.now(),rating=rating)
    f.save()
=======
    uid=request.POST["uid"]
    pid=request.POST["pid"]
    fb=request.POST["feedback"]
    rating=request.POST["rating"]
    Feedback.objects.create(user_id=uid,product_id=pid,feedback=fb,date=datetime.now(),rating=rating)
>>>>>>> 3528a25 (Add requirements.txt)
    response = {'status':'success'}
    return JsonResponse(response)
        
def view_feedback(request):
    pid=request.POST["pid"]
<<<<<<< HEAD
    # lid=request.POST['fid']
=======
>>>>>>> 3528a25 (Add requirements.txt)
    data = []
    fb_list = Feedback.objects.filter(product_id=pid).select_related('user')
    for fb in fb_list:
        data.append({
            'user':fb.user.name,
            'feedback':fb.feedback,
            'rating':fb.rating,
            'date':fb.date.strftime("%y-%m-%d")
        })
        return JsonResponse({'status':'success','data':data})
    
    
def farmerprofile(request):
    uid = request.POST.get('uid')
    try:
        farmer = FarmerTable.objects.get(id=uid)
        data = [{
            'name': farmer.name,
            'email': farmer.email,
            'phone': farmer.phone,
            'photo': farmer.photo.name,
            'dob': farmer.dob,
            'gender': farmer.gender,
            'place': farmer.place,
            'post': farmer.post,
            'pin': farmer.pin,
            'district': farmer.district,
            'username': farmer.username,
            'password': farmer.password,
            'login_id': farmer.login_id,
        }]
        return JsonResponse({'status': 'success', 'data': data})
    except FarmerTable.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Farmer not found'})



<<<<<<< HEAD
=======
def deliverystaffregister(request):
    
      
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            place = request.POST.get('place')
            post = request.POST.get('post')
            pin = request.POST.get('pin')
            district = request.POST.get('district')
            drivinglicense = request.POST.get('drivinglicense')
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(name,'iiiiiiiiiiiiiiiiiiii')

            u=User.objects.create(username=username,password=password)
            staff = DeliveryStaff(
                name=name,
                dob=dob,
                gender=gender,
                email=email,
                phone=phone,
                place=place,
                post=post,
                pin=pin,
                district=district,
                drivinglicense=drivinglicense,
                username=username,
                password=password,
                login_id=u.pk
            )
            staff.save()
            return JsonResponse({"status": "success", "message": "Delivery staff registered successfully"})
        
>>>>>>> 3528a25 (Add requirements.txt)
def farmerregister(request):
    
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
<<<<<<< HEAD
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        img_path = fs.save(photo.name, photo)
=======
        photo = request.POST.get('photo')  # file upload
>>>>>>> 3528a25 (Add requirements.txt)
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        place = request.POST.get('place')
        post = request.POST.get('post')
        pin = request.POST.get('pin')
        district = request.POST.get('district')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create a user login entry
<<<<<<< HEAD
        u = User.objects.create(username=username, password=make_password(password))
        u.groups.add(Group.objects.get(name='farmer'))
=======
        u = User.objects.create(username=username, password=password)

>>>>>>> 3528a25 (Add requirements.txt)
        # Create farmer entry
        farmer = FarmerTable(
            name=name,
            email=email,
            phone=phone,
<<<<<<< HEAD
            photo=img_path,
=======
            photo=photo,
>>>>>>> 3528a25 (Add requirements.txt)
            dob=dob,
            gender=gender,
            place=place,
            post=post,
            pin=pin,
            district=district,
            username=username,
            password=password,
            login_id=u.pk
        )
        farmer.save()
<<<<<<< HEAD
        response= ({"status": "success", "message": "Farmer registered successfully"})
        return JsonResponse(response)

def sendcomplaint(request):
    uid=request.POST['lid']

    complaints=request.POST['c']
    sc=ComplaintTable(date=datetime.now(),complaints=complaints,reply='pending',status='pending',login_id=uid)
=======
        return JsonResponse({"status": "success", "message": "Farmer registered successfully"})

def sendcomplaint(request):
    
    complaints=request.POST['complaints']
    reply=request.POST['reply']
    status=request.POST['status']

    sc=ComplaintTable(date=datetime.now(),complaints=complaints,reply=reply,status=status)
>>>>>>> 3528a25 (Add requirements.txt)
    sc.save()
    response = {"status":"success"}
    return JsonResponse(response)

<<<<<<< HEAD


=======
>>>>>>> 3528a25 (Add requirements.txt)
def profregfar(request):
        uid=request.POST['uid']
        o=FarmerTable.objects.get(id=uid)
        o.name = request.POST.get('name')
        o.email = request.POST.get('email')
        o.phone = request.POST.get('phone')
        o.photo = request.POST.get('photo')  # file upload
        o.dob = request.POST.get('dob')
        o.gender = request.POST.get('gender')
        o.place = request.POST.get('place')
        o.post = request.POST.get('post')
        o.pin = request.POST.get('pin')
        o.district = request.POST.get('district')
        o.username = request.POST.get('username')
        o.password = request.POST.get('password')
        o.save()
    

        return JsonResponse({"status": "success", "message": "Farmer Edited successfully"})
    
def managestaff(request):
            uid=request.POST['uid']
            i=DeliveryStaff.objects.get(id=uid)
            i.name = request.POST.get('name')
            i.dob = request.POST.get('dob')
            i.gender = request.POST.get('gender')
            i.email = request.POST.get('email')
            i.phone = request.POST.get('phone')
            i.place = request.POST.get('place')
            i.post = request.POST.get('post')
            i.pin = request.POST.get('pin')
            i.district = request.POST.get('district')
            i.drivinglicense = request.POST.get('drivinglicense')
            i.username = request.POST.get('username')
            i.password = request.POST.get('password')
            
            i.save()
            return JsonResponse({"status": "success", "message": "Delivery staff edited successfully"})
        
        
        
def chatwithus(request):
            msg = request.POST.get('message')
            fi = request.POST.get('fromid')
            ti = request.POST.get('toid')
<<<<<<< HEAD
            uid = Person.objects.get(login_id=lid)
            lid = Person.objects.get(login_id=fid)
            t=ChatTable(date=datetime.now(),message=msg,fromid=uid,toid=lid)
=======
            from_user = Person.objects.get(pk=int(fi))
            to_user = Person.objects.get(pk=int(ti))
            t=ChatTable(date=datetime.now(),message=msg,fromid=from_user,toid=to_user)
>>>>>>> 3528a25 (Add requirements.txt)
            t.save()
            response={'status':'success'}
            return JsonResponse(response)

<<<<<<< HEAD

def manageuser(request):
    lid = request.POST.get('lid')
    try:
        a = UserTable.objects.get(login_id=lid)

        data = {
            'status': 'ok',
            'user': {
                'id': a.id,
                'name': a.name,
                'email': a.email,
                'phone': a.phone,
                'place': a.place,
                'post': a.post,
                'pin': a.pin,
                'district': a.district,
                'dob': str(a.dob),
                'gender': a.gender,
                'photo': a.photo.url if a.photo else None,  # return full photo URL
            }
        }
        print(data)
        return JsonResponse(data)

    except UserTable.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def updateuserprofile(request):
                lid = request.POST.get("lid")
                    
                user = UserTable.objects.get(login_id=lid)


                user.name = request.POST.get("name", user.name)
                user.email = request.POST.get("email", user.email)
                user.phone = request.POST.get("phone", user.phone)
                user.place = request.POST.get("place", user.place)
                user.post = request.POST.get("post", user.post)
                user.pin = request.POST.get("pin", user.pin)
                user.district = request.POST.get("district", user.district)
                user.dob = request.POST.get("dob", user.dob)
                user.gender = request.POST.get("gender", user.gender)


                if "photo" in request.FILES:
                    user.photo = request.FILES["photo"]

                user.save()
                return JsonResponse({"status": "ok", "message": "Profile updated successfully"})

           
def productes(request):

    prod=request.POST['product']
    photo=request.FILES['photo']
    fs = FileSystemStorage()
    img_path = fs.save(photo.name, photo)
    price=request.POST['price']
    details=request.POST['details']
    farmer_id=request.POST['lid']
    
 
    farm=ProductTable(productname=prod,photo=img_path,price=price,details=details,farmer_id=farmer_id)
    farm.save()
    response={'status':'sucess'}
    return JsonResponse(response)


def manageproduct(request):
    pid = request.POST.get('pid')
    w = ProductTable.objects.get(id=pid)

    w.productname = request.POST.get('product')
    w.price = request.POST.get('price')
    w.details = request.POST.get('details')
    w.farmer_id = request.POST.get('fid')

    if 'photo' in request.FILES:  # check if file uploaded
        w.photo = request.FILES['photo']

    w.save()
    return JsonResponse({'status': 'success'})
=======
def manageuser(request):
        uid=request.POST.get('uid')
        a=UserTable.objects.get(id=uid)
        a.name = request.POST['name']
        a.dob = request.POST['date']
        a.gender = request.POST['gender']
        a.photo = request.POST['image']
        a.phone = request.POST['phone']
        a.email = request.POST['email']
        a.place = request.POST['place']
        a.post = request.POST['post']
        a.pin = request.POST['pin']
        a.district = request.POST['district']

        a.save()

        return JsonResponse({'status': 'success', 'message': 'Account edited created'})

def productes(request):

    prod=request.POST['product']
    photo=request.POST['photo']
    price=request.POST['price']
    details=request.POST['details']
    farmer_id=request.POST['fid']
    
 
    farm=ProductTable(productname=prod,photo=photo,price=price,details=details,farmer_id=farmer_id)
    farm.save()
    response={'status':'sucess'}
    return JsonResponse(response) 



def manageproduct(request):
    pid=request.POST['pid']
    w=ProductTable.objects.get(id=pid)
    w.productname=request.POST['product']
    w.photo=request.POST['photo']
    w.price=request.POST['price']
    w.details=request.POST['details']
    w.farmer_id=request.POST['fid']
    w.save()
    response={'status':'sucess'}
    return JsonResponse(response) 

>>>>>>> 3528a25 (Add requirements.txt)

def deleteprod(request):
    pid=request.POST['pid']
    h=ProductTable.objects.get(id=pid)
    h.delete()
    response={'status':'deleted'}
    return JsonResponse(response) 


def viewcomplaint(request):
<<<<<<< HEAD
    lid=request.POST['lid']
    a=ComplaintTable.objects.filter(login_id=lid)
=======
    a=ComplaintTable.objects.all()
>>>>>>> 3528a25 (Add requirements.txt)
    data = []
    for i in a:
        data.append(
            {
        'complaints':i.complaints,
        'reply':i.reply,
<<<<<<< HEAD
        'date':i.date,
=======
        'date':i.date
>>>>>>> 3528a25 (Add requirements.txt)
        }
        )
        response={'status':'success','data':data}
        return JsonResponse(response)
    
<<<<<<< HEAD
from django.db.models import Q
    
def viewwchattt(request):
    fid=request.POST['fid']

    uid=request.POST['uid']
    s=ChatTable.objects.filter(Q(fromid_id=uid,toid_id=uid)|Q(toid_id=fid,fromid_id=fid))
=======
    from django.db.models import Q
    
def viewwchattt(request):
    uid=request.POST['uid']
    s=ChatTable.objects.filter(Q(fromid_id=uid)|Q(toid_id=uid))
>>>>>>> 3528a25 (Add requirements.txt)
    data=[]
    for j in s:
        data.append({
            'date':j.date,
            'message':j.message,
            'fromid':j.fromid_id,
            'toid':j.toid_id,
        })
        response={'status':'success','data':data}
        return JsonResponse(response)   
    
def viewuser(request):
<<<<<<< HEAD
   
=======
    uid=request.POST['uid']
>>>>>>> 3528a25 (Add requirements.txt)
    a=UserTable.objects.all()
    data = []
    for i in a:
        data.append({
<<<<<<< HEAD
            'id':i.login.pk,
           'name':i.name,
           'date':i.dob,
           'gender':i.gender,
           'image':i.photo.name,
=======
           'name':i.name,
           'date':i.dob,
           'gender':i.gender,
           'image':i.photo.url if i.photo else "",
>>>>>>> 3528a25 (Add requirements.txt)
           'phone':i.phone,
           'email':i.email,
           'place':i.place,
           'post':i.post,
           'pin':i.pin,
           'district':i.district,
<<<<<<< HEAD
          
        })

        print(data)
        response = {'status':'success','data':data}
        return JsonResponse(response)
    
=======
           'uname':i.username,
           'pwd':i.password,
           
        })
        response = {'status':'success','data':data}
        return JsonResponse(response)
    
def viewfarmer(request):
    uid = request.POST['uid']
    a = FarmerTable.objects.all()
    data = []
    for i in a:
        data.append({
            'name': i.name,
            'email': i.email,
            'phone': i.phone,
            'photo': i.photo.url if i.photo else "",   
            'dob': i.dob,
            'gender': i.gender,
            'place': i.place,
            'post': i.post,
            'pin': i.pin,
            'district': i.district,
            'username': i.username,
            'password': i.password,   

        })
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)
>>>>>>> 3528a25 (Add requirements.txt)


def viewdeliverystaff(request):
    uid = request.POST['uid']
    a = DeliveryStaff.objects.all()
    data = []
    for i in a:
        data.append({
            'name': i.name,
            'dob': i.dob,
            'gender': i.gender,
            'email': i.email,
            'phone': i.phone,
            'place': i.place,
            'post': i.post,
            'pin': i.pin,
            'district': i.district,
            'drivinglicense': i.drivinglicense,
            'username': i.username,
            'password': i.password,  
            
        })
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)


<<<<<<< HEAD
def uviewfamers(request):
    farmers = FarmerTable.objects.all()
    data = []
    for p in farmers:
        data.append({
             'id':p.pk,
            'name': p.name,
            'photo': p.photo,  
            'phone': p.phone,
            'email': p.email,
            'place':p.place
        })
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)

def usendchattofamers(request):
    uid=request.POST['uid']
    fid=request.POST['fid']
    c=request.POST['c']
    sc=ChatTable(date=datetime.now(),message=c,fromid_id=uid, toid_id=fid)
    sc.save()
    response = {"status":"success"}
    return JsonResponse(response)





def viewproduct(request):
    fid=request.POST['fid']
    products = ProductTable.objects.filter(farmer_id=fid)
    data = []
    print("rrrrrrr",data)
    for p in products:
        data.append({
            'id':p.pk,
            'productname':p.productname,
            'photo': p.photo.url if p.photo else "",
            'price': p.price,
            'details': p.details,

        })
    print(data)
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)

def viewineprod(request):
    data=[]
    pid = request.POST.get('pid')
    print('pid',pid)
    p = ProductTable.objects.get(id=pid)
    data.append({
                'id': p.pk,
                'product': p.productname,
                'photo': p.photo.url if p.photo else "",
                'price': p.price,
                'details': p.details,
            })
    print("ggggggg",data)
    return JsonResponse({'status': 'success', 'data': data})


def addtocart(request):
    pid = request.POST['pid']
    uid = request.POST['uid']
    q = request.POST['quantity']
    print('hhhhhhhh',q,pid,uid)
    c=Cart(date=datetime.now(),product_id=pid,user_id=uid,quantity=q)
    c.save()
    

    response = {'status': 'success'}

    return JsonResponse(response)



def viewcart(request):
    uid = request.POST['uid']

    cartitem = Cart.objects.filter(user_id=uid)
    data = []
    for p in cartitem:
        data.append({
            'id':p.pk,
            'product': p.product.productname,
            'photo': p.product.photo.url if p.photo else "",  
            'price': p.product.price,
            'details': p.product.details,
=======
def viewproduct(request):
    pid = request.POST['pid']
    products = ProductTable.objects.all()
    data = []
    for p in products:
        data.append({
            'product': p.productname,
            'photo': p.photo.url if p.photo else "",  
            'price': p.price,
            'details': p.details,
>>>>>>> 3528a25 (Add requirements.txt)
         
        })
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)

<<<<<<< HEAD
=======

>>>>>>> 3528a25 (Add requirements.txt)
        
def view_feedbackfar(request):
    far=Feedback.objects.all()
    data = []
    
    for fb in far:
        data.append({
            'feedback':fb.feedback,
            'rating':fb.rating,
            'date':fb.date.strftime("%y-%m-%d")
        })
<<<<<<< HEAD
    print('iiiiiiiiii',data)
    return JsonResponse({'status':'success','data':data})

def ffeedback(request):
    lid=request.POST['lid']
    far=Feedback.objects.filter(product__farmer__login_id=lid)
    data = []
    
    for fb in far:
        data.append({
            'user':fb.user.username,
            'product':fb.product.productname,
            'feedback':fb.feedback,
            'rating':fb.rating,
            'date':fb.date.strftime("%y-%m-%d")
        })
    print(data,lid)
    return JsonResponse({'status':'success','data':data})

def viewwassign(request):
    did=request.POST['did']
    s=AssignTable.objects.filter(delivery__login_id=did)
=======
        return JsonResponse({'status':'success','data':data})

def viewwassign(request):
    did=request.POST['did']
    s=AssignTable.objects.all()
>>>>>>> 3528a25 (Add requirements.txt)
    data=[]
    for j in s:
        data.append({
            'date':j.date,
<<<<<<< HEAD
            'status':j.status   ,
=======
            'status':j.status,
>>>>>>> 3528a25 (Add requirements.txt)
    
    
        })
        response={'status':'success','data':data}
        return JsonResponse(response)   

def assignorder(request):
<<<<<<< HEAD
    did = request.POST.get('did')
    oid = request.POST.get('oid')

    try:
        # optional: check if already assigned
        if AssignTable.objects.filter(ordermain_id=oid).exists():
            return JsonResponse({'status': 'already_assigned'})

        a=AssignTable(
            date=datetime.now().date(),            
            status='assigned',
            deliverystaff_id=did,
            ordermain_id=oid
        )
        a.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
=======
    did=request.POST['did']
    oid=request.POST['oid']
    status=request.POST['status']
    AssignTable.objects.create(date=datetime.now(),status=status,deliverystaff_id=did,ordermain_id=oid)
    response= {'status':'success'}
    return JsonResponse(response)
>>>>>>> 3528a25 (Add requirements.txt)


def change_password(request):
    if request.method == "POST":
        uid = request.POST.get('uid') 
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

       
        user = UserTable.objects.get(id=uid)

            
        print(f"UID: {uid}, Username: {user.username}")
        print(f"Entered current password: {current_password}")

           
        if check_password(current_password, user.password):
                if new_password == confirm_password:
                    user.set_password(new_password)  # built-in method handles hashing
                    user.save()
        response = {"status": "success", "message": "Password changed successfully"}

    return JsonResponse(response)

def fluttertodjango(request):
    a = request.POST['parsingname']
    print(a,'iiiiiiiiii')
    response= {'status':'success'}
<<<<<<< HEAD
    return JsonResponse(response)

    
def dsendcomplaint(request):
    did=request.POST['did']

    complaints=request.POST['c']
    sc=ComplaintTable(date=datetime.now(),complaints=complaints,reply='pending',status='pending',login_id=did)
    sc.save()
    response = {"status":"success"}
    return JsonResponse(response)

def stviewcomplaints(request):
   q=ComplaintTable.objects.all()
   data = []
   for i in q:
     data.append(
       {
        'complaints':i.complaints,
        'reply':i.reply,
        'date':i.date,
       }
   )
     response = {'status':'success','data':data}
     return JsonResponse(response)          

def viewwchattt(request):
    fid=request.POST['did']

    uid=request.POST['uid']
    s=ChatTable.objects.filter(Q(fromid_id=uid,toid_id=uid)|Q(toid_id=fid,fromid_id=fid))
    data=[]
    for j in s:
        data.append({
            'date':j.date,
            'message':j.message,
            'fromid':j.fromid_id,
            'toid':j.toid_id,
        })
        response={'status':'success','data':data}
        return JsonResponse(response)  

def forders(request):
    orderdata.append = []
    fid = request.POST['fid']
    o=OrderMain.objects.filter(farmer_id=fid)
    for i in o:
        s= OrderSub.objects.filter(OrderMain_id=i.pk)
        data.append
        

def updateorderstatus(request):
   
            oid = request.POST.get("oid")  
            status = request.POST.get("status")

           
            assign = AssignTable.objects.filter(ordermain_id=oid).last()
            if assign:
                assign.status = status
                assign.date = datetime.now()
                assign.save()
                response = ({"status": "success", "message": "Order status updated"})
                return JsonResponse(response)
            
def dviewfeedback(request):
    lid=request.POST["lid"]
    data = []
    fb_list = Feedback.objects.filter(user_id=lid)
    for fb in fb_list:
        
        data.append({
            'user':fb.user.username,
            'feedback':fb.feedback,
            'rating':fb.rating,
            'date':fb.date,
        })
        return JsonResponse({'status':'success','data':data})
    
def dsendcomplaint(request):
    did=request.POST['did']
    complaint=request.POST['c']
    s=ComplaintTable(date=datetime.now(),complaints=complaint,reply='pending',status='pending',login_id=did)
    s.save()
    response = {"status":"success"}
    return JsonResponse(response)

def dviewcomplaint(request):
    did=request.POST['did']
    a=ComplaintTable.objects.filter(deliverystaff_id=did)
    data = []
    for i in a:
        data.append(
            {
        'complaints':i.complaints,
        'reply':i.reply,
        'date':i.date
        }
        )
        response={'status':'success','data':data}
        return JsonResponse(response)
    



def dchatwithuser(request):

            msg = request.POST['c']
            fi = request.POST['fid']
            ti = request.POST['lid']
            chats = ChatTable.objects.filter(login_id=ti)

            print(fi,ti,msg,'iiiiiiiiiiiiiiiiiiiii')


            u = ChatTable(date=datetime.now(), message=msg, fromid_id=fi, toid_id=ti)
            u.save()

            response = ({'status': 'success','data':list(chats)})
            return JsonResponse(response)

def dviewwuschat(request):
    did=request.POST['did']
    uid=request.POST['uid']
    s=ChatTable.objects.filter(Q(fromid_id=uid,toid_id=uid)|Q(toid_id=did,fromid_id=did))
    data=[]
    for j in s:
        data.append({
            'date':j.date,
            'message':j.message,
            'fromid':j.fromid_id,
            'toid':j.toid_id,
        })
        response={'status':'success','data':data}
        return JsonResponse(response)  

def userviewed(request):
    u=UserTable.objects.all()
    data = []
    for i in u:
      data.append({
        'id':i.login.pk,
        'name':i.name,
        'place':i.place,
        'phone':i.phone,
    })
    print('iiiiiiiiii',u)
    response = {'status':'success','data':data}
    return JsonResponse(response)


def learn(request):
    r={'status':'sucess'}
    return JsonResponse(r)

    

def viewfarmer(request):
    
    farmers = FarmerTable.objects.all()

    data = []
    for f in farmers:
        data.append({
            'id':f.login.pk,
            'name': f.name,
            'email': f.email,
            'phone': f.phone,
            'photo': f.photo.name,
            'dob': f.dob,  
            'gender': f.gender,
            'place': f.place,
            'post': f.post,
            'pin': f.pin,
            'district': f.district,
        })
        print(data)

    response = {'status': 'success', 'data': data}
    return JsonResponse(response)

def viewStafff(request):
    
    staff = DeliveryStaff.objects.all()

    data = []
    for f in staff:
        data.append({
            'id': f.login.pk,
            'name': f.name,
            'dob': f.dob,
            'gender': f.gender,
            'email': f.email,
            'phone': f.phone,
            'place': f.place,
            'post': f.post,
            'pin': f.pin,
            'district': f.district,
            'drivinglicense': f.drivinglicense,
        })
        print(data)


    response = {'status': 'success', 'data': data}
    return JsonResponse(response)


def viewcartee(request):
    lid = request.POST['lid']
    fid=request.POST['fid']
    carts = Cart.objects.filter(user_id=lid,product__farmer_id=fid)

    data = []
    for c in carts:
        data.append({
            'id': c.pk,
            'date': c.date,
            'quantity': c.quantity,
            'product_id': c.product.id,
            'photo':c.product.photo.url if c.product.photo else '',
            'product_name': c.product.productname,  
            'price': c.product.price,              
            # 'user_id': c.user.id,
        })

    response = {'status': 'success', 'data': data}
    return JsonResponse(response)


def makeorder(request):
    lid=request.POST['lid']
    fid=request.POST['fid']

    s=Cart.objects.filter(product__farmer_id=fid,user_id=lid)
    
    data = []

    amount = 0
    for i in s:
        amount=amount+(i.product.price*i.quantity)
    o=OrderMain(date=datetime.now(),status='pending',amount=amount,farmer_id=fid,user_id=lid)
    o.save()


    for j in s:
        d=OrderSub(
            quantity = i.quantity,
            ordermain_id=o.id,
            product_id=i.product_id,
          
        )
        d.save()
    for k in s:
        
        k.delete()
        response = {'status': 'success', 'data': data,'oid':o.id}
        return JsonResponse(response)


def pay(request):
    oid=request.POST['oid']
    o=OrderMain.objects.get(id=oid)
    o.status='paid'
    o.save()
    response = {'status': 'success'}
    p=Payment(date=datetime.now(),ordermain_id=oid,totalamount =o.amount,status=o.status)
    p.save()
    return JsonResponse(response)



def vieworder(request):
    lid=request.POST['lid']
    
    s=OrderSub.objects.filter(ordermain__user_id=lid)
    data = []
    for i in s:
        data.append({
            'id':i.product.pk,
             'quantity':i.quantity,
             'p':i.product.productname,
            'photo':i.product.photo.name,
             'a':i.product.price,
             'o':i.ordermain.date,
             's':i.ordermain.status,

        })
        
    print("ggggggggggg",lid)
    print("fffffffffff",data)
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)
    
    
    

def farmerverify(request):
    lid=request.POST['lid']

    
    s=OrderSub.objects.filter(ordermain__farmer__login_id=lid)
    data = []
    for i in s:
        data.append({
            'oid':i.ordermain.pk,
            'id':i.product.pk,
             'quantity':i.quantity,
             'p':i.product.productname,
             'a':i.product.price,
             'o':i.ordermain.date,
             's':i.ordermain.status,
             'f':i.ordermain.farmer.name,
        })
        
    print("ggggggggggg",lid)
    print("fffffffffff",data)
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)



def userchated(request):
            c = request.POST['c']
            f =request.POST['fid']
            ti=request.POST['lid']
            print(f,ti,c,'iiiiiiiiiiiiiiiiiiiii')


            d = ChatTable(date=datetime.now(),message=c,fromid_id=ti,toid_id=f)
            d.save()

            response = ({'status': 'success'})
            return JsonResponse(response)


def dchatwithfar(request):
    c = request.POST['c']
    fi = request.POST['lid']
    ti = request.POST['fid']
    print(fi, ti, c, 'iiiiiiiiiiiiiiiiiiiii')

    u = ChatTable(date=datetime.now(), message=c, fromid_id=fi, toid_id=ti)
    u.save()

    response = ({'status': 'success'})
    return JsonResponse(response)


from django.db.models import Q

def dviewwchat(request):
    fid = request.POST['fid']   
    lid = request.POST['lid']  
    
   
    s = ChatTable.objects.filter(
        Q(fromid_id=lid, toid_id=fid) | Q(fromid_id=fid, toid_id=lid)
    ).order_by("date")   
    
    data = []
    for j in s:
        data.append({
            'date': j.date,
            'message': j.message,
            'fromid': j.fromid_id,
            'toid': j.toid_id,
        })
    
    response = {'status': 'success', 'data': data}
    return JsonResponse(response)




def viewuserr(request):
    lid=request.POST['lid']
    a=UserTable.objects.get(login_id=lid)
    data = []
    for i in a:
        data.append({
            'id':i.login.pk,
           'name':i.name,
           'date':i.dob,
           'gender':i.gender,
           'image':i.photo.name,
           'phone':i.phone,
           'email':i.email,
           'place':i.place,
           'post':i.post,
           'pin':i.pin,
           'district':i.district,
          
        })

        print(data)
        response = {'status':'success','data':data}
        return JsonResponse(response)
    


def pickupview(request):
    did = request.POST.get("did")  
    oid = request.POST.get("oid")   


    assign = AssignTable.objects.get(
        deliverystaff_id=did,
        ordermain_id=oid
    )
    assign.status = "Picked Up"
    assign.date = datetime.now().date()   # only date part
    assign.save()
    print(did,oid,assign)
    return JsonResponse({"status": "success", "message": "Pickup updated"})


def deliver(request):
    did = request.POST.get("did")  
    oid = request.POST.get("oid")   
    o=OrderMain.objects.get(id=oid)
    o.status='Delivered'

    assign = AssignTable.objects.get(
        deliverystaff_id=did,
        ordermain_id=oid
    )
    assign.status = "Delivered"
    assign.date = datetime.now().date()   # only date part
    assign.save()
    print(did,oid,assign)
    return JsonResponse({"status": "success", "message": "Pickup updated"})

    

def farmerverify(request):
    lid = request.POST.get('lid')
    o=OrderMain.objects.filter(farmer_id=lid).values_list('id',flat=True)

    orders = OrderSub.objects.filter(ordermain_id__in=o)

    data = []
    for i in orders:
        data.append({
            'oid': i.ordermain.pk,
            'id': i.product.pk,
            'quantity': i.quantity,
            'p': i.product.productname,
            'a': str(i.product.price),
            'o': i.ordermain.date.strftime("%Y-%m-%d"),
            's': i.ordermain.status,
        })

    print("fffffffffff", data, orders, lid,o)

    response = {'status': 'success', 'data': data}
    return JsonResponse(response)




def pickupview(request):
    did = request.POST.get("did")  
    oid = request.POST.get("oid")   

    try:
        o=OrderMain.objects.get(id=oid)
        o.status='Picked up'
        assign = AssignTable.objects.get(
            deliverystaff_id=did,
            ordermain_id=oid
        )
        assign.status = "Picked Up"
        assign.date = datetime.now().date()   # only date part
        assign.save()
        return JsonResponse({"status": "success", "message": "Pickup updated"})
    except AssignTable.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Assignment not found"})


def viewwassign(request):
    did = request.POST.get('lid')   # from Flutter you passed 'lid'

    assignments = AssignTable.objects.filter(deliverystaff_id=did)
    data = []
    d=DeliveryStaff.objects.get(login_id=did)

    for j in assignments:
        data.append({
            'ordermain_id': j.ordermain.id,
            'date': j.date.strftime("%Y-%m-%d"),
            'status': j.status,
            'name': d.name,    # who placed the order
            'phone':d.phone,
            'email': d.email,
            'place': d.place,
        })
    print(data,'iiiiiiiiiiiiiiiiiiiiiiiiiii',assignments,did)

    response = {'status': 'success', 'data': data}
    return JsonResponse(response)


def password(request):
    lid=request.POST['lid']
    oldpassword=request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']

response = {'status':'success'}



def sendfeedbackk(request):
    lid=request.POST['lid']
    product=request.POST['pid']
    a=request.POST['rating']
    b=request.POST['feedback']
    feed=Feedback(date=datetime.now(),feedback=b,rating=a,product_id=product,user_id=lid)
    feed.save()
    response = {'status':'success'}
    return JsonResponse(response)

def viewfeedbackstaff(request):
    data=[]
    lid=request.POST['lid']
    pid=request.POST['pid']
    f=Feedback.objects.filter(product_id=pid,user_id=lid)
    for i in f:
        data.append({
            'date':i.date,
            'feedback':i. feedback,
            'rating':i.rating,
            'productname':i.product.productname,
            'details':i.product.details,
        })

    response={'status':'success','data':data}
    return JsonResponse(response)






def sendcomplaintsuser(request):
     lid=request.POST['lid']
     c=request.POST['complaint']
     comp=ComplaintTable(date=datetime.now(),complaints=c,reply='pending',status='pending',login_id=lid)
     comp.save()
     response={'status':'success'}
     return JsonResponse(response)


def viewcomplaintsuserrr(request):
    data=[]
    lid=request.POST['lid']
    comp=ComplaintTable.objects.filter(login_id=lid)
    for i in comp:
         data.append({
            'complaints':i.complaints,
           })
    response={'status':'success','data':data}
    return JsonResponse(response)


































=======
    return JsonResponse(response)
>>>>>>> 3528a25 (Add requirements.txt)
