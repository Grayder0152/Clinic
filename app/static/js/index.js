$('.slider').slick({
    centerMode:true,
    centerPadding:'100px',
    infinite: true,
    autoplay: true,
    autoplaySpeed: 4000,
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow:'<a class="prev">&#10094;</a>',
    nextArrow:'<a class="next">&#10095;</a>',
    responsive: [
    {
      breakpoint: 720,
      settings: {
        centerMode:false,
        arrows:false,
        dots:true,
        dotsClass:'dots'
      }
    }
    ]
});

$("#review_form").validate({
    rules: {
        name: {
            required: true,
            minlength: 2,
            maxlength: 30
        },
        text: {
            required: true,
            minlength: 15,
            maxlength: 100
        }
    },
    messages: {
        name: {
            required: "*Ви не ввели своє ім'я!",
            minlength:"*Ім'я занадто коротке!",
            maxlength:"*Макс. 30 символів!"
        },
        text: {
            required: "*Ви не ввели ваш відгук!",
            minlength:"*Відгук повинен містити більше ніж 15 символів!",
            maxlength:"*Макс. 100 символів!"
        }
    }
});
