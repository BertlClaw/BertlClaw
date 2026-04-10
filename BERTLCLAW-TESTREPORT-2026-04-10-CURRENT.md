# BertlClaw Current State Report — 2026-04-10

## Zweck
Aktueller Gesamtstand nach mehreren Sanierungs- und Optimierungsrunden für BertlClaw.

Dieser Report ersetzt nicht alle älteren Notizen, ist aber der **verlässlichere Ist-Zustand** für Entscheidungen ab jetzt.

---

## Executive Summary
BertlClaw ist im Verlauf dieser Session spürbar stabiler, glaubwürdiger und kommerziell verwertbarer geworden.

### Was sich deutlich verbessert hat
- zentrale Broken-Link-Probleme wurden bereinigt
- `faq.html` wurde hergestellt
- `robots.txt` wurde auf die Live-Sitemap korrigiert
- die Sitemap wurde lokal stark bereinigt und auf echte Seiten reduziert
- Reminder-/Audit-Tools wurden aus Git rekonstruiert und wieder lauffähig gemacht
- mehrere Kernseiten wurden conversion-stärker formuliert
- Trust-/Entity-Signale wurden auf wichtigen Seiten verstärkt
- CTA-Tracking wurde auf zentrale Einstiegs- und Angebotsseiten ausgerollt

### Was weiterhin offen ist
- Live-Push auf GitHub ist weiterhin durch Authentifizierung blockiert
- Teile des sichtbaren Live-Zustands auf `bertlclaw.at` können deshalb noch hinter dem lokalen Stand zurückliegen
- Reminder-Audit zeigt historische fehlende Hourly-Slots
- der ältere Testreport `BERTLCLAW-TESTREPORT-2026-04-10.md` ist teilweise überholt

---

## Was wurde in dieser Runde getestet und verbessert?

## 1. Technische Basis
### Geprüft
- interne Broken Links
- `robots.txt`
- `sitemap.xml`
- Reminder-/Audit-Skripte
- wichtige HTML-Seiten auf Trust-/Canonical-/CTA-Konsistenz

### Aktueller Status
- interne Broken Links: **0**
- `robots.txt`: lokal korrekt auf `https://bertlclaw.at/sitemap.xml`
- Reminder-Skripte: wiederhergestellt und ausführbar
- `faq.html`: existiert wieder lokal

### Bewertung
**Deutlich verbessert.**
Die technische Basis ist lokal wesentlich stabiler als zu Beginn.

---

## 2. Conversion- und Vertrauensverbesserungen
### Überarbeitet wurden insbesondere
- `index.html`
- `services.html`
- `preise.html`
- `kontakt.html`
- `proof.html`
- `erstgespraech.html`
- `landingpages.html`
- `landingpage-sprint.html`
- `positionierung-website-texte.html`
- `digital-clarity-setup.html`
- `use-cases.html`
- `ueber-bertlclaw.html`

### Typische Verbesserungen
- CTA-Texte konkreter gemacht
- mehr Trust-Signale nahe der CTA eingebaut
- Hürden vor Kontakt gesenkt
- "2–4 Sätze genügen"-Logik mehrfach verstärkt
- "kein Pflicht-Call" / "ehrliche Einordnung" / "direkt mit Dominic" sichtbarer gemacht
- Proof, Services und Kontakt besser untereinander verlinkt

### Bewertung
**Stark verbessert.**
Die Seiten sind jetzt insgesamt weniger diffus und anfragefreundlicher.

---

## 3. Entity- und Betreibervertrauen
### Geprüft / verbessert
- `ueber-bertlclaw.html`
- `use-cases.html`
- mehrere Angebotsseiten
- strukturierte Daten / Canonical-Signale auf mehreren Seiten

### Verbesserungen
- Betreiberklarheit gestärkt
- Dominic Reisenbichler, MSc. sichtbarer als reale verantwortliche Person
- BertlClaw klarer als Projektmarke einer realen Person positioniert
- mehrere GitHub-basierte Canonical-/OG-Signale auf Live-Domain korrigiert

### Bewertung
**Wichtig verbessert.**
Gerade für skeptische Besucher und Google-Entity-Signale ist das ein echter Fortschritt.

---

## 4. Tracking / Messbarkeit
### Ergänzt
CTA-Tracking über `data-track-click` auf zentralen Seiten:
- `index.html`
- `kontakt.html`
- `use-cases.html`
- `ueber-bertlclaw.html`
- `landingpage-sprint.html`
- `positionierung-website-texte.html`
- `digital-clarity-setup.html`
- `erstgespraech.html`
- `proof.html` (bereits vorhanden / ausgebaut)
- `services.html` (bereits vorhanden)
- `preise.html` (bereits vorhanden)

### Warum relevant
Damit lassen sich künftig echte Funnel-Fragen beantworten:
- Welche Seite erzeugt Anfragen?
- Welche Trust-Seite wird wirklich genutzt?
- Gehen Leute eher auf Proof, Erstgespräch, Services oder Kontakt?
- Welche Angebotsseite zieht am stärksten?

### Bewertung
**Deutlich verbessert.**
BertlClaw ist jetzt wesentlich besser messbar als zuvor.

---

