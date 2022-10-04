from cgi import print_arguments
from django.shortcuts import render, redirect
from .models import Comentario, TipoUsuario, Usuario, Puntos_Usuarios, Bonificacion, Agenda
from django.contrib import messages
from django.contrib.auth import authenticate, login

def iniciop(request, name):
    #empresa = Usuario.objects.all().values()
    #nombreusuario = empresa[0]
    usuario = Usuario.objects.filter(nombreEmpresa = name)
    return render(request, 'index.html', {"name":name,"usuario": usuario})

def inicio(request):
    #empresa = Usuario.objects.all().values()
    #nombreusuario = empresa[0]
    #usuario = Usuario.objects.filter(nombreEmpresa = name)
    return render(request, 'index.html')

def bonos(request, name):
    empresas  = Usuario.objects.all()
    empresaespe = Usuario.objects.filter(nombreEmpresa = name).values()
    print(empresaespe)
    empresaespe = empresaespe[0]
    print(empresaespe)
    puntos = Puntos_Usuarios.objects.filter(identificacion = empresaespe['id']).values()
    print(puntos)
    cantidadp= puntos[0]['cantidad']
    bonificacion=Bonificacion.objects.all()
    return render(request, 'bonos.html', {"name":name, "cantidad": cantidadp, "bono": bonificacion, "empresas": empresas})

def bonos1(request):
    bonificacion=Bonificacion.objects.all()
    return render(request, 'bonos.html', {"bono": bonificacion})

def verCatalogo(request):
    if request.method == 'POST':
        return redirect('/bonos/%s' %(request.POST.dict()["nombreEmpresa"])) 
    return redirect('/bonos1/')


def intercambio(request, name):
    formulario = request.POST.dict()
    empresa = Usuario.objects.filter(nombreEmpresa = name).values()
    id_empresa = empresa[0]
    id_empresa = id_empresa["id"]
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion = id_empresa).values()
    cantidad_puntos= objeto_puntos[0]
    cantidad_puntos = cantidad_puntos["cantidad"]
    puntos = 0
    if(formulario["tipoMaterial"] == "1"):
        puntos = int(formulario["peso"])*2
    elif(formulario["tipoMaterial"] == "2"):
        puntos = int(formulario["peso"])*3
    elif(formulario["tipoMaterial"] == "3"):
        puntos = int(formulario["peso"])*2
    elif(formulario["tipoMaterial"] == "4"):
        puntos = int(formulario["peso"])*5
    else:
        print("que material es ese?")    
    suma = puntos + cantidad_puntos
    o_p = Puntos_Usuarios.objects.filter(identificacion_id = id_empresa).values()
    o_p.update(cantidad=suma)
    return redirect('/inicio/%s' %(name))

def redimir(request, name, puntosbono):
    usuario=Usuario.objects.filter(nombreEmpresa=name)
    listusuario = usuario.values()
    listusuario = listusuario[0]
    listusuario = listusuario['id']
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion_id=listusuario).values()
    list_objetos_puntos = objeto_puntos[0]
    cantidad_objetos_puntos = list_objetos_puntos['cantidad']
    if(cantidad_objetos_puntos < puntosbono):
        messages.info(request, 'Your password has been changed successfully!')
        print("no redimió")
        return redirect('/bonos/%s' %(name))
    else:
        o_p = Puntos_Usuarios.objects.filter(identificacion_id=listusuario)
        diferencia = cantidad_objetos_puntos - puntosbono
        o_p.update(cantidad=diferencia)
        print("redimió")
    return redirect('/bonos/%s' %(name))

def registro(request):
    formulario = request.POST.dict()
    T1 = TipoUsuario.objects.get(idtipousuario= request.POST['idtipousuario'])
    empresa = Usuario(nombreEmpresa = formulario['nombreEmpresa'], NIT = formulario['NIT'], direccion = formulario['direccion'], correo = formulario['correo'], clave = formulario['clave'], idtipousuario = T1)
    empresa.save()
    empresa1 = Usuario.objects.filter(nombreEmpresa = formulario['nombreEmpresa']).values()
    empresa1 = empresa1[0]
    puntosU = Puntos_Usuarios(identificacion_id = empresa1['id'], cantidad = 0)
    puntosU.save()
    print(formulario)
    return redirect('/')          

def comentario(request):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa= Usuario.objects.get(nombreEmpresa = request.POST['nombreEmpresa'])   
    comentario = Comentario(identificacion = idEmpresa, desComent = formulario['Comentario'])
    comentario.save()
    return redirect('/')        

def agenda(request):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa= Usuario.objects.get(nombreEmpresa = request.POST['nombreEmpresa'])   
    agenda = Agenda(identificacion = idEmpresa, fechaAgenda = formulario['fecha'], estado = 'En proceso')
    agenda.save()
    return redirect('/inicio/%s' %(request.POST['nombreEmpresa']))  

def signin(request):
    formulario=request.POST.dict()
    if request.method == 'POST':
        user = Usuario.objects.filter(nombreEmpresa = formulario["nombreEmpresa"]).filter(clave = formulario["clave"])
        print(user.values())
        
        if len(user.values()) != 0:
            tipouser = user.values()[0]
            tipouser = tipouser["idtipousuario_id"]
            if tipouser == 2:
                return redirect('/administrador/')
            return redirect('/inicio/%s' %(formulario["nombreEmpresa"]))
        else: 
            print("sUPer Malo")
            messages.error(request, "sUPer Malo")
    return render(request, 'login.html')

def signout(request):
    return redirect('/')

def administrador(request):
    return render(request, 'admin.html')