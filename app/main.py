from fastapi import FastAPI,Depends
import asyncio
import uvicorn
from model.back import Bd

from model import back
from schema.schema import Paiement,Mail,Identite,IdentiteInfo,MailStandard
from security import verify_api

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import Table,MetaData,Column,Integer,String,Float,Double,DateTime,Date,select
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import update
import sqlite3
import random
import httpx 
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app=FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)


headersMail={

    "Authorization": "Bearer r6woTN2CdOF4yAcE77z2isd1NFL05iNnURbdfmoH2JG2CZ4iZEozyAZCbb3o0E0a",
    "Content-Type": "application/json"
}


headers={

        "Authorization": "Bearer r6woTN2CdOF4yAcE77z2isd1NFL05iNnURbdfmoH2JG2CZ4iZEozyAZCbb3o0E0a",
        "Content-Type": "application/json"
    }


@app.get('/')

def index():

    return "WELCOME IN PAY 11 avril"



@app.post('/mail/info')

async def recuperation(data:dict,client=Depends(verify_api)):

    valable=[]
    echec=[]

    try:

        IdentiteInfo(**data)

        data['id_coperant']=random.randint(1000,50000)

        valable.append(data)
    
    except:

        echec.append(data)

    valableMail=[]
    echecMail=[]

    etatMail=False

    dataMail={}

    if valable :
    
        dataMail= {

            'receveid':data['gmail'],
            'msg':data['msg'],

            'sender':'askyas2001@gmail.com',
            'pwd':'airrsousodyzvuiq',

        }

        try:

            MailStandard(**dataMail)

            valableMail.append(dataMail)
        
        except:

            echecMail.append(dataMail)

       

        if valableMail:

            try:


                try:

                    subect=data['subject']
                    
                except:

                    subect='TELCOP'

                label=''

                try:

                    label=data['userGmail']
                
                except:

                    label=""


                html=""" <html> <body> <h1 style='color:black;text-align:left'>""" + subect + """ </h1> <br><bR> <h1 style='color:red;border:dashed 2px black;text-align:center'>  Urgence   <br>  """+ dataMail['msg']+  label +""" <br>  </h1>  <bR><bR> <div style="width:50%;height:50px;background-color:red;color:white;font-weight:bold;border-radius:25px;margin-left:22%;font-size:18px;padding-left:20%;padding-top:20px">Valider</div> <bR><BR> </body> </html>"""


                msg=MIMEMultipart('alternative')

                

                msg['subject']=subect

                msg['From']=dataMail['sender']
                msg['To']=dataMail['receveid']


                msg.attach(MIMEText(html,'html'))

                server=smtplib.SMTP('smtp.gmail.com',587)


                try:

                    async with httpx.AsyncClient(timeout=10.0) as client:

                        server.starttls()

                        server.login(dataMail['sender'],dataMail['pwd'])

                        server.sendmail(dataMail['sender'],dataMail['receveid'],msg.as_string())

                        server.quit()

                        etatMail=True

                except:

                    etatMail=False
                
            except:

                pass

    return {

        'create':etatMail,
        'echec':echecMail,
        'valable':valableMail

        }


@app.post('/mail/validate')

