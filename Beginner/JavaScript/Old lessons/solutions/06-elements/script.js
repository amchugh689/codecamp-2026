function changeHeaderText(){
    header = document.getElementById("demo");
    header.innerHTML = "Hello, this text has been changed!";
}

function changeHeaderColor(){
    header = document.getElementById("demo");
    header.style.color = 'red';
}

function changeParaColors() {
    paras = document.querySelectorAll('p');
    paras.forEach(para => {
        para.style.color = 'green';
    });
}

function changeImage() {
    let images = ["placeholder1.jpg", "placeholder2.jpg", "placeholder3.jpg", "placeholder4.png"];
    let image = document.querySelector('.imageclass')

    let imageNum = parseInt(image.id);

    alert(imageNum)
    if(imageNum == 3) {
        image.src = "img/"+ images[0]
        image.id = 0;
    }
    else {
        imageNum++;
        image.src = "img/"+images[imageNum];
        image.id=imageNum;
    }



}
