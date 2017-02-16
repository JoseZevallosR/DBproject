# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:13:36 2017

@author: jose
"""

import sqlite3
import pandas as pd

def tablaCreacion(nombre):
    conn=sqlite3.connect("caudales.bd")
    cursor = conn.cursor()
    cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Niveles_Convencionales (fecha DATE,n1 REAL,
                n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                n24 REAL ,codigo REAL, FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                
    cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Niveles_Automaticos (fecha DATE,n1 REAL,
                n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                n24 REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                
        
        
    cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Aforos (fecha DATE,N REAL,q REAL,area REAL,V REAL,
            ti REAL,tc REAL,td REAL,L REAL,b REAL,K REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
            
        
    cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Alertas (fecha DATE,
             h_ama REAL,h_nar REAL,h_roj REAL,codigo REAL,FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")

    cursor.execute ("""CREATE TABLE IF NOT EXISTS """+str(nombre)+"""_Caudales (fecha DATE,n1 REAL,
                n2 REAL,n3 REAL,n4 REAL,n5 REAL,n6 REAL,n7 REAL,n8 REAL,n9 REAL,n10 REAL,n11 REAL,n12 REAL,
                n13 REAL,n14 REAL,n15 REAL,n16 REAL,n17 REAL,n18 REAL,n19 REAL,n20 REAL,n21 REAL,n22 REAL,n23 REAL,
                n24 REAL ,codigo REAL, FOREIGN KEY(codigo) REFERENCES Maestro(Codigo))""")
                
             
    return True

def tablaMaestro():
    conn=sqlite3.connect("caudales.bd")
    cursor = conn.cursor()
    cursor.execute ("""CREATE TABLE IF NOT EXISTS Maestro (Codigo string,
    Nombre string,DRE string,Sishidro string,
             Cuenca string,rio string,DPTO string,PROV string,
             DISTRITO string,LONG REAL,
             LAT REAL,ALT REAL, Inicio string,ENT string,Q string)""")

def registrar():
    conn = sqlite3.connect("caudales.bd")
    cursor = conn.cursor()
    tabla=pd.read_csv('maestro.csv')
    #tabla.to_sql("Maestro", conn, if_exists='append', index=False)
    

    m,n=tabla.shape
     
    def lt(x,n):
        resultado=[]
        for i in range(n):
            resultado.append(x[i])
        return resultado
    for k in range(m):
        print k
        registro=tuple(lt(tabla.iloc[k,:],n))
        cursor.execute("""INSERT INTO """+ "Maestro"+ """ (Codigo,Nombre,DRE,Sishidro,
              Cuenca,rio,DPTO,PROV,DISTRITO,LONG,LAT,ALT, Inicio,ENT,Q) 
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
             """,registro)
        conn.commit()


def llenado():
    tabla=pd.read_csv('maestro.csv')
    m,n=tabla.shape
    
    for i in range(m):
        #print i
        tablaCreacion(tabla['Nombre'][i].decode('utf8').replace(' ','_'))
        print i
    



def run():
    tablaMaestro()
    registrar()
    llenado()
