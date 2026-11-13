from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import Table,MetaData,Column,Integer,String,Float,Double,DateTime,Date,select
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import update,func

from sqlalchemy import desc,asc,not_,exists

import sqlite3

import random 

from datetime import datetime

class Bd():

    def __init__(self):

        global engine,sessionLocal,metadata,datte,datettime,date

        datte=datetime.now().strftime('%Y-%m-%d')
        date=datetime.now().strftime('%Y-%m-%d')
        datettime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        urlBAse="mysql+mysqlconnector://askyas:askyas@localhost:3306/paiementAPI"
        engine=create_engine(urlBAse)

        #urlBAse="mysql+mysqlconnector://askyas:askyas@localhost:3306/kenamelBD.db"

        #engine=create_engine("sqlite:///kenamelBD.db")
        #metadata=MetaData()

        sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

        metadata=MetaData()

        ccon=engine.connect()
        
    def testBase(self):  

        
        try: 

            with sessionLocal() as session:
                res=session.execute(text("SELECT DATABASE()"))

                rep=res.fetchone()  

        except Exception as e:

            print(e)
            rep=""

        
        return rep

    def createPaiementPay(self,data):

        dataa={}

        dataNew=[]

        for li in data:

            dataa['id_facture']=li['Id_facture']
            dataa['id_org']=li['Id_org']
            dataa['ref_user']=li['Ref_user']
            dataa['ref_activity']=li['Ref_activity']
            dataa['refPartenaire']=li['RefPartenaire']
            dataa['callbackUrl']=li['callbackUrl']
            dataa['mobileMoney']=li['MobileMoney']
            dataa['devise']=li['Devise']
            dataa['montant']=int(li['Montant'])
            dataa['motif']=li['Motif']
            dataa['refTrans']=li['RefTransa']
            dataa['action']=li['Action']
            dataa['status']=li['Status']
            dataa['create_date']=li['Create_date']
        
        
        dataNew.append(dataa)
        
        
        
        t_bloc=Table("paiement",metadata,autoload_with=engine)
        t_bloc_Activity=Table("activity",metadata,autoload_with=engine)
        t_blocUser=Table("user",metadata,autoload_with=engine)
        

        dataActivity={}


        dataActivity['ref_activity']=dataa['ref_activity']
        dataActivity['id_org']=dataa['id_org']
        dataActivity['detail']=dataa['motif']
        dataActivity['create_date']=datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

        etatCreateRefOrder=False

        try:

            with engine.connect() as session:

                session.execute(t_bloc_Activity.insert(),dataActivity)

                session.commit()

                etatCreateRefOrder=True

                
        except Exception as e:

            etatCreateRefOrder=False


        tabvalUser=[]

        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_blocUser).where(t_blocUser.c.ref_user==dataa['ref_user']))

                tabvalUser=res.mappings().all()
                
        except:
            
            tabvalUser=[]
            msg='ERROR'
    

        etatCreate=False
        

        if tabvalUser :

            try:

                with engine.connect() as session:

                    session.execute(t_bloc.insert(),dataNew)

                    session.commit()

                    etatCreate=True

                    error="succes"

            except Exception as e:

                etatCreate=False
                error="echec"
            
        else:


            dataUser={}

            dataUser['ref_user']= dataa['ref_user']
            dataUser['id_org']= dataa['id_org']
            dataUser['detail']=str(dataa['id_org'])+'client'+datettime
            dataUser['etat']=True
            dataUser['create_date']=datettime


            etatUser=False


            try:

                with engine.connect() as session:

                    session.execute(t_blocUser.insert(),dataUser)

                    session.commit()

                    etatUser=True

                   
            except Exception as e:

                etatUser=False

            if etatUser==True:

                try:

                    with engine.connect() as session:

                        session.execute(t_bloc.insert(),dataNew)

                        session.commit()

                        etatCreate=True

                        error="succes"

                except Exception as e:

                    etatCreate=False
                    error=e

        
        return {
                'create':etatCreate
            }


    def paiementDetailUser(self,ref_user,ref_activity):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)
        

        try:

            t_blocUser=Table("user",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('id_org',Integer),
            Column('detail',String),
            Column('etat',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_blocUser=Table("user",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).join(t_blocUser, t_bloc.c.ref_user==t_blocUser.c.ref_user).where(and_(t_bloc.c.ref_user==ref_user, t_bloc.c.ref_activity ==ref_activity,t_bloc.c.action=='C2B',t_blocUser.c.etat==True)).order_by(desc(t_bloc.c.create_date)))

                tabval=res.mappings().all()

                
        except:
            
            tabval=[]
                
        return {

            'data':tabval
        }


    def paiementDetailUserB2C(self,ref_user,ref_activity):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)
        

        try:

            t_blocUser=Table("user",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('id_org',Integer),
            Column('detail',String),
            Column('etat',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_blocUser=Table("user",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).join(t_blocUser, t_bloc.c.ref_user==t_blocUser.c.ref_user).where(and_(t_bloc.c.ref_user==ref_user, t_bloc.c.ref_activity ==ref_activity,t_bloc.c.action=='B2C',t_blocUser.c.etat==True)).order_by(desc(t_bloc.c.create_date)))

                tabval=res.mappings().all()

                
        except:
            
            tabval=[]
                
        return {

            'data':tabval
        }


    def paiementDetailUserRetraitB2C(self,ref_user):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)
        

        try:

            t_blocUser=Table("user",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('id_org',Integer),
            Column('detail',String),
            Column('etat',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_blocUser=Table("user",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).join(t_blocUser, t_bloc.c.ref_user==t_blocUser.c.ref_user).where(and_(t_bloc.c.ref_user==ref_user,t_blocUser.c.etat==True, t_bloc.c.status==False, t_bloc.c.action=='B2C')).order_by(desc(t_bloc.c.create_date)))

                tabval=res.mappings().all()

                
        except:
            
            tabval=[]
                
        return {

            'data':tabval
        }



    def paiementDetailUserSucces(self,ref_user,ref_activity):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)
        
        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc.c.refTrans).where(and_(t_bloc.c.ref_user==ref_user, t_bloc.c.ref_activity ==ref_activity,t_bloc.c.status==True,t_bloc.c.action=='C2B')).order_by(desc(t_bloc.c.create_date)))

                tabval=res.mappings().all()

                
        except:
            
            tabval=[]
                
        return tabval
        


    def paiementDetail(self,id_org):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc.c.refTrans).where(t_bloc.c.id_org==id_org).order_by(desc(t_bloc.c.create_date)).limit(5))

                tabval=res.mappings().all()

                if tabval:

                    msg="succes"

                else:

                    msg="operation introuvable"
                
        except:
            
            tabval=[]
            msg='ERROR'

                
        return {

            'data':tabval
        }
    


    def paiementReussi(self,id_org):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).order_by(desc(t_bloc.c.create_date)).where(t_bloc.c.id_org==id_org,t_bloc.c.status==True))

                tabval=res.mappings().all()

                if tabval:

                    msg="succes"

                else:

                    msg="operation introuvable"
                
        except:
            
            tabval=[]
            msg='ERROR'

                
        return {

            'data':tabval,
            'message': msg
        }
    

    def paiementEchec(self,id_org):
        
        tabval=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('refPartenaire',String),
            Column('ref_activity',String),
            Column('callbackUrl',String),
            Column('mobileMoney',String),
            Column('devise',String),
            Column('montant',Integer),
            Column('motif',String),
            Column('refTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)

        
        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).order_by(desc(t_bloc.c.create_date)).where(t_bloc.c.id_org==id_org,t_bloc.c.status==False))

                tabval=res.mappings().all()

                if tabval:

                    msg="succes"

                else:

                    msg="operation introuvable"
                
        except:
            
            tabval=[]
            msg='ERROR'

                
        return {

            'data':tabval,
            'message': msg
        }
    



    def recupRef_Org(self,id_org):

        tabval=[]
        
        try:

            t_bloc=Table("partenaire",metadata,

            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('id_org',Integer),
            Column('refPartenaire',String),
            Column('active',bool),
            Column('create_date',DateTime)
        )
    
        except:

            t_bloc=Table("partenaire",metadata,autoload_with=engine)
        

        try:
                
            with engine.connect() as con:

                res=con.execute(select(t_bloc).where(and_(t_bloc.c.id_org==id_org,t_bloc.c.active==True)))

                tabval=res.mappings().all()

                
        except:
            
            tabval=[]
        
        return tabval


    def selectPaiement(self,id_org:int):

        tabdata=[]

        try:

            t_bloc=Table("paiement",metadata,

            Column('Id',Integer,primary_key=True,autoincrement=True),
            Column('ref_user',String),
            Column('RefPartenaire',String),
            Column('ref_activity',String),
            Column('CallbackUrl',String),
            Column('MobileMoney',String),
            Column('Devise',String),
            Column('Montant',Integer),
            Column('Motif',String),
            Column('RefTrans',String),
            Column('action',String),
            Column('status',bool),
            Column('Create_date',Date)
        )
    
        except:

            t_bloc=Table("paiement",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con:

                res=con.execute(select(t_bloc).order_by(desc(t_bloc.c.create_date)).where(t_bloc.c.id_org==id_org))

                tabval=res.mappings().all()

                if tabval:

                    msg="succes"

                else:

                    msg="operation introuvable"

        except Exception as e:

            error=e
            tabval=[]
                
        return {

            'data':tabval,
            'message': msg
        }


    def updateEtatPaiementRetrait(self,data):

        try:
                        
            table2=Table("paiement",metadata,
                        
                Column('id',Integer,primary_key=True,autoincrement=True),
                Column('ref_user',String),
                Column('refPartenaire',String),
                Column('ref_activity',String),
                Column('callbackUrl',String),
                Column('mobileMoney',String),
                Column('devise',String),
                Column('montant',String),
                Column('motif',String),
                Column('refTrans',String),
                Column('action',String),
                Column('status',bool),
                Column('create_date',DateTime)
            )

        except:

            table2=Table("paiement",metadata,autoload_with=engine)
        
        etat=False 

        try:

            with engine.connect() as con:

                for li in data:

                    if li['success']==True and li['data']['StatutWonya']=="Reçu":  

                        res=update(table2).where(and_(table2.c.refTrans==li['data']['refTransa'])).values(status=True)

                        con.execute(res)  

                        con.commit()

                        etat=True

        except:

            etat=False 
        
        return  etat


    def updateEtatPaiement(self,data):

        table2=Table("paiement",metadata,autoload_with=engine)

        table2FACT=Table("factures",metadata,autoload_with=engine)
        
        etat=True 

        try:

            with engine.connect() as con:

                for li in data:

                    res=update(table2).where(and_(table2.c.refTrans==li['data']['refTransa'])).values(status=True)

                    resss=update(table2FACT).where(and_( table2FACT.c.id_facture==table2.c.id_facture ,table2.c.refTrans==li['data']['refTransa'])).values(status=True)

                    con.execute(res) 
                    con.execute(resss)  

                    con.commit()    

                    etat=True

                 
        except:

            etat=False 
        
        return  etat
 


    def getFatcure(self,id_org:int):
    
        tabval=[]

        t_blocFAC=Table("factures",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con: 

                res=con.execute(select(t_blocFAC).order_by(desc(t_blocFAC.c.create_date)).where(and_(t_blocFAC.c.id_org==id_org,t_blocFAC.c.status==False)))

                tabval=res.mappings().all()


        except Exception as e:

            error=e
            tabval=[]
                
        return {

            'data':tabval
        }


    def getPaieENCOURS(self,id_org:int):
    
        tabval=[]

        t_blocFAC=Table("paiement",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con: 

                res=con.execute(select(t_blocFAC).where(and_(t_blocFAC.c.id_org==id_org,t_blocFAC.c.status==False)))

                tabval=res.mappings().all()


        except Exception as e:

            error=e
            tabval=[]
                
        return {

            'data':tabval
        }


    def getPaieVALIDER(self,id_org:int):
        
        tabval=[]

        t_blocFAC=Table("paiement",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con: 

                res=con.execute(select(t_blocFAC).where(and_(t_blocFAC.c.id_org==id_org,t_blocFAC.c.status==True)))

                tabval=res.mappings().all()


        except Exception as e:

            error=e
            tabval=[]
                
        return {

            'data':tabval
        }


    def getFatcurePay(self,id_org:int):
        
        tabval=[]

        t_blocFAC=Table("factures",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con: 

                res=con.execute(select(t_blocFAC,func.datediff(func.now(),t_blocFAC.c.create_date).label('jr')).where(and_(t_blocFAC.c.id_org==id_org,t_blocFAC.c.status==False)))

                tabval=res.mappings().all()


        except Exception as e:

            error=e
            tabval=[]

            
                
        return  tabval

    
    def getFatcurePayHISTO(self,id_org:int): 
        
        tabval=[]

        t_blocFAC=Table("factures",metadata,autoload_with=engine)

        try:
        
            with engine.connect() as con: 

                res=con.execute(select(t_blocFAC).where(and_(t_blocFAC.c.id_org==id_org,t_blocFAC.c.status==True)))

                tabval=res.mappings().all()


        except Exception as e:

            error=e
            tabval=[]
                
        return tabval
        

 
   
   # il faut maintenant creer un ordre rejoind
 
    