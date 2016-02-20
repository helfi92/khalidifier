// Checking page title
if (document.title.indexOf("Google") != -1) {
    //Creating Elements
    
    
    

    var blackOverlayDiv = document.createElement("div");
    blackOverlayDiv.style.cssText = "position: fixed;width:100%;height:100%;background-color:rgba(0,0,0,0.1);";
    
    khaledImages = ["assets/images/khaled-1.png"];


    var imgDiv = document.createElement("div");
	var img = document.createElement("img");
	imgDiv.style.cssText = "width:100%;height:100%";
    


	var imgURL = chrome.extension.getURL(khaledImages[0]);
    img.src = imgURL;
    img.style.width = "100%";
    imgDiv.appendChild(img);


    //document.body.appendChild(blackOverlayDiv);
    document.body.appendChild(imgDiv);
    


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
	return $(this).text().replace(/"+"/g, '"' + quotes.choose() + '"');
}); 

    console.log('extension!');



