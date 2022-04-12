from django.views.generic import TemplateView
from django.shortcuts import render

from proyectocoder.Pentrega.models import informacion, peliculas, personaje

class PentregaView(TemplateView):
    template_name = 'v2/index.html'


    def post(self, request):
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        email = request.POST['email']

        nombrep = request.POST['nombrep']
        razonp = request.POST['razonp']
        escenafavp = request.POST['escenafavp']

        pnombre = request.POST['pnombre']
        razon = request.POST['razon']
        identificado = request.POST['identificado']
        escenafav = request.POST['escenafav']

        print(f'NOMBRE: {nombre}')
        print(f'EDAD:  {edad}')
        print(f'EMAIL:  {email}')
        print(f'NOMBREP: {nombrep}')
        print(f'RAZONP:  {razonp}')
        print(f'ESCENAP: {escenafavp}')
        print(f'PNOMBRE: {pnombre}')
        print(f'RAZON: {razon}')
        print(f'IDENTIFICADO {identificado}')
        print(f'ESCCENAFAV: {escenafav}')

        obj_informacion = informacion(nombre=nombre, edad=edad, email=email)
        obj_informacion.save()

        obj_peliculas = peliculas(nombrep=nombrep, razonp=razonp, escenafavp=escenafavp)
        obj_peliculas.save()

        obj_personaje = personaje(pnombre=pnombre, razon=razon, identificado=identificado, escenafav=escenafav)
        obj_personaje.save()

        return render(request,self.template_name)


class SearchView(TemplateView):
    template_name = 'v2/search.html'

    def post(self, request):

        print('Nombre de la pelicula')
        print(request.POST.get('nombrep'))
        context = {
            "elements": peliculas.objects.filter(
                nombrep=request.POST.get('nombrep')
            )
        }

        return render(request, self.template_name, context)
