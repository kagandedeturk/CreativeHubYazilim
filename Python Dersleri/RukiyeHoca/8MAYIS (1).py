#!/usr/bin/env python
# coding: utf-8

# In[55]:


import modul_dene
sonuc=modul_dene.cember_cevresi(4)
print(sonuc)


# In[57]:


import modul_dene
sonuc=modul_dene.daire_alanı(4)
print(sonuc)


# In[58]:


from modul_dene import daire_alanı
sonuc=daire_alanı(4)
print(sonuc)


# In[59]:


import kare_ucgen_modul
sonuc=kare_ucgen_modul.kare_alanı(7)
print(sonuc)


# In[60]:


import kare_ucgen_modul
sonuc=kare_ucgen_modul.ücgen_alanı(7,5)
print(sonuc)


# In[61]:


#en sık kullanılan fonskiyonlar modülde cok fazla fonk var
#random uniform fonk
#randint ve randrange
#choice,shuffle ve sample
import random

for i in range(10):
    print(random.random()) #0 ile 1 aralığında ranstgele ondalk sayı üretir


# In[62]:


import random

for i in range(5):
    print(random.uniform(10,30)) #10 ile 30 aralığında ranstgele ondalk sayı üretir, ondalık sayı dikkat


# In[63]:


import random

for i in range(10):
    print(random.randint(1,5)) #normalde 1 dahil 5 değil olur ama ranintte farklı bunların ikisi de dahil


# In[18]:


import random

for i in range(10):
    print(random.randrange(1,10,2)) #üç parametre alıyor. 1 ile başla 1,3,5,7,9 dan random üret


# In[64]:


import random

for i in range(10):
    print(random.randrange(1,10,3)) #belirli bir miktar artıyor #üç parametre alıyor. 1 ile başla 1,3,5,7,9 dan random üret..1 4 7 10. Burda 10 dahil değil


# In[22]:


import random

for i in range(10):
    print(random.randrange(1,10))#ne kadar aratcağı belii değil


# In[25]:


liste=["siyah","beyaz","mor","mavi","yesil","gri","turuncu"]
print(random.choice(liste))  #listeden rastgele eleman seciyor, her sferinde farklı


# In[29]:


liste=["siyah","beyaz","mor","mavi","yesil","gri","turuncu"]
random.shuffle(liste)
print(liste) #listeyi karıştır demek


# In[31]:


liste=["siyah","beyaz","mor","mavi","yesil","gri","turuncu"]
print(random.sample(liste,3))  #verilen listeden istedğin kadar rastgele eleman seçme


# In[54]:


import random
#zar atılınca 1 gelme oalsılığı 1/6 pratikte de böyle mi
#zarı 100 kere atıcan kaç kere 1 geldi

zarlar={1:0,2:0,3:0,4:0,5:0,6:0} #sözlük key ve valuelardan oluşuyor. 1 0 kere var 2 0 kere var

for i  in range(100):
    zar=random.randint(1,6)
    zarlar[zar]+=1
    
for zar in zarlar: #zar keylerin yerine geçiyor i yerinde olna
    print(f"{zar} gelme olasılığı {zarlar[zar]/100}")
    



# In[53]:


import random #6 6 gelme olasılığı

alti_alti=0
deneme_sayısı=0

while True: #benim belirlediğim koşul gerekleşene kadar devam et
    deneme_sayısı=deneme_sayısı+1
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    if zar1==6 and zar2==6:
        alti_alti+=1
    if alti_alti==10:
        print(f"10 kere 6-6  gelmesi için zarlar {deneme_sayısı} kadar atıldı")
        break


# In[ ]:





# In[ ]:




