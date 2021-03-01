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

function openCity(evt, tag) {
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
// if(document.body.scrollTop > 100){
//     document.getElementById('menu')
// }
// window.onscroll = function() {

// }
// if(document.body.scrollTop > 100){
//     document.getElementById('top_btn').style.display = 'flex';
// }
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