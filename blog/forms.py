from django import forms

from .models import Character, Pericias, Post, RespostaPost, Aventura
# RespostaRespotaPost

class CharacterForm(forms.ModelForm):
    """docstring for CharacterForm."""
    class Meta:
        model = Character
        fields =   '__all__'
        exclude = ['author']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'classe': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'tamanho': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'idade': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'olhos': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'cabelo': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'pele': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'divindade': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            'forca': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'constituicao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'destreza': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'inteligencia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'sabedoria': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'carisma': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'pontosDeVida': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'iniciativa': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
            'deslocamento': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
        }


class PericiasForm(forms.ModelForm):
    """docstring for CharacterForm."""
    class Meta:
        model = Pericias
        fields =   '__all__'
        exclude = ['character']
        widgets = {
         'acrobacia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'atletismo': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'blefe': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'diplomacia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'exploracao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'furtividade': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'historia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'intimidacao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'intuicao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'ladinagem': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'manha': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'natureza': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'percepcao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'religiao': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'socorro': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),
         'tolerancia': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'-?[0-9]*(\.[0-9]+)?'}),

        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'categoria',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mdl-textfield__input'}),

        }

class RespostaForm(forms.ModelForm):
    class Meta:
        model = RespostaPost
        fields = ('resposta', )
  



class AventuraForm(forms.ModelForm):
    class Meta:
        model = Aventura
        fields = '__all__'
        exclude = ['author', 'create_date']
 

