<%inherit file="base.mako"/>

<%block name="title">Mvmap-Pyramid项目首页</%block>

<%block name="main">
    <span>
       <a href="${request.application_url}/logout">登出</a>
    </span>
    
    <ul>
    % for a in ("one", "two", "three"):
        <li>Item ${loop.index}: ${a}</li>
    % endfor
    </ul>
    
    <%
        rows = [[v for v in range(0,10)] for row in range(0,10)]
    %>
    <table>
        % for row in rows:
            ${makerow(row)}
        % endfor
    </table>

    <%def name="makerow(row)">
        <tr>
        % for name in row:
            <td>${name}</td>\
        % endfor
        </tr>
    </%def>

</%block>