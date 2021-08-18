var myImage = document.querySelector('img');

/* Фотки при клике меняются */
myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/norw.jfif') {
      myImage.setAttribute ('src','images/firefox2.png');
    } else {
      myImage.setAttribute ('src','images/norw.jfif');
    }
}

/* Создание кнопки, запрос имения пользователя и сохранение его*/
var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
  var myName = prompt('Введите свое имя.');
  localStorage.setItem('name', myName);
  myHeading.textContent = 'Привет тебе, ' + myName;
}

if(!localStorage.getItem('name')) {
  setUserName();
} else {
  var storedName = localStorage.getItem('name');
  myHeading.textContent = 'Mozilla is cool, ' + storedName;
}

myButton.onclick = function() {
  setUserName();
}
