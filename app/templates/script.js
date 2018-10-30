var path = '/images',
    imgs = ['1.jpg','2.jpg','3.jpg'],
    i = Math.floor(Math.random()*imgs.length);
$('.el').append("<img src='"+path+imgs[i]+"'>").hide().fadeIn(2000);