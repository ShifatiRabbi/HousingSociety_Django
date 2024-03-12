import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import  *
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CommunityCenter, Booking
from .forms import *

def homePage(request):
    return render(request, 'home.html')


class MemberListView(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'members'
    template_name = 'members_list.html'


class MemberCreateView(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email' ,'username']
    template_name = 'register.html'
    success_url = reverse_lazy('home')


class MemberUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'member_form.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        # Get the initial values from the user object
        initial = super().get_initial()
        initial['first_name'] = self.object.first_name
        initial['last_name'] = self.object.last_name
        initial['email'] = self.object.email
        return initial


class MemberDeleteView(DeleteView):
    model = User
    template_name = 'member_confirm_delete.html'
    success_url = reverse_lazy('home')

#************************************************************************
#************************************************************************

class CommunityCenterListView(ListView):
    model = CommunityCenter
    queryset = CommunityCenter.objects.all()
    context_object_name = 'communitycenters'
    template_name = 'communitycenters_list.html'


class CommunityCenterCreateView(CreateView):
    model = CommunityCenter
    fields = ['name', 'address', 'capacity']
    template_name = 'communitycenter_form.html'
    success_url = reverse_lazy('communitycenter_list')


class CommunityCenterUpdateView(UpdateView):
    model = CommunityCenter
    fields = ['name', 'address', 'capacity']
    template_name = 'communitycenter_form.html'
    success_url = reverse_lazy('communitycenter_list')


class CommunityCenterDeleteView(DeleteView):
    model = CommunityCenter
    template_name = 'communitycenter_confirm_delete.html'
    success_url = reverse_lazy('communitycenter_list')


class BookingListView(ListView):
    model = Booking
    queryset = Booking.objects.all()
    context_object_name = 'bookings'
    template_name = 'bookings_list.html'


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['payment_status']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')



@login_required

def book_community_center(request, community_center_id):
    context = {}
    a = 1
    if request.method == 'POST':
        ff = BookingForm(request.POST)
        if ff.is_valid():
            f1 = ff.cleaned_data['name']
            f2 = ff.cleaned_data['date']
            Queryset = CenterAvailability.objects.filter(Q(type = 1) & Q(name = f1) & Q(date = f2))
            ok = 0
            for x in Queryset:
              if x :
                  ok = 1
            if ok == 1 :
                 messages.error(request, "Unsuccessful booking !!! already booked....")
                 return render(request,'book_community_center.html')
                 
            else:
                ss = CenterAvailability(type = 1,name = f1,date = f2)
                ss.save()
                bcc = Booking(user = request.user, community_center=f1, date=f2)
                bcc.save()
                messages.success(request, "Successful booking !!!")
                return render(request,'book_community_center.html')
               
        else:
            ff = BookingForm()
        context = {'form':ff}
    return render(request,'book_community_center.html',context)


def community_centers(request):
    centers = CommunityCenter.objects.all()
    context = {'centers': centers}
    return render(request, 'community_centers.html', context)
#************************************************************************
#************************************************************************

class PlayGroundListView(ListView):
    model = PlayGround
    queryset = PlayGround.objects.all()
    context_object_name = 'playgrounds'
    template_name = 'playgrounds_list.html'


class PlayGroundCreateView(CreateView):
    model = PlayGround
    fields = ['name', 'address', 'capacity']
    template_name = 'playground_form.html'
    success_url = reverse_lazy('playground_list')


class PlayGroundUpdateView(UpdateView):
    model = PlayGround
    fields = ['name', 'address', 'capacity']
    template_name = 'playground_form.html'
    success_url = reverse_lazy('playground_list')


class PlayGroundDeleteView(DeleteView):
    model = PlayGround
    template_name = 'playground_confirm_delete.html'
    success_url = reverse_lazy('playground_list')


class BookingGroundListView(ListView):
    model = BookingGround
    queryset = BookingGround.objects.all()
    context_object_name = 'bookinggrounds'
    template_name = 'bookinggrounds_list.html'


class BookingGroundUpdateView(UpdateView):
    model = BookingGround
    fields = ['payment_status']
    template_name = 'bookingground_form.html'
    success_url = reverse_lazy('bookingground_list')


class BookingGroundDeleteView(DeleteView):
    model = BookingGround
    template_name = 'bookingground_confirm_delete.html'
    success_url = reverse_lazy('bookingground_list')


@login_required

def book_play_ground(request, play_ground_id):
    context = {}
    a = 1
    if request.method == 'POST':
        ff = BookingGroundForm(request.POST)
        if ff.is_valid():
            f1 = ff.cleaned_data['name']
            f2 = ff.cleaned_data['date']
            Queryset = GroundAvailability.objects.filter(Q(type = 1) & Q(name = f1) & Q(date = f2))
            ok = 0
            for x in Queryset:
              if x :
                  ok = 1
            if ok == 1 :
                 messages.error(request, "Unsuccessful booking !!! already booked....")
                 return render(request,'book_play_ground.html')
                 
            else:
                ss = GroundAvailability(type = 1,name = f1,date = f2)
                ss.save()
                bpg = BookingGround(date=f2, play_ground=f1, user=request.user)
                bpg.save()
                messages.success(request, "Successful booking !!!")
                return render(request,'book_play_ground.html')
               
        else:
            ff = BookingGroundForm()
        context = {'form':ff}
    return render(request,'book_play_ground.html',context)


def play_grounds(request):
    grounds = PlayGround.objects.all()
    context = {'grounds': grounds}
    return render(request, 'play_grounds.html', context)

#************************************************************************
#************************************************************************






from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")



