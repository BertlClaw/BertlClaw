# Rolling 5000 Execution Plan

## Ausgangslage
Die rekonstruierte große historische URL-Landschaft umfasst aktuell:
- **5029 URLs** insgesamt
- **68 lokal vorhanden**
- **4961 lokal fehlend**

Davon entfallen auf fehlende Seiten:
- **4933 Landingpage-/Cluster-Seiten**
- **28 sonstige HTML-Seiten**

## Schlussfolgerung
Das ist kein reines Deployment-Problem.
Es ist vor allem ein **Produktions- und Qualitätsproblem**:
Die meisten URLs existieren lokal noch nicht.

## Sichere Rollout-Strategie

### Sicherheitsstufe 1 — Quellwahrheit
Fertig:
- `data/sitemap-master-reconstructed.csv`
- `data/sitemap-master-reconstructed.json`
- `data/sitemap-reconstructed-status.csv`
- `data/sitemap-reconstructed-status.json`

### Sicherheitsstufe 2 — Validierung nur für existierende Seiten
Fertig:
- `scripts/validate-sitemap-pages.py`

### Sicherheitsstufe 3 — Clusterweiser Wiederaufbau
Jetzt notwendig:
1. fehlende URLs nach Mustern gruppieren
2. für jeden Seitentyp Templates definieren
3. pro Welle 20–100 Seiten erzeugen
4. jede Welle validieren
5. erst dann deployen

## Empfohlene Produktionswellen

### Welle A — High intent / money-first
- Unternehmensberater
- Interim Manager
- KI-Berater
- ERP-/IT-/Projektmanager-nahe Seiten

### Welle B — starke DACH-Dienstleistungscluster
- Coaches
- Berater
- Texter
- Webentwickler
- Grafikdesigner
- Finanzberater

### Welle C — breite Longtail-Berufscluster
- restliche Berufe pro Stadt / Region

## Notwendige nächste Artefakte
1. URL-Pattern-Parser
2. Cluster-Generator
3. Template-System pro Beruf / Stadt / Land
4. Wellenplan mit Prioritäten
5. automatische Qualitätssicherung vor Deployment

## Nicht tun
- nicht 4961 Seiten blind generieren und live schieben
- nicht wieder eine Monster-Sitemap ohne Existenzprüfung ausliefern
- nicht alle Cluster gleich priorisieren

## Nächster konkreter Schritt
Ein Generator soll jetzt die 4933 fehlenden Landingpages nach Mustern klassifizieren und priorisieren, damit die erste kontrollierte Produktionswelle vorbereitet werden kann.
