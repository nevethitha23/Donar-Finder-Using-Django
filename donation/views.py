from django.shortcuts import render, get_object_or_404, redirect
from .models import Donor
from .forms import DonorForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Hospital
from .forms import HospitalSubmissionForm


def home(request):
    return render(request, 'donation/home.html')


def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'donation/success.html', {'message': 'Registered successfully!'})
    else:
        form = DonorForm()
    return render(request, 'donation/register.html', {'form': form})

def donor_list(request):
    donors = Donor.objects.all()

    blood_group_filter = request.GET.get('blood_group')
    organ_filter = request.GET.get('organ')

    if blood_group_filter:
        donors = donors.filter(blood_group=blood_group_filter)
    if organ_filter:
        donors = donors.filter(organ=organ_filter)

    blood_groups = Donor.objects.values_list('blood_group', flat=True).distinct()
    organs = Donor.objects.values_list('organ', flat=True).distinct()

    return render(request, 'donation/donor_list.html', {
        'donors': donors,
        'blood_groups': blood_groups,
        'organs': organs,
        'selected_bg': blood_group_filter,
        'selected_og': organ_filter,
    })
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'donation/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # or any success page
    else:
        form = AuthenticationForm()
    return render(request, 'donation/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home') 
def hospital_list(request):
    query = request.GET.get('q')
    hospitals = Hospital.objects.all()
    if query:
        hospitals = hospitals.filter(name__icontains=query)
    return render(request, 'donation/hospital_list.html', {'hospitals': hospitals})

def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'donation/hospital_detail.html', {'hospital': hospital})

def hospital_form(request, pk, form_type):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.hospital = hospital
            submission.form_type = form_type
            submission.save()
            return render(request, 'donation/confirmation.html', {'hospital': hospital, 'form_type': form_type})
    else:
        form = HospitalSubmissionForm()
    return render(request, 'donation/hospital_form.html', {'form': form, 'hospital': hospital, 'form_type': form_type})