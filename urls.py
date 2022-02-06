from django.urls import path, include
from . import views
from .cismp_modules import _1, _3, _4, _5
from .views import HomeView, RandomModuleView

cismp_patterns = [
    path('random/', RandomModuleView.as_view(modules = (_1, _3, _4, _5)), name = 'all_random'),
    path('information_security_principles/', RandomModuleView.as_view(modules = (_1,)), name = 'information_security_principles'),
    #path('information_risk/', RandomModuleView.as_view(modules = (_2,)), name = 'rest_api'),
    path('information_security_frameworks/', RandomModuleView.as_view(modules = (_3,)), name = 'files_os'),
    path('security_life_cycles/', RandomModuleView.as_view(modules = (_4,)), name = 'files_os'),
    path('procedural_and_people_security_controls/', RandomModuleView.as_view(modules = (_5,)), name = 'files_os'),
    #path('technical_security_controls/', RandomModuleView.as_view(modules = (_6,)), name = 'files_os'),
    #path('physical_and_environments_security/', RandomModuleView.as_view(modules = (_7,)), name = 'files_os'),
    #path('disaster_recovery_and_business_continuity_management/', RandomModuleView.as_view(modules = (_8,)), name = 'files_os'),
    #path('cryptography/', RandomModuleView.as_view(modules = (_9,)), name = 'files_os'),
]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cismp/', include(cismp_patterns)),
] 