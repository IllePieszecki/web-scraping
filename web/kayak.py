from numpy.ma.core import masked
from selenium.webdriver.common.by import By
import time
from components.driver_browser import Browser
from datetime import datetime, timedelta
from web.components.web_page import WebPage
from csv import writer
from pathlib import Path

class Kayak(Browser, WebPage):
    def __init__(self):
        # Inicializa la clase base
        self.initialize_browser()
        rows = []

    def search_dates(self):
        rows = []
        fecha_inicial = '2026-01-13'
        rango_busqueda = 2
        rango_vacaciones = 16
        formato = "%Y-%m-%d"
        fecha_inicial_cf = datetime.strptime(fecha_inicial, formato)
        resultados = []

        for i in range(rango_busqueda):
            fecha_inicio = fecha_inicial_cf + timedelta(days=i)
            fecha_final = fecha_inicio + timedelta(days=rango_vacaciones)


            print(f'>>> Del día {fecha_inicio.strftime("%Y-%m-%d")} al {fecha_final.strftime("%Y-%m-%d")}({i+1})\n ')
            self.extract_flights(fecha_inicio,fecha_final,resultados, rows)
            print('\n\n')

        print(resultados)

        self.write_csv(
            rows,
            "files/datos_vuelos.csv",
            header=["fecha_inicio", "fecha_final", "aerolinea", "ruta ida", "horario ida", "ruta vuelta", "horario vuelta", "precio"]
        )


    def extract_flights(self, inicio: datetime, final: datetime, resultados, rows):
        # url = f'https://www.kayak.com.mx/flights/MTY-TYO/{inicio.strftime("%Y-%m-%d")}/{final.strftime("%Y-%m-%d")}/3adults?fs=stops=1&ucs=1l5lyfb&sort=bestflight_a'
        url = f'https://www.kayak.com.mx/flights/LAX-TYO/{inicio.strftime("%Y-%m-%d")}/{final.strftime("%Y-%m-%d")}/3adults?fs=stops=0&ucs=1l5lyfb&sort=bestflight_a'
        self.driver.get(url)
        self.wait_page(5)
        self.wait_for_element('div.skp2-hidden')

        vuelos = self.find_all('.Fxw9-result-item-container')

        for i, vuelo in enumerate(vuelos):
            if i < 5:
                vuelo_ida=[]
                vuelo_vuelta=[]
                mas_1_ida=[]
                mas_1_vuelta=[]
                horario_ida = []
                horario_vuelta = []
                ruta_ida = []
                ruta_vuelta = []

                horarios = self.find_all('.c3J0r-container', vuelo)
                for j, horario in enumerate(horarios):
                    info_vuelo = self.find_all('.c3J0r-container > div:nth-of-type(3)', horario)
                    if j == 0:
                        vuelo_ida = info_vuelo[0].text.split('\n')
                        mas_1_ida = vuelo_ida[1] if len(vuelo_ida) == 5 else ''
                        horario_ida = vuelo_ida[0] + mas_1_ida
                        ruta_ida = vuelo_ida[-3] + " - " + vuelo_ida[-1]

                    if j == 1:
                        vuelo_vuelta = info_vuelo[0].text.split('\n')
                        mas_1_vuelta = vuelo_vuelta[1] if len(vuelo_vuelta) == 5 else ''
                        horario_vuelta = vuelo_vuelta[0] + mas_1_vuelta
                        ruta_vuelta = vuelo_vuelta[-3] + " - " + vuelo_vuelta[-1]

                    precio_ext = self.find_all('.e2GB-price-text-container', vuelo)[0].text.split('\n')
                    precio = precio_ext[0]
                    aerolineas_ext = self.find_all('.J0g6-operator-text', vuelo)[0].text.split('\n')

                    if len(aerolineas_ext)>1:
                        aerolineas = " - ".join(aerolineas_ext)
                    else :
                        aerolineas = aerolineas_ext[0]

                    if len(vuelo_ida) > 0 and len(vuelo_vuelta) > 0:
                        print(
                            f'{aerolineas_ext} {vuelo_ida[0]}{mas_1_ida} - {vuelo_ida[-3]} // {vuelo_vuelta[0]}{mas_1_vuelta} - {vuelo_vuelta[-3]} >> {precio_ext[0]} x Persona')
                        rows.append([
                            inicio.strftime("%Y-%m-%d"),
                            final.strftime("%Y-%m-%d"),
                            aerolineas,
                            ruta_ida,
                            horario_ida,
                            ruta_vuelta,
                            horario_vuelta,
                            precio,
                        ])

        self.driver.get(url)
        self.wait_page(2)


    def write_csv(self, rows, path, header=None):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open('w', newline='', encoding='utf-8-sig') as f:
            w = writer(f)
            if header:
                w.writerow(header)
            w.writerows(rows)

    def close(self):
        self.driver.quit()


kayak = Kayak()  # Inicializa Buyee
kayak.search_dates()