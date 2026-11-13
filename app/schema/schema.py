from pydantic import BaseModel,EmailStr,Field,conint
from typing import Literal


class Mail(BaseModel):

    receveid:EmailStr=Field(description="gmail incorrect")
    sender:EmailStr=Field(description="gmail incorrect")
    pwd:str=Field(...,min_length=1,description="ref user ncorrect")
    code:int=Field(gt=0,description="code OTP")

class MailStandard(BaseModel):

    receveid:EmailStr=Field(description="gmail incorrect")
    sender:EmailStr=Field(description="gmail incorrect")
    pwd:str=Field(...,min_length=1,description="ref user ncorrect")
    msg:str=Field(...,min_length=1,description="ref user ncorrect")

class Paiement(BaseModel): 

    Id_facture:int=Field(gt=0,description="identifiant invalide")
    Id_org:int=Field(gt=0,description="identifiant invalide")
    Ref_user:str=Field(...,min_length=1,description="ref user ncorrect")
    Ref_activity:str=Field(...,min_length=1,description="ref activity incorrect")
    #RefPartenaire:str=Field(...,min_length=1,description="Ref Partenaire Incorrect")
    callbackUrl:str=Field(...,min_length=1,description="Url Incorrect")
    MobileMoney:str=Field(...,min_length=10,description="numero Mobile incorrect")
    Devise:Literal["USD","CDF"]
    Montant:int=Field(gt=0,description="montant invalide")
    Motif:str=Field(...,min_length=1,description="motif invalide") 

class Identite(BaseModel):

    nom_complet:str=Field(...,min_length=1,description="nom user ncorrect")
    gmail:EmailStr=Field(description="gmail incorrect")
    contact:str=Field(...,min_length=10,max_length=10,description="contact  incorrect")
    code:int=Field(gt=0,description="montant invalide")


class IdentiteInfo(BaseModel):

    nom_complet:str=Field(...,min_length=1,description="nom user ncorrect")
    gmail:EmailStr=Field(description="gmail incorrect")
    userGmail:EmailStr=Field(description="gmail incorrect")
    contact:str=Field(...,min_length=10,max_length=10,description="contact  incorrect")
    msg:str=Field(...,min_length=1,description="info  incorrect")

    


     