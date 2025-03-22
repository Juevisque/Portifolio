

window.alert("Wellcome to my Js Webpage!")

//Comment

/* 
    Multiline
    comment
*/

//varibles declaration: (var, let, const)

let Fname = "joo"; 
let age = 20;
let student = true;

console.log("Hello", Fname);
console.log("You are",age,"years old");
console.log("Enrolled:",student);

document.getElementById("p1").innerHTML = "Hello " + Fname;
document.getElementById("p2").innerHTML = "You are " + age + "years old";
document.getElementById("p3").innerHTML = "Enrolled: " + student;

/*
    ARITHMETIC EXPRESSIONS
age = age + 1;
age = age - 1;
age = age * 1;
age = age / 1;
let anotherAge = age % 3;

kinda the same think, but simplificated:

age += 1;
age -= 1;
age *= 1;
age /= 1;

console.log(anotherAge)
*/

//How to accept user input in EASY and DIFFICULT ways:

//EASY: window prompt

//let username = window.prompt("What's your name?");
//console.log(username)

//DIFFICULT: HTML textbox

let username;

document.getElementById("mybutton").onclick = function(){
    username = document.getElementById("mytext").value;
    console.log(username);
    document.getElementById("p4").innerHTML = "Hello " + username;
}
