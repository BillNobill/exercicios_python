idade = int(input("Digite sua idade: "))
cnh = input("Você possui CNH? (s/n): ").strip().upper()

if idade >= 18 and cnh == "S":
    print("Você pode dirigir.")
elif idade < 18:
    print("Você não pode dirigir por ser menor de idade.")
elif cnh != "S":
    print("Você não pode dirigir por não possuir CNH.")