<%inherit file="base.mako"/>

<%block name="title">Mvmap-Pyramid项目首页</%block>

<%block name="main">
    <span tal:condition="logged_in">
       <a href="${request.application_url}/logout">登出</a>
    </span>
</%block>