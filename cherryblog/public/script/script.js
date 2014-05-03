/**
 * Created by malach on 5/1/14.
 */
$(function(){

    $('.postTitle').click(function(){
       $('article').has($(this)).toggleClass('open');
        var top=$(this).offset().top;
        $('html,body').animate({scrollTop: top +'px'});
    });

    $('#loginPanelButton').click(function(){
        $('.loginForm').slideToggle();
    });
});