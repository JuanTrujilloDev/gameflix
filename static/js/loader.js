$(window).on("load",function(){
    
    $(".loader-wrapper").delay(1500).fadeOut("slow");
    $(this).scrollTop(0);
    
    setTimeout(function(){
    $("body").removeClass("hidden");
    $("nav").removeClass("hidden");
    $("div").removeClass("hidden");
    $("header").removeClass("hidden");
    $("header").focus();

    }, 1800);
    
    
});