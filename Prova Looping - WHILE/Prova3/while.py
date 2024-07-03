#Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o úsuario digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

def main():
    numeros = []
    
    while True:
        numero = int(input("Digite um número (ou 0 para sair): "))
        if numero == 0:
            break
        numeros.append(numero)
        
    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade if quantidade > 0 else 0
    
    print(f"quantidade de números digitados: {quantidade}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média aritmética dos números digitados: {media:.2f}")

if __name__ == "__main__":
    main()        
    
  