import nltk;

quotes = [];
	print (	"CC, CD, DT, EX, FW, IN, JJ, JJR, JJS, LS, MD, NN, NNS, NNP, NNPS , PDT , POS, PRP, PRPX, RB, RBR, RBS, RP, SYM, TO, UH, VB, VBD, VBG, VBN, VBP, VBZ, WDT, WP, WPX , WRB",file = text_file);
	for i in quotes:
		words = nltk.word_tokenize(i);
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
			#print (j);
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
		
		print (	CC, CD, DT, EX, FW, IN, JJ, JJR, JJS, LS, MD,
				NN, NNS, NNP, NNPS , PDT , POS, PRP, PRPX, RB, RBR, RBS, RP, SYM, TO, UH, VB, VBD, VBG, VBN, VBP, VBZ, WDT, WP, WPX , WRB, sep = ",",file = text_file);
