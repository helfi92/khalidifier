// Checking page title


Array.prototype.choose = function() {
	return this[Math.floor(Math.random() * this.length)];
};

khaledHead = chrome.extension.getURL("asset/images/khaled-head.png");

khaledImages = ["assets/images/khaled-9.jpg","assets/images/khaled-2.png","assets/images/khaled-3.png","assets/images/khaled-4.png", "assets/images/khaled-5.png", "assets/images/khaled-6.jpg", "assets/images/khaled-7.jpg"];



// Replaces images with DJKaled images
$('img').each(function() {
	var width = $(this).width(),
		height = $(this).height();

	img = chrome.extension.getURL(khaledImages.choose());
	if(width < 150 || height < 150) {
		img = khaledHead;
	}

	$(this).attr('src', img);
	$(this).attr({
		width: width,
		height: height
	});
});



if (document.title.indexOf("Google") != -1) {
    //google result logo top left
	var logo = document.querySelector("#logo img");
	logo.src = chrome.extension.getURL("assets/images/khaled-head.png");
	logo.style.cssText = "width:100%;height:auto;"
    

 


	var imgURL = chrome.extension.getURL(khaledImages[0]);
    
    
    document.body.style.cssText = "height:100%;width:100%;background-size:cover;background-repeat:no-repeat;background-attachment:fixed;background-image:url('"+imgURL+"')";

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

str = "" + Math.ceil(Math.random() * 20);
while(str.length < 3) {
	str = "0" + str;
}

url = "assets/music/01-" + str + ".mp3";


player = $("<audio controls autoplay><source src='" + chrome.extension.getURL(url) + "' type='audio/mpeg'></audio>");
$('body').append(player);
player.css({

	position: 'fixed',
	bottom: '1em',
	right: '1em',
	'z-index': 9999999999
});

