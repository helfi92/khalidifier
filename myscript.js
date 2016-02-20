// Checking page title
if (document.title.indexOf("Google") != -1) {
    //Creating Elements
    var btn = document.createElement("BUTTON")
    var t = document.createTextNode("CLICK ME");
    btn.appendChild(t);
    //Appending to DOM 
    document.body.appendChild(btn);
}


quotes = [
	"Smh they get mad when u have joy.",
	"Baby, you smart. I want you to film me taking a shower."
];

Array.prototype.choose = function() {
	return this[Math.floor(Math.random() * this.length)];
};

// Replaces all quotes
$('*:not(:has(*))').text(function() {
	return $(this).text().replace(/"[^"]+"/g, '"' + quotes.choose() + '"');
}); 
