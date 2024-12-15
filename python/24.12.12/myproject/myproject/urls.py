from django.contrib import admin
from django.urls import path, include
from .views import redirect_to_login
from accounts.views import home_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),    
    path('', home_view, name='home'),  # 메인 페이지 URL 설정
    path('logout/', logout_view, name='logout'),  # 로그아웃 URL 설정
]