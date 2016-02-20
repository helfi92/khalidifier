// Checking page title

// Replaces images with DJKaled images
$('img').each(function() {
	var width = $(this).width(),
		height = $(this).height();

	$(this).attr('src', chrome.extension.getURL(khaledImages.choose()));
	$(this).attr({
		width: width,
		height: height
	});
});
khaledImages = ["assets/images/khaled-1.png","assets/images/khaled-2.png","assets/images/khaled-3.png","assets/images/khaled-4.png", "assets/images/khaled-5.png", "assets/images/khaled-6.jpg", "assets/images/khaled-7.jpg"];


if (document.title.indexOf("Google") != -1) {
    //Creating Elements
 
    //var blackOverlayDiv = document.createElement("div");
    //blackOverlayDiv.style.cssText = "position: absolute;width:100%;height:100%;background-color:rgba(0,0,0,0.3);z-index:-1;";

    var imgDiv = document.createElement("div");
	var img = document.createElement("img");
	imgDiv.style.cssText = "width:100%;height:100%;text-align:center;";
    

	//var randomImg = Math.floor(Math.random() * (khaledImages.length - 0));
	//console.log('random: ', randomImg);

	var imgURL = chrome.extension.getURL(khaledImages[4]);
    img.src = imgURL;
    img.id ="khaled-background";
    img.style.height = "auto";
    imgDiv.appendChild(img);


    //document.body.appendChild(blackOverlayDiv);
    document.body.appendChild(imgDiv);
    

    //replace class .g to white
    $("<style>.g{background-color:rgba(255,255,255,0.8);}</style>").appendTo("body");

}


quotes = [
	"Smh they get mad when u have joy.",
	"Baby, you smart. I want you to film me taking a shower.",
	"The key is to make it.",
	"Key to more success is clean heart and clean face.",
	"You smart! You loyal! You're a genius!",
	"Give thanks to the most high.",
	"They will try to close the door on u, just open it.",
	"They don't want you to win. They don't want you to have the No. 1 record in the country. They don't want you to get healthy. And they don't want you to have that view.",
	"I don't have no favorite rock bands. I'm a fan of rock music though.",
	"I wanted to see what type of trees is growing in Marcy Projects, what type of water Jay Z was drinking.",
	"Those that weather the storm r the great ones.",
	"The key to more success is coco butter.",
	"I changed... a lot.",
	"My fans expect me to be greater and keep being great.",
	"There will be road blocks but we will overcome it.",
	"They don't want you to jet ski.",
	"Them doors that was always closed, I ripped the doors off, took the hinges off. And when I took the hinges off, I put the hinges on the f*ckboys' hands.",
	"Congratulations, you played yourself.",
	"You want my advice? Don't play yourself.",
	"Another one, no. Another two, drop two singles at a time.",
	"I can deal with everything. I got the answer for anything. This DJ Khaled.",
	"Go buy yo' momma a house. Go buy your whole family houses. Put this money in your savings account.",
	"Another one. Another one. Another one.",
	"Baby I got us calm down relax who you love.",
	"The key to more success is to have a lot of pillows.",
	"You see that bamboo behind me though. You see that bamboo. Ain't nothin' like bamboo.",
	"Life is smooth. It's on you if you want to be smooth. Some people want to live life rough and crazy."
];

// Replace all quotes with DJKaled quotes

Array.prototype.choose = function() {
	return this[Math.floor(Math.random() * this.length)];
};

jQuery = jQuery || $;

textNodes = jQuery('*').contents().filter(function() {
  return this.nodeType == 3;
});

// replaces all quotes
jQuery(textNodes).each(function() {
	if(this.nodeValue === undefined) {
		console.log(this);
		return;
	}
	this.nodeValue = this.nodeValue.replace(/"[^"]+"/g, function() {
		return '"' + quotes.choose() + '"';
	});
	this.nodeValue = this.nodeValue.replace(/“[^”]+”/g, function() {
		return '“' + quotes.choose() + '”';
	});

}); 

console.log('extension!');

// Player DJKaled song

player = $("<audio controls autoplay><source src='" + chrome.extension.getURL('assets/music/sample.wav') + "' type='audio/wav'></audio>");
$('body').append(player);
player.css({

	position: 'fixed',
	bottom: '1em',
	right: '1em',
	'z-index': 9999999999
});

