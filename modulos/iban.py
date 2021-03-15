import requests
from bs4 import BeautifulSoup
def iban(iban):
  iban = iban

  page = requests.get(f"https://iban.codes/iban_validieren.html?&no_cache=1&tx_valIBAN_pi1%5biban%5d={iban}&tx_valIBAN_pi1%5bfi%5d=fi")

  soup = BeautifulSoup(page.content,"html.parser")

  k = soup.find_all("p")

  ñ=0

  list = []
  for i in k:
      list.append(i.text)
  if "This IBAN is incorrect." in list:
    msg = "❌ IBAN INVALIDO ❌"
  else:
    try:
      list[9] = list[9].replace("BIC:","").replace("""$('[data-toggle="popover"]').popover({trigger:'hover','placement':'top'});   BIC into the clipboard""","").replace("BIC into the clipboard","")

      list[3] = list[3].replace("""This IBAN has the correct length for this country""","").replace("(","").replace(").","")

      list[4] = list[4].replace("Bankleitzahl (bank code)","").replace(": This  is correct.","")

      list[5] = list[5].replace("Account number","").replace(": The account number contains a valid checksum.","")

      list[10] = list[10].replace("Bank:","")
      msg = f"""

✅ IBAN VALID ✅

🔰 IBAN : <code>{iban}</code>
🔰 country :<code>{list[3]}</code> 
🔰 BANK CODE :<code>{list[4]}</code> 
🔰 ACCOUNT NUMBER :<code>{list[5]} </code>
🔰 BIC :<code>{list[9]}</code>
🔰 BANK :<code>{list[10]}</code>"""
    except:
      msg = "❌ IBAN INVALIDO ❌"
  return msg