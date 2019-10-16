from django.http import HttpResponse, , HttpResponseRedirect

from polls.models import Pregunta

from django.template import loader

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

def agregar_preguntas(request):
	template = loeader.get_template(polls/agregar_preguntas.html)
	context = {}
	return HttpResponse(template.render(context, request))
	<
def index(request):
	Preguntas = Pregunta.objects.order_by('-fecha')[:5]
	template = loader.get_template('polls/index.html')
	context = {'Preguntas': Preguntas,}
	return HttpResponse(template.render(context, request))

def validar_formulario(request):
	c1 = request.POST.get("campo1")
	c2 = request.POST.get("campo2")
	resultado = c1 + " y " + c2 
	if c1.strip() == "" or c2.strip() == "";
		return HttpResponse("Debe llenar todos los campos")
	else;
		return HttpResponse(request)


def detalle(request, id_pregunta):
	pregunta = Pregunta.objects.get(id=id_pregunta)
	template = loader.get_template('polls/detalle.html')
	context ={ 'pregunta': pregunta,}
	return HttpResponse(template.render(context, request))


def resultados(request, total):
    latest_question_list = Pregunta.objects.order_by('fecha')[:total]
	question = get_object_or_404(pregunta, pk=id_pregunta)
    output = ', '.join([q.descripcion for q in latest_question_list])
    return HttpResponse(output)

def vote(request, id_pregunta):
	pregunta = get_object_or_404(pregunta, pk=id_pregunta)
	try:
		selected_choice = pregunta.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the pregunta voting form.
		return render(request, 'polls/detalle.html', {
			'pregunta': pregunta,
			'error_message': "No se selecciono una opcion.",
			})
		else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(id_pregunta,)))    

"""
	-Construir una vista que retorne todas las opciones asociadas a una pregunta
	*FILTRAR POR ID DE PREGUNTA
"""