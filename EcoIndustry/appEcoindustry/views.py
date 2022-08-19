from django.shortcuts import render, redirect
from .models import Usuario, Puntos_Usuarios, Bonificacion

def inicio(request):
    empresa = Usuario.objects.all().values()
    nombreusuario = empresa[0]
    return render(request, 'index.html', {"name":nombreusuario["nombreEmpresa"]})

def bonos(request, name):
    bonificacion=Bonificacion.objects.all().values()
    print(bonificacion)
    print(bonificacion[0])
    bono1=bonificacion[0]
    bono2=bonificacion[1]
    bono3=bonificacion[2]
    bono4=bonificacion[3]
    
    
    return render(request, 'bonos.html', {"name": name, "mesa":bono1, "lampara": bono2, "papelera":bono3, "silla":bono4})

def intercambio(request, name):
    formulario = request.POST.dict()
    empresa = Usuario.objects.filter(nombreEmpresa = name).values()
    id_empresa = empresa[0]
    id_empresa = id_empresa["id"]
    print(id_empresa)
    print(empresa[0])
    print(formulario)
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion = id_empresa).values()
    cantidad_puntos= objeto_puntos[0]
    cantidad_puntos = cantidad_puntos["cantidad"]
    print(objeto_puntos)
    print("tipo material", formulario["tipoMaterial"])
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
    print(puntos)
    suma = puntos + cantidad_puntos
    o_p = Puntos_Usuarios.objects.filter(identificacion_id = id_empresa).values()
    o_p.update(cantidad=suma)
    return redirect('/inicio/')

def redimir(request, name, puntosbono):
    usuario=Usuario.objects.filter(nombreEmpresa=name)
    print(usuario.values())
    listusuario = usuario.values()
    listusuario = listusuario[0]
    listusuario = listusuario['id']
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion_id=listusuario).values()
    list_objetos_puntos = objeto_puntos[0]
    cantidad_objetos_puntos = list_objetos_puntos['cantidad']
    if(cantidad_objetos_puntos < puntosbono):
        return redirect('/bonos/%s' %(name))
    else:
        o_p = Puntos_Usuarios.objects.filter(identificacion_id=listusuario)
        diferencia = cantidad_objetos_puntos - puntosbono
        o_p.update(cantidad=diferencia)
    return redirect('/bonos/%s' %(name))