async def recuperation(data:dict,client=Depends(verify_api)):

    valable=[]
    echec=[]

    try:

        Identite(**data)

        data['id_coperant']=random.randint(1000,50000)

        valable.append(data)
    
    except:

        echec.append(data)

    valableMail=[]
    echecMail=[]

    etatMail=False

    dataMail={}

    if valable :
    
        dataMail= {

            'receveid':data['gmail'],
            'code':data['code'],

            'sender':'askyas2001@gmail.com',
            'pwd':'airrsousodyzvuiq',

        }

        try:

            Mail(**dataMail)

            valableMail.append(data)
        
        except:

            echecMail.append(data)

        subect=""

        if valableMail:

            try:


                try:

                    subect=data['subject']
                    
                except:

                    subect='TELCOP'


                html=""" <html> <body> <h1 style='color:black;text-align:left'> """ + subect +  """ </h1> <br><bR> <h1 style='color:red;border:dashed 2px black;text-align:center'>Code OTP   <br>  """+ str(dataMail['code']) +""" <br>  </h1>  <bR><bR> <div style="width:50%;height:50px;background-color:red;color:white;font-weight:bold;border-radius:25px;margin-left:22%;font-size:18px;padding-left:20%;padding-top:20px">Valider</div> <bR><BR> </body> </html>"""


                msg=MIMEMultipart('alternative')



                msg['subject']=subect


                msg['From']=dataMail['sender']
                msg['To']=dataMail['receveid']


                msg.attach(MIMEText(html,'html'))

                server=smtplib.SMTP('smtp.gmail.com',587)


                try:

                    async with httpx.AsyncClient(timeout=15.0) as client:

                        server.starttls()

                        server.login(dataMail['sender'],dataMail['pwd'])

                        server.sendmail(dataMail['sender'],dataMail['receveid'],msg.as_string())

                        server.quit()

                        etatMail=True

                except:

                    etatMail=False
                
            except:

                pass

    return {

        'create':etatMail,
        'echec':echec,
        'valable':valable

        }


@app.post('/mail/send')

async def recuperation(data:dict,client=Depends(verify_api)):

    valable=[]
    echec=[]

    try:

        Mail(**data)

        valable.append(data)
    
    except:

        echec.append(data)

    etat=False

    if valable:

        html=""" <html>   <body>  <h1 style='color:black;text-align:left'>TelCop </h1>  <br><bR>  <h1 style='color:red;border:dashed 2px black;text-align:center'>Code OTP  """+ str(data['code']) +"""  </h1> <div style="width:50%;height:50px;background-color:red;color:white;font-weight:bold;border-radius:25px;margin-left:22%;font-size:18px;padding-left:20%;padding-top:20px">Valider</div>  <bR><BR>  </body>  </html> """

        msg=MIMEMultipart('alternative')

        msg['subject']='TELCOP'
        msg['From']=data['sender']
        msg['To']=data['receveid']


        msg.attach(MIMEText(html,'html'))

        server=smtplib.SMTP('smtp.gmail.com',587)


        try:
            async with httpx.AsyncClient(timeout=10.0) as client:

                server.starttls()

                server.login(data['sender'],data['pwd'])

                server.sendmail(data['sender'],data['receveid'],msg.as_string())

                server.quit()

                etat=True

        except:

            etat=False
        

    return {

        'create':etat

        }

@app.post('/cPaiement/create')

async def recuperation(data:dict,client=Depends(verify_api)):
            
    valable=[]

    echec=[]

    repdata=[]

    refTrans=''

    ref_Partenaire=''
    
    try:

        Paiement(**data)

        id_org=data['Id_org']

        # selectionner le refPartnaire

        data_org=Bd().recupRef_Org(id_org)


        if data_org:

            ref_Partenaire=data_org[0]['refPartenaire']

        refTrans= 'AsK'  + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','').replace('-','').replace(' ','')+'w'+str(random.randint(1555,999999)) + str(random.randint(1555,999999))
        refTrans=refTrans[0:20]

        data['RefPartenaire']=ref_Partenaire        

        data['RefTransa']=refTrans
        data['Status']=False
        data['Create_date']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data['Action']='C2B'

        valable.append(data)

    
    except:

        echec.append(data)
    
    response=''


    etatConnexion=False
    
    if valable:

        repdata=Bd().createPaiementPay(valable)


        if repdata['create']==True:

            try:

                url = "https://app-api.wonyasoft.com/payment" 

                async with httpx.AsyncClient(timeout=15.0) as client:

                    response= await client.post(url,headers=headers, json = data)

                    response=response.json()

                    etatConnexion=True

            except:

                response=""

                etatConnexion=False


    return {

        'connexion':etatConnexion,
        'response':response
        
        }