## 5. Sales-/Ops-Unterlagen
### Neu oder relevant vorhanden
- `BERTLCLAW-LEAD-TRACKER.csv`
- `BERTLCLAW-SALES-OPS-CADENCE.md`
- `LEAD-WORKFLOW.md`
- `REPLY-TEMPLATES.md`
- `BERTLCLAW-PROOF-SYSTEM.md`

### Nutzen
- Leads systematisch erfassen
- nächsten Schritt pro Lead erzwingen
- Follow-ups sichtbar machen
- Sales-Rhythmus im Alltag stabilisieren

### Bewertung
**Operativ stark verbessert.**
Nicht nur Website, sondern auch Lead-Bearbeitung wurde substanziell vorbereitet.

---

## Wichtige Ergebnisse nach Themenfeld

## A. SEO / Indexierung
### Positiv
- wichtige Kernseiten lokal technisch sauberer
- `landingpages.html` semantisch gestärkt
- FAQ wieder vorhanden
- Sitemap lokal bereinigt

### Offen
- Search Console muss morgen manuell fortgesetzt werden ab:
  - `https://bertlclaw.at/ueber-bertlclaw.html`
- Live-Rollout der lokalen Verbesserungen ist noch nicht vollständig gesichert, solange GitHub-Push blockiert ist

### Bewertung
**Fortschritt gut, aber noch nicht abgeschlossen.**

---

## B. CRO / Funnel
### Positiv
- Hero-CTAs klarer
- Kontakt-Hürde gesenkt
- Proof besser in Anfragewege eingebunden
- Erstgespräch stärker als risikoarmer Einstieg positioniert
- mehrere Seiten stärker auf schriftlichen Erstkontakt optimiert

### Bewertung
**Klar verbessert.**

---

## C. Vertrauen / Glaubwürdigkeit
### Positiv
- echte Person dahinter sichtbarer
- kein anonymer Funnel / kein Pflicht-Call mehrfach kommuniziert
- ehrliche Absage als positives Vertrauenssignal eingebaut
- Proof-Logik sauberer erklärt

### Bewertung
**Sehr wichtig verbessert.**

---

## D. Technik / Betrieb
### Positiv
- Reminder-Tools wiederhergestellt
- Audit wieder ausführbar
- Logs/State wieder funktionsfähig

### Offen
- historische Hourly-Gaps bestehen weiter
- Taktung sollte später separat gehärtet werden

### Bewertung
**Wieder funktionsfähig, aber noch nicht vollständig gehärtet.**

---

## Bekannte offene Punkte

## 1. Live-Push blockiert
Lokale Änderungen sind vielfach committed, aber nicht sicher live, weil Push auf GitHub aktuell an Auth scheitert.

### Auswirkung
- lokaler Stand besser als möglicher Live-Stand
- manche Live-Checks können noch alte Zustände zeigen

### Priorität
**Hoch.**

---

## 2. Search Console manuell fortsetzen
Dokumentierter nächster Startpunkt:
- `https://bertlclaw.at/ueber-bertlclaw.html`

Danach:
- `landingpages.html`
- `use-cases.html`
- `faq.html`
- `sitemap.xml`

### Priorität
**Hoch.**

---

## 3. Reminder-Schedule härten
Reminder-Audit zeigt fehlende Hourly-Slots früher am Tag.

### Priorität
**Mittel.**

---

## 4. Älteren Testreport nicht mehr blind verwenden
`BERTLCLAW-TESTREPORT-2026-04-10.md` enthält teilweise inzwischen veraltete Aussagen.

### Priorität
**Mittel.**

---

## Konkrete nächste Prioritäten

## Priorität 1
**Live-Push / Deployment lösen**
- damit die Verbesserungen wirklich auf `bertlclaw.at` ankommen

## Priorität 2
**Search Console weiter abarbeiten**
- Start bei `ueber-bertlclaw.html`

## Priorität 3
**Tracking später auswertbar machen**
- sicherstellen, dass GoatCounter-/Event-Logik sauber konsolidiert ist

## Priorität 4
**Lead-Tracker aktiv benutzen**
- jede Anfrage erfassen
- nächste Aktion definieren

## Priorität 5
**Nächste SEO-/Sales-Seiten gezielt ausbauen**
- keine breite Massenproduktion, sondern hochwertige, kommerziell sinnvolle Seiten

---

## Gesamturteil
### Vorher
BertlClaw hatte eine gute inhaltliche Basis, aber:
- zu viele strukturelle Inkonsistenzen
- schwächere Vertrauenssignale
- unklare Funnel-Stellen
- zu wenig Messbarkeit
- kaputte Betriebs-/Reminder-Bausteine

### Jetzt
BertlClaw ist lokal deutlich weiter:
- technischer sauber
- vertrauenswürdiger
- conversion-stärker
- operativ brauchbarer
- messbarer

## Schlussbewertung
**Der lokale Projektzustand ist jetzt insgesamt klar besser und geschäftlich deutlich belastbarer als zu Beginn der Session.**

Der größte verbleibende Hebel ist aktuell nicht mehr primär Copy oder Technik — sondern:
1. **Live bringen**
2. **Search Console weiterziehen**
3. **aus den verbesserten Seiten echte Anfragen und Tracking-Daten gewinnen**
