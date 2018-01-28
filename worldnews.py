import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import os
import httplib2
from multiprocessing import Pool
c=0
import requests
from datetime import datetime
import multiprocessing
from multiprocessing import current_process
import time
import os
import sys
FORMAT = '%d-%m-%Y %H:%M:%S'
my=open('log.txt','a',encoding='utf-8')
def make_soup2(url):
  match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
  my.write('\nnot stuck1'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
  if re.search(match,url):
   while(True):
    try:
     r = requests.get(url, timeout=5) #number of seconds to wait for response before throwing exception
     break
    except:
      print("timed out")
      continue
   page =BeautifulSoup(r.text, parse_only=SoupStrainer('div'))
   return page
  else:
      return None
def make_soup1(url):
    match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
    my.write('\nnot stuck1'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
    if re.search(match,url):
     while(True):
      try:
       try:
        r = requests.get(url, timeout=5) #number of seconds to wait for response before throwing exception
        my.write('\nnot stuck2'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
        page =BeautifulSoup(r.text, parse_only=SoupStrainer('div'))
        my.write('\nnot stuck3'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
        break
       except requests.exceptions.Timeout: 
        print("timed out")
      except:
         continue
     return page
    else:
      return None
def make_soup(s):
   match=re.compile('https://|http://|www.|.com|.in|.org|gov.in')
   #my.write(s)
   if re.search(match,s):
    while(True):
     try:
      http = httplib2.Http()
      #my.write('\nnot stuck1'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
      break
     except:
         #print('stuck1')
         continue
    while(True):
     try:
      status, response = http.request(s)
      #my.write('\nnot stuck2'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
      break
     except:
         #print('stuck2')
         continue
    while(True):
     try:
      page = BeautifulSoup(response,"html.parser",parse_only=SoupStrainer('div'))
      #my.write('\nnot stuck3'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
      break
     except:
         #print('stuck3')
         continue
    return page
   else:
     return None
def test_internet():
   #my.write('\nin test_internet'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   while(True):
      try:
         http = httplib2.Http()
         status, response = http.request("https://www.google.com")
         #my.write('\nSUCCESS test_internet'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
         break
      except:
            continue
def parse1(s):
   #my.write('\nin parse'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   global c
   temp_set=set()
   soup=make_soup(s)
   if(soup!=None):
      for div in soup.find_all('div',class_=[ "thing" , "id-t3_3ua12m" ,"linkflair" , "linkflair-normal" , "odd" ,  "link"]):
       try:
         if(div.p!=None and div.p.next_sibling!=None and div.p.next_sibling.next_sibling!=None):
          x=div.p.next_sibling.next_sibling.next_sibling['class']
          #print(x)
          if(x[0]=='entry'):
            element='\nPROMPT '+str(c+1)+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling!=None and div.p.next_sibling.next_sibling.next_sibling.p!=None and div.p.next_sibling.next_sibling.next_sibling.p.a!=None):
               element=element+div.p.next_sibling.next_sibling.next_sibling.p.a.string+'\n'
               element=element+div.p.next_sibling.next_sibling.next_sibling.p.a['href']+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'})!=None and div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time!=None):
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time['datetime']+'\t'
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time['title']+'\t'
                  element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).time.string+'\n'
            if(div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'})!=None and div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).a!=None):
               element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).a.string+'\n'
               element=element+div.p.next_sibling.next_sibling.next_sibling.find('p',{'class':'tagline'}).text+'\n'
            if(div.div.find('div',{'class':'score likes'})!=None):
               element=element+'score likes '+div.div.find('div',{'class':'score likes'}).string+'\t'
               element=element+'score dislikes '+div.div.find('div',{'class':'score dislikes'}).string+'\t'
               element=element+'score unvoted '+div.div.find('div',{'class':'score unvoted'}).string+'\n\n'
            f.write(element)
            c=c+1
          elif(x[0]=='thumbnail'):
            element='\nPROMPT '+str(c+1)+'\n'
            if(div.find('div',{'class':'entry unvoted'})!=None and div.find('div',{'class':'entry unvoted'}).p!=None and div.find('div',{'class':'entry unvoted'}).p.a!=None and div.find('div',{'class':'entry unvoted'}).p.a.string!=None):
               element=element+div.find('div',{'class':'entry unvoted'}).p.a.string+'\n'
               element=element+div.find('div',{'class':'entry unvoted'}).p.a['href']+'\n'
               if(div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'})!=None and div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time != None):
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time['datetime']+'\t'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time['title']+'\t'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).time.string+'\n'
               if(div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).a!=None):
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).a.string+'\n'
                  element=element+div.find('div',{'class':'entry unvoted'}).find('p',{'class':'tagline'}).text+'\n'
               if(div.p.next_sibling.next_sibling.find('div',{'class':'score likes'})!=None and div.p.next_sibling.next_sibling.find('div',{'class':'score dislikes'})!=None and div.p.next_sibling.next_sibling.find('div',{'class':'score unvoted'})!=None):
                  element=element+'score likes '+div.p.next_sibling.next_sibling.find('div',{'class':'score likes'}).string+'\t\t'
                  element=element+'score dislikes '+div.p.next_sibling.next_sibling.find('div',{'class':'score dislikes'}).string+'\t\t'
                  element=element+'score unvoted '+div.p.next_sibling.next_sibling.find('div',{'class':'score unvoted'}).string+'\n'
            #my.write('\nSUCCESS PARSE 1'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
            f.write(element)
            c=c+1
       except:
            my.write('ERROR'+datetime.now().strftime(FORMAT)+'\n')
            continue

    
