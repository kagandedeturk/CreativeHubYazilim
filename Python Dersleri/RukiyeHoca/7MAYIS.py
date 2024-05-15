#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NORMAL SÖZLÜK GİBİ DÜŞÜNÜNÜ PHYTON KEY VE VALUE DİYOR:

#isim=key
#ali=value
#key=string veya integer olmak zorunda ama value hem string hem liste hem int olabilir.Value herşey olabilir

kisi= {"isim": "ali","yas":"20","cinsiyet":"m","hobiler":["sinema", "konser","yazılım"]}
print(kisi)


# In[2]:


print(kisi["isim"])


# In[3]:


print(kisi["cinsiyet"])


# In[4]:


#eleman değiştirmek istersek
print(kisi)


# In[5]:


#sözlükte eleman güncelleme
kisi["isim"]="Yiğit"
print(kisi)


# In[7]:


#hem isim mesela hem cinsiyet güncellersek(aynı anda iki alan değiştirmek)

kisi.update({"isim":"Ege", "yas":3})
print(kisi)


# In[10]:


#tc numarası eklesek

kisi["id"]=9876543
print(kisi)


# In[11]:


#eğer bu id yi silmek istersek
del kisi["id"]
print(kisi)


# In[12]:


#sözlüğü for döngüüs ile yazdırmak (keyleri yazdırmak)

for x in kisi:
    print(x)


# In[14]:


print(kisi.keys())


# In[13]:


#valuelar yazılıyor
for x in kisi:
    print(kisi[x])


# In[15]:


print(kisi.values())


# In[16]:


print(kisi.items())


# In[18]:


for k in kisi.items():
    print(k)


# In[19]:


# k anahtar v value
for k,v in kisi.items():
    print(k,v)


# In[22]:


print(kisi["id"])


# In[23]:


print(kisi.get("id")) $yoksa o eleman none değerini döndürüyor


# In[24]:


print(kisi.get("hobiler"))


# In[25]:


print(kisi.get("yas")) #varsa değeri verir


# In[26]:


print(kisi.get("id","bulunamadı")) #yoksa böyle verir


# In[27]:


##MODULLER

#COOK KULLANILAN FONKSIYONLARIN BIR ARAYA GETIRMESIYLE OLUŞAN PAKET

#mesela faktöriyel


# In[29]:


import math
sonuc=math.factorial(6)
print(sonuc)


# In[31]:


sonuc=math.sqrt(64)
print(sonuc)


# In[32]:


sonuc=math.fabs(65)
print(sonuc)


# In[37]:


sonuc=math.fabs(-65)
print(int(sonuc))   #int almak istersen böyle


# In[38]:


from math import factorial

sonuc=factorial(4)
print(sonuc)


# In[39]:


from math import factorial,sqrt

sonuc=factorial(6)
print(sonuc)                #burada math modülünün tamamını import etmiyorsun o yzüden mah. yazmıyuorsun


# In[ ]:


from math import*
sonuc=sqrt()
sonuc=factorial()
sonuc=fabs()                   #burada math modülünün tamamını import etmiyorsun o yzüden mah. yazmıyuorsun yıldız ile de kullanbilirsin


# In[4]:


import modul_dene
sonuc=modul_dene.cember_cevresi(4)
print(sonuc)


# In[6]:


import modul_dene
sonuc=modul_dene.daire_alanı(4)
print(sonuc)


# In[10]:


from modul_dene import daire_alanı
sonuc=daire_alanı(4)
print(sonuc)


# In[9]:


#ismi kısaltma

import modul_dene as md
sonuc=md.daire_alanı(4)
print(sonuc)


# In[ ]:


import os
import time
import datetime
import selenium

