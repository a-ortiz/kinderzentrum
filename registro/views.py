from django.shortcuts import render, render_to_response
from registro.forms import * #Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext
from registro.modelos.familiars_models import DatosFamiliaresOtros

# Create your views here.
def registro_view(request):
    mensaje = ""
    if request.method == "POST":
        mensaje = "guardando datos"
    else:
        mensaje = "enviando forma"
    #datos 
    datos = Ficha_PacienteForm()
    datos_familia = Ficha_DatosFamiliaresForm()
    datos_medico = Ficha_DatosMedicoForm()
    historial_madre = Ficha_HistorialMadreForm()
    #paciente = PacienteForm()
    #madre = MadreForm()
    #padre = PadreForm()
    descripcion_paciente = Ficha_DescripcionPacienteForm()
    alimentacion = AlimentacionForm()
    datos_familiares = DatosFamiliaresOtrosForm()
    hermanos_formset = HermanosFormset(instance=DatosFamiliaresOtros())
    ctx = {'ficha_datos_medico_form':datos_medico,
           'ficha_datos_familia_form':datos_familia,
           'ficha_datos_form':datos,
           'descripcion_paciente':descripcion_paciente,
           'historial_madre_form': historial_madre,
           #'paciente': paciente,
           #'padre': padre,
           #'madre': madre,
           'mensaje':mensaje,
           'alimentacion': alimentacion,
           'datos_familiares': datos_familiares,
           'hermanos_formset': hermanos_formset,
           'pagina_actual':'registro'}
    return render_to_response('registro/registro_ficha_medica.html',ctx,context_instance=RequestContext(request))
