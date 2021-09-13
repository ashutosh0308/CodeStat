import requests as req
import lxml
import bs4

def cc():
    try:
        inp=input("Enter Your CODECHEF ID : ")
        if(inp == "NA"):
            print("Thanks a lot for using the crawler. See you soon !")
            
        else:
            cc_res=req.get("https://www.codechef.com/users/"+inp)
            cc_soup=bs4.BeautifulSoup(cc_res.text,"lxml")
            cc_name=cc_soup.select("header h2")[0].text
            cc_rating=cc_soup.select(".rating-number")[0].text
            cc_stars=cc_soup.select(".rating-star")[0].text
            cc_ranks=cc_soup.select(".rating-ranks .inline-list a strong")
            cc_global=cc_ranks[0].text
            cc_country=cc_ranks[1].text
            cc_probs=cc_soup.select(".rating-data-section .content h5")
            cc_probs_full=cc_probs[0].text
            cc_probs_part=cc_probs[1].text
            print("Hey "+cc_name+" !")
            print("Your CodeChef Rating : "+cc_rating)
            print("Your CodeChef Stars : "+cc_stars)
            print("Your CodeChef GLOBAL RANK : "+cc_global)
            print("Your CodeChef COUNTRY RANK : "+cc_country)
            print("Codechef Problems : "+cc_probs_full+" & "+cc_probs_part)
            print("\n")
    except:
        print("Invalid Username! Please Try Again")


def cf():
  while(True):
    try:
        inp=input("Enter Your CODEFORCES ID : ")
        if(inp == "NA"):
            print("Thanks a lot for using the crawler. See you soon !")
            break
        else:
            cf_res=req.get("https://codeforces.com/profile/"+inp)
            cf_soup=bs4.BeautifulSoup(cf_res.text,"lxml")
            cf_details=cf_soup.select("ul li span ")
            cf_probs = cf_soup.select("._UserActivityFrame_counterValue")[0].text
            cf_rank = cf_details[5].text.replace(",","").upper()
            cf_curr_rating = cf_details[3].text
            cf_max_rating = cf_details[6].text
            print("Hey "+inp+" !")
            print("Your CodeForces Rank : "+cf_rank)
            print("Your CodeForces Current Rating : "+cf_curr_rating)
            print("Your CodeForces Max Rating : "+cf_max_rating)
            print("CodeForces Problems : "+cf_probs)
            print("\n") 
    except:
        print("Invalid Username! Please Try Again")

def hr():
  while(True):
    try:
        inp=input("Enter Your HACKERRANK ID : ")
        if(inp == "NA"):
            print("Thanks a lot for using the crawler. See you soon !")
            break
        else:
            agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            hr_res=req.get("https://www.hackerrank.com/"+inp,headers=agent)
            hr_soup=bs4.BeautifulSoup(hr_res.text,"lxml")
            hr_name=hr_soup.select(".profile-heading")[0].text
            hr_badges=hr_soup.select(".badge-title")
            numbadge=len(hr_badges)
            badge_name=[]
            item=0
            for item in range(0,numbadge):
                badge_name.append(hr_badges[item].text)
                item=item+1
            hr_star=hr_soup.find_all("g",class_='star-section')
            item=0
            score=[]
            for item in range(0,numbadge):
                x=list(hr_star[item].children)
                y=list(x[0].children)
                z=len(y)
                score.append(z)
                item=item+1
            print("Hey "+hr_name+" !")
            print("Your Badges : ")
            item=0
            for item in range(0,numbadge):
                print("> "+str(badge_name[item])+" : "+str(score[item])+" ⭐")
                item=item+1
            hr_certi=hr_soup.find_all("h2",class_="certificate-heading")
            print("\nYour Certificates : ")
            item=0
            for item in range(0,len(hr_certi)):
                hr_certi[item]=hr_certi[item].text.replace("Certificate: ","")
                print("> "+hr_certi[item])
                item=item+1
            print("") 
    except:
        print("Invalid Username! Please Try Again")

hr()




def gfg(inp):
    try:
        if(inp.upper() == "NA"):
            return "Thanks a lot for using the crawler. See you soon !"
        else:
            agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
            gfg_res=req.get("https://auth.geeksforgeeks.org/user/"+inp+"/practice",headers=agent)
            gfg_soup=bs4.BeautifulSoup(gfg_res.text,"lxml")
            gfg_name = gfg_soup.select(".mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold")[0].text
            gfg_inst = gfg_soup.select(".mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold")[1].text
            gfg_rank = gfg_soup.select(".mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold")[2].text
            gfg_rank=gfg_rank.replace('#','')
            g = gfg_soup.select('.mdl-cell.mdl-cell--6-col.mdl-cell--12-col-phone.textBold')[0].text
            gfg_score=''
            for item in g:
              if item in ['0','1','2','3','4','5','6','7','8','9']:
                gfg_score+=item
            p = gfg_soup.select('.mdl-cell.mdl-cell--6-col.mdl-cell--12-col-phone.textBold')[1].text
            gfg_probs=''
            for item in p:
              if item in ['0','1','2','3','4','5','6','7','8','9']:
                gfg_probs+=item 
            op_gfg = list([gfg_name,gfg_inst,gfg_rank,gfg_probs,gfg_score])
            return op_gfg 
    except:
        return "Invalid Username! Please Try Again"


x=gfg("ashu03")
print(x)