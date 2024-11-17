# Dokumentation

- API wurde in Python entwickelt
- Framework „Flask“ wurde verwendet
    - „pip install flask“ zum Installieren
- Anwendung muss ausgeführt werden
    - über IDE oder
    - „python api.py“
- Anwendung läuft lokal über „http://127.0.0.1:8000“ 

# OWASP-API-Kategorien

## Server-Side Request Forgery
- API enthält Endpunkt „/fetch-url“, der Nutzer ermöglicht, eine URL zu übergeben, welche dann vom Server abgerufen wird
- URL wird nicht validiert
- Angreifer könnte internen Dienst als URL übergeben
- Server ruft möglicherweise sensible Daten ab

## Unrestricted Resource Consumption
- API enthält Endpunkt „/upload“ zum Hochladen von Dateien
- Hat keine Begrenzung für die Größe der hochgeladenen Datei
- Datei wird einfach im Ordner „/uploads“ gespeichert
- Server ist anfällig für DoS-Angriffe

## Security Misconfiguration
- Debug-Modus von Flask ist aktiviert, d.h. detaillierte Fehlerberichte und Stack-Traces werden zurückgegeben
- Es könnten sensible Informationen darin enthalten sein
- Angreifer könnte Infos nutzen, um Schwachstellen zu identifizieren

## Unsafe Consumption of APIs 
- API enthält Endpunkt „/external-api“, der Daten von einer externen API entgegennimmt
- Benutzer muss GET-Anfrage, mit URL von externer API im Body, an diese URL schicken und erhält eine Antwort
- Externe API wird nicht validiert
- Angreifer könnte maliziöse Daten einschleusen