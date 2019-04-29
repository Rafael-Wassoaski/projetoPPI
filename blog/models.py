from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    """docstring for Post."""
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title =  models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(blank = True, null = True)
    CATEGORIA=(
        ('AV', 'Aventura'),
        ('PR', 'Personagem'),
        ('IT', 'Item'),
        ('FC', 'Ficha'),
        ('TM', 'Tema Livre'),
        )
    categoria = models.CharField(max_length=2, choices=CATEGORIA, default='AV')
    # image = models.ImageField(upload_to = 'images', blank = True)
    create_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class RespostaPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    resposta = models.TextField();
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    repostaMain = models.ForeignKey('self', on_delete = models.CASCADE, null=True, blank = True)
    respResp = models.BooleanField(default = False)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        

class Character(models.Model):
    """docstring for Character."""
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    CLASSES = (
        ('BA','BARBARO'),
        ('LA', 'LADINO'),
        ('CL', 'CLERIGO'),
        

        )
    classe = models.CharField(max_length = 25)
    tamanho = models.IntegerField(default = 0, blank = True, null = True)
    RACAS = (

        ('HUM','HUMANO'),   
        ('DRA','DRACONATOS'),  
        ('ELF','ELFOS'), 
        ('GNO','GNOMOS'),
        ('ANO','ANOES'),
        ('HAL','HALFLINGS'),
        ('ELA','ELADRIN'),

        )
    raca = models.CharField(max_length = 15, choices = RACAS, default = 'HUMANO')
    idade = models.IntegerField(default = 0)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length = 1, choices = SEX)
    altura = models.FloatField(default = 0)
    peso = models.FloatField(default = 0)
    olhos = models.CharField(max_length = 20)
    cabelo = models.CharField(max_length = 30)
    pele = models.CharField(max_length = 30)
    divindade = models.CharField(max_length = 50, default='', blank = True, null=True)

    TENDENCIA = (
        ('LG', 'LAWFUL GOOD'),
        ('NG', 'NEUTRAL GOOD'),
        ('CG', 'CHAOTIC GOOD'),
        ('LN', 'LAWFUL NEUTRAL'),
        ('TN', 'TRUE NEUTRAL'),
        ('CN', 'CHAOTIC NEUTRAL'),
        ('LE', 'LAWFUL EVIL'),
        ('NE', 'NEUTRAL EVIL'),
        ('CE', 'CHAOTIC EVIL'),
        )
    tendencia = models.CharField(max_length=2, choices = TENDENCIA, default='LG')
    idiomas = models.TextField(default='', null = True, blank = True)
    forca = models.IntegerField(default = 0)
    constituicao = models.IntegerField(default = 0)
    destreza = models.IntegerField(default = 0)  
    inteligencia = models.IntegerField(default = 0)
    sabedoria = models.IntegerField(default = 0)
    carisma = models.IntegerField(default = 0)
    pontosDeVida = models.IntegerField(default = 5)
    iniciativa = models.IntegerField(default = 0)
    deslocamento = models.IntegerField(default = 2)
    # rosto = models.ImageField(upload_to='images', null = True, blank = True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Pericias(models.Model):
    character = models.IntegerField()
    acrobacia = models.IntegerField(default = 0)
    atletismo = models.IntegerField(default = 0)
    blefe = models.IntegerField(default = 0)
    diplomacia = models.IntegerField(default = 0)
    exploracao = models.IntegerField(default = 0)
    furtividade = models.IntegerField(default = 0)
    historia = models.IntegerField(default = 0)
    intimidacao = models.IntegerField(default = 0)
    intuicao = models.IntegerField(default = 0)
    ladinagem = models.IntegerField(default = 0)
    manha = models.IntegerField(default = 0)
    natureza = models.IntegerField(default = 0)
    percepcao = models.IntegerField(default = 0)
    religiao = models.IntegerField(default = 0)
    socorro = models.IntegerField(default = 0)
    tolerancia = models.IntegerField(default = 0)
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Aventura(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    aventura = models.TextField(default = "")
    create_date = models.DateTimeField(blank = True, null = True)
    GENERO = (
        ('TR','Terror'),
        ('MD', 'Medieval'),
        ('CY', 'Cyberpunk'),
        ('MO', 'Moderno')
        )
    genero = models.CharField(max_length = 2, choices = GENERO, default= 'TR' )
    itens = models.TextField()
    numeroJogadores = models.IntegerField(default = 2)
    npcs = models.TextField()


