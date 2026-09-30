#!/usr/bin/env python3
"""Generate Dimension Exterior Cleaning static HTML pages from approved copy."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def picture(stem, alt, width, height, class_name=""):
    """WebP + JPG picture markup with absolute asset paths."""
    cls = f' class="{class_name}"' if class_name else ""
    return (
        f'<picture{cls}>'
        f'<source srcset="/assets/images/{stem}.webp" type="image/webp">'
        f'<img src="/assets/images/{stem}.jpg" alt="{alt}" loading="lazy" '
        f'width="{width}" height="{height}">'
        f'</picture>'
    )


def gallery_photo(stem, label, alt, width, height):
    return (
        f'<figure class="gallery-card gallery-card--photo">'
        f'{picture(stem, alt, width, height)}'
        f'<figcaption><span>{label}</span></figcaption>'
        f'</figure>'
    )


def gallery_pair(stem_a, stem_b, label, alt_a, alt_b, width, height):
    return (
        f'<figure class="gallery-card gallery-card--photo gallery-card--pair">'
        f'<div class="pair-grid">'
        f'{picture(stem_a, alt_a, width, height)}'
        f'{picture(stem_b, alt_b, width, height)}'
        f'</div>'
        f'<figcaption><span>{label}</span></figcaption>'
        f'</figure>'
    )


PHONE_DISPLAY = "07494 503865"
PHONE_TEL = "+447494503865"
PHONE_WA = "447494503865"
EMAIL = "joe@dimensioncleaning.co.uk"

HEADER = '''  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <a class="brand-banner" href="/">
      <picture>
        <source srcset="/assets/images/brand-header.webp" type="image/webp">
        <img src="/assets/images/brand-header.jpg" alt="" width="1206" height="393" decoding="async">
      </picture>
      <span class="sr-only">Dimension Exterior Cleaning</span>
    </a>
    <div class="site-nav-bar">
      <div class="container header-inner">
        <a class="brand" href="/">
          <span class="brand-name">Dimension Exterior Cleaning</span>
          <span class="brand-tag">Sheffield &amp; South Yorkshire</span>
        </a>
        <div class="header-actions">
          <a class="btn btn-header-cta" href="/get-a-quote/">Get a quote</a>
          <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">Menu</button>
        </div>
        <nav class="site-nav" id="site-nav" aria-label="Main">
          <a href="/" data-nav="home">Home</a>
          <div class="nav-dropdown">
            <button type="button" aria-expanded="false" aria-haspopup="true">Services <span class="chevron" aria-hidden="true">▾</span></button>
            <div class="dropdown-menu" role="menu">
              <a role="menuitem" href="/gutter-cleaning/" data-nav="gutter-cleaning">Gutters</a>
              <a role="menuitem" href="/soffits-fascias/" data-nav="soffits-fascias">Soffits &amp; fascias</a>
              <a role="menuitem" href="/drive-patio/" data-nav="drive-patio">Drive &amp; patio</a>
              <a role="menuitem" href="/roof-cleaning/" data-nav="roof-cleaning">Roof</a>
            </div>
          </div>
          <a href="/care-plan/" data-nav="care-plan">Care plan</a>
          <a href="/areas/" data-nav="areas">Areas</a>
          <a href="/faq/" data-nav="faq">FAQ</a>
          <a href="/get-a-quote/" data-nav="get-a-quote">Get a quote</a>
          <a href="/contact/" data-nav="contact">Contact</a>
        </nav>
      </div>
    </div>
  </header>'''

FOOTER = f'''  <footer class="site-footer">
    <div class="container footer-inner">
      <div>
        <div class="footer-brand">© Dimension Exterior Cleaning</div>
        <div><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
      </div>
      <ul class="footer-links">
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
  </footer>
  <nav class="mobile-bar" aria-label="Quick actions">
    <a class="mb-call" href="tel:{PHONE_TEL}">Call</a>
    <a class="mb-wa" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">WhatsApp</a>
    <a class="mb-quote" href="/get-a-quote/">Get a quote</a>
  </nav>
  <script src="/assets/js/main.js" defer></script>'''

SITE_ORIGIN = "https://dimensioncleaning.co.uk"
OG_IMAGE = f"{SITE_ORIGIN}/assets/images/path-after.jpg"
LOGO_IMAGE = f"{SITE_ORIGIN}/assets/images/path-after.jpg"

LOCAL_BUSINESS_SCHEMA = f'''{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "{SITE_ORIGIN}/#business",
  "name": "Dimension Exterior Cleaning",
  "description": "Gutter cleaning and exterior cleaning in Sheffield and South Yorkshire. Clear band prices, roof softwash, and a care plan that saves money.",
  "url": "{SITE_ORIGIN}/",
  "telephone": "{PHONE_TEL}",
  "email": "{EMAIL}",
  "image": "{LOGO_IMAGE}",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Sheffield",
    "addressRegion": "South Yorkshire",
    "addressCountry": "GB"
  }},
  "areaServed": [
    {{"@type": "City", "name": "Sheffield"}},
    {{"@type": "AdministrativeArea", "name": "South Yorkshire"}},
    "Worksop", "Dinnington", "Aston", "Mosborough", "Doncaster"
  ],
  "priceRange": "££",
  "makesOffer": [
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Gutter cleaning", "url": "{SITE_ORIGIN}/gutter-cleaning/"}}}},
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Drive and patio cleaning", "url": "{SITE_ORIGIN}/drive-patio/"}}}},
    {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Roof cleaning", "url": "{SITE_ORIGIN}/roof-cleaning/"}}}}
  ],
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "08:00",
    "closes": "19:00"
  }}
}}'''


def page(title, description, nav_id, body, *, schema=False, canonical="/", crumb=None, extra_scripts=""):
    schema_block = ""
    if schema:
        schema_block = f'\n  <script type="application/ld+json">\n{LOCAL_BUSINESS_SCHEMA}\n  </script>'
    header = HEADER
    if nav_id:
        header = header.replace(f'data-nav="{nav_id}"', f'data-nav="{nav_id}" aria-current="page"')
    crumb_html = ""
    if crumb:
        crumb_html = (
            '    <nav class="breadcrumb" aria-label="Breadcrumb">\n'
            '      <div class="container">\n'
            '        <a href="/">Home</a>\n'
            '        <span class="bc-sep" aria-hidden="true">/</span>\n'
            f'        <span aria-current="page">{crumb}</span>\n'
            '      </div>\n'
            '    </nav>\n'
        )
    scripts = extra_scripts or ""
    abs_url = f"{SITE_ORIGIN}{canonical}"
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{abs_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{abs_url}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <link rel="icon" href="/assets/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/assets/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta name="theme-color" content="#ffffff">
  <meta name="color-scheme" content="light only">
  <meta name="supported-color-schemes" content="light">
  <link rel="stylesheet" href="/assets/css/styles.css?v=banner1">{schema_block}
</head>
<body>
{header}
  <main id="main">
{crumb_html}{body}
  </main>
{FOOTER}
{scripts}</body>
</html>
'''


def write(relpath, html):
    path = ROOT / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


# —— HOME ——
home_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Gutter cleaning and exterior cleaning in Sheffield</h1>
        <p class="sub">Clear prices. Proper roof softwash. A care plan that actually saves you money.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary btn-lg" href="/contact/">Book a gutter clean from £50</a>
          <a class="btn btn-secondary btn-lg" href="/care-plan/">See the care plan from £98/year</a>
          <a class="btn btn-secondary btn-lg" href="/get-a-quote/">Get a guide price</a>
        </div>
      </div>
    </section>

    <div class="trust-strip">
      <div class="container">
        <span>Sheffield &amp; South Yorkshire</span><span class="trust-dots">Worksop</span><span class="trust-dots">Dinnington</span><span class="trust-dots">Aston</span><span class="trust-dots">Mosborough</span><span class="trust-dots">Doncaster fringe</span>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <h2>What we do</h2>
        <div class="card-grid">
          <article class="card">
            <h3>Gutters</h3>
            <p>Vac clean from £50. First two downpipes included.</p>
            <p class="mt-1"><a href="/gutter-cleaning/">Gutter cleaning →</a></p>
          </article>
          <article class="card">
            <h3>Care plan</h3>
            <p>Two gutter visits a year. 15% off other services.</p>
            <p class="mt-1"><a href="/care-plan/">Care plan →</a></p>
          </article>
          <article class="card">
            <h3>Drive, patio &amp; roof</h3>
            <p>Measured on site. Roof work is scrape and softwash.</p>
            <p class="mt-1"><a href="/drive-patio/">Drive &amp; patio →</a> · <a href="/roof-cleaning/">Roof →</a></p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Pricing teaser</h2>
        <div class="table-wrap">
          <table class="pricing">
            <thead>
              <tr><th>Home size</th><th>Gutters</th><th>Care plan (year)</th></tr>
            </thead>
            <tbody>
              <tr><td>Small (terrace 1-2 bed)</td><td class="price">£50</td><td class="price">£70</td></tr>
              <tr class="highlight"><td>Medium (semi 2-3 bed)</td><td class="price">£70</td><td class="price">£98</td></tr>
              <tr><td>Large (detached 3-4)</td><td class="price">£100</td><td class="price">£140</td></tr>
              <tr><td>XL (detached 5+)</td><td class="price">£150</td><td class="price">£210</td></tr>
            </tbody>
          </table>
        </div>
        <p class="muted">Full prices on each service page.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="callout">
          <h2>Pay once. Two gutter visits. 15% off other services.</h2>
          <p>Most semis: <span class="price-em">£98 a year.</span></p>
          <a class="btn btn-primary" href="/care-plan/">See how the care plan works →</a>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>How it works</h2>
        <ol class="steps">
          <li>Tell us the job and postcode.</li>
          <li>We confirm a price band or measure on site for drive/roof.</li>
          <li>We turn up, do the work, leave it looking sorted.</li>
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Before &amp; after</h2>
        <p class="muted mb-2">Real jobs from around Sheffield. Gutters, downpipes, path, driveway, conservatory, and roof.</p>
        <div class="gallery">
          {gallery_pair("gutter-before", "gutter-after", "Gutters", "Gutter before cleaning, full of moss and debris", "Gutter after vac cleaning, clear and tidy", 1400, 1866)}
          {gallery_photo("downpipe-blocked", "Downpipe", "Blocked downpipe packed with leaves and sludge", 1200, 1600)}
          {gallery_pair("path-before", "path-after", "Path", "Dirty flagstone path before cleaning", "Cleaned flagstone path after pressure washing", 1200, 1600)}
          {gallery_pair("drive-before", "drive-after", "Driveway", "Dirty herringbone driveway before cleaning", "Cleaned herringbone driveway after pressure washing", 1200, 1600)}
          {gallery_pair("conservatory-before", "conservatory-after", "Conservatory", "Conservatory roof before cleaning, algae on polycarbonate panels", "Conservatory roof after cleaning, clear polycarbonate panels", 1600, 1200)}
          {gallery_photo("roof-scrape", "Roof", "Moss scrape on a terracotta roof", 1200, 1600)}
          {gallery_photo("roof-softwash", "Softwash", "Softwash foam on a pantile roof", 1200, 1600)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Ready for a clean?</h2>
        <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> · Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
    </section>'''

write("index.html", page(
    "Exterior cleaning Sheffield | Dimension Exterior Cleaning",
    "Gutter, roof, driveway and patio cleaning in Sheffield and South Yorkshire. Clear prices, on-site measures and 15% off with the care plan.",
    "home",
    home_body,
    schema=True,
    canonical="/",
))

# —— GUTTER ——
gutter_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Gutter vac cleaning in Sheffield</h1>
        <p class="sub">Cleared gutters and downpipes. Clear band prices. No hidden “call for a quote” games on a standard house.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p>A gutter can look fine from the ground and still be packed with moss, leaves and roof grit. The warning signs are easy to spot: water spilling over the front edge in rain, damp marks below the gutter, staining on the fascia, or a downpipe that stays quiet when the gutter is full. Left alone, overflow can run down brickwork and collect around the base of the house.</p>
        <p>Joe clears the gutter run with a high-reach vacuum, working along the full length rather than just scooping out the worst bit. The vacuum keeps the debris contained and means there is less mess around windows, paths and flower beds. Once the run is clear, he checks the outlets and the first two downpipes included in the standard price. If a downpipe is slow or blocked, he will tell you what he found before any extra work is done.</p>
        <p>This is useful on the tree-lined streets of Sheffield, where autumn leaves can fill a run quickly. We regularly work around S8, S10, S13, S20, S2 and S9, as well as Aston, Mosborough and nearby South Yorkshire homes. The same practical clean works for a terrace, a two-storey semi or a larger detached property. The price is based on the home size and the number of extras, rather than a vague price that changes when we arrive.</p>
        <p>As a guide, standard gutter cleans start at £50 for a small terrace, £70 for a medium semi, £100 for a larger detached home and £150 for an XL property. A conservatory or extension is £15, and extra downpipes after the first two are £10 each. The <a href="/get-a-quote/">quote builder</a> gives you the right price band once you enter your property details. You can also email <a href="mailto:joe@dimensioncleaning.co.uk">joe@dimensioncleaning.co.uk</a> or call <a href="tel:+447494503865">07494 503865</a>.</p>
        <p>If your gutters need attention twice a year, the care plan keeps it simple. You get two gutter visits, six months apart, and 15% off other exterior cleaning while the plan is active. It suits homes with trees nearby or owners who would rather prevent the overflow than wait for the next heavy downpour.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Prices</h2>
        <div class="table-wrap">
          <table class="pricing">
            <thead><tr><th>Home</th><th>Price</th></tr></thead>
            <tbody>
              <tr><td>Small (terrace 1-2 bed)</td><td class="price">£50</td></tr>
              <tr class="highlight"><td>Medium (semi 2-3 bed)</td><td class="price">£70</td></tr>
              <tr><td>Large (detached 3-4)</td><td class="price">£100</td></tr>
              <tr><td>XL (detached 5+)</td><td class="price">£150</td></tr>
            </tbody>
          </table>
        </div>
        <p><strong>Add-ons:</strong> Conservatory or extension +£15. Extra downpipes after the first two +£10 each.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <h2>While we’re up there</h2>
        <p>While we’re up there: soffits and fascias (often twice the gutter price). Windows can go on the same visit. Care plan customers get two gutter cleans a year and 15% off other work.</p>
        <div class="callout-plain mt-3">
          <p><strong>Not ready for a full clean?</strong> Ask for a free gutter check with photos. We’ll show you what’s going on.</p>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Before &amp; after</h2>
        <p class="muted mb-2">What a blocked run and a cleared gutter look like on a real job.</p>
        <div class="gallery gallery--proof">
          {gallery_photo("gutter-before", "Before", "Gutter before cleaning, full of moss and debris", 1400, 1866)}
          {gallery_photo("gutter-after", "After", "Gutter after vac cleaning, clear and tidy", 1400, 1866)}
          {gallery_photo("downpipe-blocked", "Blocked downpipe", "Blocked downpipe packed with leaves and sludge", 1200, 1600)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Book a gutter clean</h2>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-2"><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("gutter-cleaning/index.html", page(
    "Gutter vac cleaning Sheffield | Dimension Exterior Cleaning",
    "Cleared gutters and downpipes. Clear band prices from £50. No hidden call-for-a-quote games on a standard house.",
    "gutter-cleaning",
    gutter_body,
    schema=True,
    canonical="/gutter-cleaning/",
    crumb="Gutter cleaning",
))

# —— SOFFITS ——
soffits_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Soffits and fascias cleaned properly</h1>
        <p class="sub">Usually done with the gutters. Optional windows on the same visit.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p>Black algae and traffic film on white PVC looks worse than dirty gutters. We clean soffits and fascias so the whole eaves line looks finished.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Prices (guide)</h2>
        <div class="table-wrap">
          <table class="pricing">
            <thead>
              <tr><th>Home</th><th>Fascias (with gutters = 2× gutter)</th><th>Fascias + windows</th></tr>
            </thead>
            <tbody>
              <tr><td>Small</td><td class="price">£100</td><td class="price">£120</td></tr>
              <tr class="highlight"><td>Medium</td><td class="price">£140</td><td class="price">£165</td></tr>
              <tr><td>Large</td><td class="price">£200</td><td class="price">£235</td></tr>
              <tr><td>XL</td><td class="price">£300</td><td class="price">£355</td></tr>
            </tbody>
          </table>
        </div>
        <p>Window add-on only: Small £20 · Medium £25 · Large £35 · XL £55.</p>
        <p class="mt-1">Care plan members: <strong>15% off</strong>.</p>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Get a fascia quote</h2>
        <p>Email or call: <a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-2"><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("soffits-fascias/index.html", page(
    "Soffits & fascias Sheffield | Dimension Exterior Cleaning",
    "Usually done with the gutters. Optional windows on the same visit. Guide prices from £100.",
    "soffits-fascias",
    soffits_body,
    schema=True,
    canonical="/soffits-fascias/",
    crumb="Soffits &amp; fascias",
))

# —— DRIVE ——
drive_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Drive and patio cleaning</h1>
        <p class="sub">Price from the surface and the size. Quotes held 30 days after we measure.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p>A clean drive or patio starts with the surface, not a one-size-fits-all setting. Joe checks the paving, joints, edges and drainage before washing. That matters because block paving, concrete, resin, tarmac and natural stone all respond differently to water pressure and cleaning products. The aim is a cleaner, more even finish without needlessly disturbing sound joints.</p>
        <p>Block paving is washed and the joints are refilled with kiln-dried sand where needed. A patio clean removes the green film, dirt and general weathering from the slabs. If the joints have failed, patio re-grouting is available at £7 per square metre and that price includes cleaning the patio first. You are not paying for a separate clean on top of the re-grout.</p>
        <p>White spots can be left behind when salts or residue dry on paving. Lichen can grip the edges and shaded areas, especially where a patio stays damp. Joe will point out what is likely to lift during the clean and what may remain as a mark in the material. That gives you a realistic result before the work starts, rather than promising that every old stain will disappear.</p>
        <p>A narrow path usually needs a different approach from a block-paved drive. Paths have tighter edges, steps, walls and planting to protect, while a drive often needs more attention to jointing and sand loss. The quote reflects the actual surface and access. Drive and patio work can be combined on one visit, with one £200 minimum for the wash visit. Sealing is separate and is normally done after the joints have dried, usually 24 to 48 hours later.</p>
        <p>Send a postcode, a rough size or a photo for a guide price. Joe measures the area on site before confirming the locked quote, so awkward corners, borders and changes between surfaces are included properly. Care plan customers receive 15% off wash and seal work. To arrange a measure, use the <a href="/get-a-quote/">quote builder</a>, email <a href="mailto:joe@dimensioncleaning.co.uk">joe@dimensioncleaning.co.uk</a> or call <a href="tel:+447494503865">07494 503865</a>.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Rates</h2>
        <div class="table-wrap">
          <table class="pricing">
            <thead><tr><th>Surface</th><th>Rate</th></tr></thead>
            <tbody>
              <tr><td>Block paving + resand</td><td class="price">£5/m²</td></tr>
              <tr><td>Patio clean</td><td class="price">£3/m²</td></tr>
              <tr><td>Patio re-grout (includes clean)</td><td class="price">£7/m²</td></tr>
              <tr><td>Tarmac / concrete / resin</td><td class="price">£3/m²</td></tr>
              <tr><td>Seal (after wash, dry)</td><td class="price">£5/m²</td></tr>
            </tbody>
          </table>
        </div>
        <p class="muted mt-1">Re-grout price includes cleaning the patio first.</p>
        <div class="prose">
          <p><strong>Pressure washing / drive &amp; patio wash:</strong> from £3/m² (patio, tarmac, concrete, resin) or £5/m² (block paving + resand), <strong>£200 minimum charge</strong>. Drive + patio on the same visit share one £200 minimum. Seal is separate at £5/m² with its own £200 minimum. We seal once joints are dry, usually 24 to 48 hours later. Block + seal = £9/m².</p>
          <p class="mt-2">Care plan: <strong>15% off</strong> wash and seal.</p>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Before &amp; after</h2>
        <p class="muted mb-2">Path and driveway cleans on real jobs. Dry after is what your neighbours will see.</p>
        <div class="gallery gallery--proof">
          {gallery_pair("path-before", "path-after", "Path", "Dirty flagstone path before cleaning", "Cleaned flagstone path after pressure washing", 1200, 1600)}
          {gallery_pair("drive-before", "drive-after", "Driveway", "Dirty herringbone driveway before cleaning", "Cleaned herringbone driveway after pressure washing", 1200, 1600)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Get a guide price</h2>
        <p>Send postcode + rough size (or a photo) for a guide price. On-site measure for the locked quote.</p>
        <p class="mt-2"><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("drive-patio/index.html", page(
    "Drive & patio cleaning Sheffield | Dimension Exterior Cleaning",
    "Price from the surface and the size. Quotes held 30 days after we measure. £200 minimum charge on wash quotes.",
    "drive-patio",
    drive_body,
    schema=True,
    canonical="/drive-patio/",
    crumb="Drive &amp; patio",
))

# —— ROOF ——
roof_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Roof cleaning in Sheffield</h1>
        <p class="sub">We scrape the moss, then softwash the roof so it stays clearer for longer.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <h2>How we clean roofs</h2>
        <p>Moss is more than a change of colour on a roof. It holds moisture against the tiles, grows through laps and can keep gutters full of loose debris. Lichen can leave a hard crust on the surface, while shaded roof faces often stay damp for longer. A roof clean is worth considering when moss is spreading across the tiles, growth is falling into the gutters or the roof looks heavily weathered from the street.</p>
        <p>Joe starts by scraping the moss from the roof by hand and with suitable tools. The loose growth is collected and cleared from the gutters and surrounding area. He then softwashes the tiles to deal with the remaining organic growth and residue. The two stages matter: scraping removes the heavy layer, while the treatment reaches the roots and helps the roof stay clearer for longer.</p>
        <p>Safety comes first on every roof. Joe assesses the pitch, access, tile condition and working area before agreeing the job. He uses the access and equipment suited to the property, protects nearby surfaces where needed and explains any issue that could affect the clean. Steep roofs, fragile slate, difficult access or scaffold requirements are discussed at the visit, so they are not hidden inside a guess made from a street photo.</p>
        <p>The guide rate is £12 per square metre, with a minimum charge of £500 where that applies to the job. Joe measures the pitched roof face on site rather than relying on the footprint of the house. The final price takes account of the roof size, pitch, access and condition. A photo and postcode can produce a useful starting guide, but the on-site measure is what makes the quote accurate.</p>
        <p>There is no pressure to book during the measure. You get a clear explanation of what needs doing, what can wait and whether roof cleaning is sensible for the tiles. Care plan customers receive 15% off while the plan is active. To ask about a roof in Sheffield or South Yorkshire, use the <a href="/get-a-quote/">quote builder</a>, email <a href="mailto:joe@dimensioncleaning.co.uk">joe@dimensioncleaning.co.uk</a> or call <a href="tel:+447494503865">07494 503865</a>.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Proof</h2>
        <p class="muted mb-2">Moss scrape and softwash on a terracotta roof.</p>
        <div class="gallery gallery--proof">
          {gallery_photo("roof-scrape", "Roof scrape", "Moss scrape on a terracotta roof", 1200, 1600)}
          {gallery_photo("roof-softwash", "Softwash", "Softwash foam on a pantile roof", 1200, 1600)}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Want a roof quote?</h2>
        <p>Send your postcode and a photo if you have one. We measure on site.</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-2"><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("roof-cleaning/index.html", page(
    "Roof cleaning Sheffield | Dimension Exterior Cleaning",
    "Roof scrape and softwash in Sheffield. Guide price from £12/m², £500 minimum. We measure on site.",
    "roof-cleaning",
    roof_body,
    schema=True,
    canonical="/roof-cleaning/",
    crumb="Roof cleaning",
))

# —— CARE PLAN ——
care_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Pay once. Two gutter visits. 15% off other services.</h1>
        <p class="sub">Annual care plan. Most semis: <strong>£98 a year</strong>.</p>
        <p class="mt-2"><a class="btn btn-primary btn-lg" href="/contact/">Ask to join the care plan</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>What’s included</h2>
        <ul>
          <li>Two gutter cleans, six months apart</li>
          <li>Visits show as covered (no extra gutter fee those days)</li>
          <li><strong>15% off</strong> soffits, drive, patio, seal, roof, and render while the plan is live</li>
        </ul>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>Prices</h2>
        <div class="table-wrap">
          <table class="pricing">
            <thead><tr><th>Home</th><th>Care plan / year</th></tr></thead>
            <tbody>
              <tr><td>Small</td><td class="price">£70</td></tr>
              <tr class="highlight"><td>Medium</td><td class="price">£98</td></tr>
              <tr><td>Large</td><td class="price">£140</td></tr>
              <tr><td>XL</td><td class="price">£210</td></tr>
            </tbody>
          </table>
        </div>
        <p class="muted">How we price it: double the gutter band, take 30%. Paid up front.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <h2>Who it’s for</h2>
        <p>You want gutters done twice a year without chasing a booking every autumn, plus a real discount when you add drive, roof, or fascias later.</p>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Ask to join the care plan</h2>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-1 muted" style="color:rgba(255,255,255,0.7)">(Or ask when we’re on site for a one-off gutter.)</p>
        <p class="mt-2"><a class="btn btn-primary" href="/contact/">Get in touch</a></p>
      </div>
    </section>'''

write("care-plan/index.html", page(
    "Care plan Sheffield | Dimension Exterior Cleaning",
    "Pay once. Two gutter visits. 15% off other services. Most semis: £98 a year.",
    "care-plan",
    care_body,
    schema=True,
    canonical="/care-plan/",
    crumb="Care plan",
))

# —— AREAS ——
areas_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Sheffield, South Yorkshire, and nearby</h1>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="lead mb-2">We work across Sheffield and the surrounding towns we already serve:</p>
        <ul class="area-list">
          <li>Sheffield (including S8, S10, S13, S20, S2, S9 and nearby)</li>
          <li>Aston / Mosborough (S26)</li>
          <li>Worksop / Dinnington (S25, S80)</li>
          <li>Doncaster fringe (DN4, DN11)</li>
          <li>Retford area (by arrangement)</li>
        </ul>
        <div class="prose mt-3">
          <p>Dimension Exterior Cleaning is based around Sheffield and takes on exterior cleaning work across South Yorkshire and nearby North Nottinghamshire. Joe plans jobs by route, which keeps the visit practical and helps customers get a straightforward answer on availability. Send the postcode before booking and he will confirm whether the property sits within the current run.</p>
          <p><strong>Sheffield</strong> is the main service area, including S8, S10, S13, S20, S2 and S9, plus nearby postcodes. The city has a mix of terraces, semis, steep gardens and larger detached homes, so the job is priced around the property rather than just the postcode. Gutter vacuum cleaning, driveways, patios, roof work, soffits and fascias can all be discussed in the same visit where access and timing make sense.</p>
          <p><strong>Aston and Mosborough</strong>, including S26, are regular parts of the route. Homes here often have larger drives, rear paths and roof areas than a typical city terrace. Joe can measure a drive or roof on site, while gutter cleaning is usually placed into a clear home-size price band.</p>
          <p><strong>Dinnington and Worksop</strong>, including S25 and S80, are covered on planned route days. This area includes older properties, newer estates and homes with mature trees, so the work can range from a seasonal gutter clean to a full patio or roof clean. A postcode and a couple of photos are enough to start the conversation, with the measure done at the property where the surface or roof needs it.</p>
          <p><strong>Doncaster fringe</strong>, including DN4 and DN11, is also within the area we already serve. These jobs are grouped sensibly with nearby work where possible, but the service stays personal rather than being passed to a call centre. Joe will confirm the route, then explain the price and next step in plain English.</p>
          <p><strong>Retford and further out</strong> may be possible by arrangement. It depends on the route that month and the size of the job, so it is better to ask than assume. Email <a href="mailto:joe@dimensioncleaning.co.uk">joe@dimensioncleaning.co.uk</a> with your postcode and service, or call <a href="tel:+447494503865">07494 503865</a>. If the location works, you will get a clear reply before any booking is made.</p>
          <p>For properties across the area, gutter cleans use clear home-size bands, while driveways, patios and roofs are measured where the surface or access makes that necessary. The care plan is available for regular gutter visits and includes 15% off other exterior cleaning while it is active. Use the <a href="/get-a-quote/">quote builder</a> to send the basics and get the right next step.</p>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Check we cover you</h2>
        <p>Send your postcode: <a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-2"><a class="btn btn-primary" href="/contact/">Send your postcode</a></p>
      </div>
    </section>'''

write("areas/index.html", page(
    "Areas we cover | Dimension Exterior Cleaning",
    "Sheffield, South Yorkshire, and nearby: Worksop, Dinnington, Aston, Mosborough, Doncaster fringe. Retford by arrangement.",
    "areas",
    areas_body,
    schema=True,
    canonical="/areas/",
    crumb="Areas",
))

# —— ABOUT ——
about_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Local exterior cleaning. One proper job day at a time.</h1>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p>Dimension Exterior Cleaning is a Sheffield-area exterior cleaning business. Gutters first. Clear prices. Roof softwash done the right way.</p>
        <p>We keep the offer simple: band prices for gutters and fascias, measure-on-site for drive and roof, and a care plan for people who want two cleans a year plus 15% off other work.</p>
        <p class="muted mt-3">Insurance details are available on request.</p>
        <p class="mt-2"><strong>Contact:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2>What we cover</h2>
        <figure class="flyer-proof">
          {picture("flyer-services", "Dimension Exterior Cleaning services flyer.", 1415, 2000)}
        </figure>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Get in touch</h2>
        <p><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("about/index.html", page(
    "About us | Dimension Exterior Cleaning",
    "Local exterior cleaning in Sheffield. Gutters first. Clear prices. Roof softwash done the right way.",
    "about",
    about_body,
    schema=True,
    canonical="/about/",
    crumb="About",
))

# —— FAQ ——
faq_items = [
    ("How often should gutters be cleaned?",
     "Most houses once or twice a year. Trees nearby = lean toward twice. That’s what the care plan is for."),
    ("What’s included in a gutter clean?",
     "Vac of the runs, outlets checked, first two downpipes included. Extra downpipes +£10 each. Conservatory/extension +£15."),
    ("How do you clean roofs?",
     "We scrape the moss first, then softwash the roof. That clears growth at the root and leaves the tiles in better shape."),
    ("Why is there a £200 minimum on drives and patios?",
     "Small jobs still need setup, water, and time. The per-m² rate applies above that minimum."),
    ("When do you seal?",
     "After the wash has dried, usually 24 to 48 hours later. We seal once joints are dry."),
    ("Can I pay half now?",
     "On bigger jobs (around £200+), we can split half now / half in 30 days when that helps. Ask."),
    ("Do you cover my area?",
     'Sheffield and nearby South Yorks / North Notts. See <a href="/areas/">Areas</a>, or send your postcode if you are unsure.'),
    ("What’s the care plan again?",
     "Pay once for the year. Two gutter visits. 15% off other exterior work while you’re on the plan. Medium homes usually £98/year."),
]
faq_html = "\n".join(
    f'        <div class="faq-item">\n          <h3>{q}</h3>\n          <p>{a}</p>\n        </div>'
    for q, a in faq_items
)

faq_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>FAQ</h1>
        <p class="sub">Straight answers on gutters, roofs, drives, and the care plan.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="faq-list">
{faq_html}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>Still unsure?</h2>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a> / <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p class="mt-2"><a class="btn btn-primary" href="/get-a-quote/">Get a quote</a></p>
      </div>
    </section>'''

write("faq/index.html", page(
    "FAQ | Dimension Exterior Cleaning",
    "How often should gutters be cleaned? How we clean roofs, care plan, drive minimums, and more.",
    "faq",
    faq_body,
    schema=True,
    canonical="/faq/",
    crumb="FAQ",
))

# —— CONTACT ——
contact_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Get a quote or book in</h1>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="contact-grid">
          <div>
            <dl class="contact-details">
              <dt>Email</dt>
              <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
              <dt>Mobile</dt>
              <dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd>
              <dt>WhatsApp</dt>
              <dd><a href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">{PHONE_DISPLAY}</a></dd>
            </dl>
            <p class="mt-2"><a href="/get-a-quote/">Prefer a guide price first? Use the quote builder.</a></p>
            <p class="form-note mt-3">Prefer to talk? Call {PHONE_DISPLAY} (lunchtime or early evening before 7pm).</p>
          </div>
          <div>
            <div id="form-success" class="form-success" role="status" aria-live="polite"></div>
            <form id="contact-form" action="#" method="get" novalidate>
              <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required autocomplete="name">
              </div>
              <div class="form-group">
                <label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" required autocomplete="tel">
              </div>
              <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required autocomplete="email">
              </div>
              <div class="form-group">
                <label for="postcode">Postcode</label>
                <input type="text" id="postcode" name="postcode" required autocomplete="postal-code">
              </div>
              <div class="form-group">
                <label for="service">Service</label>
                <select id="service" name="service" required>
                  <option value="">Select…</option>
                  <option>Gutters</option>
                  <option>Care plan</option>
                  <option>Fascias</option>
                  <option>Drive-patio</option>
                  <option>Roof</option>
                  <option>Not sure</option>
                </select>
              </div>
              <div class="form-group">
                <label for="message">Message / photo note</label>
                <textarea id="message" name="message" rows="4"></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-lg">Send</button>
            </form>
          </div>
        </div>
      </div>
    </section>'''

write("contact/index.html", page(
    "Contact | Dimension Exterior Cleaning",
    "Get a quote or book in. Email joe@dimensioncleaning.co.uk or call 07494 503865.",
    "contact",
    contact_body,
    schema=True,
    canonical="/contact/",
    crumb="Contact",
))


# —— GET A QUOTE ——
quote_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Get a guide price</h1>
        <p class="sub">Pick your services and house size for an instant guide estimate. We confirm the final price before work starts.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div id="quote-success" class="form-success" role="status" aria-live="polite"></div>
        <div id="quote-error" class="form-error" role="alert" aria-live="assertive"></div>

        <form id="quote-form" class="quote-layout" data-access-key="YOUR_WEB3FORMS_ACCESS_KEY" novalidate>
          <div class="quote-panel">
            <div class="quote-section" id="house-size-wrap">
              <h2>House size</h2>
              <p class="house-size-hint muted" style="margin-bottom:0.75rem">Needed for gutters, fascias, windows, and the care plan.</p>
              <div class="house-size-grid" role="radiogroup" aria-label="House size">
                <label class="quote-radio"><input type="radio" name="house_size" value="small"> Small (terrace 1-2 bed)</label>
                <label class="quote-radio"><input type="radio" name="house_size" value="medium"> Medium (semi 2-3 bed)</label>
                <label class="quote-radio"><input type="radio" name="house_size" value="large"> Large (detached 3-4)</label>
                <label class="quote-radio"><input type="radio" name="house_size" value="xl"> XL (detached 5+)</label>
              </div>
            </div>

            <div class="quote-section">
              <h2>Services</h2>
              <p class="muted" style="margin-bottom:0.75rem">Select at least one. Gutter one-off and care plan cannot both be selected.</p>

              <label class="quote-check"><input type="checkbox" id="svc-gutter" name="svc_gutter"> Gutter clean (one-off)</label>
              <div id="gutter-addons" class="quote-nested" hidden>
                <label class="quote-check"><input type="checkbox" id="addon-conservatory"> Conservatory or extension (+£15)</label>
                <div class="form-group" style="margin:0.5rem 0 0">
                  <label for="addon-downpipes">Extra downpipes after the first two (£10 each)</label>
                  <input type="number" id="addon-downpipes" min="0" step="1" value="0" inputmode="numeric">
                </div>
              </div>

              <label class="quote-check"><input type="checkbox" id="svc-care" name="svc_care"> Care plan (annual): two gutter visits, 15% off other work</label>

              <label class="quote-check"><input type="checkbox" id="svc-fascias" name="svc_fascias"> Soffits &amp; fascias</label>
              <div id="fascias-options" class="quote-nested" hidden>
                <label class="quote-radio"><input type="radio" name="fascias_mode" id="fascias-only" value="fascias" checked> Fascias only</label>
                <label class="quote-radio"><input type="radio" name="fascias_mode" id="fascias-windows" value="fascias_windows"> Fascias + windows</label>
              </div>

              <div id="windows-wrap">
                <label class="quote-check"><input type="checkbox" id="svc-windows" name="svc_windows"> Windows only</label>
              </div>

              <h3>Drive / patio</h3>
              <p class="quote-helper">Add m² for a guide price. Leave blank if you want us to measure on site. Pressure washing / wash has a £200 minimum charge (drive + patio same visit share one minimum). Seal has its own £200 minimum.</p>

              <div class="drive-surface">
                <label class="quote-check"><input type="checkbox" id="drive-block"> Block paving + resand (£5/m²)</label>
                <div class="m2-row" id="row-m2-block" hidden>
                  <label for="m2-block">m²</label>
                  <input type="number" id="m2-block" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
              </div>
              <div class="drive-surface">
                <label class="quote-check"><input type="checkbox" id="drive-patio"> Patio clean (£3/m²)</label>
                <div class="m2-row" id="row-m2-patio" hidden>
                  <label for="m2-patio">m²</label>
                  <input type="number" id="m2-patio" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
              </div>
              <div class="drive-surface">
                <label class="quote-check"><input type="checkbox" id="drive-regrout"> Patio re-grout, includes clean (£7/m²)</label>
                <div class="m2-row" id="row-m2-regrout" hidden>
                  <label for="m2-regrout">m²</label>
                  <input type="number" id="m2-regrout" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
              </div>
              <div class="drive-surface">
                <label class="quote-check"><input type="checkbox" id="drive-tarmac"> Tarmac / concrete / resin (£3/m²)</label>
                <div class="m2-row" id="row-m2-tarmac" hidden>
                  <label for="m2-tarmac">m²</label>
                  <input type="number" id="m2-tarmac" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
              </div>
              <div class="drive-surface">
                <label class="quote-check"><input type="checkbox" id="drive-seal"> Seal after wash (£5/m²)</label>
                <div class="m2-row" id="row-m2-seal" hidden>
                  <label for="m2-seal">m²</label>
                  <input type="number" id="m2-seal" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
                <p class="quote-helper">Usually 24 to 48 hours after the wash. Can be the same enquiry.</p>
              </div>

              <h3>Roof softwash</h3>
              <label class="quote-check"><input type="checkbox" id="svc-roof" name="svc_roof"> Roof softwash (£12/m², £500 minimum)</label>
              <div id="roof-options" class="quote-nested" hidden>
                <div class="m2-row" style="margin-left:0">
                  <label for="m2-roof">Pitched roof face m²</label>
                  <input type="number" id="m2-roof" min="0" step="0.1" inputmode="decimal" placeholder="Optional">
                </div>
                <p class="quote-helper">Steep / slate / scaffold extras confirmed on visit.</p>
              </div>
            </div>

            <div class="quote-section">
              <h2>Your details</h2>
              <div class="quote-inline-fields two">
                <div class="form-group">
                  <label for="q-name">Name</label>
                  <input type="text" id="q-name" name="name" required autocomplete="name">
                </div>
                <div class="form-group">
                  <label for="q-phone">Phone</label>
                  <input type="tel" id="q-phone" name="phone" required autocomplete="tel">
                </div>
              </div>
              <div class="quote-inline-fields two">
                <div class="form-group">
                  <label for="q-email">Email</label>
                  <input type="email" id="q-email" name="email" required autocomplete="email">
                </div>
                <div class="form-group">
                  <label for="q-postcode">Postcode</label>
                  <input type="text" id="q-postcode" name="postcode" required autocomplete="postal-code">
                </div>
              </div>
              <div class="form-group">
                <label for="q-notes">Notes / photo note (optional)</label>
                <textarea id="q-notes" name="notes" rows="3"></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-lg">Send guide estimate</button>
            </div>
          </div>

          <aside class="quote-totals-panel" aria-live="polite">
            <h2>Guide estimate</h2>
            <ul class="quote-lines" id="quote-lines">
              <li class="quote-line muted">Select services to see a guide estimate.</li>
            </ul>
            <div class="quote-total-row">
              <span class="label">Guide total</span>
              <span class="value" id="quote-total">£0</span>
            </div>
            <p class="quote-disclaimer">Guide estimate only. We confirm the final price before work starts. Drive, patio, and roof are locked after we measure on site.</p>
            <p class="muted mt-2" style="font-size:0.85rem">Or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> / <a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </aside>
        </form>
      </div>
    </section>'''

write("get-a-quote/index.html", page(
    "Get a quote | Dimension Exterior Cleaning",
    "Instant guide estimate for gutters, care plan, fascias, drive, patio, and roof in Sheffield. We confirm the final price before work starts.",
    "get-a-quote",
    quote_body,
    schema=True,
    canonical="/get-a-quote/",
    crumb="Get a quote",
    extra_scripts='  <script src="/assets/js/quote-builder.js" defer></script>\n',
))

# —— PRIVACY ——
privacy_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Privacy</h1>
        <p class="sub">Short notice for dimensioncleaning.co.uk. A fuller UK privacy policy can follow before go-live if needed.</p>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p>Dimension Exterior Cleaning (“we”) collects the information you send us when you ask for a quote or book work: typically your name, phone, email, postcode, and message details.</p>
        <p>We use that information only to respond to your enquiry, arrange visits, and keep records of jobs we do for you. We do not sell your details.</p>
        <p>Emails and calls may be stored in our inbox, phone, or simple business tools. You can ask us what we hold about you, or ask us to delete it where we no longer need it for the job, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <p>This site does not use advertising cookies or analytics trackers at present. If that changes, this page will be updated.</p>
        <p class="muted mt-3">Last updated: September 2026.</p>
      </div>
    </section>'''

write("privacy/index.html", page(
    "Privacy | Dimension Exterior Cleaning",
    "Short UK privacy notice for Dimension Exterior Cleaning: how we handle enquiry details.",
    "privacy",
    privacy_body,
    canonical="/privacy/",
    crumb="Privacy",
))

# —— robots.txt + sitemap.xml ——
ROBOTS = """User-agent: *
Allow: /

Sitemap: https://dimensioncleaning.co.uk/sitemap.xml
"""
write("robots.txt", ROBOTS)

SITEMAP_PATHS = [
    "/",
    "/gutter-cleaning/",
    "/drive-patio/",
    "/roof-cleaning/",
    "/soffits-fascias/",
    "/care-plan/",
    "/about/",
    "/areas/",
    "/get-a-quote/",
    "/contact/",
    "/faq/",
    "/privacy/",
]
sitemap_urls = "\n".join(
    f"  <url>\n    <loc>{SITE_ORIGIN}{p}</loc>\n  </url>" for p in SITEMAP_PATHS
)
SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
"""
write("sitemap.xml", SITEMAP)

print("Done.")
