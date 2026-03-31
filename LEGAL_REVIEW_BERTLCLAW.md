# BertlClaw – Legal/Compliance Review (AT/DACH, practical, non-lawyer)

Scope reviewed: `index.html`, `impressum.html`, `datenschutz.html`, related CTA/contact pages, Formspree form, WhatsApp/phone/mailto flows, visible scripts.

## Priority findings

### P1 — Datenschutzerklärung is too thin for the actual setup
Current policy names GitHub Pages and briefly mentions Formspree, but does **not** adequately cover the real processing flows visible on the site.

Missing/too vague:
- Formspree as external processor/service provider for the contact form
- categories of data actually sent via the form (`name`, `email`, `topic`, `message`)
- purpose and legal basis of processing (pre-contractual communication / legitimate interest, depending on context)
- transfer to third countries / provider location risk where relevant
- retention / deletion criteria
- WhatsApp contact flow
- phone and email contact flows
- rights info is incomplete: complaint right to Austrian DSB is not mentioned

**Risk:** classic easy-abmahnung / trust issue because the contact setup is visible and the policy does not really explain it.

### P1 — Contact form should reference privacy notice directly at point of collection
The form currently has no privacy notice or acknowledgement next to submit.

**Recommended minimum:** small notice under the button such as:
> Mit dem Absenden stimmst du zu, dass deine Angaben zur Bearbeitung deiner Anfrage verarbeitet werden. Infos in der [Datenschutzerklärung].

Better:
- direct link to `datenschutz.html`
- mention Formspree right there
- optional checkbox if desired for stronger evidence/documentation

### P1 — WhatsApp flow is not covered enough
Multiple pages link to `https://wa.me/436781299919`.

This should be disclosed clearly because clicking it can transfer metadata to WhatsApp/Meta before an actual message exchange and then communication runs via a third-party platform.

**Needed in privacy notice:**
- that WhatsApp is offered as optional contact channel
- that provider data protection terms apply additionally
- recommendation not to send sensitive data via WhatsApp
- legal basis / purpose for handling incoming WhatsApp enquiries

### P2 — Impressum is plausible but should be tightened editorially
What exists now is a decent base (name, postal address, email, content responsibility). Still worth improving for clarity and AT/German-speaking expectations:
- clearly label operator as website owner / media owner / content responsibility in one structured block
- add phone number if this channel is actively offered across the site
- optional but useful: “Unternehmensgegenstand / Angebot” in plain words
- if a business registration / UID / chamber membership / supervisory authority exists, it belongs there; if none exists, do not invent one

No need to add items that do not apply.

### P2 — No visible cookie banner needed *for the current static setup*, but only as long as this remains true
From reviewed HTML there is **no visible non-essential tracking**: no GA, Meta Pixel, GTM, Hotjar, reCAPTCHA, embedded maps/videos, consent tooling, or ad scripts. The chatbot is local JS only and does not appear to store data in cookies/localStorage.

So for the reviewed files:
- **No cookie consent banner appears necessary right now** for the site itself
- but privacy notice should still say that only technically necessary processing via hosting may occur and that no own tracking/cookies are currently used (if true)

Important caveat:
- external links to WhatsApp/mail/phone do **not** by themselves create a cookie banner duty on page load
- if later analytics, YouTube embeds, maps, fonts from third parties, or Meta/Google tools are added, reassess immediately

### P2 — Privacy notice should mention GitHub Pages more concretely
GitHub Pages hosting is named, but too generically.

Should mention in a more concrete way:
- hosting/access logs may be processed for technical delivery and security
- provider is GitHub / GitHub Pages
- link to provider privacy information
- note that this happens even without using the contact form

### P3 — Footer/nav consistency and page hygiene
Some pages and sitemap reference many landing pages. Compliance pages should be easy to find from all pages (already mostly true via footer). Keep:
- `Impressum` and `Datenschutz` in footer on every page
- optional direct privacy link close to WhatsApp CTA areas if that becomes a major channel

## Concrete fixes to implement

### 1) Replace `datenschutz.html` with a fuller version covering actual flows
Suggested structure:
1. Verantwortlicher
2. Hosting über GitHub Pages
3. Server-Logdaten / technische Bereitstellung
4. Kontakt per E-Mail / Telefon
5. Kontakt per WhatsApp (optional, warning re sensitive data)
6. Kontaktformular über Formspree
   - data fields
   - purpose
   - legal basis
   - recipients/processors
   - third-country note if applicable
   - storage duration / deletion criteria
7. Betroffenenrechte incl. complaint to Austrian DSB
8. Stand / version date

### 2) Add short privacy notice below the form in `index.html`
Suggested text:
> Mit dem Absenden des Formulars werden deine Angaben zur Bearbeitung deiner Anfrage an Formspree übertragen und von mir weiterverarbeitet. Details findest du in der Datenschutzerklärung.

Optional checkbox text:
> Ich habe die Datenschutzerklärung zur Kenntnis genommen.

### 3) Update Impressum wording
Suggested additions if true/applicable:
- `Telefon: +43 678 1299919`
- `Medieninhaber und für den Inhalt verantwortlich: Dominic Reisenbichler`
- `Unternehmensgegenstand: Dienstleistungen rund um Landingpages, Website-Texte, Positionierung und digitale Struktur`

Only include registry/VAT/chamber fields if they actually exist.

### 4) Internal rule for future website changes
If any of the following is added, legal review must be repeated before publishing:
- analytics / ads / pixels
- cookie/consent tools
- embedded maps/videos/social widgets
- Calendly or other booking SaaS
- chat widgets with backend/API
- newsletter tools

## Draft wording snippets

### For the form section (`index.html`)
```html
<p class="form-note">
  Mit dem Absenden des Formulars werden deine Angaben zur Bearbeitung deiner Anfrage
  an <strong>Formspree</strong> übertragen und von mir weiterverarbeitet.
  Details findest du in der <a href="datenschutz.html">Datenschutzerklärung</a>.
</p>
```

Optional checkbox:
```html
<label class="privacy-check">
  <input type="checkbox" name="privacy_ack" required />
  Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> zur Kenntnis genommen.
</label>
```

### For `datenschutz.html` WhatsApp paragraph
```html
<p>
  Du kannst optional auch per WhatsApp Kontakt aufnehmen. Dabei erfolgt die Kommunikation
  über WhatsApp Ireland / Meta. Bereits beim Öffnen des WhatsApp-Links können Daten an den
  Anbieter übertragen werden. Bitte übermittle über WhatsApp keine sensiblen Informationen.
</p>
```

## Bottom line
Main risk is **not** cookies right now; main risk is an **underpowered privacy notice** compared to actual contact channels (especially Formspree + WhatsApp). Impressum is mostly fine as a base, but should be made more complete/clean if phone contact is actively advertised.
