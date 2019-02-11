$(document).ready(function() {

    // позиционирование контента главного меню
    $(window).resize(function(){
        width_dropdown_menu_item_1 = $('#main_menu_item_1').next('div').css('width');
        $('#main_menu_content_wrapper').css('margin-left', width_dropdown_menu_item_1);
    });

    $('main_menu_item_1_submenu').click(function(e) {
        e.preventDefault();
    });


    $(".menu_item_allowed_to_hover_event").mouseover(function (e) {

        $(this).addClass("hovered");
        
        // если у пункта меню контент в контейнере
        if( $('[data-content_main_menu="' + $(this).attr('id') + '"]').length ) {
            // уберем фон обертки контейнера контента
            $("#main_menu_content_wrapper").css('background','none');
            // сначала скроем все блоки
            $(".main_menu_content_items").css("display", "none");
            // установим заголовок (актуально только для подменю первого пункта меню)
            $(".main_menu_content_1_title").text( $(this).text() );
            // покажем нужный блок контента
            $('[data-content_main_menu="' + $(this).attr('id') + '"]').css("display", "block");
        }

        // если у пункта меню обычное подменю
        if( $(this).next(".main_menu_usual_submenu").length ) {
            $(this).next(".main_menu_usual_submenu").css("display", "block");
        }

    });

    /*
    * Out:
    * 1. указателя с пункта меню ( menu_item_allowed_to_hover_event )
    * 2. с контейнера контента пунктов меню ( main_menu_content_items )
    * 3. со стандартного подменю ( main_menu_usual_submenu )
    * */
    $(".menu_item_allowed_to_hover_event, .main_menu_content_items, .main_menu_usual_submenu").mouseleave(function () {

        // out с пункта меню, имеющего обычное подменю
        if ( $(this).next(".main_menu_usual_submenu").length ) {
            // если указатель ушел НЕ на подменю
            if ($(this).next(".main_menu_usual_submenu:hover").length == 0) {
                $(this).removeClass("hovered");
                $(this).next(".main_menu_usual_submenu").css("display", "none");
            }
            return;
        }

        // out с обычного подменю (main_menu_usual_submenu)
        if( $(this).hasClass("main_menu_usual_submenu") ) {
            $(this).css("display", "none");
            $(this).prev("a").removeClass("hovered");
        }

        // out с контейнера контента пунктов меню
        if ( $('.main_menu_content_items:hover').length == 0 ) {
            $('.menu_item_allowed_to_hover_event').removeClass("hovered");
            $(".main_menu_content_items").css("display", "none");
            $("#main_menu_content_wrapper").css(
                'background','url("images/main_menu_content_fon.png") no-repeat;'
            );
        }

    });

    convert_view_to_mobail();
    console.log($(window).width());

    function convert_view_to_mobail() {
        if ($(window).width() <= 768) {
            $('.nav > li').css("width", "100%");
            $('header').css("display", "none");
            $('#main_menu_mobail').css("position", "fixed");
            $('#main_menu_mobail').parent().css("padding-top", "40px");
        } else {
            $('.nav > li').css("width", "20%");
            $('header').css("display", "block");
            $('#main_menu_mobail').css("position", "relative");
            $('#main_menu_mobail').parent().css("padding-top", "0px");
        }
        if ($(window).width() <= 1185) {
            //console.log('main_menu HIDE');
            $('#main_menu').css("display", "none");
            $('#main_menu_mobail').css("display", "block");
        } else {
            //console.log('main_menu SHOW');
            $('#main_menu').css("display", "block");
            $('#main_menu_mobail').css("display", "none");
        }
    }

    $(window).resize(function() {
        convert_view_to_mobail();
    });

    // if ($(window).width() <= 1185) {
    //     console.log('aaaa');
    // }




    // change_height_first_block();
    //
    // $(window).resize(function(){
    //     change_height_first_block();
    // });
    //
    // function change_height_first_block() {
    //     navbar_visible = $(".navbar-toggle").is(":visible");
    //     if (navbar_visible) {
    //         $('.navbar').addClass("navbar-fixed-top");
    //         $(".navbar").css("margin-top", "0px");
    //     }
    //     else {
    //         $('.navbar').removeClass("navbar-fixed-top");
    //         $(".navbar").css("margin-top", "-63px");
    //     }
    // }
    //
    // /* плавный переход к якорям */
    // $("a.scrollto").click(function() {
    //     var elementClick = $(this).attr("href");
    //     var destination = $(elementClick).offset().top;
    //     jQuery("html:not(:animated),body:not(:animated)").animate({
    //         scrollTop: destination
    //     }, 1200);
    //     return false;
    // });
    //
    // /* аниация цифр */
    // runned = false;
    // $(window).scroll(function(){
    //     var top = $('.counter').offset().top,
    //         sctop = $(this).scrollTop(),
    //         winh = $(this).height(),
    //         y = top - sctop - winh;
    //     if (y > 0 || -y > winh) {
    //        // console.log('Не видим');
    //     }
    //     else {
    //         //console.log('Видим');
    //         if(!runned) {
    //             $('#cnt1').prop('number', 0).animateNumber({
    //                 number: 37
    //             }, 4000);
    //             $('#cnt2').prop('number', 0).animateNumber({
    //                 number: 1285
    //             }, 4000);
    //             $('#cnt3').prop('number', 0).animateNumber({
    //                 number: 77
    //             }, 4000);
    //             $('#cnt4').prop('number', 0).animateNumber({
    //                 number: 57
    //             }, 4000);
    //             $('#cnt5').prop('number', 0).animateNumber({
    //                 number: 43
    //             }, 4000);
    //         }
    //         runned = true;
    //     }
    // });
    //
    // /* листалка проектов */
    // timerId = setInterval(function() {
    //     var div = $('.wr_btn_change_foto div[class="active"]');
    //     div.removeClass('active').siblings().addClass('active');
    //
    //     div.parent().parent().siblings('.i').filter(function() {
    //         return $(this).css("display") != "none";
    //     }).css("display","none").siblings('.i').fadeIn('slow'); // css("display","block");
    // }, 4000);
    //
    // $('.wr_btn_change_foto div').click(function(e) {
    //     if( !$(this).hasClass('active') ) {
    //         $(this).siblings().removeClass('active');
    //         $(this).addClass('active');
    //
    //         $(this).parent().parent().siblings('.i').filter(function() {
    //             return $(this).css("display") == "none";
    //         }).css("display","block").siblings('.i').css("display","none");
    //     }
    // });

    /* модалка для озывов */
    /*
    $(function() {
        $('a.item_review').click(function(e) {
            e.preventDefault();
            $('#image-modal .modal-body img').attr('src', $(this).find('img').attr('src'));
            $("#image-modal").modal('show');
        });
        $('#image-modal .modal-body img').on('click', function() {
            $("#image-modal").modal('hide')
        });
    });
    */

});