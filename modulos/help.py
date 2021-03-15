# -*- coding: UTF-8 -*-

def help_user(id,first_name):
	if id == 1528509933:
		msg = f"""
[ HELP ]

------------------------------

+ <b>start</b> : start the bot

+ <b>search</b> : search webs

+ <b>iban</b>: verify iban

+ <b>bin</b> : verify bin

+ <b>nbin</b> : create new bin

+ <b>niban</b>: create new iban

+ <b>ext</b> : extrapolate (bin or cc)

+ <b>gen</b> : generate from bin

+ <b>li</b> : linux command handling

+ <b>admin_web</b> : find admin panel

+ <b>info</b> : view user information

------------------------------

[ OWNER : <code>{first_name}</code> ]"""
	else:
		msg = f"""
[ HELP ]

------------------------------

+ <b>start</b> : start the bot

+ <b>search</b> : search webs

+ <b>iban</b> : verify iban

+ <b>bin</b> : verify bin

+ <b>nbin</b> : create new bin

+ <b>niban</b> : create new iban

+ <b>ext</b> : extrapolate (bin or cc)

+ <b>gen</b> : generate from bin

+ <b>admin_web</b> : find admin panel

+ <b>info</b> : view user information

------------------------------

[ USER : <code>{first_name}</code> ]"""
	return msg