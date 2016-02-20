// Checking page title
if (document.title.indexOf("Google") != -1) {
    //Creating Elements
    
    
    

    var blackOverlayDiv = document.createElement("div");
    blackOverlayDiv.style.cssText = "position: fixed;width:100%;height:100%;background-color:rgba(0,0,0,0.3);";
    


    var imgDiv = document.createElement("div");
	var img = document.createElement("img");
	div.style.cssText = "width:100%;height:100%";
    img.src = "https://tctechcrunch2011.files.wordpress.com/2015/12/khaled-snapchat1.jpg?w=1279&h=727&crop=1";
    img.style.width = "100%";
    div.appendChild(img);


    document.body.appendChild(blackOverlayDiv);
    document.body.appendChild(div);
    


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



