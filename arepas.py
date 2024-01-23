agua = int(input("¿Cuántas tazas de agua necesitas? "))
harina = int(input("¿Cuántas tazas de harina necesitas? "))
sal = float(input("¿Cuántas cucharadas de sal necesitas? "))
print (f"{sal} cucharadas son {(sal*1/16)} tazas")
sal_taza = sal*1/16
print (f"Tus arepas necesitan {agua + harina + sal_taza} tazas")
aceite = int (input("¿Cuántas cucharadas de aceite necesitas para cocinar las arepas? "))
print (f"{aceite} cucharadas son {(aceite*1/16)} tazas")
aceite_taza = aceite*1/16
print (f"Necesitas {aceite_taza} tazas de aceite para cocinar tus arepas")
print ("¡Disfruta!")