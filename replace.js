quotes = [
	"Smh they get mad when u have joy.",
	"Baby, you smart. I want you to film me taking a shower."
];

Array.prototype.choose = function() {
	return this[Math.floor(Math.random() * this.length];
};

$('*:not(:has(*))').text(function() {
	return $(this).text().replace(/"+"/g, quotes.choose());
}); 