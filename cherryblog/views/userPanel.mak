% if  cherrypy.session.get('_cp_username')!=None:

<div id="userPanel"><a href="/doLogout" class="fa fa-sign-out" title="logout"></a></div>
% else:
<span id="loginPanelButton"></span>
<div class="loginForm">
	<section id="loginContent">
		<form action="/doLogin" method="post">
			<h1>Login Form</h1>
			<div>
				<input autocomplete="off" type="text" placeholder="Username" name="username" required="" id="username" />
			</div>
			<div>
				<input  autocomplete="off" type="password" placeholder="Password" name="password"  required="" id="password" />
			</div>
			<div>
				<input type="submit" value="Log in" />
			</div>
		</form><!-- form -->

	</section><!-- content -->
</div><!-- container -->

% endif
