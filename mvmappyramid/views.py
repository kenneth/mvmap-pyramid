from pyramid.response import Response
from pyramid.view import view_config,forbidden_view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


#@view_config(route_name='home', renderer='templates/mytemplate.pt')
@view_config(route_name='home',renderer='index.mako')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'mvmap-pyramid'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_mvmap-pyramid_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

@view_config(route_name='test', renderer='templates/test.pt')
def test_view(request):
    return {'project': 'demo'}

@view_config(route_name='json',renderer='json')
def hello_world(request):
    return {'content':'Hello!'}

#@view_config(route_name='mako',renderer='mvmappyramid:templates/test.mako')
@view_config(route_name='mako',renderer='test.mako')
def mako(request):
    return {'content':'Hello!'}

#Cornice: A REST framework for Pyramid
from cornice import Service
from pyramid.security import remember, authenticated_userid, Allow, Everyone, Deny, ALL_PERMISSIONS

def _check_acl(request):
    return [
        (Deny, Everyone, ALL_PERMISSIONS),
        (Allow, 'admin', 'add'),
        (Allow, 'admin', 'view')
    ]

hello = Service(name='hello', path='/api', description="Simplest app",acl=_check_acl)

@hello.get(permission='add')
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}


@view_config(route_name='view_wiki')
def view_wiki(request):
    return {}

@view_config(route_name='view_page', renderer='detail.mako')
def view_page(request):
    return {}

@view_config(route_name='add_page', renderer='edit.mako', permission='edit')
def add_page(request):
    return {}

@view_config(route_name='edit_page', renderer='edit.mako', permission='edit')
def edit_page(request):
    return {}
    
@view_config(route_name='login', renderer='login.mako')
@forbidden_view_config(renderer='ban.mako')
def login(request):
    return {}

@view_config(route_name='logout')
def logout(request):
    return {}


