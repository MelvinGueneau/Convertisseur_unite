def convertir_celsius_en_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertir_fahrenheit_en_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertir_kilometres_en_miles(kilometres):
    miles = kilometres * 0.621371
    return miles

def convertir_miles_en_kilometres(miles):
    kilometres = miles / 0.621371
    return kilometres

print("=== Convertisseur d'unités ===")

while True:
    print("\nChoisissez une option :")
    print("1. Conversion degrés Celsius en degrés Fahrenheit")
    print("2. Conversion degrés Fahrenheit en degrés Celsius")
    print("3. Conversion kilomètres en miles")
    print("4. Conversion miles en kilomètres")
    print("5. Quitter")

    choix = input("Entrez le numéro de l'option : ")

    if choix == "1":
        celsius = float(input("Entrez la valeur en degrés Celsius : "))
        fahrenheit = convertir_celsius_en_fahrenheit(celsius)
        print(f"{celsius} degrés Celsius équivaut à {fahrenheit} degrés Fahrenheit.")

    elif choix == "2":
        fahrenheit = float(input("Entrez la valeur en degrés Fahrenheit : "))
        celsius = convertir_fahrenheit_en_celsius(fahrenheit)
        print(f"{fahrenheit} degrés Fahrenheit équivaut à {celsius} degrés Celsius.")

    elif choix == "3":
        kilometres = float(input("Entrez la valeur en kilomètres : "))
        miles = convertir_kilometres_en_miles(kilometres)
        print(f"{kilometres} kilomètres équivaut à {miles} miles.")

    elif choix == "4":
        miles = float(input("Entrez la valeur en miles : "))
        kilometres = convertir_miles_en_kilometres(miles)
        print(f"{miles} miles équivaut à {kilometres} kilomètres.")

    elif choix == "5":
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")


#                                               
#                                                ██████████████                          
#                                        ████████▓▓▓▓██░░░░██▓▓████                      
#                                ████████░░░░░░░░██▓▓██░░░░██▓▓▓▓▓▓██                    
#                            ████░░██▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                        ████░░░░░░░░██▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                      ██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                        
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                            
#                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                
#                          ████████▓▓▓▓▓▓▓▓▓▓▓▓██████                                    
#                                  ████████████           