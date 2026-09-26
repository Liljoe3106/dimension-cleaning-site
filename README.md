# Dimension Exterior Cleaning — public website (v1)

Static multi-page site for **Dimension Exterior Cleaning** (target domain: `dimensioncleaning.co.uk`).

Copy source of truth: [`SITE-PLAN-AND-COPY.md`](./SITE-PLAN-AND-COPY.md). Keep that file in the repo.

## Path

```
/workspace/dimension-site/
```

Pages live as folder `index.html` files so clean URLs work without a build step (`/gutter-cleaning/`, `/care-plan/`, etc.).

## Preview locally

From this directory:

```bash
cd /workspace/dimension-site
npx --yes serve . -p 4173
```

Or:

```bash
python3 -m http.server 4173
```

Then open http://localhost:4173/

`npm start` / `npm run preview` run the same `serve` command via `package.json`.

## Deploy

No build step. Point the host at this folder (site root = where `index.html` sits).

### Cloudflare Pages

1. Connect the Git repo (or upload this folder).
2. **Build command:** leave empty (or `exit 0`).
3. **Output directory:** `/` (or `.` — the folder that contains `index.html`).
4. Deploy. Attach custom domain `dimensioncleaning.co.uk` when DNS is ready.

### Netlify

1. New site from Git (or drag-and-drop this folder).
2. **Build command:** empty.
3. **Publish directory:** `.` (this folder).
4. Add domain when ready.

Optional `public/_redirects` is not required for folder `index.html` routing. If you later move files under `public/`, set publish dir to `public`.

### Vercel

1. Import the project.
2. **Framework preset:** Other.
3. **Build command:** leave empty.
4. **Output directory:** `.`
5. Deploy.

## Domain / DNS (Joe still needs)

The site is **not live** on `dimensioncleaning.co.uk` yet. Before cutover:

1. Confirm the registrar for `dimensioncleaning.co.uk` (move DNS away from Replit if it still points there).
2. Point the domain at Cloudflare Pages / Netlify / Vercel using their DNS instructions (usually A/CNAME or nameservers).
3. Do **not** publish publicly until Joe approves copy + before/after photos with permission (see checklist in `SITE-PLAN-AND-COPY.md`).

## Contact form

The contact page uses a **mailto fallback**: Submit opens the visitor’s email app with subject/body filled for `joe@dimensioncleaning.co.uk`.

## Quote builder (`/get-a-quote/`)

Client-side guide estimate. Submit prefers **Web3Forms** (emails Joe without the visitor opening a mail app). Until a real access key is set, it falls back to `mailto:joe@dimensioncleaning.co.uk` with the full breakdown.

### How Joe gets a Web3Forms access key

1. Go to [https://web3forms.com/](https://web3forms.com/) and create a free account (or use “Create Access Key”).
2. Use the destination email **`joe@dimensioncleaning.co.uk`** so enquiries land in Joe’s inbox.
3. Copy the **Access Key**.
4. In the site source, open `_build_pages.py` (quote form) or the generated `get-a-quote/index.html` and replace:

   `data-access-key="YOUR_WEB3FORMS_ACCESS_KEY"`

   with your real key. Then run `python3 _build_pages.py` if you edited the builder.

   Alternatively set `window.DIMENSION_WEB3FORMS_KEY = 'your-key';` in a small script before `quote-builder.js` loads.

5. Confirm a test submit from `/get-a-quote/` arrives at Joe’s inbox (check spam once).

## Intentional omissions (v1)

- **Insurance:** muted “available on request” on About — no raw `[INSURANCE]` placeholder.
- **Facebook / Instagram:** omitted until real profiles exist (no fake footer links).
- **Before/after photos:** placeholder cards only (“Photos coming soon”).
- **Landline:** none — public mobile only `07494 503865` (call + WhatsApp).
- **DNS / live domain:** not done in this build.

## Brand lock

Always **Dimension Exterior Cleaning** — never “Powerwash” on this site/domain.

## Regenerating pages

Optional: `python3 _build_pages.py` rewrites the HTML pages from the embedded approved copy (shared header/footer). Edit copy in that script (or hand-edit HTML) and keep `SITE-PLAN-AND-COPY.md` in sync.
