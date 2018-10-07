print("Money");
print("Determina il numero minimo di banconote.");

money = input("\nImporto (dollari):");
x = int(money);

if x < 0:
    print("Si prega si inserire un numero positivo");

else:
    b20 = x // 20;
    x -= b20 * 20;

    b10 = x // 10;
    x -= b10 * 10;

    b5 = x // 5;
    x -= b5 * 5;

    b1 = x;

print("\nbiglietti da $20: ", b20);
print("\nbiglietti da $10: ", b10);
print("\nbiglietti da $5: ", b5);
print("\nbiglietti da $1: ", b1);
