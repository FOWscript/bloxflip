import os
import time

import cloudscraper as cs
from discord_webhook import DiscordEmbed, DiscordWebhook

from keepalive import keep_alive

webhookkey1 = os.environ['webhookkey']
keep_alive()
webhookurl = f"https://discord.com/api/webhooks/{webhookkey1}"
webhook_enable = True
minimum_amount = 500
ping = "<@&1190896859921788999>"
refresh = 50

if webhook_enable is True:
  webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")

while True:
    try:
      if webhook_enable is True:
        webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")
        print("check")
        scraper = cs.create_scraper()
        r = scraper.get('https://api.bloxflip.com/chat/history').json()
        check = r['rain']
        if check['active'] is True:
            if check['prize'] >= minimum_amount:
                grabprize = str(check['prize'])[:-2]
                prize = (format(int(grabprize),","))
                host = check['host']
                getduration = check['duration']
                created = check['created']
                umduration = getduration + created
                eduration = umduration/1000
                duration = round(eduration)
                if webhook_enable is True:
                    embed = DiscordEmbed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)
                    embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                    embed.add_embed_field(name="Expiration", value=f"<t:{duration}:R>")
                    embed.set_timestamp()
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1179047888261754962/1190910016375500850/image.png?ex=65a38461&is=65910f61&hm=7f118e1c897586dd3de68e01b05d619f8b029b4eab025d63731b2bff87f798e8&")
                    webhook.add_embed(embed)
                    webhook.execute()
                    webhook.remove_embed(0)
                    time.sleep(240)
            else:
                time.sleep(refresh)
        elif check['active'] is False:
            time.sleep(refresh)
    except Exception as e:
        print(e)
        time.sleep(refresh)
