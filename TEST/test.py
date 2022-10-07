info = {'username': 'abir', 'follower_count': '12',
        'us1': 'dabir', 'follower_count1': '16'}
# print("Username :", z['username'],"-", "Profile :", f"https://instagram.com/{z['username']}" )

# with open('info1.txt', 'a') as f:
#     f.write("[+]")
#     f.write(" Username:")
#     f.write(f" {info['username']}")
#     f.write(" [-] ")
#     f.write("Followers: ")
#     f.write(f"{info['follower_count']} ")
#     f.write("\t [-] Profile:")
#     f.write(f" https://instagram.com/{info['username']}")
#     f.write("\n")
#     f.close()
print('Username:', info['username'], " "*(20-len(info['username'])), "Followers:", info['follower_count'])
print('Username:', info['us1'], " "*(20-len(info['us1'])), "Followers:", info['follower_count1'])
