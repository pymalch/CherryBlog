<!DOCTYPE html>
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		${self.meta()}
		<title>${self.title()}</title>
		<link type="text/css" href="/public/css/style.css" rel="stylesheet" />
		<script language="javascript" src="public/script/jquery.js"></script>

<link href="public/css/font-awesome.css" rel="stylesheet">

<script language="javascript" src="public/script/script.js"></script>
	</head>
	<body>
	<div id="content">
		<header><div id="website">Cherry Blog System </div></header>

				${self.main_menu()}
				${self.body()}
	</div>
	</body>
</html>

<%def name="meta()"></%def>

<%def name="title()">Cherry Blog</%def>

<%def name="main_menu()"></%def>


