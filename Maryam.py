from flask import Flask, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>For Mariam ❤️</title>

<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300&display=swap" rel="stylesheet">

<style>

body{
margin:0;
padding:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
text-align:center;
background: linear-gradient(135deg,#0f0c29,#302b63,#24243e);
font-family:'Poppins',sans-serif;
color:white;
overflow:hidden;
}

.container{
width:75%;
max-width:900px;
}

.title{
font-family:'Great Vibes',cursive;
font-size:65px;
color:#ff7aa2;
margin-bottom:40px;
text-shadow:0 0 25px rgba(255,122,162,0.9);
}

#text{
font-size:22px;
line-height:1.8;
white-space:pre-line;
}

/* floating hearts */

.heart{
position:absolute;
bottom:-50px;
color:#ff4d6d;
animation: float 8s linear infinite;
opacity:0.8;
}

@keyframes float{

0%{
transform:translateY(0) scale(1);
opacity:1;
}

100%{
transform:translateY(-1000px) scale(1.5);
opacity:0;
}

}

</style>
</head>

<body>

<div class="container">

<div class="title">
Happy Belated Birthday Maryam ❤️
</div>

<div id="text"></div>

</div>

<script>

const message = `Even though your special day has already passed, I still wanted to create something meaningful for you, something small but sincere that carries my wishes and appreciation for the wonderful person you are.

Sometimes words cannot fully explain how much someone means, but I still wanted to try. You are someone truly special, someone whose kindness, patience, and warmth can make a simple moment feel beautiful.

On this new chapter of your life, I pray that Allah fills your days with peace, your heart with joy, and your path with success and blessings.

May this year bring you more laughter, more unforgettable memories, more opportunities, and many moments that remind you how valued and appreciated you truly are.

Even if this message comes after your birthday has passed, the sincerity of the wishes remains the same.

So once again from the heart:

Happy Belated Birthday Maryam ❤️

May the days ahead bring you happiness, peace, success, and beautiful surprises.`;


let i = 0;

let speed = 55;

function typeWriter(){

if(i < message.length){

document.getElementById("text").innerHTML += message.charAt(i);

i++;

setTimeout(typeWriter, speed);

}

}

typeWriter();


// floating hearts

setInterval(function(){

let heart = document.createElement("div");

heart.innerHTML = "❤️";

heart.className = "heart";

heart.style.left = Math.random()*100 + "vw";

heart.style.fontSize = (20 + Math.random()*25) + "px";

document.body.appendChild(heart);

setTimeout(function(){

heart.remove();

},8000);

},400);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)

if __name__ == "__main__":
    app.run(debug=True)
