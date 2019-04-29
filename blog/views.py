from django.shortcuts import render, redirect
from .models import Post, Character, Pericias, Aventura
from django.utils import timezone
from urllib.parse import urlencode
from django.urls import reverse
from .forms import CharacterForm, PericiasForm, PostForm, RespostaForm, RespostaPost, AventuraForm


def post_list(request):
    posts = Post.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    categoria = 'POSTS'
    return render(request, 'blog/HTML/post_list.html', {'posts' : posts, 'categoria':categoria})

def post_listCategoria(request, categoria):
    
    cate = ''
    posts = Post.objects.filter(categoria = categoria, create_date__lte=timezone.now()).order_by('-create_date')
    if categoria == 'AV':
        cate = cate + 'Aventura'
    elif categoria == 'PR':
        cate = 'Personagem'
    elif categoria == 'IT':
        cate = 'Item'
    elif categoria == 'FC':
        cate = 'Ficha'
    elif categoria == 'TM':
        cate = 'Tema Livre'

    return render(request, 'blog/HTML/post_list.html', {'posts' : posts, 'categoria':cate})





def aventura_details(request, pk):
    aventura = Aventura.objects.get(pk = pk)
    return render(request, 'blog/HTML/aventura_details.html', {'aventura': aventura})

def respostaRespostaDetails(post, resposta):
    return RespostaPost.objects.filter(post = post, repostaMain = resposta, respResp = True)






def aventuras_list(request):
    aventuras = Aventura.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return render(request, 'blog/HTML/aventuras_list.html', {'aventuras': aventuras})

def createAventura(request):
    aventuraForm = AventuraForm()

    if request.method == "POST":
        aventura = AventuraForm(request.POST)
        if aventura.is_valid():
            aventura = aventura.save(commit = False)
            aventura.author = request.user
            aventura.create_date = timezone.now()
            aventura.save()
            return redirect('blog:aventuras_list')

    return render(request, 'blog/HTML/createAventura.html', {'aventuraForm':aventuraForm,})



def createResposta(request, pk):
    formResposta = RespostaForm()
    if request.method == "POST":
        resposta = RespostaForm(request.POST)
       
        if resposta.is_valid():
            resposta = resposta.save(commit = False)
            resposta.author = request.user
            resposta.published_date = timezone.now()
            resposta.post = Post.objects.get(pk = pk)
            resposta.save()            
            return redirect('blog:post_list')



    return render(request, 'blog/HTML/respostaPost.html', {'respostaForm':formResposta,})



def createRespostaResposta(request, pkPost, pkResposta):
    formResposta = RespostaForm()
    if request.method == "POST":
        resposta = RespostaForm(request.POST)
       
        if resposta.is_valid():
            resposta = resposta.save(commit = False)
            resposta.author = request.user
            resposta.published_date = timezone.now()
            resposta.post = Post.objects.get(pk = pkPost)
            resposta.repostaMain = RespostaPost.objects.get(pk = pkResposta)
            resposta.respResp = True
            resposta.save()            
            return redirect('blog:post_list')



    return render(request, 'blog/HTML/respostaPost.html', {'respostaForm':formResposta,})
    
def readPost(request, pk):

    post = Post.objects.get(pk = pk)
    respostas = RespostaPost.objects.filter(post = post, respResp = False)
    respostasRespostas =  RespostaPost.objects.filter(post = post, respResp = True)

    return render(request, 'blog/HTML/post.html', {'post':post, 'respostas':respostas, 'respostasRespostas':respostasRespostas } )

def postCreate(request):
    formPost = PostForm()
    if request.method == "POST":
        post = PostForm(request.POST)
       
        if post.is_valid():
            post = post.save(commit = False)
            post.author = request.user
            post.create_date = timezone.now()
            post.publish()
            post.save()            
            return redirect('blog:post_list')



    return render(request, 'blog/HTML/PostForm.html', {'postForm':formPost,})




def createChar(request):
    formChar = CharacterForm()
    formPer = PericiasForm()
    
    if request.method == "POST":
        char = CharacterForm(request.POST)
        per = PericiasForm(request.POST)
        if char.is_valid() and per.is_valid():
            char = char.save(commit = False)
            char.author = request.user
            char.published_date = timezone.now()
            char.save()
            per = per.save(commit = False)
            per.published_date = timezone.now();
            per.character = char.pk
            per.save()
            return redirect('blog:post_list')


    return render(request, 'blog/HTML/createChar.html', {'fomularioChar':formChar,'formularioPer': formPer})


def charList(request):
    chars = Character.objects.all();
    return render(request, 'blog/HTML/charList.html', {'chars': chars})



def charDetails(request, pk):
    char = Character.objects.get(pk = pk)
    pericias = Pericias.objects.get(character = pk)
    return render(request, 'blog/HTML/charDetails.html', {'char':char, 'per': pericias})





