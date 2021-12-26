from turtle import forward, right, left, shape
shape("turtle") #kresli zelva

def sestiuhelnik(): #Sestiuhelnik 
    for i in range(6):
        forward(100)
        left(60)

def po_sesti_uhelniku1(): #Zmena postaveni zelvy po prvnim sestiuhelniku
    right(120)

def dalsi_sestiuhelniky(): #Zmena postaveni zelvy po druhem sestiuhelniku az do konce
    right(120)
    forward(100)
    right(60)

for i in range(6): #Kompletni sestaveni obrazce
    sestiuhelnik()
    po_sesti_uhelniku1()
    dalsi_sestiuhelniky()
