from django.shortcuts import render,redirect
from Student.forms import UsForm,ChpwdForm,Medform,ImForm,GuestForm,ServiceForm,OrgForm,DonationForm,UsPerm,RequestForm
from django.contrib import messages
from Student.models import MedicineInfo,DonationInfo,AbstractUser,User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from Project import settings
from datetime import date


# Create your views here.
def management(request):
	return render(request,'htfiles/management.html')

def HomePage(rt):
	return render(rt,'htfiles/HomePage.html')


def about(request):
	return render(request,'htfiles/about.html')

def mainpage(request):
	mdl = MedicineInfo.objects.filter(uid_id=request.user.id)
	return render(request,'htfiles/mainpage.html',{'t':mdl})	

# def registration(fh):
# 	if fh.method=="POST":
# 		d=Reg(fh.POST)
# 		if d.is_valid():
# 			d.save()
# 			messages.success(fh,"You have registered successfully")
# 			return redirect('/login')
# 	d=Reg()
# 	return render(fh,'htfiles/registration.html',{'t':d})

# def ref(request):
# 	if request.method=="POST":
# 		t=RequestForm(request.POST)
# 		if t.is_valid():
# 			t.save()
# 			print(t)
# 		return redirect('inx')
# 	t.save()		
# 	return render(req,'htfiles/request.html',{'r':t})

def registration1(fh):
	if fh.method=="POST":
		d=UsForm(fh.POST)
		if d.is_valid():
			d.save()
			messages.success(fh,"You have registered successfully")
			return redirect('/login')
	d=UsForm()
	return render(fh,'htfiles/lg.html',{'t':d})

def donate(rf):
	return render(rf,'htfiles/donate.html')

def organization(request):
	data=MedicineInfo.objects.all()
	return render(request,'htfiles/organization.html',{'o':data})

