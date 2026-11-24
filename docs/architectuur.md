\#Architectuuroverzicht 



&#x09;4.1 Doel van het systeem 

&#x09;

&#x09;Het doel van het systeem is om leerlingen te helpen bij het begrijpen van paragraaf 	15.1 van het theorieboek natuurkunde.

&#x09;Aan het begin van een sessie maakt de leerling een instaptoets, bestaande uit tien 	vragen gebaseerd op de lesstof uit het 	theorieboek. Op basis van de resultaten wordt 	een studentmodel opgesteld, waarin wordt vastgesteld welke concepten de leerling 	beheerst en welke concepten extra aandacht nodig hebben. 



&#x09;Daarna genereert het systeem een gepersonaliseerde uitleg, opdrachten, hints en 	socratische vragen. Na iedere opdracht wordt het antwoord van de leerling 	geëvalueerd en wordt het studentmodel bijgewerkt. Daardoor ontstaat er een adaptieve 	feedbacklus, waarbij de begeleiding steeds wordt afgestemd op het kennisniveau dat 	een leerling op dat moment heeft.



&#x09;

&#x09;4.2 Architectuuroverzicht 

&#x09;De architectuur van het systeem bestaat uit verschillende componenten die samenwerken 	om gepersonaliseerde begeleiding mogelijk te 	maken. 

&#x09;

&#x09;Leerling -> leerlingprofiel -> instaptoets -> diagnosemodule -> student model -> 	tutor agent -> RAG-systeem -> uitleg en 	opdrachten -> evaluatiemodule -> 	student model bijwerken -> en opnieuw

&#x09;

&#x09;De verschillende componenten worden hieronder beschreven. 



&#x09;4.3 leerlingprofiel 

&#x09;Het leerlingprofiel bevat de algemene informatie over de leerling. Hiervoor worden de 	categorieën slecht, matig, voldoende, goed 	en uitstekend gebruikt. Ook bevat het 	informatie over eerdere misconcepties van de leerling en eventueel voorkennis van de 	leerling. De informatie wordt gebruikt om de begeleiding verder te personaliseren. 



&#x09;4.4 Instaptoets

&#x09;De instaptoets bestaat uit tien vragen die gebaseerd zijn op paragraaf 15.1 van het 	theorieboek. De toets bestaat 7 A-vragen, 2 B-	vragen en 1 C-vraag.

&#x09;Tijdens de toets wordt er geen feedback gegeven aan de leerling, het is echt bedoeld 	om het beginniveau van de leerling vast te stellen.



&#x09;4.5 Diagnosemodule 

&#x09;Na het afronden van de instaptoets analyseert de diagnosemodule de antwoorden van de 	leerling. Voor ieder concept, zoals fotonen, interferentie, etc. wordt bepaald tot `	welke mate een leerling een concept beheerst. Ook worden er eventuele misconcepties 	of herhalende fouten geïdentificeerd. De uitkomsten van de diagnose vormen de basis 	voor het student model. 



&#x09;4.6 Domeinmodel 

&#x09;Het domeinmodel bevat de belangrijkste concepten uit paragraaf 15.1 en de relaties 	tussen deze concepten. 

&#x09;Licht

&#x09;│

&#x09;├── Foton

&#x09;├── Interferentie

&#x09;├── Buiging

&#x09;└── Golf-deeltjedualiteit

&#x09;

&#x09;Alle vragen, opdrachten en evaluaties worden gekoppeld aan een of meer concepten uit 	dit model. 



&#x09;4.7 Student model 

&#x09;Het student model bevat de kennis van de leerling die steeds opnieuw geüpdatet wordt. 	Voor ieder concepet uit het domeinmodel wordt er een score tussen 0 en 1 toegekend en 	daarna bijgehouden. Een score van 0 betekent dat er geen beheersing is, terwijl een 	score van 1 zegt dat er sprake is van een volledige beheersing. 



&#x09;Voorbeeld:



&#x09;{

&#x20;	 "foton": 0.9,

&#x20; 	"interferentie": 0.6,

&#x20; 	"buiging": 0.4,

&#x20; 	"golf\_deeltjedualiteit": 0.2

&#x09;}

&#x09;

&#x09;De scores worden na iedere opdracht bijgewerkt op basis van de antwoorden. 

&#x09;

&#x09;4.8 Tutor Agent 

&#x09;Dit is de centrale besluitvormer van het systeem. Op basis van het studentmodel 	bepaalt de tutoragent wat voor een leerling op het moment het beste is. Hij kiest 	daarbij tussen: 



&#x09;1. Het geven van een uitleg; 

&#x09;2. Een opdracht aanbieden; 

&#x09;3. Een hint geven; 

&#x09;4. Een socratische vraag stellen. 

&#x09;

&#x09;Het doel van de tutor agent is om de leerling zo efficiënt mogelijk te begeleiden, 	zodat zij de stof kunnen begrijpen. 



&#x09;4.9 RAG-systeem	

&#x09;Het theorieboek is de primaire kennisbron. Met behulp van RAG worden relevante 	tekstfragmenten of antwoorden uit het theorieboek opgehaald op het moment dat er een 	uitleg moet worden gegeven of dat er een vraag wordt gesteld door een leerling. De 	antwoorden zijn dan vergelijkbaar met de inhoud van het theorieboek. 



&#x09;4.10 Evaluatiemodule 

&#x09;De evaluatiemodule beoordeelt de antwoorden van een leerling bij opdrachten en 	oefenvragen. De resultaten worden dan gebruikt 	voor: 

&#x09;

&#x09;1. Het student model te actualiseren; 

&#x09;2. Misconcepties te identificeren; 

&#x09;3. De volgende activiteit (het stellen van een socratische vraag, uitleg geven) 	bepalen. 



&#x09;Hierdoor ontstaat er een continue feedbacklus waarbij de tutor zich voortdurend 	aanpast aan de voortgang van een leerling. 



&#x09;4.11 Adaptieve beslisregels

&#x09;De tutor gebruikt beheersingsscores uit het student model om nieuwe activiteiten te 	kiezen. 



&#x09;Score		Actie

&#x09;0.80 – 1.00	Moeilijkere opdracht

&#x09;0.60 – 0.79	Standaard opdracht

&#x09;0.40 – 0.59	Extra uitleg + opdracht

&#x09;0.00 – 0.39	Uitleg, hint en scaffolding



&#x09;Op het moment da teen leerling een concept voldoende heeft beheerst (score is 0,80 of 	hoger), dan wordt er een volgend concept binnen het domeinmodel geselecteerd. 



&#x09;4.12 Adaptieve leercyclus 

&#x09;Het systeem werkt volgens een cyclisch leerproces. 



&#x09;Instaptoets

&#x20;   	 	↓

&#x09;Diagnose

&#x20;     		↓

&#x09;Studentmodel

&#x20;     		↓

&#x09;Uitleg / Opdracht

&#x20;     		↓

&#x09;Evaluatie

&#x20;     		↓

&#x09;Studentmodel bijwerken

&#x20;     		↓

&#x09;Nieuwe leeractiviteit

&#x20;    		 ↺



&#x09;De cyclus wordt herhaald totdat de leerdoelen van 15.1 voldoende zijn beheerst. 