@app.get('/cPaiement/B2C/detail/{ref_user}')

async def recuperation(ref_user:int,client=Depends(verify_api)):

    datanew=Bd().paiementDetailUserRetraitB2C(ref_user)

    etatConnexion=False

    dataPaiement=[]

    if datanew['data']:

        for li in datanew['data']:


            try:

                url = "https://app-api.wonyasoft.com/transactionStatus/status/" + li['refTrans']

                async with httpx.AsyncClient(timeout=40.0) as client:

                    response=await client.get(url,headers=headers)

                    response=response.json()

                    response['RefTransa']=li['refTrans']

                    dataPaiement.append(response)

                    etatConnexion=True

            except:

                response=False

                etatConnexion=False
    
    etatUpdate=False

    if dataPaiement:

        etatUpdate=Bd().updateEtatPaiementRetrait(dataPaiement)
    
    else:

        etatUpdate=True


    return {

        'update':etatUpdate
        
        }


@app.post('/cPaiement/B2C/create')

async def recuperation(data:dict,client=Depends(verify_api)):
            
    valable=[]

    echec=[]

    repdata=[]

    refTrans=''

    ref_Partenaire=''
    
    try:

        Paiement(**data)

        id_org=data['Id_org']

        # selectionner le refPartnaire

        data_org=Bd().recupRef_Org(id_org)


        if data_org:

            ref_Partenaire=data_org[0]['refPartenaire']

        refTrans= 'AsK'  + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','').replace('-','').replace(' ','')+'w'+str(random.randint(1555,999999)) + str(random.randint(1555,999999))
        refTrans=refTrans[0:20]

        data['RefPartenaire']=ref_Partenaire        

        data['RefTransa']=refTrans
        data['Status']=False
        data['Create_date']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data['Action']='B2C'

        valable.append(data)
    
    except:

        echec.append(data)
    
    response=''


    etatConnexion=False
    
    if valable:

        repdata=Bd().createPaiementPay(valable)


        if repdata['create']==True:


            try:

                url = "https://app-api.wonyasoft.com/payment" 

                async with httpx.AsyncClient(timeout=40.0) as client:

                    response= await client.post(url,headers=headers, json = data)

                    response=response.json()

                    etatConnexion=True

            except:

                response=""

                etatConnexion=False


    return response,etatConnexion


@app.get('/cPaiement/refUserForActivitySucces/{ref_user}/{ref_activity}')

async def recuperation(ref_user:str,ref_activity:str,client=Depends(verify_api)):
    
    # il fau chercher à changer l'etat de transstion du paiement

    datanew=Bd().paiementDetailUserSucces(ref_user,ref_activity)


    dataPaiement=[]

    etatConnexion=True

    if datanew:

        for li in datanew:

            try:

                url = "https://app-api.wonyasoft.com/transactionStatus/status/" + li['refTrans']

                async with httpx.AsyncClient(timeout=40.0) as client:

                    response=await client.get(url,headers=headers)

                    response=response.json()

                    response['RefTransa']=li['refTrans']

                    dataPaiement.append(response)

                    etatConnexion=True

            except:

                response=False

                etatConnexion=False
    
   
    else:

        etatConnexion=True


    return dataPaiement,etatConnexion


# recuperation des operation de l'utilisateur en refefrence de son identifiant et l activité

 
@app.get('/cPaiement/refUserForActivity/B2C/{ref_user}/{ref_activity}')

