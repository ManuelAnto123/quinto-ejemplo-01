while(True):
    print("""
            Bienvenidos al sistema de circunferencia
             __  __                         _ 
            |  \/  | __ _ _ __  _   _  ___ | |
            | |\/| |/ _` | '_ \| | | |/ _ \| |  ♥♥♥♥
            | |  | | (_| | | | | |_| |  __/| |  ♥♥♥♥
            |_|  |_|\__,_|_| |_|\__,_|\___||_|              
    """)
    area = 0
    peri = 0
    print("Area y perímetro de la Circunferencia")
    print("=====================================")
    print()
    radio = float(input("Ingrese radio: "))
    area = 3.14 * radio * radio
    peri = 2*3.14*radio
    print("Mostrando Resultados")
    print("Area      : ",area.__round__(2))
    print("Perimetro : ",peri.__round__(2))
    while(True):
        try: 
            op = int(input("Desea continuar? 1. Si 2. No: ")) 
            if (op==0 or op==1):
                break
            else:
                print("Animal, solo ingresa 1 o 0")
        except:
                print("Caballerín, no letras.")
    if(op==0):
        break
print()
print("Ud a terminado el sistema")
print("Visitame en mi casa")