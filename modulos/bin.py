import re,requests,json
def check_bin(bin):
  bin = bin
  if len(bin) >= 6:
    bin= str(bin)
  try:
    bin= bin.replace("x","")
    bin= bin.replace("X","")
    bin= bin.split("|")[0]
  except:
    pass
  bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
  lenLuhn=len(str(bin))
  sinccheck=bin[:16]
  bin = str(bin)
  bin = re.sub('([a-zA-Z]){1,}', '', bin)
  try:
    unks = 0
    url='https://lookup.binlist.net/'+str(bin)
    try:
      page = requests.get(url)
      page.raise_for_status()
    except:
      pass
    page= page.content.decode()
    dic = json.loads(page)
    try:
      marca=dic['scheme'].upper()
    except:
      marca='DESCONOCIDO'
    try:
      tipo=dic['type'].upper()
    except:
      tipo='DESCONOCIDO'
    try:
      brnd=dic['brand'].upper()
    except:
      brnd='DESCONOCIDO'
    try:
      el_alpha=dic['country']['alpha2'].upper()
    except:
      el_alpha='DESCONOCIDO'
    try:
      pais=dic['country']['name'].upper()
    except:
      pais='DESCONOCIDO'
    try:
      emote=dic['country']['emoji'].upper()
    except:
      emote='DESCONOCIDO'
    try:
      tipo_moneda=dic['country']['currency'].upper()
    except:
      tipo_moneda='DESCONOCIDO'
    try:
      bank_name=dic['bank']['name'].upper()
    except:
      bank_name='DESCONOCIDO'
    try:
      bank_url=dic['bank']['url'].upper()
    except:
      bank_url='DESCONOCIDO'
    try:
      bank_phone=dic['bank']['phone'].upper()
    except:
      bank_phone='DESCONOCIDO'
    msg = f"""
🔰 Bin : <code>{bin}</code> {emote}

🔰 Marca : <b><u>{marca}</u></b>

🔰 Tipo de tarjeta: <b><u>{tipo}</u></b>

🔰 Nivel de tarjeta: <b><u>{brnd}</u></b>

🔰 Banco : <b><u>{bank_name}</u></b>

🔰 País : <b><u>{pais}</u></b> - <b><u>{el_alpha}</u></b> - 💲 <b><u>{tipo_moneda}</u></b>

🔰 URL Banco : {bank_url}"""
  except:
    msg = "❌ BIN INVALIDO ❌"
  return msg