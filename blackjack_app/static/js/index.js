var play = document.getElementById("play")
var hit = document.getElementById("hit")
var stand = document.getElementById("stand")
var deck = [
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A"
]
var ranindex = Math.floor(Math.random()*deck.length);

console.log(deck)


play.onclick = function(){
    document.getElementById("first-user-card").append(deck.splice(ranindex, 1)[0]);
    document.getElementById("second-user-card").append(deck.splice(ranindex, 1)[0]);
    document.getElementById("first-dealer-card").append(deck.splice(ranindex, 1)[0]);
    document.getElementById("second-dealer-card").append(deck.splice(ranindex, 1)[0]);
    console.log(deck)
}

hit.onclick = function(){
    var newp = document.createElement("p")
    newp.textContent=deck.splice(ranindex, 1)[0]
    document.getElementById("user").append(newp)
    console.log(deck)
}