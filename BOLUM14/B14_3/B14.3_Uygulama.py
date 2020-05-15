import sys
import json
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from urllib import  request,parse


class HavaraDurumuRapor:
    def __init__(self,root):
        self.root = root
        self.ust_cerceve()
        self.goruntu_cerceve()

    def ust_cerceve(self):
        ustcrcv = Frame(self.root)
        ustcrcv.grid(row=1,sticky='w')
        Label(ustcrcv,text="Yeri Giriniz").grid(row=1,column=1,sticky="w")
        self.girilenYer = StringVar()
        Entry(ustcrcv,textvariable=self.girilenYer).grid(row=1,column=2,sticky="w")
        Button(ustcrcv,text="Getir",command=self.hava_getir_tikla).grid(row=1,column=3,sticky="w")

    def goruntu_cerceve(self):
        goruntucrv = Frame(self.root)
        goruntucrv.grid(row=2,sticky="ew",columnspan=5)
        self.canvas = Canvas(goruntucrv,height="410",width="300",background="Red")
        self.canvas.create_rectangle(5,5,305,415,fill="#000000")
        self.canvas.grid(row=2,sticky="w",columnspan=5)

    def hava_durumu_al(self):
        from tkinter import messagebox
        try:
            anahtar="97d138883b11c68aed3aa69662c5d06e"
            apiurl = f"http://api.openweathermap.org/data/2.5/weather?q={self.girilenYer.get()}&appid={anahtar}"
            data = request.urlopen(apiurl)
            okuData = data.read()
            
            return okuData
        except IOError as hata:
            messagebox.showerror("Api Error",hata)

    def json_dict(self, json_data):
        decoder = json.JSONDecoder()
        decoded_json_data = decoder.decode(json_data.decode("utf-8"))
        flattened_dict = {}
        for key, value in decoded_json_data.items():
            if key == 'weather':
                for ke, va in value[0].items():
                    flattened_dict[str(ke)] = str(va).upper()
                continue
            try:
                for k, v in value.items():
                    flattened_dict[str(k)] = str(v).upper()
            except:
                flattened_dict[str(key)] = str(value).upper()
        return flattened_dict


    def hava_getir_tikla(self):
        if not self.girilenYer.get():
            return
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(5,5,305,415,fill="#000000")
        self.havabilgisi  = self.hava_durumu_al()
        self.havabilgisi  = self.json_dict(self.havabilgisi)
        self.format_data()
        self.ekranda_goster()

    def clear_canvas(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(10, 10, 330, 415, fill='#F6AF06')

    def format_data(self):
        data = self.havabilgisi
        self.isim = data['name']
        self.enlem = self.str2num(data['lat'], 3)
        self.boylam = self.str2num(data['lon'], 3)
        self.ulke = data['country']
        self.zaman = self.time_stamp_to_data(data['dt'])

        self.icon_name = "weatherimages/{}.png".format(data['icon'].lower())
        self.bulutlar = data['all'] + ' %'
        self.gun_dogumu = self.time_stamp_to_time(data['sunrise'])
        self.gun_batimi = self.time_stamp_to_time(data['sunset'])
        self.sicaklik_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp'])), 2) + u' \u2103'
        self.sicaklik_fahrenheit = self.str2num(
            self.kelvin_to_fahrenheit(float(data['temp'])), 2) + u' \u2109'
        self.min_sicaklik_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp_min'])), 2) + u' \u2103'
        self.max_sicaklik_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp_max'])), 2) + u' \u2103'

    def kelvin_to_celsius(self, k):
        return k - 273.15

    def kelvin_to_fahrenheit(self, k):
        return (k * 9 / 5 - 459.67)

    def str2num(self, string, precision):
        return "%0.*f" % (precision, float(string))

    def ekranda_goster(self):
        if not self.havabilgisi:
            messagebox.showerror(
                'Şehir Bulunamadı', "Bulamadık")
            return
        data = self.havabilgisi
        opts = {'fill': 'white', 'font': 'Helvetica 12'}
        self.canvas.create_text(52, 30, text=self.isim, **opts)
        self.canvas.create_text(
            245, 35, text='Enlem    :' + self.enlem, **opts)
        self.canvas.create_text(
            245, 53, text='Boylam: ' + self.boylam, **opts)
        self.canvas.create_text(
            55, 50, text='Ülke : ' + self.ulke, **opts)
        self.canvas.create_text(155, 80, text=self.zaman, **opts)
        self.canvas.create_text(85, 105, text='Şimdi', **opts)
        self.img = PhotoImage(file=self.icon_name)
        self.canvas.create_image(140, 105, image=self.img)
        self.canvas.create_text(85, 155, text='Sıcaklık', **opts)
        self.canvas.create_text(
            87, 175, text=self.min_sicaklik_celcius + ' ~ ' + self.max_sicaklik_celcius, **opts)
        self.canvas.create_text(
            225, 140, text=self.sicaklik_celcius, **opts)
        self.canvas.create_text(
            225, 180, text=self.sicaklik_fahrenheit, **opts)
        self.canvas.create_text(95, 215, text='Nem', **opts)
        self.canvas.create_text(198, 215, text=data['humidity'] + ' %', **opts)
        self.canvas.create_text(77, 235, text='Rüzgar Hızı', **opts)
        self.canvas.create_text(205, 235, text=data['speed'] + ' m/s ', **opts)
        self.canvas.create_text(80, 275, text='Basınç(at.)', **opts)
        self.canvas.create_text(
            225, 275, text=data['pressure'] + ' millibars', **opts)
        if '3h' in data:
            self.canvas.create_text(83, 293, text='Yağmur (Son Üç Saat)', **opts)
            self.canvas.create_text(
                200, 293, text=data['3h'] + ' mm', **opts)  # rain
        self.canvas.create_text(58, 310, text='Bulutlar', **opts)
        self.canvas.create_text(200, 310, text=self.bulutlar, **opts)  # clouds
        self.canvas.create_text(60, 328, text='Gün Doğumu', **opts)
        self.canvas.create_text(200, 328, text=self.gun_dogumu, **opts)
        self.canvas.create_text(59, 343, text='Gün Batımı', **opts)
        self.canvas.create_text(200, 343, text=self.gun_batimi, **opts)
        self.canvas.create_text(159, 378, text='Kaynak :', **opts)
        self.canvas.create_text(
            159, 398,
            text='www.openweathermap.org \n \
            https://www.packtpub.com/web-development/tkinter-gui-application-development-cookbook',
            **opts)

    def time_stamp_to_time(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S'))

    def time_stamp_to_data(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S'))


def main():
    root = Tk()
    HavaraDurumuRapor(root)
    root.mainloop()

if __name__ == "__main__":
    main()