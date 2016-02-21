#!flask/bin/python
from flask import Flask, jsonify, request
import urllib
import json
import nltk;
url = 'https://ussouthcentral.services.azureml.net/workspaces/0fbc667abffc433ca9f0c7ffb2127fa6/services/f4f3fd4a45be412c9d4e6177078701e8/execute?api-version=2.0'
api_key = 'MIjisO57tPoSr8zmQY11FUs9/+7ggSxX3tYvNvk0kgO88NuIwBCf/Hb4ZRHt4p+Xz/eixaLIDMgpxuUrlAl+7A==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

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

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks/<string:i>', methods=['GET'],)
def get_task(i):
	b = i;
	b = b.replace("_"," ");
	words = nltk.word_tokenize(b);
	tokens = nltk.pos_tag(words);
	CC = 0;
	CD = 0;
	DT = 0;
	EX = 0;
	FW = 0;
	IN = 0;
	JJ = 0;
	JJR = 0;
	JJS = 0;
	LS = 0;
	MD = 0;
	NN = 0;
	NNS = 0;
	NNP =0;
	NNPS = 0;
	PDT = 0;
	POS = 0;
	PRP = 0;
	PRPX = 0;
	RB = 0;
	RBR = 0;
	RBS = 0;
	RP = 0;
	SYM = 0;
	TO = 0;
	UH = 0;
	VB = 0;
	VBD = 0;
	VBG = 0;
	VBN = 0;
	VBP = 0;
	VBZ = 0;
	WDT = 0;
	WP = 0;
	WPX = 0;
	WRB = 0;
	for j in tokens:
		if j[1] == "CC":
			CC+=1;
		elif j[1] == "CD":
			CD +=1;
		elif j[1] == "DT":
			DT+=1;
		elif j[1] == "EX":
			EX+=1;
		elif j[1] == "FW":
			FW+=1;
		elif j[1] == "IN":
			IN +=1;
		elif j[1] == "JJ":
			JJ+=1;
		elif j[1] =="JJR":
			JJR+=1;
		elif j[1] == "JJS":
			JJS +=1;
		elif j[1] == "LS":
			LS +=1;
		elif j[1] == "MD":
			MD+=1;
		elif j[1] =="NN":
			NN+=1;
		elif j[1] == "NNS":
			NNS +=1;
		elif j[1] == "NNP":
			NNP+=1;
		elif j[1] =="NNPS":
			NNPS+=1;
		elif j[1] == "PDT":
			PDT +=1;
		elif j[1] == "POS":
			POS+=1;
		elif j[1] =="PRP":
			PRP+=1;
		elif j[1] == "PRPX":
			PRPX +=1;
		elif j[1] == "RB":
			RB +=1;
		elif j[1] =="RBR":
			RBR+=1;
		elif j[1] == "RP":
			RP +=1;
		elif j[1] == "SYM":
			SYM+=1;
		elif j[1] =="TO":
			TO+=1;
		elif j[1] == "UH":
			UH +=1;
		elif j[1] == "VB":
			VB+=1;
		elif j[1] =="VBD":
			VBD+=1;
		elif j[1] == "VBG":
			VBG +=1;
		elif j[1] == "VBN":
			VBN +=1;
		elif j[1] =="VBP":
			VBP+=1;
		elif j[1] == "VBG":
			VBG +=1;
		elif j[1] == "VBN":
			VBN+=1;
		elif j[1] =="VBP":
			VBP+=1;
		elif j[1] == "VBZ":
			VBZ +=1;
		elif j[1] == "WDT":
			WDT+=1;
		elif j[1] =="WP":
			WP+=1;
		elif j[1] == "WPX":
			WPX +=1;
		elif j[1] == "WRB":
			WRB +=1;
	data={
    "Inputs": {

            "input1":
            {
                "ColumnNames": ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRPX", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WPX", "WRB"],
                "Values": [ [ CC, CD, DT, EX, FW, IN, JJ, JJR, JJS, LS, MD, NN, NNS, NNP, NNPS , PDT , POS, PRP, PRPX, RB, RBR, RBS, RP, SYM, TO, UH, VB, VBD, VBG, VBN, VBP, VBZ, WDT, WP, WPX , WRB ], ]
            },        },
        "GlobalParameters": {}
	}

	#
	#return(jsonify(data))

	body = str.encode(json.dumps(data))

	req = urllib.request.Request(url, body, headers) 

	try:
		response = urllib.request.urlopen(req)
		result = response.read()
		encoding = response.info().get_content_charset('utf8')  # JSON default
		data = json.loads(result.decode(encoding))
		arr = []
		maxNum = 0;
		index = 0;
		theIndex = 0;
		for no in data['Results']['output1']['value']['Values'][0]:
			arr.append(no)

		for i in arr:
			j = i
			if float(j) > maxNum:
				maxNum = float(j)
				theIndex = index;
			index +1;


		if index == 0:
			return str(quotes[0])
		
		elif index == 1:
			return str(quotes[1])
		
		elif index == 2:
			return str(quotes[2])
		
		elif index == 3:
			return str(quotes[3])
		
		elif index == 4:
			return str(quotes[4])
		
		elif index == 5:
			return str(quotes[5])
		
		elif index == 6:
			return str(quotes[6])
		
		elif index == 7:
			return str(quotes[7])
		
		elif index == 8:
			return str(quotes[8])
			
		elif index == 9:
			return str(quotes[9])
		
		elif index == 10:
			return str(quotes[10])
		
		elif index == 11:
			return str(quotes[11])
		
		elif index == 12:
			return str(quotes[12])
				
		elif index == 13:
			return str(quotes[13])
		
		elif index == 14:
			return str(quotes[14])
		
		elif index == 15:
			return str(quotes[15])
		
		elif index == 16:
			return str(quotes[16])
		
		elif index == 17:
			return str(quotes[17])
		
		elif index == 18:
			return str(quotes[18])
		
		elif index == 19:
			return str(quotes[19])
		
		elif index == 20:
			return str(quotes[20])
		
		elif index == 21:
			return str(quotes[21])
		
		elif index == 22:
			return str(quotes[22])
		
		elif index == 23:
			return str(quotes[23])
		
		elif index == 24:
			return str(quotes[24])
		
		elif index == 25:
			return str(quotes[25])
		
		elif index == 26:
			return str(quotes[26])
		
		
	except urllib.error.HTTPError as err:
	    return ("The request failed with status code: " + str(err.code))

	    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
	    print(err.info())

	    print(json.loads(err.read()))

	    encoding = err.info().get_content_charset('utf8')  # JSON default
		# data = json.loads(result.decode(encoding))

	    return ("The request failed with status code: " + str(err.code),err.info() + str(json.loads(err.read().decode(encoding))))
	    return ("error")


if __name__ == '__main__':
    app.run(debug=True)
