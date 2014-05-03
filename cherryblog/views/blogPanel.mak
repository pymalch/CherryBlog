<div class="panel">
	<section id="panel">
		<form action="/add" method="post">
			<h1>Add Post</h1>
			<div class="row inpTitle">
			<span class="before fa-flag fa"></span>
				<input type="text" placeholder="Title" name="title" required="true" id="title" />
			</div>
			<div  class="row inpContent">
			<span class="before fa-align-justify fa"></span>
				<textarea placeholder="description ..." name="content"></textarea>
			</div>
			<div  class="row">
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