async def recuperation(ref_user:str,ref_activity:str,client=Depends(verify_api)):
    
    # il fau chercher à changer l'etat de transstion du paiement

    datanew=Bd().paiementDetailUserB2C(ref_user,ref_activity)

    dataRefTrans=[]

    dataReturn=[]

    dataRefTrans=datanew['data']

    etatConnexion=True

    for li in dataRefTrans:

        try:

            url = "https://app-api.wonyasoft.com/transactionStatus/status/" + li['refTrans']

            async with httpx.AsyncClient(timeout=40.0) as client:

                response=await client.get(url,headers=headers)

                response=response.json()

                response['RefTransa']=li['refTrans']


                dataReturn.append(response)

                etatConnexion=True

        except:

            response=False

            etatConnexion=False
    
    data={}

    etatUpdate=False


    valide=[]
    encours=[]
    annules=[]


    if dataReturn:

        #etatUpdate=Bd().updateEtatPaiement(dataReturn)

        for li in dataReturn:

            
            if li['success']==True and li['data']['StatutWonya']=="Reçu":

                valide.append(li)
            
            else:

                annules.append(li)


    dataPaiement={}


    dataPaiement['valide']=valide
    dataPaiement['annules']=annules

    #dataPaiement['encours']=encours
    #data['update']=etatUpdate
    
    data['connexion']= etatConnexion

    data['data']= dataPaiement

    

    return {

        'data':data
    }

 
@app.get('/cPaiement/refUserForActivity/{ref_user}/{ref_activity}')

async def recuperation(ref_user:str,ref_activity:str,client=Depends(verify_api)):
    
    # il fau chercher à changer l'etat de transstion du paiement

    datanew=Bd().paiementDetailUser(ref_user,ref_activity)

    dataRefTrans=[]

    dataReturn=[]

    dataRefTrans=datanew['data']

    etatConnexion=True

    for li in dataRefTrans:

        try:

            url = "https://app-api.wonyasoft.com/transactionStatus/status/" + li['refTrans']

            async with httpx.AsyncClient(timeout=25.0) as client:

                response=await client.get(url,headers=headers)

                response=response.json()

                response['RefTransa']=li['refTrans']

                response['ref_activity']=ref_activity


                dataReturn.append(response)

                etatConnexion=True

        except:

            response=False

            etatConnexion=False
    
    data={}

    etatUpdate=False


    valide=[]
    encours=[]
    annules=[]


    if dataReturn:

        etatUpdate=Bd().updateEtatPaiement(dataReturn)

        for li in dataReturn:


            if li['success']==True and li['data']['status']=="pending":

                encours.append(li)
            
            elif li['success']==True and li['data']['status']=="completed":

                valide.append(li)
            
            else:

                annules.append(li)


    dataPaiement={}


    dataPaiement['valide']=valide
    dataPaiement['encours']=encours
    dataPaiement['annules']=annules

    data['update']=etatUpdate
    data['connexion']= etatConnexion

    data['data']= dataPaiement

    

    return data


@app.get('/cPaiement/detail/{id_org}')

async def recuperation(id_org:int,client=Depends(verify_api)):
    
    datanew=Bd().paiementDetail(id_org)

    dataRefTrans=[]

    dataReturn=[]

    dataRefTrans=datanew['data']

    url = "https://api.wonyasoft.com/cpayment/detail" 

     

    for li in dataRefTrans:

        try:

            data={
                
                "RefTransa": li['refTrans']

            }

            async with httpx.AsyncClient(timeout=40.0) as client:

                response=await client.post(url,headers=headers, json = data)

                response=response.json()

                response['ref']=li['refTrans']

                dataReturn.append(response)

        except:

            response=False
    
    data={}

    etatUpdate=False

    if dataReturn:

        etatUpdate=Bd().updateEtatPaiement(dataReturn)
    
    data['update']=etatUpdate

    data['data']=dataReturn

    return data

@app.get('/cPaiementAll/{id_org}')

def recuperation(id_org:int, client=Depends(verify_api)):
            
    datanew=Bd().selectPaiement(id_org) 

    return datanew



@app.get('/cPaiementAll/reussi/{id_org}')

def recuperation(id_org:int,client=Depends(verify_api)):
            
    datanew=Bd().paiementReussi(id_org) 

    return datanew
 

@app.get('/cPaiementAll/echec/{id_org}')

