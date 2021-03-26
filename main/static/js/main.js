window.onload = function() {
    window.setTimeout(function () {
        document.querySelector('.preloader').classList.add("preloader-remove");
    }, 2500);
};

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


