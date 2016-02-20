import nltk;

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
	"I can deal with everything. I got the answer for anything. This DJ Khaled."
];

for i in quotes:
	tokens = nltk.word_tokenize(i);
	print(nltk.pos_tag(tokens));


#print (quotes);