from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    titulo = 'Para usted mi sñrta'
    texto = 'Perdon por demorar mucho, pero tuve editar todo :('
    texto1 = 'Bueno a pesar de todo siempre as estado conmigo, y eso me da una alegria inmensa'
    texto2 = 'con todo eso no me pienso rendir con usted, sos alguien que estas metida tan dentro de mis sentimientos'
    texto3 = 'y de mi corazon, se que no soy alguien perfecto y tengo muchisimo desperfectos, pero quiero poder seguir a su lado'
    texto4 = 'ya se lo eh dicho miles veces, pero se lo seguire diciendo hasta que lo entienda y lo compruebe por usted mismo'
    texto5 = 'y esque sos la unica persona que tengo en mi corazon, la cual amo y adoro muchisimo, jamas podria ver a alguien mas'
    texto6 = 'se lo aseguro porque a pesar de las peleas y de todo lo que hemos pasado me consta decirle, que pienso en usted como'
    texto7 = 'la primera vez en que le dije que la amaba en todos estos dias y meses que pasaron, la eh amando incondicionalmente'
    texto8 = 'sos mi vida, cada suspiro de ella, sos todo por lo que quiero vivir y seguir adelante, ademas de la meta de la universidad'
    texto9 = 'es pasar mi vida a su lado, solo quiero poder ser feliz con usted, sos todo lo bueno que le veo a esta vida'
    texto10 = 'Te amo Nela, te amo y te amare toda mi vida, sos mi sueño a lograr y contigo esta toda mi felicidad'
    imagen = '/static/images/images.jpeg'

    contexto = {
        'titulo' : titulo,
        'texto' : texto,
        'texto1' : texto1,
        'texto2' : texto2,
        'texto3' : texto3,
        'texto4' : texto4,
        'texto5' : texto5,
        'texto6' : texto6,
        'texto7' : texto7,
        'texto8' : texto8,
        'texto9' : texto9,
        'texto10' : texto10,
        'imagen' : imagen
    }
    return render(request, 'nela/nela.html', contexto)