from django import forms

from .models import Quiz, Pergunta, Resposta

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ['title', 'descricao', 'numPerguntas']
		widgets = {
            'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
           	'numPerguntas': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
        }

class PerguntasForm(forms.ModelForm):
	class Meta:
		model = Pergunta
		fields = ['pergunta']
		exclude = ['quiz',]
		widgets = {
            'pergunta': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class RespostaForm(forms.ModelForm):
	class Meta:
		model = Resposta
		fields = ['resposta']
		widgets = {
            'resposta': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
        }








