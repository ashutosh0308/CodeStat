from flask import Flask, request, render_template
import requests as req
import lxml
import bs4
from flask_mail import Mail
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ashutosh.sahay9@gmail.com',
    MAIL_PASSWORD=  'hqelblwwkluytgfb'
)
mail = Mail(app)



@app.route('/')
def index():
    cc_inp=request.args.get("cc_inp","")
    cf_inp=request.args.get("cf_inp","")
    hr_inp=request.args.get("hr_inp","")
    gfg_inp=request.args.get("gfg_inp","")
    fdb_user=request.args.get("fdb_user","")
    fdb_msg=request.args.get("fdb_msg","")
    
    
    cf_msg="Click on Get Details"
    hr_msg="Click on Get Details"
    gfg_msg="Click on Get Details"
    
    if cc_inp:
        op_cc=cc(cc_inp)
        cc_msg="Click on Get Details"
    else:
        op_cc=""
        cc_msg=""

    if cf_inp:
        op_cf=cf(cf_inp)
        cf_msg="Click on Get Details"
    else:
        op_cf=""
        cf_msg=""

    if hr_inp:
        op_hr=hr(hr_inp)
        hr_msg="Click on Get Details"
    else:
        op_hr=""
        hr_msg=""

    if gfg_inp:
        op_gfg=gfg(gfg_inp)
        cc_msg=""
    else:
        op_gfg=""
        gfg_msg=""

    if fdb_msg and fdb_user:
        send_fdb(fdb_user,fdb_msg)
    
   

    return render_template('index.html',op_cc=op_cc,op_cf=op_cf,op_hr=op_hr,op_gfg=op_gfg,cc_msg=cc_msg,cf_msg=cf_msg,hr_msg=hr_msg,gfg_msg=gfg_msg)

def cc(inp):
    try:
        if(inp.upper() == "NA"):
            return ""
        else:
            cc_res=req.get("https://www.codechef.com/users/"+inp)
            cc_soup=bs4.BeautifulSoup(cc_res.text,"lxml")
            cc_name=inp
            cc_rating=cc_soup.select(".rating-number")[0].text
            cc_stars=cc_soup.select(".rating-star")[0].text
            cc_ranks=cc_soup.select(".rating-ranks .inline-list a strong")
            cc_global=cc_ranks[0].text
            cc_country=cc_ranks[1].text
            cc_probs=cc_soup.select(".rating-data-section .content h5")
            cc_probs_full=cc_probs[0].text
            cc_probs_part=cc_probs[1].text
            op_cc=list([cc_name,cc_rating,cc_stars,cc_global,cc_country,cc_probs_full,cc_probs_part])
            return op_cc
        
    except:
        return ""

def cf(inp):
    try:
        if(inp.upper() == "NA"):
            return ""
        else:
            cf_res=req.get("https://codeforces.com/profile/"+inp)
            cf_soup=bs4.BeautifulSoup(cf_res.text,"lxml")
            cf_details=cf_soup.select("ul li span ")
            cf_probs = cf_soup.select("._UserActivityFrame_counterValue")[0].text
            cf_rank = cf_details[3].text.replace(",","").upper()
            cf_curr_rating = cf_details[1].text
            cf_max_rating = cf_details[4].text
            op_cf=list([inp,cf_rank,cf_curr_rating,cf_max_rating,cf_probs])
            return op_cf
    except:
        return ""  

def hr(inp):
    try:
        if(inp.upper() == "NA"):
            return ""
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
                score.append(str(z)+'⭐')
                item=item+1
            hr_certi=hr_soup.find_all("h2",class_="certificate-heading")
            item=0
            for item in range(0,len(hr_certi)):
                hr_certi[item]=hr_certi[item].text.replace("Certificate: ","")
                item=item+1
            hr_badgesAndstars = dict(zip(badge_name,score))
            op_hr = list([hr_name,hr_badgesAndstars,hr_certi])
            return op_hr 
    except:
        return ""



def gfg(inp):
    try:
        if(inp.upper() == "NA"):
            return ""
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
        return ""


def send_fdb(fdb_user,fdb_msg):
    sender_email = 'CodeStat'
    msg=fdb_user+" says :\n"+fdb_msg
    mail.send_message("CodeStat Update from "+ fdb_user,sender=sender_email,recipients=['ashutosh.sahay9@gmail.com'], body=msg )
            


if __name__ == "__main__":
    app.run(debug=True)
