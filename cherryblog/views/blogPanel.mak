<div class="panel">
	<section id="panel">
		<form action="/add" method="post">
			<h1>Add Post</h1>
			<div>
				<input type="text" placeholder="Title" name="title" required="true" id="title" />
			</div>
			<div>
				<textarea placeholder="description ..." name="content"></textarea>
			</div>
			<div>
				<input type="submit" value="Publish Blog" />

			</div>
		</form><!-- form -->

	</section><!-- content -->
</div><!-- container -->
<script language="javascript">
$(function(){
    $('.posts article').each(function(){
        $(this).prepend('<span class="actions"><a class="fa fa-edit" href="#0"><a>   <a class="fa fa-times" href="delete/' + $(this).attr('data-id')+ '"><a></span>')
    });
    $('.actions .fa-times').click(function(){
        return confirm('Are you sure to delete this post?');
    }

    );
});
</script>