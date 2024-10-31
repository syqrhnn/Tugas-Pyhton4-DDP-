status = str(input("""silakan pilih keanggotaan seperti dibawah ini:
GOLD | SILVER | BRONZE
masukkan pilihan anda
= """))

if status.upper() == "GOLD" or status.upper() == "SILVER" :
    print("selamat kamu mendapatkan diskon!")
else :
    print("mohon maaf kamu tidak mendapatkan diskon")