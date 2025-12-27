"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Main URL configuration - Django starts here and routes to app-specific URLs
# include() delegates URL matching to app's urls.py file
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    # Include app URLs - URLs starting with "api/" go to apis/urls.py
    path("api/", include("apis.urls")), # apis begins with "api/..." with be handled there like requestmapping 
    # URLs starting with "db/" go to employee/urls.py
    path("db/", include("employee.urls")),
    # URLs starting with "auth/" go to authentication/urls.py
    path("auth/", include("authentication.urls"))
]