def count_next_of_current(s,m):
    #my.write('\nin count_next_of current'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
    soup=make_soup(s)
    y='https://www.reddit.com/r/'+m+'/'+select_tab+'/?count='
    match=re.compile(y)
    for link in soup.find_all('a',{'rel':['next']}):
        href=link['href']
        #my.write('\nSUCCESS count_next_of current'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
        return href

def read_reddit_images(change_file_number,m,x):
    #my.write('\nin read_reddit_images'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
    global f
    global select_tab
    select_tab=x
    x=m+'_'+select_tab+'.txt'
    #test_internet()
    s='https://www.reddit.com/r/'+m+'/'+select_tab
    soup=make_soup(s)
    f=open(x,'a',encoding='utf-8')
    f.write('\n\n\n\niteration number '+str(change_file_number)+' '+datetime.now().strftime(FORMAT)+'\n\n')
    maximum_number_of_next_pages=5
    parse1(s)
    count=0
    print('for '+m+' '+select_tab+' current page number is'+'\n'+str(count))
    while(count<maximum_number_of_next_pages):
        #test_internet()
        s=count_next_of_current(s,m)
        if(s!=None):
            parse1(s)
            count=count+1
            print(count)
        else:
            break
    f.write('\n\niteration number '+str(change_file_number)+' '+datetime.now().strftime(FORMAT)+'\n\n')
    f.close()
    #my.write('\nSUCCESS read_reddit_images'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')

def main(m,i):
   #my.write('\nin maincall'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   my.write('\n'+str(type(m))+' '+m+' '+str(type(i))+' '+str(i)+'\n')
   read_reddit_images(i,m,'new')
   read_reddit_images(i,m,'hot')
   read_reddit_images(i,m,'top')
   #read_reddit_images(i,m,'rising')
   #read_reddit_images(i,m,'controversial')
   #read_reddit_images(i,m,'gilded')
   my.write('\n'+str(type(m))+' '+m+' '+str(type(i))+' '+str(i)+'   SUCCESS SUCCESS SUCCESS\n')
   #my.write('\nSUCCESS maincall'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
