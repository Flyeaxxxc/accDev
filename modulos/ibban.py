import requests,json
def ibban():

  url = "https://api.generadordni.es/v2/bank/account?results=3&bic,iban_formatted,ccc_formatted"

  response = requests.get(url)
  if response.status_code==200:
    response_json = response.json()
    var = response_json[0]
    ccc = var["ccc"]
    iban = var["iban"]
    entity = var["entity"]
    bics = var["bic"]
    msg = f"""
ಠ-> CCC : <code>{ccc}</code>

ಠ-> IBAN : <code>{iban}</code>

ಠ-> Entity : <code>{entity}</code>

ಠ-> BIC : <code>{bics}</code>"""
  else:
    msg = "ಠ-> ERROR : <b>PROBLEMA DE CONEXION</b>"
  return msg