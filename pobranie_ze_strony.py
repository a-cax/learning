from lxml import html
import requests

#adres strony
url = 'https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne'

#ścieżka do elementu XPATH
xpath_zdr_m = '//*[@id="p_p_id_56_INSTANCE_KuRRUjcNsApi_"]/div/div/div[1]/div/div[2]/div/table[2]/tbody/tr[3]/td[6]/text()'
xpath_cho_m = '//*[@id="p_p_id_56_INSTANCE_KuRRUjcNsApi_"]/div/div/div[1]/div/div[2]/div/table[2]/tbody/tr[3]/td[5]/text()'
xpath_wyp_m = '//*[@id="p_p_id_56_INSTANCE_KuRRUjcNsApi_"]/div/div/div[1]/div/div[2]/div/table[2]/tbody/tr[3]/td[4]/text()'
xpath_ren_m = '//*[@id="p_p_id_56_INSTANCE_KuRRUjcNsApi_"]/div/div/div[1]/div/div[2]/div/table[2]/tbody/tr[3]/td[3]/text()'
xpath_eme_m = '//*[@id="p_p_id_56_INSTANCE_KuRRUjcNsApi_"]/div/div/div[1]/div/div[2]/div/table[2]/tbody/tr[3]/td[2]/text()'


#pobiera stronę
page = requests.get(url)

#parsuje stronę
tree = html.fromstring(page.text)

# wyszukuje interesujący nas element
zdr_m = tree.xpath(xpath_zdr_m)[0].split()
zdr_m = zdr_m[0]
zdr_m = zdr_m.replace(",",".")
zdr_m = float(zdr_m)

eme_m = tree.xpath(xpath_eme_m)[0].split()
eme_m = eme_m[0]
eme_m = eme_m.replace(",",".")
eme_m = float(eme_m)

ren_m = tree.xpath(xpath_ren_m)[0].split()
ren_m = ren_m[0]
ren_m = ren_m.replace(",",".")
ren_m = float(ren_m)

wyp_m = tree.xpath(xpath_wyp_m)[0].split()
wyp_m = wyp_m[0]
wyp_m = wyp_m.replace(",",".")
wyp_m = float(wyp_m)

cho_m = tree.xpath(xpath_cho_m)[0].split()
cho_m = cho_m[0]
cho_m = cho_m.replace(",",".")
cho_m = float(cho_m)

spo_m = eme_m + ren_m + wyp_m + cho_m

# wyświetla wyniki działania
print ('Skladki zdrowotne: ',zdr_m)
print ('Skladki spoleczne: ',spo_m)
print ('Suma skladek: ',zdr_m + spo_m)
