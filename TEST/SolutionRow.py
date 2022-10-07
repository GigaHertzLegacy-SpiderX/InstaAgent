z = """
    [+] Username: mohammad.ali.ruppy [-] Followers: 155 	 [-] Profile: https://instagram.com/mohammad.ali.ruppy
[+] Username: msmorshed77 [-] Followers: 98 	 [-] Profile: https://instagram.com/msmorshed77
[+] Username: sefi_fashion_boutique_official [-] Followers: 6 	 [-] Profile: https://instagram.com/sefi_fashion_boutique_official
[+] Username: ajmir1998 [-] Followers: 6 	 [-] Profile: https://instagram.com/ajmir1998

"""

print(z.replace("[+]", ",[+]").replace("[-]", " "*(20-12)))