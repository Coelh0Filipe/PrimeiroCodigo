cont = True

while cont:
    print ("1 para Fahrenheit e 0 para Celsius")
    opcao = int(input("Escolha a temperatura: "))
    
    if opcao == 1:
    
        temperaturaFahrenheit = input("Digite a temperatura em Fahrenheit: ")

        temperaturaCelsius = (int(temperaturaFahrenheit) - 32) * 5 / 9

        print ("A temperatura em Celsius é ", int(temperaturaCelsius),"ºC")

    elif opcao == 0:

        temperaturaCelsius = input("Qual a temperatura em ºC?: ")

        temperaturaFahrenheit = (float(temperaturaCelsius) * 1.8) + 32

        print ("A temperatura em Fahrenheit é: ", int(temperaturaFahrenheit),"ºF")

    else :
        print ("Não válido") 
    
    if input("Deseja continuar? ") != 's':
        cont = False

