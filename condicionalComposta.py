nota1= int(input("Digite a primeira nota"))
nota2= int(input("Digite a segunda nota"))

media = (nota1 + nota2)/2
print (media)

if media >= 6:
    print ("Aprovado")
elif media < 6 and media >= 4:
    print ("recuperação")   
else: 
    print ("reprovado!")   