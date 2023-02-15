# Python_project - baza filmów i aktorów

# 1. Opis programu
Program służy do zarządzania zbiorem danych filmów oraz aktorów. Użytkownik może dodawać nowe dane, usuwać i modyfikować te już istniejące. Program pobiera dane z odpowiedniego pliku, a następnie wyświetla je użytkownikowi. Dzięki skorzystaniu z biblioteki Tkinter możliwe było stworzenie przejrzystego interfejsu graficznego użytkownika.

Dane przechowywane są w 3 plikach. 
- Plik actor.json przechowuje dane dotyczące aktorów. Przechowywane dane to: id, imię, nazwisko, data urodzenia. 
- Plik movie.json przechowuje dane dotyczące filmów. Przechowywane dane: id, tytuł, reżyser, długość, rodzaj, data produkcji.
- Plik link.json przechowuje id filmu oraz id aktora.

W programie zadeklarowane są 3 listy przechowujące dane z odpowiednich plików:
- my_data_list_m to lista przechowująca dane filmów,
- my_data_list_ma to lista przechowująca dane aktorów,
- my_data_list_lnk to lista przechowująca id aktora oraz filmu potrzebne do wyświetlenia wszystkich filmów, w których grał wybrany aktor.

# 2. Zawartość
- main.py
- actor.json
- movie.json
- link.json
- pliki .png z ikonami

# 3. Funkcjonalności programu:
- wyświetlanie bazy filmów/aktorów,
- dodawaie nowego filmu, aktora lub danych dotyczących powiązania aktora z określonym filmem,
- wprowadzanie zmian w istniejących danych,
- usuwanie wybranych danych.
