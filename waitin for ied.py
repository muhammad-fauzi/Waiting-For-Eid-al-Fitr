
print (3*"="+"Menunggu Idul Fitri"+3*"="+"\n")

#1. gw pengen si user input tanggal
#2. stlh tanggal diinput,kode nampilin hari dan tanggal
#3. kode nampilin perkiraan hari dan tgl idul fitri
#4. kode nampilin sisa hari dan waktu menuju idul fitri

import datetime 

#input tanggal
inputHari = input("masukkan tanggal (dd-mm-yy): ") #string

formatTanggal = datetime.datetime.strptime(inputHari,"%d-%m-%Y") #diubah ke tanggal

namaHari = {
1 : "Senin",
2 : "Selasa",
3 : "Rabu",
4 : "Kamis",
5 : "Jumat",
6 : "Sabtu",
7 : "Minggu"
}

print ("\n"+f'sekarang hari: {namaHari[formatTanggal.isoweekday()]}')
print (f'tanggal: {formatTanggal.strftime("%d-%m-%Y")}')

print ("\n"+3*"="+"Perkiraan Idul Fitri"+3*"="+"\n")

formatIed = datetime.datetime (2026,3,21)
print ("\n"+f'Perkiraan Ied: {namaHari[formatIed.isoweekday()]}, {formatIed.strftime ("%d-%m-%Y")}')

prediksiHari = datetime.date(2026,3,21)
formatPrediksi = formatTanggal.date()

sisaHari = prediksiHari - formatPrediksi

print ("\n"+f"Sisa hari menuju Idul Fitri : {sisaHari.days} hari")
