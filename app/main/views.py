from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source,Article

#Views
@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    #Getting source
    sources = get_sources('sources')

    return render_template('index.html', sources = sources)

@main.route('/articles/<id>')
def articles(id):
    """
    View Articles page function that returns the source details page and its data
    """
    articles = get_articles(id)
    title= f'{id}'

    return render_template('articles.html', id = id,articles= articles)