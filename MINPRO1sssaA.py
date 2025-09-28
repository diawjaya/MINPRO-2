d5 = []
d10 = []
d25 = []
d50 = []

akun = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "test", "password": "1234", "role": "admin"},
    {"username": "karyawan", "password": "karyawan", "role": "user"}
]

def login():
    try:
        while True:
            print("|     Login     |")
            username = input("Username: ")
            password = input("Password: ")

            user = next((u for u in akun if u["username"] == username), None)

            if not user:
                print("Username tidak ditemukan")
                continue

            if password == user["password"]:
                print("| Login berhasil |")
                print(f"Role anda: {user['role']}")
                print("\n\n")
                return user["role"]
            else:
                print("| Login gagal |")
            return None
    except EOFError:
        print("Input tidak valid")

    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")
        exit()


def menu():
    while(True):
        print('1. [Masukan Paket]')
        print('2. [Ambil Paket]')
        print('3. [Ganti password akun]')
        print('4. [List Paket]')
        print('5. [Quit]')
        try:
            opsi = int(input("Silahkan Pilih Menu = "))
            if opsi == 1:
                tambah()
            elif opsi == 2:
                ambil()
            elif opsi ==3:
                update()
            elif opsi == 4:
                listbarang()
            elif opsi == 5:
                    print("Dadah ( *・∀・)ノ゛")
                    return True
            else:
                print('Menu tidak tersedia')
        except ValueError:
            print("input angka")
        except EOFError:
            print("Input tidak valid")
        except KeyboardInterrupt:
            print("\nProgram dihentikan paksa")
            exit()
        return False


def tambah():
    try:
        berat = float(input('Beratnya (kg)= '))
        if berat <= 5:
            di5kg = input("Nama barang = ")
            d5.append(di5kg)
            print('[Barang Dimasukan]')
        elif berat <= 10:
            di10kg = input("Nama barang = ")
            d10.append(di10kg)
            print('[Barang Dimasukan]')
        elif berat <= 25:
            di25kg = input("Nama barang = ")
            d25.append(di25kg)
            print('[Barang Dimasukan]')
        elif berat <= 50:
            dia50kg = input("Nama barang = ")
            d50.append(dia50kg)
            print('[Barang Dimasukan]')
        else :
            print('[Barang keberatan]')
    except ValueError:
            print("input angka")

    except EOFError:
            print("Input tidak valid")

    except KeyboardInterrupt:
            print("\nProgram dihentikan paksa")


def listbarang():
    print(" <= 5kg : ",d5," <= 10kg : ",d10," <= 25kg : ",d25," <= 50kg : ",d50)

def ambil():
    try:
        barang =float(input('Beratnya (kg)= '))
        if barang <= 5:
            adi5kg = input("Nama barang = ")
            if adi5kg in d5:
                d5.remove(adi5kg)
                print('[Barang Diambil]')
            else:
                print('Barang tidak ada')
        elif barang <= 10:
            adi10kg = input("Nama barang = ")
            if adi10kg in d10:
                d10.remove(adi10kg)
                print('[Barang Diambil]')
            else:
                print('Barang tidak ada')
        elif barang <= 25:
            adi25kg = input("Nama barang = ")
            if adi25kg in d25:
                d25.remove(adi25kg)
                print('[Barang Diambil]')
            else:
                print('Barang tidak ada')
        elif barang <= 50:
            adia50kg = input("Nama barang = ")
            if adia50kg in d50:
                d50.remove(adia50kg)
                print('[Barang Diambil]')
            else:
                print('Barang tidak ada')
        else:
            print('[Error]')
    except ValueError:
            print("input angka")

    except EOFError:
            print("Input tidak valid")

    except KeyboardInterrupt:
            print("\nProgram dihentikan paksa")


def update():
    try:
        usernames = input("Masukkan username yang ingin diubah password-nya: ")
        user = next((u for u in akun if u["username"] == usernames), None)

        if not user:
            print("Username tidak ditemukan.")
            return
        password_baru = input('Masukkan password baru = ')
        user["password"] = password_baru
        print (akun)

    except EOFError:
        print("Input tidak valid")

    except KeyboardInterrupt:
        print("\nProgram dihentikan paksa")



mulai = login()
if mulai == "admin":
    while True:
        if menu():
            break
elif mulai == "user":
    listbarang()
    exit()