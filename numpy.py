# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:41:50 2022

@author: Acelya
"""

#Numpy
#Sayısal işlemler ,istatistiksel işlemler için yazılmış içinde bir sürü farklı metod olan bir kütüphanedir.
#import numpy ile import ediyoruz

import numpy as np

array=np.array([1,2,3])
#1*4 vektör--> 1 satır 4 sütündan oluşan bir matris

new_array=np.array([1,2,3,4,5,6,7,8,9,7,5,4,6,3,1,5])
print(new_array.shape)

son=new_array.reshape(4,4)
print(son)
print("shape:",son.shape)
print("dimension:",son.ndim)
print("data type:",son.dtype)
print("size:",son.size)
print("type:",type(son))

np.zeros((3,4)) #Allocation--> Yer ayırtma
zeros=np.zeros((3,4))
zeros[0,0]=5
print(zeros)

np.ones((3,5))
np.empty((2,5))

a=np.arange(10,20,2)
#ilk sayı dahil, son sayı dahil değil,2şer artır
print(a)



b=np.linspace(10,50,20)
print(b)

#%% Numpy Basic Operations


array1=np.array([1,2,3,4,5,6])
array2=np.array([7,8,9,10,11,12])

print(array1+array2)
print(array1*array2)
print(array2/array1)
print(array1**2)


print(np.sin(array1))
#sinüs alma


print(array1<2)


a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,7],[2,5,8]])

#element wise product

print(a*b)
#matrix product, transposu alıyoruz(T)
a.dot(b.T)



a=np.random.random((5,5))


print(a.sum())
print(a.max())
print(a.min())


print(a.sum(axis=0)) #columnları toplar.
print(a.sum(axis=1))#rowları toplar.

print(np.sqrt(a))#karekök
print(np.square(a))#kare

np.add(a,a)



a = np.array([[1,2,3],[4,5,6]])

b = np.array([[1,2,3],[4,5,6]])

a.dot(b.T)



#%%Indexing and Slicing


array=np.array([1,2,3,4,5,6]) # vectör dimension:1(tek boyutlu)

#arrayler listeye benzer, saymaya sıfırdan başlanır.

print(array[0])
print(array[3])

print(array[0:4]) #0 dahil 4. eleman dahil değil.

reverse_array=array[::-1] #arrayi ters çeviriyoruz.
print(reverse_array)


arrayim=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arrayim[1,1])
print(arrayim[:,1]) #: bütün satırları al demektir.
print(arrayim[1,1:4])

print(arrayim[-1,:])
print(arrayim[:,-1])


#%% Shape Manipulation

array_shape=np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten--düz hale getirmek
ar=array_shape.ravel()

new_ar=ar.reshape(3,3) #eski haline getirdik.

arrayT=new_ar.T
print(arrayT.shape)

array5=np.array([[1,2],[3,4],[5,6]])

print(array5.reshape(2,3))
array5.resize(3,2)






#%% Stacking Arrays

#iki arrayi birleştirmek

array1=np.array([[1,2],[5,6]])
array2=np.array([[-8,9],[-7,6]])

#vertical birleştirme
array3=np.vstack((array1,array2))


#horizontal birleştirme
array4=np.hstack((array1,array2))



#%% Convert and Copy Array

liste=[1,2,3,4] #liste

array=np.array(liste) #np.array()

liste2=list(array) #arrayi listeye çevirdik.
#bazı yerlerde listeyle çalışmak numpy arraydan daha faydalı olabiliyor.


#copy
a=np.array([1,2,3])

b=a
c=b

#memoryde hepsi aynı alanda depo ediliyor.
#Yani birinin değeri değişse hepsi değişiyor.


#copy metoduyla , 3ü için 3 farklı alan tahsis edilcek.
#Birinin değeri değişse diğerleri aynı kalır.
d=np.array([8,9,10])
e=d.copy()
f=e.copy()













































