from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecord
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'web/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registretion succcessfuly')
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request,'web/register.html', context)



# login user
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username= request.POST.get('username')
            password= request.POST.get('password')
            
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login succcessfuly')

                return redirect('dashboard')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'web/login.html', context)

# dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request,'web/dashboard.html',context={'records':records})



# records
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ' Record is created')

            return redirect('dashboard')
    else:
        form = CreateRecordForm()

    context = {'form':form}
    return render(request,'web/create-record.html',context)

# view
@login_required(login_url='login')
def view_record(request,record_id):
    all_records = get_object_or_404(Record, id=record_id)
    context = {'record':all_records}
    return render(request, 'web/view_record.html',context)


# update
@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = UpdateRecord(instance=record)
    if request.method == 'POST':
        form = UpdateRecord(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record is updated')

            return redirect('dashboard')
    
    context = {'form':form}
    return render(request, 'web/update_record.html', context)


# delete record
@login_required(login_url='login')
def delete_record(request,record_id):
    record = get_object_or_404(Record,id=record_id)
    record.delete()
    messages.success(request, 'Record is deleted')
    return redirect('dashboard')


# search 
logger = logging.getLogger(__name__)
@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Record.objects.filter(Q(first_name__icontains=query) | Q(id__icontains=query) )
    except Exception as e:
        logger.error('Error during search: %s', e)
    
    return render(request, 'web/search.html' , context={'results': results, 'query':query})

# logout 
def my_logout(request):
    logout(request)
    return redirect('login')

# 404 page
def custom_page_not_found(request,exception):
    return render(request,'web/404.html', status=404)
