const smoothLinks = document.querySelectorAll('a[href^="#"]');
for (let smoothLink of smoothLinks) {
    smoothLink.addEventListener('click', function (e) {
        e.preventDefault();
        const id = smoothLink.getAttribute('href');

        document.querySelector(id).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
};


function viewTag(evt, tag) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tag).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("default_open").click(); 



function openNav(id) {
    document.getElementById(id).style.height = "100vh";
}

function closeNav(id) {
    document.getElementById(id).style.height = "0";
} 
function burger(el){
    el.classList.toggle('active');
    document.getElementById('menu').classList.toggle('show_menu');
}

window.addEventListener('scroll', function() {
    if(pageYOffset > 300){
        document.getElementById('top_btn').style.bottom = '20px';
        document.getElementById('top_btn').style.opacity = '1';
    }
    else{
        document.getElementById('top_btn').style.bottom = '-50px';
        document.getElementById('top_btn').style.opacity = '0';
    }
});

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slide");
    var dots = document.getElementsByClassName("dot");

    if (n > slides.length) {
      slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}
var slideIndex = 2;
showSlides(slideIndex);

function plusSlide() {
    showSlides(slideIndex += 1);
}

function minusSlide() {
    showSlides(slideIndex -= 1);  
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}