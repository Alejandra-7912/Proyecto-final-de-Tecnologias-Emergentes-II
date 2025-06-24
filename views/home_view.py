from flask import render_template
    
def render_list(peliculas):
    return render_template('home/index.html', peliculas=peliculas)

def render_catalogo(peliculas):
    return render_template('home/catalogo.html', peliculas=peliculas)

def render_generos(generos, peliculas, genero_id):
    return render_template(
        'home/generos.html',
        generos=generos,
        peliculas=peliculas,
        genero_id=genero_id
    )
