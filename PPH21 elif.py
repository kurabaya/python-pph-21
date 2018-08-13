""" Aplikasi Penghitung Pph 21 (using elif statement) - Faizal SF """

attempt = 1
angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lanjut = 'no'

print('Selamat datang di Aplikasi Penghitung Pph 21!')

while attempt == 1 :
    #Input PKP dibulatkan ke bawah menjadi ribuan penuh (Pasal 17 UU Pph)
    def round_down(num, divisor):
        return num - (num%divisor)

    #Filter input PKP agar tidak mengandung karakter selain angka
    def filter_angka(pkp, number) :
        global lanjut
        index = 0
        while index < len(Pkp) :
            if pkp[index] in number :
                lanjut = 'ok'
            else :
                lanjut = 'no'
            index = index + 1
            
    #Filter input karakter kosong
    Pkp = input("\nBerapa PKP anda tahun ini? ")
    if Pkp == '' :
        print('Maaf karakter yang anda masukkan salah. Silakan coba lagi. ')
    else :
        
        #Filter input PKP (lihat : definisi filter_angka)
        daftar = list(Pkp)
        filter_angka(daftar, angka) 
        if lanjut.lower() != 'ok' :
            print('Maaf karakter yang anda masukkan salah. Silakan coba lagi. ')
            attempt = 1
            
        else :
            #Input PKP yang telah berupa int dihitung sesuai tarif pph yang dikenakan
            Ubah_angka = int(Pkp)
            Penghasilan = round_down(Ubah_angka,1000)  #Pembulatan ribuan ke bawah Input PKP
            Tarifawal = 50000000 * 0.05
            Tarifawal2 = 200000000 * 0.15
            Tarifawal3 = 250000000 * 0.25
            if 0 <= Penghasilan < 1000: 
                print("PKP anda kurang dari Rp 1000. Pajak penghasilan anda 0 yang berarti anda hanya dikenakan wajib lapor.")
                attempt = 0
            elif Penghasilan < 0:
                print("Maaf, format angka yang anda masukkan salah.")
                attempt = 0
            elif 1000 <= Penghasilan <= 50000000:
                Tarif1 = 0.05 * Penghasilan
                print("Pajak penghasilan anda tahun ini adalah", int(Tarif1))
                print("Angsuran pajak penghasilan per bulan anda adalah", int(Tarif1 / 12))
                attempt = 0
            elif 50000000 < Penghasilan <= 250000000 :
                Tarif2 = (Penghasilan - 50000000) * 0.15
                print("Pajak penghasilan anda tahun ini adalah", int(Tarifawal + Tarif2))
                print("Angsuran pajak penghasilan per bulan anda adalah", int((Tarifawal + Tarif2) / 12))
                attempt = 0
            elif 250000000 < Penghasilan <= 500000000:
                Tarif3 = (Penghasilan - 250000000) * 0.25
                print("Pajak penghasilan anda tahun ini adalah", int(Tarifawal + Tarifawal2 + Tarif3))
                print("Angsuran pajak penghasilan per bulan anda adalah", int((Tarifawal + Tarifawal2 + Tarif3) / 12))
                attempt = 0
            elif Penghasilan > 500000000 :
                Tarif4 = (Penghasilan - 500000000) * 0.3
                print("Pajak penghasilan anda tahun ini adalah", int(Tarifawal + Tarifawal2 + Tarifawal3 + Tarif4))
                print("Angsuran pajak penghasilan per bulan anda adalah", int((Tarifawal + Tarifawal2 + Tarifawal3 + Tarif4) / 12))
                attempt = 0
            else :
                print('Maaf karakter yang anda masukkan salah. Silakan coba lagi.')
                attempt = 1
                
        #Konfirmasi pengulangan program
        while attempt == 0 :
            answer = input("Apakah anda ingin menghitung Pph 21 lagi? (Y/N) ")
            if answer.lower() == 'y' :
                attempt = 1
            elif answer.lower() == 'n' :
                print('Terima kasih telah menggunakan aplikasi penghitung Pph 21.')
                break
            else :
                print('Maaf, karakter yang anda masukkan salah. Silakan coba lagi. ')
                attempt = 0

        
