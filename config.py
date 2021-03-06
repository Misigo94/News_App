import os

class Config():
    '''
    General configuration of the parent class

    '''
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?apiKey={}"
    ARTICLE_API_BASE_URL= "https://newsapi.org/v2/everything?sources={}&apiKey={}"
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    production configuration of child class 
    Args :
        config - the parent configuration class with  general configuration settings
    '''

class DevConfig(Config) :
    '''
     Development configuration of the parent class
     
     Args:
        Config - the parent configuration class with  general configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}    
