from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
import random 
import pandas as pd
from django.contrib.auth.decorators import login_required
from .models import NumeroSorteo 
from .forms import NumeroSorteoForm
from .utils import generar_serie_unica
from .forms import CustomUserCreationForm

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form':CustomUserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('panel')
            except:
                return render(request, 'registro.html', {
                    'form':CustomUserCreationForm,
                    'msj': 'El nombre de usuario ya existe'
                })
            
        else:
            return render(request, 'registro.html', {
                'form':CustomUserCreationForm,
                'msj': 'Los passwords no son iguales'
            })

def ingreso(request):

    if request.method == 'GET':
        return render(request, 'ingreso.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingreso.html', {
                'form': AuthenticationForm,
                'msj': 'Usuario o password incorrecto'
            })
        else:
            login(request, user)
            return redirect('panel')

def salir(request):
    logout(request)
    return redirect('ingreso')

def panel(request):
    return render(request, 'panel.html')

@login_required
def generar_numero(request):
    if request.method == 'POST':
        serie_valida, primos_agregados, serie_cadena = generar_serie_unica()
        nuevo_numero = NumeroSorteo(
            usuario=request.user,
            r1=serie_valida[0],
            r2=serie_valida[1],
            r3=serie_valida[2],
            r4=serie_valida[3],
            r5=serie_valida[4],
            r6=serie_valida[5]
        )
        nuevo_numero.save()
        return redirect('ver_numeros')
    return render(request, 'generar_numero.html')

@login_required
def ver_numeros(request):
    numeros = NumeroSorteo.objects.filter(usuario=request.user)
    return render(request, 'ver_numeros.html', {'numeros': numeros})

@login_required
def eliminar_numero(request, id):
    numero = NumeroSorteo.objects.get(id=id, usuario=request.user)
    if numero:
        numero.delete()
    return redirect('ver_numeros')
