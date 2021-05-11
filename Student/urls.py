from django.urls import path
from Student import views
from django.contrib.auth import views as v
urlpatterns=[
	path('',views.management,name="mag"),
	path('home/',views.HomePage,name="home"),
	path('login/',v.LoginView.as_view(template_name="htfiles/AdminPage.html"),name="log"),
	path('lgo/',v.LogoutView.as_view(template_name='htfiles/logout.html'),name="logo"),
	# path('registration/',views.registration,name="reg"),
	path('registration1/',views.registration1,name="nreg"),
	path('mn/',views.mainpage,name="mnp"),
	path('donate/',views.donate,name="don"),
	path('org/',views.organization,name="og"),
	path('chpwd/',views.cgf,name="cg"),
	path('reset/',v.PasswordResetView.as_view(template_name="htfiles/resetpassword.html"),name="reset_password"),
	path('rst_done/',v.PasswordResetDoneView.as_view(template_name='htfiles/resetpassworddone.html'),name="password_reset_done"),
	path('ret_cf/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='htfiles/resetpasswordconfirm.html'),name="password_reset_confirm"),
	path('rst_cmplt/',v.PasswordResetCompleteView.as_view(template_name="htfiles/reset_password_complete.html"),name="password_reset_complete"),
	path('role/',views.role,name="ro"),
	path('userpage/',views.userpage,name="up"),
	path('pro/',views.profile,name="profile"),
	path('updf/',views.uppro,name="upf"),
	path('cr/',views.crud,name="crud"),
	path('tb/',views.tab,name="tab"),
	path('del/<str:id>',views.deletedata,name="delete"),
	path('delete/<int:id>',views.delete,name="del"),
	path('e/<int:si>/',views.userupdate,name="ue"),
	#path('ui/<str:uname>/',views.userinfo,name="uin"),
	path('view/',views.view,name="vi"),
	path('eper/<int:k>/',views.gvper,name="gp"),
	path('prm/',views.peruser,name="pmu"),
	
	# path('doninfo/',views.donationinfo,name="do"),
	# path('sh1/',views.showdata,name="sh"),
	path('index/',views.index1,name="inx"),
	path('rc/',views.rolechange,name="rc"),
	path('about',views.about,name="ab")
]