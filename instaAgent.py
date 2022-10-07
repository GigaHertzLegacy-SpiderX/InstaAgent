from instabot import Bot
from idinfo import idname, idpass

bot = Bot()
bot.login(username=f"{idname}", password=f"{idpass}")

count = 1
follwers = bot.get_user_followers("_mo_rt_al_")
for follower in follwers:
    info = bot.get_user_info(user_id=follower)
    with open('info.txt', 'a') as f:
        f.write("[+]")
        f.write(" Username:")
        f.write(f" {info['username']}")
        f.write(" "*(30-int(str(len(info['username'])))))
        f.write(" [-] ")
        f.write("Followers: ")
        f.write(f"{info['follower_count']} ")
        f.write(" "*(8-len(str(info['follower_count']))))
        f.write("[-] Profile:")
        f.write(f" https://instagram.com/{info['username']}")
        f.write("\n")
        f.close()
        print(f"{count}"
              "[+]", "Username:", info['username'], " "*(30-int(str(len(info['username'])))),
              "[-]", "Followers:", info['follower_count'], " "*(8-len(str(info['follower_count']))),
              "[-]", "Profile :", f"https://instagram.com/{info['username']}"
              )
        count += 1