def subs(b):
   my.write('\nin subs'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   test_internet()
   t=open("mytext.txt",'r')
   i=t.read()
   temp=int(i)
   temp=temp+1
   t.close()
   t=open("mytext.txt",'w')
   t.write(str(temp))
   t.close()
   for k in b:
        maincall(k,i)
   my.write('\nSUCCESS subs'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
def list_subreddits():
   my.write('\nin list_subreddits'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n')
   test_internet()
   b=[]
   b=b+['buildapc','offmychest','datamining','DebateReligion','DecidingToBeBetter','depression','ECE','Economics','eebooks','electronics','Feminism','findareddit']
   b=b+['PoliticalDiscussion','books','shittyaskscience','AskScienceFiction','linux','ProgrammerHumor','holdmybeer','socialism','InternetIsBeautiful','changemyview']
   b=b+['AskScienceDiscussion','AskSocialScience','askphotography','badcode','bestofTLDR','biology','bookquotes','bugs','C_Programming','chipdesign','coding']
   b=b+['compilers','complexsystems','compression','computerforensics','computers','computerscience','cosmology','coursearea','Cplusplus','cpp','CppForbeginners']
   b=b+['CrappyDesign','CrazyIdeas','crypto','cryptography','cs50','csbooks','cscareerquestions','dailyprogrammer','dailyscripts','darkinternet','dataisbeautiful']
   b=b+['relationships','showerthoughts','explainlikeimfive','technology','science','music','india','conspiracy','talesfromtechsupport','sex','AskWomen']
   b=b+['24hoursupport','3amjokes','AcademicPhilosophy','AcademicPsychology','AMA','AndroidQuestions','Android','androiddev','Anger','answers','Anxiety']
   b=b+['Ask_Politics','AskAnthropology','AskComputerScience','AskElectronics','AskEngineers','AskHistorians','asklinguistics','askmath','AskMen','AskPhysics']
   b=b+['askscience','writingprompts','DIY','LifeProTips','bodybuilding','GetMotivated','TrueReddit','teenagers','AskHistorians','programming','NoStupidQuestions']
   b=b+['Foodforthought','illegaltorrents','improvevocab','intel','intelligence','interview','iWantToLearn','java','javacodegeeks','javahelp','javascript','javaTIL']
   b=b+['Freethought','getdisciplined','GetStudying','goldredditsays','grammar','GraphicsProgramming','hacking','HomeworkHelp','humanism','ideasfortheadmins']
   b=b+['learnjava','learnmath','learnjavascript','linux','linux4noobs','linuxquestions','literature','logic','MachineLearning','math','mathbooks','MathHelp']
   b=b+['meditation','mysql','networking','Neuropsychology','obvious','opengl','osdev','perl','philosophy','philosophyofScience','privacy','productivity']
   b=b+['programmingchallenges','PhsychologicalTricks','puzzles','Python','quotes','rage','rational','riddles','selfimprovement','shittyideas','shittyprogramming']
   b=b+['socialskills','software','softwarearchitecture','softwaredevelopment','softwaregore','sysadmin','systems','talesfromtechsupport','techsupport','bestof']
   b=b+['worldnews','lifehacks','AskHistorians','programming','politics','compsci','javahelp','learnprogramming','cpp_questions','physics','writingprompts']
   b=b+['getmotivated','news','gadgets','InternetIsBeautiful','india','science','IAmA','askscience','jokes','explainlikeimfive','technology','showerthoughts']
   b=b+['movies','documentaries','dataisbeautiful','history','AskReddit','funny','todayilearned','pics','books','space','philosophy','learnpython','askscience']
   b=b+['TrueAskReddit','Web_Development','webdev','worldnews','news','askreddit','learnprogramming','compsci']#major list, Once a week
   b=[]
   b=['24hoursupport','3amjokes','ADHD','AMA','AcademicPhilosophy','AcademicPsychology','Aerospace','Android','AndroidQuestions','Anger','Anxiety',
      'AskAnthropology','AskComputerScience','AskElectronics','AskEngineers','AskHR','AskHistorians','AskMen','AskPhysics','AskReddit','AskScienceDiscussion',
      'AskScienceFiction','AskSocialScience','AskWomen','Ask_Politics','Bash','BehavioralEconomics','BigDataJobs','BipolarReddit','CAD','C_Programming',
      'ComputerScience','Confession','CoverTheWorld','Cplusplus','CppForbeginners','CrappyDesign','CrazyIdeas','DIY','DIYCompSci','DailyProgrammer','DeadBedrooms',
      'DebateReligion','DecidingToBeBetter','DigitalNomad','DoesNotTranslate','ECE','Economics','EngineeringStudents','Entrepreneur','ExNoContact','FEA','FE_Exam',
      'Feminism','FluidMechanics','Foodforthought','FoundWords','Freethought','GetMotivated','GetStudying','GraphicsProgramming','HITsWorthTurkingFor','HTMLBattles',
      'HomeworkHelp','HowsYourJob','IAmA','IOPsychology','InternetIsBeautiful','LaTeX','LanguageLearning','LearnANewLanguage','LearnJava','LearnJavaScript',
      'LifeProTips','LinguisticsHumor','LongDistance','MachineLearning','Manufacturing','MathHelp','Meditation','NetworkingJobs','Neuropsychology','NoStupidQuestions',
      'ObjectiveC','PCMasterRace','PLC','PhilosophyofScience','PhsychologicalTricks','PoliticalDiscussion','Polyamory','PrintedCircuitBoard','Progether',
      'ProgrammerHumor','Proofreading','Python','RapeCounseling','RetailManagement','STEMdents','SWORDS','SWResources','SampleSize','SanctionedSuicide','Seduction',
      'SiblingSupport','Statistics','SuicideWatch','Swift','SysadminJobs','TechNews','ThermalPerformance','Tinder','TinyCode','TowerOfBabel','TrueAskReddit',
      'TrueReddit','Unix','VentureBiotech','WeMetOnline','Web_Development','WhatsTheWord','YoungJobs','academicpsychology','academicpublishing','accounting','advice',
      'androiddev','translator','answers','asklinguistics','askmath','askphotography','askreddit','askscience','assistance','astronomy','audiology','autism','badcode',
      'badlinguistics','beermoney','behavioralmedicine','behaviortherapy','bestof','bestofTLDR','bioengineering','biology','biotech','bodybuilding','bookquotes',
      'books','breadboard','bugs','buildapc','business','careerguidance','cfd','changemyview','chemicalengineering','chipdesign','civilengineering','cloudcomputing',
      'coding','coffeescript','cogneuro','cogneurocogsci','cognitivelinguistics','cogsci','compilers','complexsystems','compling','compression','compsci',
      'computerforensics','computers','computerscience','conlangs','conspiracy','construction','cosmology','coursearea','cpp','cpp_questions','crypto','cryptography',
      'cs50','csbooks','cscareerquestions','csharp','css','dae','dailyprogrammer','dailyscripts','darkinternet','dataisbeautiful','datamining','dementia','depression',
      'diy','documentaries','dotnet','downsyndrome','dyslexia','economics','education','eebooks','electricalengineering','electronics','engineering',
      'engineeringtechnology','entrepreneur','epidemiology','etymology','eurodiversity','everythingscience','evolution','evopsych','explainlikeimfive','favors',
      'finance','financialindependence','findareddit','forhire','forth','freelance','freelanceUK','freelanceWriters','funny','gadgets','genetics','getdisciplined',
      'getemployed','getmotivated','getting_over_it','goldredditsays','grammar','grammarwriting','graphic_design','hacking','hardware','history','holdmybeer',
      'homeworkhelp','html','htmlbasics','humanism','hwstartups','hypotheticalsituation','iWantToLearn','ideasfortheadmins','illegaltorrents','improvevocab','india',
      'ineedafavor','intel','intelligence','interview','inventions','iwantoutjobs','java','javaTIL','javacodegeeks','javahelp','javascript','jobbit','jobsearchhacks',
      'jokes','jquery','languagetechnology','learnjava','learnjavascript','learnmath','learnprogramming','learnpython','lectures','lifehacks','linguistics','linux',
      'linux4noobs','linuxquestions','literature','logic','machinelearning','marketing','masculism','math','mathbooks','mathematics','mathpsych','matlab',
      'mechanicalengineering','medicine','meditation','mentalhealth','mentors','metalworking','microsoft','mmfb','motivation','movies','music','mysql','needadvice',
      'networking','neuro','neurodiversity','neurophilosophy','neuropsychology','newproducts','news','newtoreddit','nonprofit_jobs','nootropics','obvious',
      'occupationaltherapy','ocd','offmychest','opengl','osdev','parkrangers','perl','philosophy','philosophyofScience','philosophyofscience','php','physics','pics',
      'politics','privacy','product_design','productivity','programbattles','programming','programmingbuddies','programmingchallenges','psychiatry','psychology',
      'psychopharmacology','psychotherapy','psychscience','puzzles','python','quotes','rage','rational','reasonstolive','rehabtherapy','relationship_advice',
      'relationships','resumes','riddles','robotics','ruby','saneorpsycho','schizophrenia','science','scientificresearch','self','selfhelp','selfimprovement','sex',
      'shittyaskscience','shittyideas','shittyprogramming','showerthoughts','simpleliving','slp','socialism','socialmedia','socialskills','sociology','software',
      'softwarearchitecture','softwaredevelopment','softwaregore','solotravel','space','specialed','startups','stopselfharm','suicidology','sysadmin','systems',
      'talesfromtechsupport','technology','techsupport','teenagers','testimonials','themixednuts','thisismyjob','tipofmytongue','todayilearned','tr',
      'translationstudies','travel','tutor','ultralight','undelete','undeleteShadow','undergraduateresearch','uniqueminds','visualbasic','web_programming','webdev',
      'whatisthis','whatstheword','windows','windowsazure','womenEngineers','words','work','workonline','worldnews','writingprompts']#major list, Once a week
   l=set()
   for k in b:
      l.add(k)
   b=[]
   for k in l:
      b.append(k)
   b.sort()
   subs(b)
   my.write('\nSUCCESS list_subreddits'+'-------------------------'+datetime.now().strftime(FORMAT)+'\n\n')
   #xcv=0
   #for k in b:
   #   xcv=xcv+1
   #   print(str(xcv)+"\t\t"+k)
#list_subreddits()
if __name__ == "__main__":
    processes = []
    arguments = sys.argv[2:]#it was b
    for x in arguments:
        print(x)
        p = multiprocessing.Process(target=main, args=(str(x),int(sys.argv[1]), ))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
#    my.close()
