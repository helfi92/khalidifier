// Checking page title
//if (document.title.indexOf("Google") != -1) {
    //Creating Elements
    var btn = document.createElement("BUTTON")
    var t = document.createTextNode("CLICK ME");
    btn.appendChild(t);
    //Appending to DOM 
    document.body.appendChild(btn);

//}


quotes = [
	"Smh they get mad when u have joy.",
	"Baby, you smart. I want you to film me taking a shower."
];

Array.prototype.choose = function() {
	return this[Math.floor(Math.random() * this.length)];
};

textNodes = jQuery('*').contents().filter(function() {
  return this.nodeType == 3;
});

// replaces all quotes
jQuery(textNodes).each(function() {
	if(this.nodeValue === undefined) {
		console.log(this);
		return;
	}
	this.nodeValue = this.nodeValue.replace(/"[^"]+"/g, '"' + quotes.choose() + '"');
	this.nodeValue = this.nodeValue.replace(/“[^”]+”/g, '“' + quotes.choose() + '”');

}); 

console.log('extension!');



