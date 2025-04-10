try:
    numero_acl = int(input("Introduce el número de ACL IPv4: "))

    if 1 <= numero_acl <= 99 or 1300 <= numero_acl <= 1999:
        print("Es una ACL Estándar.")
    elif 100 <= numero_acl <= 199 or 2000 <= numero_acl <= 2699:
        print("Es una ACL Extendida.")
    else:
        print("El número no corresponde a una ACL IPv4 válida.")
except ValueError:
    print("Por favor, introduce un número válido.")
