import random

def main():
    print("Számkitalálós játék!")
    titkos_szam = random.randint(1, 100)
    probalkozasok = 0

    while True:
        try:
            tipp = int(input("Tippelj egy számot 1 és 100 között: "))
            probalkozasok += 1
            if tipp < titkos_szam:
                print("Nagyobb számra gondoltam.")
            elif tipp > titkos_szam:
                print("Kisebb számra gondoltam.")
            else:
                print(f"Gratulálok! {probalkozasok} próbálkozásból kitaláltad a számot.")
                break
        except ValueError:
            print("Kérlek, egy egész számot adj meg!")

if __name__ == "__main__":
    m