"""
URL configuration for italiandelights project.

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
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ingredients", views.IngredientList.as_view(), name="ingredients"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredients/<int:pk>/update", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredients/<int:pk>/delete", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("menuitems", views.MenuItemList.as_view(), name="menuitems"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("menuitem/<pk>/update", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("menuitem/<pk>/delete", views.MenuItemDelete.as_view(), name="menuitemdelete"),
    # path("recipes", views.RecipeList.as_view(), name="recipes"),
    # path("recipe/create", views.RecipeCreate.as_view(), name="recipecreate"),
    # path("recipe/<pk>/update", views.RecipeUpdate.as_view(), name="recipeupdate"),
    # path("recipe/<pk>/delete", views.RecipeDelete.as_view(), name="recipedelete"),
    path('orders', views.OrderList.as_view(), name='orders'),
    path("order/create", views.OrderCreate.as_view(), name="ordercreate"),
    path("order/<pk>/update", views.OrderUpdate.as_view(), name="orderupdate"),
    path("order/<pk>/delete", views.OrderDelete.as_view(), name="orderdelete"),
    path('sales', views.total_sales_view, name='sales'),
    path('login', views.login_view, name='login'),
    path("", views.main_view),
]
