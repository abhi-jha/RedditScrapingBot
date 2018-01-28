import subprocess
import httplib2
import requests
from datetime import datetime
FORMAT = '%d-%m-%Y %H:%M:%S'
my=open('log.txt','a',encoding='utf-8')
def test_internet():
   my.write('\nin test_internet'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   while(True):
      try:
         http = httplib2.Http()
         status, response = http.request("https://www.google.com")
         my.write('\nSUCCESS test_internet'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
         break
      except:
            continue
   my.close()
test_internet()
t=open("mytext.txt",'r')
i=t.read()
temp=int(i)
temp=temp+1
t.close()
t=open("mytext.txt",'w')
t.write(str(temp))
t.close()

#trial
#subprocess.call(["python","worldnews_fast.py",str(i),'AskAnthropology','AskComputerScience','AskElectronics','AskEngineers','AskHR','AskHistorians','AskMen','AskPhysics','AskReddit','AskScienceDiscussion'],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),'24hoursupport','3amjokes','ADHD','AMA','AcademicPhilosophy','AcademicPsychology','Aerospace','Android','AndroidQuestions','Anger','Anxiety'],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),'ProgrammerHumor','Proofreading','Python','RapeCounseling','RetailManagement','STEMdents','SWORDS','SWResources','SampleSize','SanctionedSuicide','Seduction'],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),],shell=True)

#30 each whole list
subprocess.call(["python","worldnews_fast.py",str(i),"24hoursupport","3amjokes","ADHD","AMA","AcademicPhilosophy","AcademicPsychology","Aerospace","Android","AndroidQuestions","Anger","Anxiety","AskAnthropology","AskComputerScience","AskElectronics","AskEngineers","AskHR","AskHistorians","AskMen","AskPhysics","AskReddit","AskScienceDiscussion","AskScienceFiction","AskSocialScience","AskWomen","Ask_Politics","Bash","BehavioralEconomics","BigDataJobs","BipolarReddit","CAD","C_Programming"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"ComputerScience","Confession","CoverTheWorld","Cplusplus","CppForbeginners","CrappyDesign","CrazyIdeas","DIY","DIYCompSci","DailyProgrammer","DeadBedrooms","DebateReligion","DecidingToBeBetter","DigitalNomad","DoesNotTranslate","ECE","Economics","EngineeringStudents","Entrepreneur","ExNoContact","FEA","FE_Exam","Feminism","FluidMechanics","Foodforthought","FoundWords","Freethought","GetMotivated","GetStudying","GraphicsProgramming","HITsWorthTurkingFor","HTMLBattles"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"HomeworkHelp","HowsYourJob","IAmA","IOPsychology","InternetIsBeautiful","LaTeX","LanguageLearning","LearnANewLanguage","LearnJava","LearnJavaScript","LifeProTips","LinguisticsHumor","LongDistance","MachineLearning","Manufacturing","MathHelp","Meditation","NetworkingJobs","Neuropsychology","NoStupidQuestions","ObjectiveC","PCMasterRace","PLC","PhilosophyofScience","PhsychologicalTricks","PoliticalDiscussion","Polyamory","PrintedCircuitBoard","Progether","ProgrammerHumor","Proofreading","Python"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"RapeCounseling","RetailManagement","STEMdents","SWORDS","SWResources","SampleSize","SanctionedSuicide","Seduction","SiblingSupport","Statistics","SuicideWatch","Swift","SysadminJobs","TechNews","ThermalPerformance","Tinder","TinyCode","TowerOfBabel","TrueAskReddit","TrueReddit","Unix","VentureBiotech","WeMetOnline","Web_Development","WhatsTheWord","YoungJobs","academicpsychology","academicpublishing","accounting","advice","androiddev","translator"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"answers","asklinguistics","askmath","askphotography","askreddit","askscience","assistance","astronomy","audiology","autism","badcode","badlinguistics","beermoney","behavioralmedicine","behaviortherapy","bestof","bestofTLDR","bioengineering","biology","biotech","bodybuilding","bookquotes","books","breadboard","bugs","buildapc","business","careerguidance","cfd","changemyview","chemicalengineering","chipdesign"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"civilengineering","cloudcomputing","coding","coffeescript","cogneuro","cogneurocogsci","cognitivelinguistics","cogsci","compilers","complexsystems","compling","compression","compsci","computerforensics","computers","computerscience","conlangs","conspiracy","construction","cosmology","coursearea","cpp","cpp_questions","crypto","cryptography","cs50","csbooks","cscareerquestions","csharp","css","dae","dailyprogrammer"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"dailyscripts","darkinternet","dataisbeautiful","datamining","dementia","depression","diy","documentaries","dotnet","downsyndrome","dyslexia","economics","education","eebooks","electricalengineering","electronics","engineering","engineeringtechnology","entrepreneur","epidemiology","etymology","eurodiversity","everythingscience","evolution","evopsych","explainlikeimfive","favors","finance","financialindependence","findareddit","forhire","forth"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"freelance","freelanceUK","freelanceWriters","funny","gadgets","genetics","getdisciplined","getemployed","getmotivated","getting_over_it","goldredditsays","grammar","grammarwriting","graphic_design","hacking","hardware","history","holdmybeer","homeworkhelp","html","htmlbasics","humanism","hwstartups","hypotheticalsituation","iWantToLearn","ideasfortheadmins","illegaltorrents","improvevocab","india","ineedafavor","intel","intelligence"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"interview","inventions","iwantoutjobs","java","javaTIL","javacodegeeks","javahelp","javascript","jobbit","jobsearchhacks","jokes","jquery","languagetechnology","learnjava","learnjavascript","learnmath","learnprogramming","learnpython","lectures","lifehacks","linguistics","linux","linux4noobs","linuxquestions","literature","logic","machinelearning","marketing","masculism","math","mathbooks","mathematics"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"mathpsych","matlab","mechanicalengineering","medicine","meditation","mentalhealth","mentors","metalworking","microsoft","mmfb","motivation","movies","music","mysql","needadvice","networking","neuro","neurodiversity","neurophilosophy","neuropsychology","newproducts","news","newtoreddit","nonprofit_jobs","nootropics","obvious","occupationaltherapy","ocd","offmychest","opengl","osdev","parkrangers"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"perl","philosophy","philosophyofScience","philosophyofscience","php","physics","pics","politics","privacy","product_design","productivity","programbattles","programming","programmingbuddies","programmingchallenges","psychiatry","psychology","psychopharmacology","psychotherapy","psychscience","puzzles","python","quotes","rage","rational","reasonstolive","rehabtherapy","relationship_advice","relationships","resumes","riddles","robotics"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"ruby","saneorpsycho","schizophrenia","science","scientificresearch","self","selfhelp","selfimprovement","sex","shittyaskscience","shittyideas","shittyprogramming","showerthoughts","simpleliving","slp","socialism","socialmedia","socialskills","sociology","software","softwarearchitecture","softwaredevelopment","softwaregore","solotravel","space","specialed","startups","stopselfharm","suicidology","sysadmin","systems","talesfromtechsupport"],shell=True)
subprocess.call(["python","worldnews_fast.py",str(i),"technology","techsupport","teenagers","testimonials","themixednuts","thisismyjob","tipofmytongue","todayilearned","tr","translationstudies","travel","tutor","ultralight","undelete","undeleteShadow","undergraduateresearch","uniqueminds","visualbasic","web_programming","webdev","whatisthis","whatstheword","windows","windowsazure","womenEngineers","words","work","workonline","worldnews","writingprompts"],shell=True)

#20 each whole list
#subprocess.call(["python","worldnews_fast.py",str(i),"24hoursupport","3amjokes","ADHD","AMA","AcademicPhilosophy","AcademicPsychology","Aerospace","Android","AndroidQuestions","Anger","Anxiety","AskAnthropology","AskComputerScience","AskElectronics","AskEngineers","AskHR","AskHistorians","AskMen","AskPhysics","AskReddit","AskScienceDiscussion"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskScienceFiction","AskSocialScience","AskWomen","Ask_Politics","Bash","BehavioralEconomics","BigDataJobs","BipolarReddit","CAD","C_Programming","ComputerScience","Confession","CoverTheWorld","Cplusplus","CppForbeginners","CrappyDesign","CrazyIdeas","DIY","DIYCompSci","DailyProgrammer","DeadBedrooms","DebateReligion"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"DecidingToBeBetter","DigitalNomad","DoesNotTranslate","ECE","Economics","EngineeringStudents","Entrepreneur","ExNoContact","FEA","FE_Exam","Feminism","FluidMechanics","Foodforthought","FoundWords","Freethought","GetMotivated","GetStudying","GraphicsProgramming","HITsWorthTurkingFor","HTMLBattles","HomeworkHelp","HowsYourJob"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"IAmA","IOPsychology","InternetIsBeautiful","LaTeX","LanguageLearning","LearnANewLanguage","LearnJava","LearnJavaScript","LifeProTips","LinguisticsHumor","LongDistance","MachineLearning","Manufacturing","MathHelp","Meditation","NetworkingJobs","Neuropsychology","NoStupidQuestions","ObjectiveC","PCMasterRace","PLC","PhilosophyofScience"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"PhsychologicalTricks","PoliticalDiscussion","Polyamory","PrintedCircuitBoard","Progether","ProgrammerHumor","Proofreading","Python","RapeCounseling","RetailManagement","STEMdents","SWORDS","SWResources","SampleSize","SanctionedSuicide","Seduction","SiblingSupport","Statistics","SuicideWatch","Swift","SysadminJobs","TechNews"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ThermalPerformance","Tinder","TinyCode","TowerOfBabel","TrueAskReddit","TrueReddit","Unix","VentureBiotech","WeMetOnline","Web_Development","WhatsTheWord","YoungJobs","academicpsychology","academicpublishing","accounting","advice","androiddev","translator","answers","asklinguistics","askmath","askphotography"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"askreddit","askscience","assistance","astronomy","audiology","autism","badcode","badlinguistics","beermoney","behavioralmedicine","behaviortherapy","bestof","bestofTLDR","bioengineering","biology","biotech","bodybuilding","bookquotes","books","breadboard","bugs","buildapc"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"business","careerguidance","cfd","changemyview","chemicalengineering","chipdesign","civilengineering","cloudcomputing","coding","coffeescript","cogneuro","cogneurocogsci","cognitivelinguistics","cogsci","compilers","complexsystems","compling","compression","compsci","computerforensics","computers","computerscience"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"conlangs","conspiracy","construction","cosmology","coursearea","cpp","cpp_questions","crypto","cryptography","cs50","csbooks","cscareerquestions","csharp","css","dae","dailyprogrammer","dailyscripts","darkinternet","dataisbeautiful","datamining","dementia","depression"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"diy","documentaries","dotnet","downsyndrome","dyslexia","economics","education","eebooks","electricalengineering","electronics","engineering","engineeringtechnology","entrepreneur","epidemiology","etymology","eurodiversity","everythingscience","evolution","evopsych","explainlikeimfive","favors","finance"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"financialindependence","findareddit","forhire","forth","freelance","freelanceUK","freelanceWriters","funny","gadgets","genetics","getdisciplined","getemployed","getmotivated","getting_over_it","goldredditsays","grammar","grammarwriting","graphic_design","hacking","hardware","history","holdmybeer"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"homeworkhelp","html","htmlbasics","humanism","hwstartups","hypotheticalsituation","iWantToLearn","ideasfortheadmins","illegaltorrents","improvevocab","india","ineedafavor","intel","intelligence","interview","inventions","iwantoutjobs","java","javaTIL","javacodegeeks","javahelp","javascript"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"jobbit","jobsearchhacks","jokes","jquery","languagetechnology","learnjava","learnjavascript","learnmath","learnprogramming","learnpython","lectures","lifehacks","linguistics","linux","linux4noobs","linuxquestions","literature","logic","machinelearning","marketing","masculism","math"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"mathbooks","mathematics","mathpsych","matlab","mechanicalengineering","medicine","meditation","mentalhealth","mentors","metalworking","microsoft","mmfb","motivation","movies","music","mysql","needadvice","networking","neuro","neurodiversity","neurophilosophy","neuropsychology"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"newproducts","news","newtoreddit","nonprofit_jobs","nootropics","obvious","occupationaltherapy","ocd","offmychest","opengl","osdev","parkrangers","perl","philosophy","philosophyofScience","philosophyofscience","php","physics","pics","politics","privacy","product_design"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"productivity","programbattles","programming","programmingbuddies","programmingchallenges","psychiatry","psychology","psychopharmacology","psychotherapy","psychscience","puzzles","python","quotes","rage","rational","reasonstolive","rehabtherapy","relationship_advice","relationships","resumes","riddles","robotics"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ruby","saneorpsycho","schizophrenia","science","scientificresearch","self","selfhelp","selfimprovement","sex","shittyaskscience","shittyideas","shittyprogramming","showerthoughts","simpleliving","slp","socialism","socialmedia","socialskills","sociology","software","softwarearchitecture","softwaredevelopment"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"softwaregore","solotravel","space","specialed","startups","stopselfharm","suicidology","sysadmin","systems","talesfromtechsupport","technology","techsupport","teenagers","testimonials","themixednuts","thisismyjob","tipofmytongue","todayilearned","tr","translationstudies","travel","tutor"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ultralight","undelete","undeleteShadow","undergraduateresearch","uniqueminds","visualbasic","web_programming","webdev","whatisthis","whatstheword","windows","windowsazure","womenEngineers","words","work","workonline","worldnews","writingprompts"],shell=True)


#10 each whole list
#subprocess.call(["python","worldnews_fast.py",str(i),"24hoursupport","3amjokes","ADHD","AMA","AcademicPhilosophy","AcademicPsychology","Aerospace","Android","AndroidQuestions","Anger","Anxiety"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskAnthropology","AskComputerScience","AskElectronics","AskEngineers","AskHR","AskHistorians","AskMen","AskPhysics","AskReddit","AskScienceDiscussion","AskScienceFiction","AskSocialScience"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskWomen","Ask_Politics","Bash","BehavioralEconomics","BigDataJobs","BipolarReddit","CAD","C_Programming","ComputerScience","Confession","CoverTheWorld","Cplusplus"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"CppForbeginners","CrappyDesign","CrazyIdeas","DIY","DIYCompSci","DailyProgrammer","DeadBedrooms","DebateReligion","DecidingToBeBetter","DigitalNomad","DoesNotTranslate","ECE"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"Economics","EngineeringStudents","Entrepreneur","ExNoContact","FEA","FE_Exam","Feminism","FluidMechanics","Foodforthought","FoundWords","Freethought","GetMotivated"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"GetStudying","GraphicsProgramming","HITsWorthTurkingFor","HTMLBattles","HomeworkHelp","HowsYourJob","IAmA","IOPsychology","InternetIsBeautiful","LaTeX","LanguageLearning","LearnANewLanguage"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"LearnJava","LearnJavaScript","LifeProTips","LinguisticsHumor","LongDistance","MachineLearning","Manufacturing","MathHelp","Meditation","NetworkingJobs","Neuropsychology","NoStupidQuestions"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ObjectiveC","PCMasterRace","PLC","PhilosophyofScience","PhsychologicalTricks","PoliticalDiscussion","Polyamory","PrintedCircuitBoard","Progether","ProgrammerHumor","Proofreading","Python"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"RapeCounseling","RetailManagement","STEMdents","SWORDS","SWResources","SampleSize","SanctionedSuicide","Seduction","SiblingSupport","Statistics","SuicideWatch","Swift"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"SysadminJobs","TechNews","ThermalPerformance","Tinder","TinyCode","TowerOfBabel","TrueAskReddit","TrueReddit","Unix","VentureBiotech","WeMetOnline","Web_Development"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"WhatsTheWord","YoungJobs","academicpsychology","academicpublishing","accounting","advice","androiddev","translator","answers","asklinguistics","askmath","askphotography"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"askreddit","askscience","assistance","astronomy","audiology","autism","badcode","badlinguistics","beermoney","behavioralmedicine","behaviortherapy","bestof"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"bestofTLDR","bioengineering","biology","biotech","bodybuilding","bookquotes","books","breadboard","bugs","buildapc","business","careerguidance"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"cfd","changemyview","chemicalengineering","chipdesign","civilengineering","cloudcomputing","coding","coffeescript","cogneuro","cogneurocogsci","cognitivelinguistics","cogsci"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"compilers","complexsystems","compling","compression","compsci","computerforensics","computers","computerscience","conlangs","conspiracy","construction","cosmology"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"coursearea","cpp","cpp_questions","crypto","cryptography","cs50","csbooks","cscareerquestions","csharp","css","dae","dailyprogrammer"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"dailyscripts","darkinternet","dataisbeautiful","datamining","dementia","depression","diy","documentaries","dotnet","downsyndrome","dyslexia","economics"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"education","eebooks","electricalengineering","electronics","engineering","engineeringtechnology","entrepreneur","epidemiology","etymology","eurodiversity","everythingscience","evolution"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"evopsych","explainlikeimfive","favors","finance","financialindependence","findareddit","forhire","forth","freelance","freelanceUK","freelanceWriters","funny"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"gadgets","genetics","getdisciplined","getemployed","getmotivated","getting_over_it","goldredditsays","grammar","grammarwriting","graphic_design","hacking","hardware"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"history","holdmybeer","homeworkhelp","html","htmlbasics","humanism","hwstartups","hypotheticalsituation","iWantToLearn","ideasfortheadmins","illegaltorrents","improvevocab"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"india","ineedafavor","intel","intelligence","interview","inventions","iwantoutjobs","java","javaTIL","javacodegeeks","javahelp","javascript"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"jobbit","jobsearchhacks","jokes","jquery","languagetechnology","learnjava","learnjavascript","learnmath","learnprogramming","learnpython","lectures","lifehacks"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"linguistics","linux","linux4noobs","linuxquestions","literature","logic","machinelearning","marketing","masculism","math","mathbooks","mathematics"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"mathpsych","matlab","mechanicalengineering","medicine","meditation","mentalhealth","mentors","metalworking","microsoft","mmfb","motivation","movies"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"music","mysql","needadvice","networking","neuro","neurodiversity","neurophilosophy","neuropsychology","newproducts","news","newtoreddit","nonprofit_jobs"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"nootropics","obvious","occupationaltherapy","ocd","offmychest","opengl","osdev","parkrangers","perl","philosophy","philosophyofScience","philosophyofscience"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"php","physics","pics","politics","privacy","product_design","productivity","programbattles","programming","programmingbuddies","programmingchallenges","psychiatry"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"psychology","psychopharmacology","psychotherapy","psychscience","puzzles","python","quotes","rage","rational","reasonstolive","rehabtherapy","relationship_advice"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"relationships","resumes","riddles","robotics","ruby","saneorpsycho","schizophrenia","science","scientificresearch","self","selfhelp","selfimprovement"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"sex","shittyaskscience","shittyideas","shittyprogramming","showerthoughts","simpleliving","slp","socialism","socialmedia","socialskills","sociology","software"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"softwarearchitecture","softwaredevelopment","softwaregore","solotravel","space","specialed","startups","stopselfharm","suicidology","sysadmin","systems","talesfromtechsupport"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"technology","techsupport","teenagers","testimonials","themixednuts","thisismyjob","tipofmytongue","todayilearned","tr","translationstudies","travel","tutor"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ultralight","undelete","undeleteShadow","undergraduateresearch","uniqueminds","visualbasic","web_programming","webdev","whatisthis","whatstheword","windows","windowsazure"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"womenEngineers","words","work","workonline","worldnews","writingprompts"],shell=True)

#10 each, short list
#subprocess.call(["python","worldnews_fast.py",str(i),"advice","academicpsychology","academicpublishing","accounting","Web_Development","WhatsTheWord","TrueReddit","Unix","TinyCode","TechNews","STEMdents"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"ProgrammerHumor","Proofreading","Python","PhilosophyofScience","PhsychologicalTricks","PoliticalDiscussion","Neuropsychology","NoStupidQuestions","MathHelp","Meditation","LifeProTips","LinguisticsHumor"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"HomeworkHelp","HowsYourJob","Foodforthought","FoundWords","Freethought","GetMotivated","GetStudying","ECE","Economics","EngineeringStudents","CrazyIdeas","DIY"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"DIYCompSci","DailyProgrammer","Cplusplus","CppForbeginners","ComputerScience","Confession","AskSocialScience","AskWomen","Ask_Politics","Bash","BehavioralEconomics","AskPhysics"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskReddit","AskScienceDiscussion","AskHistorians","AskAnthropology","AskComputerScience","AskElectronics","AskEngineers","AcademicPhilosophy","AcademicPsychology","AskComputerScience","AskElectronics","AskEngineers"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskHistorians","TrueAskReddit","IOPsychology","InternetIsBeautiful","LearnJava","LearnJavaScript","AskPhysics","AskReddit","C_Programming","Cplusplus","CppForbeginners","HomeworkHelp"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"MathHelp","Python","answers","asklinguistics","askmath","askscience","changemyview","coding","compsci","cpp","cpp_questions","india"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"java","javacodegeeks","javahelp","learnjava","learnmath","learnprogramming","learnpython","math","news","philosophy","physics","programming"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"science","worldnews"],shell=True)

#20,regular,short list
#subprocess.call(["python","worldnews_fast.py",str(i),"advice","academicpsychology","academicpublishing","accounting","Web_Development","WhatsTheWord","TrueReddit","Unix","TinyCode","TechNews","STEMdents","ProgrammerHumor","Proofreading","Python","PhilosophyofScience","PhsychologicalTricks","PoliticalDiscussion","Neuropsychology","NoStupidQuestions","MathHelp","Meditation"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"LifeProTips","LinguisticsHumor","HomeworkHelp","HowsYourJob","Foodforthought","FoundWords","Freethought","GetMotivated","GetStudying","ECE","Economics","EngineeringStudents","CrazyIdeas","DIY","DIYCompSci","DailyProgrammer","Cplusplus","CppForbeginners","ComputerScience","Confession","AskSocialScience","AskWomen"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"Ask_Politics","Bash","BehavioralEconomics","AskPhysics","AskReddit","AskScienceDiscussion","AskHistorians","AskAnthropology","AskComputerScience","AskElectronics","AskEngineers","AcademicPhilosophy","AcademicPsychology","AskComputerScience","AskElectronics","AskEngineers","AskHistorians","TrueAskReddit","IOPsychology","InternetIsBeautiful","LearnJava","LearnJavaScript"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"AskPhysics","AskReddit","C_Programming","Cplusplus","CppForbeginners","HomeworkHelp","MathHelp","Python","answers","asklinguistics","askmath","askscience","changemyview","coding","compsci","cpp","cpp_questions","india","java","javacodegeeks","javahelp","learnjava"],shell=True)
#subprocess.call(["python","worldnews_fast.py",str(i),"learnmath","learnprogramming","learnpython","math","news","philosophy","physics","programming","science","worldnews"],shell=True)



#b=[1,2,3]
#args = ["python","worldnews_fast.py", b]
#str_args = [ str(x) for x in args ]
#print(str_args[2])
#for x in str_args[2]:
#    print(x)
