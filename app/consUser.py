from dataclasses import Field

import requests
 

headers={

    "ASKYAS-API-KEY": "acdfe5f4d",
    "Content-Type": "application/json"

    }

data={

    "Id_org":200,
    'Ref_user':'500', 
    'Ref_activity':'235', 
    "callbackUrl": "https://ticket.chambretechniqueinfo.com",
    "MobileMoney": "0970494397",                # 📱 Format: 0+9 derniers chiffres
    "Devise": "CDF",                            # 💰 CDF ou USD
    "Montant": 1000,                         # 💵 Montant en string
    "Motif": "Paiement services",                # 📝 Description claire
   
}


code='1205'

html="""

<html>
  <body>

  <h1 style='color:red'>TelCop</h1>

  <br><bR>


  <p style='color:red;border:dashed 2px green;text-align:center'>Code OTP 

    """+code+"""

  </p>

  <div style="width:60%;height:50px;background-color:red;color:white;font-weight:bold;border-radius:25px;margin-left:20%;font-size:18px;padding-left:20px">Valider</div>

  <bR><BR>

  </body>

</html>
"""




data={

    'nom_complet':"junior ASKYAS",
    'gmail':"askyas17@gmail.com",
    'contact':"0970494397",
    'code':1422

}



data={

    'receveid':'askyas17@gmail.com',
    'sender':'askyas2001@gmail.com',
    'pwd':"airrsousodyzvuiq",
    'code':10
 
}

    

data={

    'Id_org':200,
    "Id_facture":232,
    "Id_org":200,
    'Ref_user':'500', 
    'Ref_activity':'235', 
    "callbackUrl": "https://ticket.chambretechniqueinfo.com",
    "MobileMoney": "0823382732",                # 📱 Format: 0+9 derniers chiffres
    "Devise": "CDF",                            # 💰 CDF ou USD
    "Montant": 500,                         # 💵 Montant en string
    "Motif": "Paiement services",                # 📝 Description claire
   
}

 #"RefTransa": "20B2C3D4E5F6G7H8I9J0" 
#"RefPartenaire": "AA091",         # 🆔 20 caractères alphanumériques


#rep=requests.post('http://127.0.0.1:3333/cPaiement/C2B/create', json=data,headers=headers)

#rep=requests.get('http://127.0.0.1:3333/cPaiement/status/200', headers=headers)  

    
 




headersPaie={

    "Authorization": "Bearer r6woTN2CdOF4yAcE77z2isd1NFL05iNnURbdfmoH2JG2CZ4iZEozyAZCbb3o0E0a",
    "Content-Type": "application/json"
}

dataPaie={
            
    "RefTransa":'AsK20261024161348w71'

}

#rep=requests.post('https://api.wonyasoft.com/cpayment/detail', json=dataPaie,headers=headersPaie)

#rep=requests.get('http://127.0.0.1:3333/cPaiement/factures/Pay/get/100',headers=headers)

#rep=requests.get('https://app-api.wonyasoft.com/transaction-status/status/AsK20261026121044w29',headers=headersPaie)

rep=requests.get('http://127.0.0.1:3333/cPaiement/org/status/200',headers=headers)   


if rep.status_code==200:

    data=rep.json()
   
    print(data)

else:
    print("error")



 