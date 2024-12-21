from django.contrib import admin
from django.urls import path, include
from accounts.views import home_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('PGM0100/', include('PGM0100.urls')),  # PGM0100 앱의 URL 패턴 포함
    path('', home_view, name='home'),  # 메인 페이지 URL 설정
    path('logout/', logout_view, name='logout'),  # 로그아웃 URL 설정
]