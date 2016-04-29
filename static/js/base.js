/**
 * Created by liuchao on 16-4-18.
 */

$(document).ready(function(){


    $('.nav-login').click(function(){
        $('.popover-mask').fadeIn(50);
        $('.theme-popover').show();
    });

    $('.login-title .login-close').click(function(){
        $('.popover-mask').fadeOut(50);
        $('.theme-popover').hide();
    });

    $('.nav-register').click(function(){
        $('.popover-mask').fadeIn(50);
        //$('.popover-mask').;
        $('.reg-popover').show();
    });

    $('.register-title .register-close').click(function(){
        $('.popover-mask').fadeOut(50);
        $('.reg-popover').hide();});

    $("#logout").click(function(){
        $.ajax({
            type:"POST",
            url:"/userauth/logout/",
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data,textStatus){
                location.replace("/");
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }
        });
        return false;
    });
});
