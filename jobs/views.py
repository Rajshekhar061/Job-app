from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application
from .forms import ApplicationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/add_job.html', {'form': form})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role=role)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
@login_required
def dashboard(request):
    profile = request.user.profile

    if profile.role == 'employer':
        jobs = Job.objects.filter(company=request.user.username)
        return render(request, 'dashboard_employer.html', {'jobs': jobs})
    else:
        applications = Application.objects.filter(email=request.user.email)
        return render(request, 'dashboard_applicant.html', {'applications': applications})
    

@login_required
def view_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = Application.objects.filter(job=job)

    return render(request, 'view_applications.html', {
        'job': job,
        'applications': applications
    })