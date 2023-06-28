def divisors(n):
    count = 1
    i = 1
    while i <= n/2:
        if n % i == 0:
            count += 1
        i += 1
    return count

gplays = int(input("Qual número gostaria de checar os divisores? "))
print(f"O número {gplays} tem {divisors(gplays)} divisores.")
