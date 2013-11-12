from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.base import (
    DBSession,
    Base,
    )

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from mvmappyramid.security import groupfinder

authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
authz_policy = ACLAuthorizationPolicy()

from pyramid.session import UnencryptedCookieSessionFactoryConfig
my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings,root_factory='mvmappyramid.models.base.RootFactory',session_factory = my_session_factory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_chameleon')
    config.include('pyramid_mako')
    config.include('pyramid_beaker')
    config.include('cornice')
    config.add_mako_renderer('.html')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('test', '/test')
    config.add_route('session', '/session')
    config.add_route('json', '/json')
    config.add_route('acl', '/acl')
    config.add_route('mako', '/mako')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('view_wiki', '/wiki')
    config.add_route('view_page', '/view_page/{pagename}')
    config.add_route('add_page', '/add_page/{pagename}')
    config.add_route('edit_page', '/{pagename}/edit_page')
    config.scan()
    return config.make_wsgi_app()
