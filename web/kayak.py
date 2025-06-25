from numpy.ma.core import masked
from selenium.webdriver.common.by import By
import time
from components.driver_browser import Browser
from datetime import datetime, timedelta
from web.components.web_page import WebPage

class Kayak(Browser, WebPage):
    def __init__(self):
        # Inicializa la clase base
        self.initialize_browser()

    def search_dates(self):
        fecha_inicial = '2026-01-24'
        rango_dias = 10
        rango_vacaciones = 16
        formato = "%Y-%m-%d"
        fecha_inicial_cf = datetime.strptime(fecha_inicial, formato)
        resultados = []

        for i in range(rango_dias):
            fecha_inicio = fecha_inicial_cf + timedelta(days=i)
            fecha_final = fecha_inicio + timedelta(days=rango_vacaciones)


            print(f'>>> Del día {fecha_inicio.strftime("%Y-%m-%d")} al {fecha_final.strftime("%Y-%m-%d")}({i+1})\n ')
            self.extract_flights(fecha_inicio,fecha_final,resultados)
            print('\n\n')

        print(resultados)


    def extract_flights(self, inicio: datetime, final: datetime, resultados):
        url = f'https://www.kayak.com.mx/flights/LAX-TYO/{inicio.strftime("%Y-%m-%d")}/{final.strftime("%Y-%m-%d")}/2adults?ucs=1l5lyfb&sort=bestflight_a'
        self.driver.get(url)
        self.wait_page(4)

        vuelos = self.find_all('.Fxw9-result-item-container')

        for i, vuelo in enumerate(vuelos):
            if i < 5:
                vuelo_ida=[]
                vuelo_vuelta=[]
                mas_1_ida=[]
                mas_1_vuelta=[]

                horarios = self.find_all('.c3J0r-container', vuelo)
                for j, horario in enumerate(horarios):
                    info_vuelo = self.find_all('.c3J0r-container > div:nth-of-type(3)', horario)
                    if j == 0:
                        vuelo_ida = info_vuelo[0].text.split('\n')
                        mas_1_ida = vuelo_ida[1] if len(vuelo_ida) == 5 else ''

                    if j == 1:
                        vuelo_vuelta = info_vuelo[0].text.split('\n')
                        mas_1_vuelta = vuelo_ida[1] if len(vuelo_ida) == 5 else ''

                    precio = self.find_all('.e2GB-price-text-container', vuelo)[0].text.split('\n')
                    aerolineas = self.find_all('.J0g6-operator-text', vuelo)[0].text.split('\n')

                    if len(vuelo_ida) > 0 and len(vuelo_vuelta) > 0:
                        print(
                            f'{aerolineas} {vuelo_ida[0]}{mas_1_ida} - {vuelo_ida[-3]} // {vuelo_vuelta[0]}{mas_1_vuelta} - {vuelo_vuelta[-3]} >> {precio[0]} x Persona')
                        resultados.append({
                            "fecha_inicio": inicio.strftime("%Y-%m-%d"),
                            "fecha_final": final.strftime("%Y-%m-%d"),
                            "aerolinea": aerolineas,
                            "ida": vuelo_ida,
                            "vuelta": vuelo_vuelta,
                            "precio": precio,
                        })

        self.driver.get(url)
        self.wait_page(2)

    def close(self):
        self.driver.quit()


kayak = Kayak()  # Inicializa Buyee
kayak.search_dates()