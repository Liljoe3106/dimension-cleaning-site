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

LOCAL_BUSINESS_SCHEMA = f'''{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Dimension Exterior Cleaning",
  "description": "Gutter cleaning and exterior cleaning in Sheffield and South Yorkshire. Clear band prices, roof softwash, and a care plan that saves money.",
  "url": "https://dimensioncleaning.co.uk/",
  "telephone": "{PHONE_TEL}",
  "email": "{EMAIL}",
  "areaServed": [
    {{"@type": "City", "name": "Sheffield"}},
    {{"@type": "AdministrativeArea", "name": "South Yorkshire"}},
    "Worksop", "Dinnington", "Aston", "Mosborough", "Doncaster"
  ],
  "priceRange": "££",
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
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://dimensioncleaning.co.uk{canonical}">
  <meta name="theme-color" content="#ffffff">
  <link rel="stylesheet" href="/assets/css/styles.css?v=photos3">{schema_block}
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
            <p>Two gutter visits a year. 15% off the rest of the house.</p>
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
          <h2>Pay once. Two gutter visits. 15% off the rest of the house.</h2>
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
    "Gutter cleaning Sheffield | Dimension Exterior Cleaning",
    "Clear prices. Proper roof softwash. A care plan that actually saves you money. Gutter cleaning and exterior cleaning in Sheffield.",
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
        <p>Blocked gutters overflow into walls, fascia, and foundations. We vac the run, clear the outlets, and check the first two downpipes are included in the price.</p>
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
    "Gutter cleaning Sheffield | Dimension Exterior Cleaning",
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
    "Soffits & fascias cleaning Sheffield | Dimension Exterior Cleaning",
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
          <p><strong>Minimum:</strong> Wash quotes floor at <strong>£200</strong>. Drive + patio same visit = one £200 floor. Seal is separate. We seal once joints are dry, usually 24 to 48 hours later. Seal-only trip also floors at £200. Block + seal = £9/m².</p>
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
    "Price from the surface and the size. Quotes held 30 days after we measure. Wash quotes floor at £200.",
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
        <p>Moss and lichen hold moisture on the tiles. We scrape the growth off first, then softwash the roof so the roots go as well. That leaves the granules where they belong and keeps water from getting forced under the tiles.</p>
        <p class="mt-2">Guide price is <strong>£12/m²</strong>, with a floor of <strong>£500</strong>. We measure the pitched roof face on site. If the roof is steep, slate, or needs scaffold, we confirm any extras when we visit.</p>
        <p class="mt-1">Care plan members get <strong>15% off</strong>.</p>
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
    "Roof scrape and softwash in Sheffield. Guide price from £12/m², floor £500. We measure on site.",
    "roof-cleaning",
    roof_body,
    schema=True,
    canonical="/roof-cleaning/",
    crumb="Roof cleaning",
))

# —— CARE PLAN ——
care_body = f'''    <section class="page-hero">
      <div class="container">
        <h1>Pay once. Two gutter visits. 15% off the rest of the house.</h1>
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
    "Pay once. Two gutter visits. 15% off the rest of the house. Most semis: £98 a year.",
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
        <p class="mt-3 prose">Further out? Email the postcode. If the route works that month, we’ll say yes.</p>
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
     "Small jobs still need setup, water, and time. The per-m² rate applies above that floor."),
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
              <p class="quote-helper">Add m² for a guide price. Leave blank if you want us to measure on site.</p>

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
              <label class="quote-check"><input type="checkbox" id="svc-roof" name="svc_roof"> Roof softwash (£12/m², floor £500)</label>
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

print("Done.")