@login_required
def cgf(request):
	if request.method=="POST":
		print("Yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/login')
	c=ChpwdForm(user=request)
	return render(request,'htfiles/passwordchange.html',{'g':c})

def role(request):
	return render(request,'htfiles/role.html')

def userpage(request):
	if request.method=="POST":
		p=Medform(request.POST)
		if p.is_valid():
			k = p.save(commit=False)
			k.uid_id = request.user.id
			k.save()
			return redirect('/tb')
	p=Medform()
	return render(request,'htfiles/userpage.html',{'h':p})

def profile(req):
	# if req.method=="POST":
	# 	g=GuestForm(req.POST)
	# 	k=ImForm(req.POST)
	# 	n=OrgForm(req.POST)
	# 	if g.is_valid() and k.is_valid() and n.is_valid():
	# 		g.save()
	# 		k.save()
	# 		n.save()
	# g=GuestForm()
	# k=ImForm()
	# n=OrgForm()
	return render(req,'htfiles/profile.html')

def uppro(request):
	if request.method=="POST":
		g=GuestForm(request.POST)
		k=ImForm(request.POST)
		n=OrgForm(request.POST)
		if g.is_valid() and k.is_valid() and n.is_valid():
			g.save()
			k.save()
			n.save()
	g=GuestForm()
	k=ImForm()
	n=OrgForm()
	return render(request,'htfiles/updateprofile.html',{'gu':g,'mu':k,'ou':k})

def crud(request):
	if request.method=="POST":
		un=request.POST['name']
		pas=request.POST['pwd']
		em=request.POST['eml']
		Age=request.POST['age']
		#data2=UsrRg.objects.all()
		if len(un)!=0:
			data=MedicineInfo.objects.create(Username=un,password=pas,email=em,age=Age)
		#return render(request,'html/actions.html',{'info':data2})
	data2=MedicineInfo.objects.all()
	return render(request,'htfiles/crud.html',{'info':data2})

def deletedata(req,id):
	print("1")
	data=MedicineInfo.objects.get(id=id)
	data.delete()
	print("2")
	return redirect('/cr')

def tab(hj):
	data=MedicineInfo.objects.filter(uid_id=hj.user.id)
	return render(hj,'htfiles/table.html',{'info':data})

def delete(red,id):
	data=MedicineInfo.objects.get(id=id)
	if red.method=="POST":
		data.delete()
		return redirect('/tb')
	return render(red,'htfiles/userdelete.html',{'sd':data})

def userupdate(up,si):
	a=MedicineInfo.objects.get(id=si)
	#y=NewData.objects.get(pid_id=si)
	if up.method=="POST":
		d=Medform(up.POST,instance=a)
		#k=NewUsrForm(up.POST,instance=y)
		if d.is_valid():
			d.save()
			#k.save()
			return redirect('/tb')
	d=Medform(instance=a)
	#k=NewUsrForm(instance=y)
	return render(up,'htfiles/updateuser.html',{'us':d})

# def userinfo(ty,uname):
# 	p=MedicineInfo.objects.get(medicine_name=uname)
# 	h=MedicineInfo.objects.get(pid_id=p.id)
# 	return render(ty,'htfiles/newinfo.html',{'y':p,'yu':h})

def view(request):
	return render(request,'htfiles/view.html')

# def adminpermission(req):
# 	if req.method=="POST":
# 		data=ServiceForm(req.POST)
# 		if data.is_valid():
# 			subject=' successfully changed role!!'
# 			body="Your role has been successfully changed to "   +req.POST['change_role'] 
# 			receiver=req.POST['email']
# 			sender=settings.EMAIL_HOST_USER
# 			send_mail(subject,body,sender,[receiver])
# 			data.save()
# 			messages.success(req,"Successfully sent to your mail "+receiver)
# 			return redirect('/')
# 	data=ServiceForm()
# 	return render(req,'htfiles/adminpermission.html',{'c':data})

def gvper(request,k):
	r = User.objects.get(id=k)
	if request.method == "POST":
		k = UsPerm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/prm')
	k = UsPerm(instance=r)
	return render(request,'htfiles/gvp.html',{'y':k})


def peruser(request):
	ty=User.objects.all()
	return render(request,'htfiles/peruser.html',{'q':ty})

# def donationinfo(request):
# 	if request.method=="POST":
# 		l=DonationForm(request.POST)
# 		if l.is_valid():
# 			l.save()
# 	l=DonationForm()
# 	return render(request,'htfiles/donationinfo.html',{'m':l})

# def showdata(request):
# 	data=DonationInfo.objects.filter(pid_id=request.user.id)
# 	return render(request,'htfiles/showdata1.html',{'in':data})

def index1(request):
	i = MedicineInfo.objects.filter(uid_id=request.user.id)
	g = MedicineInfo.objects.all()
	k = {}
	for m in g:
		days_count=m.expiry_date-m.created_date
		#s = User.objects.get(id=m.uid_id)
		k[m.id] = m.id,m.pharmacy_name,m.medicine_name,m.quantity,m.batch_no,m.category,m.production_date,m.entry_date,m.expiry_date,days_count
	f = k.values()
	return render(request,'htfiles/index.html',{'it':i,'d':f})
	# m.entry_date=date(2008,8,18)
	# m.expiry_date=data(2008,9,26)
	# delta=m.entry_date - m.expiry_date
	# print(delta.days)


# def rolechange(request):
# 	r=User.objects.get(k=id)
# 	if request.method=="POST":
# 		k = RequestForm(request.POST,instance=r)
# 		if k.is_valid():
# 			k.save()
# 		return redirect('/rc')
# 	k = RequestForm(instance=r)
# 	return render(request,'htfiles/mainpage.html',{'y':k})

def requ(request):
	if request.method=="POST":
		g=RequestForm(request.POST)
		if g.is_valid():
			g.save()
		return redirect('/rq/')
	g=RequestForm()
	return render(request,'htfiles/index.html',{'r':g})		