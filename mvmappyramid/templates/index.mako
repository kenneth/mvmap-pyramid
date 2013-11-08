<%inherit file="base.mako"/>

<%block name="main">
    <span tal:condition="logged_in">
       <a href="${request.application_url}/logout">登出</a>
    </span>
</%block>