from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode
from .forms import QuizForm, PerguntasForm, RespostaForm
from .models import Quiz, Pergunta, Resposta
from django.forms.formsets import formset_factory

	# Create your views here.

def quizList(request):
	quizs = Quiz.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

	return render(request, 'quiz/HTML/quizList.html', {'quizs':quizs})

def fazerQuiz(request, pkQuiz):
	quiz = Quiz.objects.get(pk = pkQuiz)
	perguntas = Pergunta.objects.filter(quiz = quiz)
	respostasFormSet = formset_factory(RespostaForm, extra=quiz.numPerguntas)
	formSet = respostasFormSet()
	
	if request.method == "POST":
		pontos = 0

		for pergunta in perguntas:
			resp = request.POST.get(str(pergunta.pergunta), '')
			respCorreta = Resposta.objects.get(pergunta = pergunta)
			if respCorreta.resposta == resp:
				print('a')
				pontos = pontos + 1
											
		urlBase = reverse('quiz:pontuacao')
		pontos = urlencode({'pontos':pontos})
		url = '{}?{}'.format(urlBase, pontos)
		return redirect(url)


	return render(request, 'quiz/HTML/fazerQuiz.html', {'quiz':quiz,'perguntas':perguntas, 'respostasForm':formSet})


def mostrarPontos(request):
	pontos = request.GET.get('pontos')

	return render(request,'quiz/HTML/mostrarPontos.html', {'pontos':pontos})


def CreateQuiz(request):
	quizForm = QuizForm()
	if request.method == "POST":
		quiz = QuizForm(request.POST)

		if quiz.is_valid():
			quiz = quiz.save(commit = False)
			quiz.author = request.user
			quiz.create_date = timezone.now()
			quiz.save()

			urlBase = reverse('quiz:criarPerguntas')
			quizPk = urlencode({'quiz':quiz.pk, 'quantidade':quiz.numPerguntas})

			url = '{}?{}'.format(urlBase, quizPk)
			return redirect(url)

	return render(request, 'quiz/HTML/createQuiz.html', {'quizForm':quizForm,})



def CreatePerguntas(request):
	pkQuiz = request.GET.get('quiz')
	quantidade = int(request.GET.get('quantidade'))
	
	perguntaForm = PerguntasForm()
	respostaForm= RespostaForm()
	
	if request.method == "POST":
	    pergunta = PerguntasForm(request.POST)
	    respForm = RespostaForm(request.POST)

	    if pergunta.is_valid() and respForm.is_valid():
	    	pergunta = pergunta.save(commit = False)
	    	pergunta.quiz = Quiz.objects.get(pk = pkQuiz)
	    	pergunta.save()
	    	respForm = respForm.save(commit = False)
	    	respForm.pergunta = Pergunta.objects.get(pk = pergunta.pk)
	    	respForm.save() 

	    	if quantidade - 1 > 0:
		    	urlBase = reverse('quiz:criarPerguntas')
		    	urlParameters = urlencode({'quiz': pkQuiz, 'quantidade': quantidade - 1})
		    	url = '{}?{}'.format(urlBase, urlParameters)
		    	return redirect(url)

	    	return redirect('quiz:quizList')

	return render(request, 'quiz/HTML/createPerguntas.html', {'pergunta': perguntaForm, 'resposta':respostaForm})



