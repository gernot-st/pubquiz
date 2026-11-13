# WIR Pub Quiz

Moderationssoftware für das Pub Quiz von **WIR für Eichgraben**: Teams verwalten, Punkte pro Runde eingeben und Zwischen- und Endstände spannend auf dem Beamer präsentieren.

Die App besteht aus einer einzigen HTML-Datei (`PubQuiz.html`), die komplett offline im Browser läuft. Schriften und Logo sind eingebettet, es ist keine Installation nötig.

**Online-Version:** https://gernot-st.github.io/pubquiz/ (für den Abend selbst besser die lokale Datei verwenden, sie läuft ohne Internet)

## Schnellstart

1. `PubQuiz.html` in **Chrome oder Edge** öffnen. Das ist die Moderationsansicht für den Laptop.
2. **„📺 Beamer-Fenster öffnen“** klicken, das Fenster auf den Beamer ziehen und mit Doppelklick oder **F** auf Vollbild schalten.
3. Unter **⚙️ Einstellungen** die Audiodateien für Trommelwirbel und „We are the Champions“ auswählen.

## Funktionen

- **Teams** mit Name und Emoji anlegen, sortieren und löschen. CSV-Import und -Export (`Teamname;Emoji`, UTF-8 mit BOM, Excel-kompatibel). Der Import erkennt außerdem Komma und Tab als Trennzeichen sowie Windows-1252-Kodierung.
- **Punkte** pro Runde eingeben (ganze Zahlen ≥ 0), mit Rundenname (Standard „Runde X“). Die Rundenanzahl ist einstellbar (Standard 4).
- **Zwischenstand**: Titelbild → alle Plätze ab 6 auf einmal → Countdown von Platz 5 bis 1, jeweils mit Trommelwirbel. Bei Gleichstand teilen sich die Teams den Platz.
- **Endstand**: Die Plätze 1–3 müssen eindeutig sein. Bei Gleichstand fordert die App ein Stechen, in dem die Moderation die Reihenfolge festlegt. Der Sieger wird mit Konfetti und „We are the Champions“ aufgedeckt, danach folgt die komplette Endtabelle.
- **Steuerung**: Leertaste, →, Bild↓ oder ein Presenter schalten weiter, ←/Bild↑ zurück. Das funktioniert auch, wenn das Beamer-Fenster den Fokus hat. In der Moderationsansicht gibt es eine Live-Vorschau des Beamers.
- **Sicherung**: Der Spielstand wird automatisch im Browser gespeichert. Zusätzlich gibt es einen JSON-Backup-Export und -Import.

## Projektstruktur

```
PubQuiz.html          fertige App (gebaut, diese Datei verwenden)
Beispiel-Teams.csv    Beispiel für den Team-Import
src/src.html          Quelltext (HTML/CSS/JS) mit Platzhaltern {{FONTS}} und {{LOGO}}
src/build.py          bettet Schriften und Logo ein und erzeugt PubQuiz.html
src/assets/           Logo und Schriften (Montserrat, Nunito – SIL Open Font License)
```

Nach Änderungen an `src/src.html` die App neu bauen:

```bash
python3 src/build.py
```

## Hinweise

- Audiodateien werden nicht mitgeliefert (Urheberrecht) und auch nicht ins Backup exportiert. Sie bleiben aber im Browser gespeichert.
- Für öffentliche Musikwiedergabe ist in Österreich in der Regel die AKM zuständig.
