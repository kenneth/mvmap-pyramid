<!DOCTYPE html>
<html lang="zh-CN">
<head>
<title><%block name="title"></%block></title>
<meta charset="UTF-8" />
<link rel="stylesheet" href="${request.static_url('mvmappyramid:static/css/bootstrap.min.css')}" />
<link rel="stylesheet" href="${request.static_url('mvmappyramid:static/css/bootstrap-theme.min.css')}" />
</head>
<body>

    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">首页</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-search navbar-form navbar-left" action="#" method="GET">
          <input type="text" placeholder="搜索" name="wd" class="form-control" id="wd">
          </form>
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">菜单</a></li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="/login">登录</a></li>
            <li><a href="/logout">登出</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">个人中心<b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">我的主页</a></li>
                <li class="divider"></li>
                <li><a href="#">设置</a></li>
                <li><a href="#">登出</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>

<div class="jumbotron"></div>
<div class="container">
  <%block name="main">
  </%block>
</div>

<script src="${request.static_url('mvmappyramid:static/js/jquery-1.10.2.min.js')}"></script>
<script src="${request.static_url('mvmappyramid:static/js/bootstrap.min.js')}"></script>
</body>
</html>