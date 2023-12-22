import telebot, requests, re, json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

FULL = [5012010632,-1001783823529,-1001824484688,-1002087649012]

bot = telebot.TeleBot("6437385774:AAFTaRB_Iwz-2RWugyGMjEM4_gLCqFIcemM")

@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
  notbin = []
  bid = men.chat.id
  mensagem = men.text
  if men.text == '/menuu':
    bot.reply_to(men, '<b>' + '⚠️ ERRADO BURRO ⚠️' + '</b>')
  else:
    try:
      menu = f'''Bem-vindo(a) ao MdzSearch, o bot mais completo de consultas do telegram!
         
🌟✨ Aqui você pode descobrir informações incríveis sobre pessoas, como nome, cpf, idade, cidade, redes sociais e muito mais. 

🕵️‍♀️🔍 Sinta-se à vontade para explorar todas as nossas utilidades e divirta-se! 

© By: @gringomdz'''
      bot.reply_to(men, menu, parse_mode='HTML', reply_markup=start_markup())
    except:
      bot.reply_to(men, menu)

def start_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
	
    markup.add(InlineKeyboardButton("🔎 Consultas", callback_data="consultas"),
    InlineKeyboardButton("🟢 Dev", url="t.me/gringomdz"),
    InlineKeyboardButton("🔰 Canal",, url="https://t.me/mdzup"),
    InlineKeyboardButton("❓ Deseja fazer Parceria?", callback_data="parceria"))
    return markup

def home_markup():
  markup = InlineKeyboardMarkup()
  markup.row_width = 2


def apagar_markup():
  markup = InlineKeyboardMarkup()
  markup.row_width = 1
  markup.add(
    InlineKeyboardButton(
      "💳 COMPRE LOGINS $",
      url="https://t.me/mdzlogins2bot"))
  return markup


def back_markup():
  markup = InlineKeyboardMarkup()
  markup.row_width = 1
  markup.add(InlineKeyboardButton("🔙 Voltar", callback_data="back"))
  return markup

def clear_markup(id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("[ 🗑 ] Apagar [ 🗑 ]", callback_data=f"delete {id}"))
    return markup 

def adm_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("👻 Administrador", url="t.me/gringomdz"))
    return markup 

