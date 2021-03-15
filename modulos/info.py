# -*- coding: UTF-8 -*-

def info(id,name,title,id_2,username,ver):
	inf_one=""
	if title == None:
		inf_one == f"CHAT ID : <code>{id_2}</code>"
	else:
		inf_one = f"""[ GROUP ]\n\nID : <code>{id_2}</code>\n\nTITLE : <code>{title}</code>"""
	if username == None:
		inf_two = "◈ <b>no username</b>"
	else:
		inf_two = f"USERNAME : <code>{username}</code>"
	msg = f"""
<b>[ USER DATA ]</b>

ID : <code>{id}</code>

{inf_two}

FIRST NAME : <code>{name}</code>

IS BOT : <code>{ver}</code>

{inf_one}
"""
	return msg
