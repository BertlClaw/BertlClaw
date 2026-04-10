# Rolling 5000 Sitemap Strategy

## Ziel
Die große Sitemap-/URL-Landschaft kontrolliert, sicher und nachvollziehbar live bringen – ohne erneut tausende tote oder qualitativ schwache Seiten auszuliefern.

## Grundsatz
Nicht alles gleichzeitig live schieben.
Nur Seiten deployen und in Sitemaps aufnehmen, die:
- lokal vorhanden sind
- technisch valide sind
- nicht thin oder leer sind
- in ein sinnvolles Cluster passen
- intern sinnvoll verlinkt sind

## Sicherheitsstufen

### Stufe 0 — Inventar
- Masterliste aller gemappten URLs in `data/sitemap-master.csv`
- JSON-Spiegel in `data/sitemap-status.json`

### Stufe 1 — Technische Validierung
Script:
- `scripts/validate-sitemap-pages.py`

Prüft pro Seite:
- Datei existiert
- Title vorhanden
- Meta Description vorhanden
- H1 vorhanden
- Canonical vorhanden
- Text nicht zu dünn

Ausgaben:
- `data/sitemap-validation.json`
- `data/sitemap-validation.csv`

### Stufe 2 — Cluster-Sitemaps
Script:
- `scripts/build-sitemap-index.py`

Erstellt gestufte Sitemaps:
- `sitemap-core.xml`
- `sitemap-blog.xml`
- `sitemap-cluster_or_other.xml`
- `sitemap-index.xml`

## Rollout-Logik

### Phase A — Bestehenden Live-Bestand sichern
- aktuelle URL-Landschaft inventarisieren
- nur validierte Seiten im gestuften Sitemap-Modell abbilden

### Phase B — Neue Wellen erzeugen
Neue Seiten immer so aufnehmen:
1. lokal bauen
2. validieren
3. Cluster-Sitemap neu generieren
4. deployen
5. live prüfen
6. erst dann Search Console / Indexierung

### Phase C — 5000er Ausbau
Wenn die ursprünglich große URL-Landschaft wieder aufgebaut werden soll:
- nicht in einem Schub
- sondern nach Clustern / Märkten / Seitentypen
- jede Welle braucht Validierung + Liveprüfung

## Freigabekriterien für neue Seiten
Eine Seite darf erst in die Sitemap, wenn:
- HTML-Datei vorhanden
- technisch valide
- kein Thin Stub
- sinnvoller CTA vorhanden
- Canonical korrekt
- interne Verlinkung vorhanden
- keine offensichtlichen Platzhalter / TODO-Reste

## Sofort einsetzbare Artefakte
- `data/sitemap-master.csv`
- `data/sitemap-status.json`
- `data/sitemap-validation.json`
- `data/sitemap-validation.csv`
- `sitemap-index.xml`
- `sitemap-core.xml`
- `sitemap-blog.xml`
- `sitemap-cluster_or_other.xml`

## Nächste sinnvolle Schritte
1. `robots.txt` später auf `sitemap-index.xml` umstellen, sobald Live-Deploy sicher aktualisiert
2. neue Seiten nur noch über Validierungs-Pipeline aufnehmen
3. Clusterweise Ausbauplanung definieren (AT, DE, CH, Berufe, Spezialseiten)
4. pro Welle 20–100 Seiten statt chaotischer Massenfreigabe

## Wichtig
Diese Strategie ist die sichere Basis für einen großen Ausbau. Sie ist **nicht** dasselbe wie blind 5000 Seiten live zu behaupten. Sie sorgt dafür, dass 5000 Seiten am Ende tatsächlich funktionsfähig, prüfbar und indexierbar live sein können.
