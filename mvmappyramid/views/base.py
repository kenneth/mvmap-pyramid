from pyramid.response import Response
from pyramid.view import view_config,forbidden_view_config

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )

from mvmappyramid.security import USERS

from sqlalchemy.exc import DBAPIError

from mvmappyramid.models.base import (
    DBSession,
    MyModel,
    )

import json

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
@view_config(route_name='home',renderer='index.html')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    #return {'one': one, 'project': 'mvmap-pyramid'}
    return dict(
        one = one,
        project = 'mvmap-pyramid',
        logged_in = authenticated_userid(request)
        )


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
    return {'project': 'mvmap-pyramid'}

@view_config(route_name='json',renderer='json')
def hello_world(request):
    return {'content':'Hello!'}

#@view_config(route_name='mako',renderer='mvmappyramid:templates/test.html')
@view_config(route_name='mako',renderer='test.html')
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


@view_config(route_name='view_wiki', renderer='wiki.html')
def view_wiki(request):
    return {}

@view_config(route_name='view_page', renderer='detail.html')
def view_page(request):
    pagename = request.matchdict['pagename']
    return dict(pagename = pagename)

@view_config(route_name='add_page', renderer='edit.html', permission='edit')
def add_page(request):
    return {}

@view_config(route_name='edit_page', renderer='edit.html', permission='edit')
def edit_page(request):
    return {}
    
@view_config(route_name='login', renderer='login.html')
@forbidden_view_config(renderer='ban.html')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        #print "========================================"+USERS.get(login)
        if USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound(location = came_from,headers = headers)
        else:
            message = 'Login Error!!!Please Check'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        logged_in = authenticated_userid(request)
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('view_wiki'),
                     headers = headers)

@view_config(route_name='session')
def session_view(request):
    session = request.session
    if 'abc' in session:
        session['fred'] = 'yes'
    session['abc'] = '123'
    if 'fred' in session:
        return Response('Fred was in the session')
    else:
        return Response('Fred was not in the session')
        
@view_config(route_name='acl',renderer='json')
def acl_view(request):
    d = {
        'admin':{'ios': 'view','android': 'add'},
        'test':{'ios':'view','android':'view'}
    }
    json_string = json.dumps(d)
    return Response(json_string)


