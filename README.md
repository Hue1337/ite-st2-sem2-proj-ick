# <font color=lightblue>Sejfy biometryczne</font>
---
## Opis projektu 

Aplikacja szyfrująca wybrane foldery, nazywane **sejfami**. Odblokowanie sejfu następuje poprzez uwierzytelenienie użytkownika metodą biometryczną.  

### <font color=grey>Kamienie milowe</font>

| \#  | Milestone                                     | Terminy |
| --- | --------------------------------------------- | ------- |
| M1  | Analiza, architektura i rdzeń kryptograficzny |         |
| M2  | Moduł rozpoznawania twarzy                    |         |
| M3  | Integracja biometrii z sejfami                |         |
| M4  | Moduł rozpoznawania głosu i MFA               |         |
| M5  | GUI, Dokumentacja                             |         |
## Opis kamieni milowych

### <font color=grey>M1 - Analiza, architektura i rdzeń kryptograficzny</font>

**Cel:** działający mechanizm zarządzania sejfami, tymczasowo zabezpieczany hasłem.

**Informacje:**
- Wybór platformy i technologii
- Model kluczy:
	- każdy sejf posiada własny klucz
	- DEK - szyfrowany kluczem głównym (KEK)
	- KEK jest chroniony hasłem przez *Agron2id* alboi przez magazyn systemowy (TPM/DPAPI, Keychain, Android Keystore)
- Format sejfu:
	- zaszyfrowane pliki, metadane, nonce, tag uwierzytelniajacy


### <font color=grey>M2 - Moduł rozpoznawania twarzy</font>

**Cel:** Rejestracja i weryfikacja użytkownika.

**Informacje:**
- Detekcja twarzy (OpenCV, MediaPipe) i ekstrakcja wektora cech (embedding)
- Rejestracja:
	- kilka ujęć, uśredniony wzorzec zapisany w postaci zaszyfrowanej, nigdy surowe zdjęcia
	- alternatywnie rejestracja poprzez wykorzystanie kamery i ruch głowy użytkownika w konkretny sposób umożliwiający skan
- Weryfikacja:
	- odległość kosinusowa i próg decyzyjny
	- detekcja żywotności

### <font color=grey>M3 - Integracja biometrii z sejfami</font>

**Cel:** Udana weryfikacja biometryczna zwalnia KEK i otwiera sejf.

**Informacje:**
- Po pozytywnej weryfikacji aplikacja pobiera KEK z bezpiecznego magazyny, odsyfrowuje DEK i odblokowuje sejf.
- Metoda awaryjna:
	- master password
	- klucz odzyskiwania generowany przy tworzeniu sejfu
- Limity prób, logi, automatyczna blokada sejfu po bezczynności.

### <font color=grey>M4 - Moduł rozpoznawania głosu i MFA</font>

**Cel:** Weryfikacja użytkownika na podstawie jego głosu i MFA.

**Informacje:**
- Weryfikacja mówcy.
- Fraza losowa wyświetlana na ekranie (challenge-response) - utrudnienie ataku nagraniem.
- Polityka per sejf:
	- twarz lub głos, twarz i głos albo fuzja wyników z wagami.

### <font color=grey>M5 - GUI, dokumentacja i testy</font>

**Cel:** Finalna wersja aplikacji, gotowa do oddania.

**Informacje:**
- Interfejs:
	- Lista sejfów
	- Kreator rejestracji biometrii
	- Podgląd z kamer 
	- Ustawienia polityk
- Dokumentacja:
	- Instrukcja użytkownika
	- Opis bezpieczeństwa
	- Opis ograniczeń
	- Prezentacja
- Testy:
	- Bezpieczeństwa
	- Jednostkowe
	- Logic faws


## Uwagi
- [ ] Czyszczenia pamieci podrecznej
- [ ] Automatyzacja zabezpieczen - uzytkownik moze zapomniec o czyms
