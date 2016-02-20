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
		CC = 0;
		CD = 0;
		DT = 0;
		EX = 0;
		FW = 0;
		IN = 0;
		JJ = 0;
4.	EX
5.	FW
6.	IN
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
	for j in tokens:
		if j[1] == "CC":
			CC++;
		else if j[1] == "CD":
			cd ++;
		else if j[1] == "DT":
			DT++;
		else if j[1] == "EX":
			EX++;
		else if j[1] == "DET":
			det++;