@bot.message_handler(commands=['cpf' , 'Cpf', 'CPF'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=cpf1&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ CPF NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                		               		
@bot.message_handler(commands=['cpf2' , 'Cpf2', 'CPF2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=cpf2&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ CPF NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')                		                		
@bot.message_handler(commands=['cnpj'])
def zn(nome):
  id1 = nome.chat.id

  ltnome = FULL
  if id1 in ltnome:
    try:
      msg = nome.text
      fl = msg.split(' ')
      ip = re.sub('[^0-9]', '', msg)
      url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
      req = url.json()
      response = f'🔎 | CNPJ ENCONTRADO!\n\n• UF: {req["abertura"]}\n• SITUAÇÃO: {req["situacao"]}\n• TIPO: {req["tipo"]}\n• NOME: {req["nome"]}\n• FANTASIA: {req["fantasia"]}\n• PORTE: {req["porte"]}\n• NATUREZA JURÍDICA: {req["natureza_juridica"]}\n• LOGRADOURO: {req["logradouro"]}\n• NÚMERO: {req["numero"]}\n• MUNICÍPIO: {req["municipio"]}\n• BAIRRO: {req["bairro"]}\n• ESTADO: {req["uf"]}\n• CEP: {req["cep"]}\n• TELEFONE: {req["telefone"]}\n• DT SITUAÇÃO: {req["data_situacao"]}\n• MOTIVO: {req["motivo_situacao"]}\n• CNPJ: {req["cnpj"]}\n• ÚLTIMA ATUALIZAÇÃO: {req["ultima_atualizacao"]}\n\n© @mdzmodders'
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.send_chat_action(nome.chat.id, 'typing')
      bot.reply_to(nome, response, reply_markup=back_markup())

    except Exception as e:
      print(e)
      bot.reply_to(nome, '<b>⚠️ CNPJ NÃO ENCONTRADO!</b>', parse_mode='html')
  else:
    bot.reply_to(nome, '『❗』Este comando é apenas para usuários premium.'
                 '')
                                 		
@bot.message_handler(commands=['perfil'])
def bniio(men):
  notbin = []
  bid = men.chat.id
  mensagem = men.text
  if men.text == '/menuu':
    bot.reply_to(men, '<b>' + '⚠️ ERRADO BURRO ⚠️' + '</b>')
  else:
    try:
      menu = f'''⚠️ - Não chame se vc estiver com dúvidas de como usar o chk ja esta bem explicado qualquer comando do bot. não chame se vc queira comprar ccs pois não vendemos! Não chame por qualquer coisa besta pois sera bloqueado chame se realmente for algo importante!!

© By: @gringomdz / @mdzup\n\n'''
      bot.reply_to(men, menu, parse_mode='HTML', reply_markup=adm_markup())
    except:
      bot.reply_to(men, menu)                		
                		
@bot.message_handler(commands=['placa', 'placa'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=placa&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ PLACA NÃO ENCONTRADA!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                		
@bot.message_handler(commands=['rg', 'rg'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=rg&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ RG NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')                		
@bot.message_handler(commands=['bitly', 'bitly'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/shortlink/bitly?url=' + ip, token)
                    req = url.json()
                    response = f'''{req["result"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ RG NÃO ENCONTRADO!</b>', parse_mode='html')                		
@bot.message_handler(commands=['score', 'score'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=score&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ CPF NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')                		                		
@bot.message_handler(commands=['disney'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = 'apitoken=keyfree1dia'
                    url = requests.get('https://xanax-apis.online/outros/disney?' + token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ BIN NÃO ENCONTRADA!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                		
@bot.message_handler(commands=['proc', 'procurados'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/procurados?query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ IMEI NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')                		
@bot.message_handler(commands=['imei', 'imei'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=imei&query=' + ip, token)
                    req = url.json()
                    response = f'''{req["resultado"]}'''
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=adm_markup())

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ IMEI NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')                		
@bot.message_handler(commands=['cep'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=cep&query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ CEP NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
				
@bot.message_handler(commands=['beneficio'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=beneficios&query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ CPF NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                		
@bot.message_handler(commands=['cnumber'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:4109/api/check-number?query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ NÚMERO NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                		
@bot.message_handler(commands=['gencc'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/gerar-cc?query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ BIN NÃO ENCONTRADA!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                 		                		
@bot.message_handler(commands=['telefone2', 'tel2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=telefone&query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ TELEFONE NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')
                    		                		
@bot.message_handler(commands=['telefone', 'tel'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    ip = re.sub('[^0-9]', '', msg)
                    token = '&apitoken=keyfree1dia'
                    url = requests.get('http://mdzapi.mdzhost.cloud:5003/api/consultas?type=tel2&query=' + ip, token)
                    req = url.json()
                    response = f'{req["resultado"]}\n\n🤖 @MDZROBOOTBOT'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>⚠️ TELEFONE NÃO ENCONTRADO!</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''『❗』Este comando é apenas para usuários premium.''')

@bot.callback_query_handler(func=lambda call: 'delete' in call.data)
def delete_handler(call):
    chat_id = call.message.chat.id
    if call.from_user.id == int(call.data.split(' ')[1]):
        try:
            bot.delete_message(chat_id, call.message.message_id)
            bot.delete_message(
                chat_id, call.message.reply_to_message.message_id)
            bot.answer_callback_query(call.id, '✅ - Mensagem deletada')
            return
        except Exception as err:
            print('⚠️ - Erro ao apagar mensagem', err)
            return
    bot.answer_callback_query(call.id, '❌ - Você não tem autorização para isso')
@bot.callback_query_handler(func=lambda call: not "delte" in call.data)
def callback_query(call):

  if call.data == 'consultas':
    return bot.edit_message_text(
      f'''☆ | COMANDOS DO MDZ BUSCAS | ☆\n\n🔄 Bases de dados atualizada, servidores otimizados!\n\n> 10 Bases On-line ao Sistema\n\n● | PARÂMETROS | ●\n\n🟢 STATUS 》ONLINE\n🟡 STATUS 》MANUTENÇÃO\n🔴 STATUS 》OFFLINE\n\n• [ CPF (1) ] •\n\n🟢 CPF1: /cpf 05344565828\n/cpf2 11976388732\n\n • [ TELEFONES (1) ] •\n\n🟢 TELEFONE: /tel
63984367346\n\n[ FOTO (2) ]\n\n🟢 FOTO RJ:\n/fotope 11374317411\n/fotorj 11976388732\n\n • [ NOME (1) ] •\n\n🟡 NOME: /nome Luis Henrique\n\n• [ SCORE (1) ] •\n\n🔴 SCORE: /score 05344565828\n\n• [ VEÍCULOS (1) ] •\n\n🔴 PLACA: /placa OGT0458\n\n• [ GERAIS (4) ] •\n\n🟢 CNPJ: /cnpj 053445628/72628\n🟢 CEP: /cep 70040010\n🟢 BIN: /bin 498408\n🔴 IP: /ip 204.152.203.157\n🟢 IMEI: /imei 358297063613954\n🟢 OPERADORA: /op 5582988279194\n🟢 IA BING: /ia test\n\n⚡️ Use os comandos em Grupos e no Privado do Bot!\n\n👤 Suporte: @gringomdz\n━━━━━━━━━━━━━━━━━''',
      call.message.chat.id,
      call.message.message_id,
      reply_markup=back_markup())

  if call.data == 'back':
    return bot.edit_message_text(
      f'Bem-vindo(a) ao MdzSearch, o bot mais commpleto de consultas do telegram!\n\n🌟✨ Aqui você pode descobrir informações incríveis sobre pessoas, como nome, cpf, idade, cidade, redes sociais e muito mais.\n\n🕵️‍♀️🔍 Sinta-se à vontade para explorar todas as nossas utilidades e divirta-se!\n\n© By: @gringomdz',
      call.message.chat.id,
      call.message.message_id,
      reply_markup=start_markup())

  if call.data == 'perfil':
    return bot.edit_message_text(
      f'👤 | Para você ver as suas informaçõe, digite /perfil no chat!',
      call.message.chat.id,
      call.message.message_id,
      reply_markup=back_markup())

  if call.data == "parceria":
    return bot.edit_message_text(
      "⚠️ ATENÇÃO!!!, DESEJA FECHAR PARCERIA COM OS PROPRIETARIO DESTE BOT COM ALGUMA AJUDA RELACIONADA A API'S, PLANOS DE DIVULGAÇÕES, ENTRE OUTROS? CHAME NO @ ABAIXO QUE BREVEMENTE NOSSA EQUIPE IRÁ TE RESPONDER!\n\n✅ NÃO ME CHAME NO PRIVADO SE NÃO FOR FECHAR NADA! CHAMOU NÃO DEU A IDEIA PRIORITARIA BLOCK + SPAM!\n\n✅ NOSSA EQUIPE VENDE VARIOS TIPOS DE SOURCE, IREI CITAR ALGUMAS AQUI EM BAIXO:\n\n💳 CC AUXILIAR\n💳 CC FULL\n💳 CONSULTAVEIS\n💳 CONSULTADAS\n🎟 LOGIN\n🪪 DOCUMENTOS\n🔍 CONSULTAS\n🔐 CHECKERS\n\n✅ TEMOS VARIAS STORES ATIVAS NESSE EXATO MOMENTO UMA DELAS ESTA OPERANDO NO TOKEN DO: \n\n© By: @gringomdz",
      call.message.chat.id,
      call.message.message_id,
      reply_markup=back_markup())    
  
      

print("Estou ON!!")
bot.infinity_polling()









#BY @MDZUP / @GRINGOMDZ