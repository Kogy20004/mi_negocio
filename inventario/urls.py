from django.urls import path

from inventario import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('tests/', views.tests, name='tests'),
    path('inventario/', views.inventario, name='inventario'),
    path('agregar_producto/',views.agregar_producto),
    path('editar_producto/<int:id>', views.editar_producto),
    path('eliminar_producto/<int:id>', views.eliminar_producto),
    path('ventas/', views.ventas, name='ventas'),
    path('compras/', views.compras, name='compras'),
]