def recuperation(id_org:int,client=Depends(verify_api)):
            
    datanew=Bd().paiementEchec(id_org) 

    return datanew

# mis a jour 

@app.get('/cPaiement/factures/Pay/get/{id_org}')

def recuperation(id_org:int,client=Depends(verify_api)): 
            
    datanew=Bd().getFatcurePay(id_org) 

    return {

        'data':datanew

    }


@app.get('/cPaiement/factures/Historique/get/{id_org}')

def recuperation(id_org:int,client=Depends(verify_api)): 
            
    datanew=Bd().getFatcurePayHISTO(id_org) 

    return {

        'data':datanew

    }

@app.get('/cPaiement/org/status/{id_org}')

async def recuperation(id_org:int,client=Depends(verify_api)): 
            
    datanew=Bd().getPaieENCOURS(id_org) 

    url = "https://app-api.wonyasoft.com/transaction-status/status/" 

    dataReturn=[]
    
    for li in datanew['data']:

        try:

            data={
                
                "RefTransa": li['refTrans']  

            }

            async with httpx.AsyncClient(timeout=25.0) as client:

                response=await client.get(url + str(li['refTrans']),headers=headers)

                response=response.json()

                response['ref']=li['refTrans']

                dataReturn.append(response)

                etatConnexion=True

        except:

            response=False

            etatConnexion=False

        encours=[]
        valide=[]
        annules=[]

        if dataReturn:
        
        
            for li in dataReturn:
    
                if li['success']==True and li['data']['status']=="completed":

                    valide.append(li)
                
                else:
    
                    encours.append(li)


        etatUpdate=Bd().updateEtatPaiement(valide)

        datanewValide=Bd().getPaieVALIDER(id_org) 

        datanewFACTURE=Bd().getFatcurePay(id_org) 
    
        dataPaiement={}
    
    
        dataPaiement['valide']=valide
        dataPaiement['encours']=encours

        data={}
    
        data['update']=etatUpdate
        data['connexion']= etatConnexion
    
        data['data']= dataPaiement

        data['transation']= datanewValide
        data['facture']=datanewFACTURE 


    return data

@app.post('/cPaiement/C2B/create')

async def recuperation(data:dict,client=Depends(verify_api)):
            
    valable=[]

    echec=[]

    repdata=[]

    refTrans=''

    ref_Partenaire=''
    
    try:

        data['Ref_user']='500'
        data['Ref_activity']='235'
        data['callbackUrl']=  "https://ticket.chambretechniqueinfo.com"

        Paiement(**data)

        id_org=data['Id_org']

        # selectionner le refPartnaire

        #data_org=Bd().recupRef_Org(id_org)

        #if data_org:

        #    ref_Partenaire=data_org[0]['refPartenaire']

        refTrans= 'AsK'  + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':','').replace('-','').replace(' ','')+'w'+str(random.randint(1555,999999)) + str(random.randint(1555,999999))
        refTrans=refTrans[0:20]

        data['RefPartenaire']='901162893236'        

        data['RefTransa']=refTrans
        data['Status']=False
        data['Create_date']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data['Action']='C2B'

        valable.append(data)

    except:

        echec.append(data)
    
    response=''

    etatConnexion=False

    repdata=[]
    
    if valable:

        repdata=Bd().createPaiementPay(valable)

        etatConnexion=False

        if repdata['create']==True:

            print("arrive")

            try:

                url = "https://app-api.wonyasoft.com/payment" 

                async with httpx.AsyncClient(timeout=25.0) as client:

                    response= await client.post(url,headers=headers, json = data)

                    response=response.json()

                    etatConnexion=True

            except:

                response=""

                etatConnexion=False
                

    return {

        'valable':valable,
        'echec':echec,
        'rep':repdata,
        'connexion':etatConnexion
        
        }




if __name__=='__main__':

    uvicorn.run('main:app',host='0.0.0.0',port=3333,reload=True)


    