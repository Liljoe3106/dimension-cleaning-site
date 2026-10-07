(function () {
  'use strict';

  var PLACEHOLDER_KEY = 'YOUR_WEB3FORMS_ACCESS_KEY';
  var JOE_EMAIL = 'joe@dimensioncleaning.co.uk';

  var GUTTER = { small: 50, medium: 70, large: 100, xl: 150 };
  var CARE = { small: 70, medium: 98, large: 140, xl: 210 };
  var FASCIAS = { small: 100, medium: 140, large: 200, xl: 300 };
  var FASCIAS_WIN = { small: 120, medium: 165, large: 235, xl: 355 };
  var WINDOWS = { small: 20, medium: 25, large: 35, xl: 55 };

  var WASH_FLOOR = 200;
  var SEAL_FLOOR = 200;
  var ROOF_RATE = 12;
  var ROOF_FLOOR = 500;
  var CARE_OFF = 0.15;
  var ADDON_CONSERVATORY = 15;
  var ADDON_DOWNPIPE = 10;
  var DOWNPIPES_INCLUDED = { small: 2, medium: 2, large: 4, xl: 6 };
  var DOWNPIPES_HINT_DEFAULT = 'Downpipes included: 2 on Small and Medium, 4 on Large, 6 on XL.';

  var SIZE_LABELS = {
    small: 'Small (terrace 1-2 bed)',
    medium: 'Medium (semi 2-3 bed)',
    large: 'Large (detached 3-4)',
    xl: 'XL (detached 5+)'
  };

  var form = document.getElementById('quote-form');
  if (!form) return;

  var linesEl = document.getElementById('quote-lines');
  var totalEl = document.getElementById('quote-total');
  var successEl = document.getElementById('quote-success');
  var errorEl = document.getElementById('quote-error');
  var houseSizeWrap = document.getElementById('house-size-wrap');

  var svcGutter = form.querySelector('#svc-gutter');
  var svcCare = form.querySelector('#svc-care');
  var svcFascias = form.querySelector('#svc-fascias');
  var svcWindows = form.querySelector('#svc-windows');
  var svcRoof = form.querySelector('#svc-roof');
  var fasciasOptions = form.querySelector('#fascias-options');
  var windowsWrap = form.querySelector('#windows-wrap');
  var gutterAddons = form.querySelector('#gutter-addons');
  var roofOptions = form.querySelector('#roof-options');
  var downpipesHint = form.querySelector('#downpipes-included-hint');

  function money(n) {
    var r = Math.round(n * 100) / 100;
    return '£' + (r % 1 === 0 ? String(r) : r.toFixed(2));
  }

  function parseM2(input) {
    if (!input) return null;
    var v = String(input.value || '').trim();
    if (v === '') return null;
    var n = parseFloat(v);
    if (!isFinite(n) || n < 0) return null;
    return n;
  }

  function sizeKey() {
    var radios = form.querySelectorAll('input[name="house_size"]');
    for (var i = 0; i < radios.length; i++) {
      if (radios[i].checked) return radios[i].value;
    }
    return '';
  }

  function needsHouseSize() {
    return !!(
      (svcGutter && svcGutter.checked) ||
      (svcCare && svcCare.checked) ||
      (svcFascias && svcFascias.checked) ||
      (svcWindows && svcWindows.checked)
    );
  }

  function syncVisibility() {
    if (gutterAddons) gutterAddons.hidden = !((svcGutter && svcGutter.checked) || (svcCare && svcCare.checked));
    if (fasciasOptions) fasciasOptions.hidden = !(svcFascias && svcFascias.checked);
    if (windowsWrap) {
      var showWin = !(svcFascias && svcFascias.checked);
      windowsWrap.hidden = !showWin;
      if (!showWin && svcWindows) svcWindows.checked = false;
    }
    if (roofOptions) roofOptions.hidden = !(svcRoof && svcRoof.checked);
    if (downpipesHint) {
      var hs = sizeKey();
      downpipesHint.textContent = hs && DOWNPIPES_INCLUDED[hs] != null
        ? 'Your size includes ' + DOWNPIPES_INCLUDED[hs] + ' downpipes. Only enter the extras.'
        : DOWNPIPES_HINT_DEFAULT;
    }
    if (houseSizeWrap) houseSizeWrap.classList.toggle('is-required', needsHouseSize());

    [
      { id: 'drive-block', row: 'row-m2-block' },
      { id: 'drive-patio', row: 'row-m2-patio' },
      { id: 'drive-regrout', row: 'row-m2-regrout' },
      { id: 'drive-tarmac', row: 'row-m2-tarmac' },
      { id: 'drive-seal', row: 'row-m2-seal' }
    ].forEach(function (pair) {
      var cb = form.querySelector('#' + pair.id);
      var row = form.querySelector('#' + pair.row);
      if (row) row.hidden = !(cb && cb.checked);
    });
  }

  function applyCare(amount, careOn) {
    if (!careOn || amount <= 0) return { pre: amount, post: amount, discounted: false };
    var post = Math.round(amount * (1 - CARE_OFF) * 100) / 100;
    return { pre: amount, post: post, discounted: true };
  }

  function calculate() {
    var size = sizeKey();
    var careOn = !!(svcCare && svcCare.checked);
    var lines = [];
    var total = 0;
    var anyService = false;

    function push(opts) {
      lines.push(opts);
      if (typeof opts.amount === 'number' && !opts.measure && !opts.pending) {
        total += opts.amount;
      }
    }

    if (svcGutter && svcGutter.checked) {
      anyService = true;
      if (size && GUTTER[size] != null) {
        push({ label: 'Gutter clean (one-off)', amount: GUTTER[size], display: money(GUTTER[size]) });
      } else {
        push({ label: 'Gutter clean (one-off)', amount: 0, display: 'Select house size', pending: true });
      }
    }

    if (svcCare && svcCare.checked) {
      anyService = true;
      if (size && CARE[size] != null) {
        push({ label: 'Care plan (annual)', amount: CARE[size], display: money(CARE[size]) });
      } else {
        push({ label: 'Care plan (annual)', amount: 0, display: 'Select house size', pending: true });
      }
    }

    // Gutter add-ons: same prices for the one-off clean and the care plan (per year on the plan).
    // Charged once even if both are ticked. Never discounted by the care plan 15%.
    var gutterOn = !!(svcGutter && svcGutter.checked);
    if ((gutterOn || careOn) && size && GUTTER[size] != null) {
      var addonSuffix = gutterOn ? '' : ' (plan)';
      var cons = form.querySelector('#addon-conservatory');
      if (cons && cons.checked) {
        push({ label: 'Conservatory / extension' + addonSuffix, amount: ADDON_CONSERVATORY, display: money(ADDON_CONSERVATORY) });
      }
      var dpEl = form.querySelector('#addon-downpipes');
      var dp = dpEl ? parseInt(dpEl.value, 10) : 0;
      if (!isFinite(dp) || dp < 0) dp = 0;
      if (dp > 0) {
        push({ label: 'Extra downpipes × ' + dp + ' (beyond ' + DOWNPIPES_INCLUDED[size] + ' included' + (gutterOn ? '' : ', plan') + ')', amount: dp * ADDON_DOWNPIPE, display: money(dp * ADDON_DOWNPIPE) });
      }
    }

    if (svcFascias && svcFascias.checked) {
      anyService = true;
      var mode = 'fascias';
      var modeRadios = form.querySelectorAll('input[name="fascias_mode"]');
      for (var mi = 0; mi < modeRadios.length; mi++) {
        if (modeRadios[mi].checked) { mode = modeRadios[mi].value; break; }
      }
      if (size && FASCIAS[size] != null) {
        var fPre = mode === 'fascias_windows' ? FASCIAS_WIN[size] : FASCIAS[size];
        var fLabel = mode === 'fascias_windows' ? 'Soffits & fascias + windows' : 'Soffits & fascias';
        var fDisc = applyCare(fPre, careOn);
        push({
          label: fLabel,
          amount: fDisc.post,
          display: money(fDisc.post),
          pre: fDisc.discounted ? fDisc.pre : null,
          careOff: fDisc.discounted
        });
      } else {
        push({ label: 'Soffits & fascias', amount: 0, display: 'Select house size', pending: true });
      }
    } else if (svcWindows && svcWindows.checked) {
      anyService = true;
      if (size && WINDOWS[size] != null) {
        var wDisc = applyCare(WINDOWS[size], careOn);
        push({
          label: 'Windows only',
          amount: wDisc.post,
          display: money(wDisc.post),
          pre: wDisc.discounted ? wDisc.pre : null,
          careOff: wDisc.discounted
        });
      } else {
        push({ label: 'Windows only', amount: 0, display: 'Select house size', pending: true });
      }
    }

    var washDefs = [
      { id: 'drive-block', m2: 'm2-block', label: 'Block paving + resand', rate: 5 },
      { id: 'drive-patio', m2: 'm2-patio', label: 'Patio clean', rate: 3 },
      { id: 'drive-regrout', m2: 'm2-regrout', label: 'Patio re-grout (includes clean)', rate: 7 },
      { id: 'drive-tarmac', m2: 'm2-tarmac', label: 'Tarmac / concrete / resin', rate: 3 }
    ];
    var washSub = 0;
    var washHasM2 = false;
    var washNames = [];

    washDefs.forEach(function (d) {
      var cb = form.querySelector('#' + d.id);
      if (!cb || !cb.checked) return;
      anyService = true;
      var m2 = parseM2(form.querySelector('#' + d.m2));
      if (m2 == null) {
        push({ label: d.label, amount: 0, display: 'measure on site', measure: true });
      } else {
        washSub += m2 * d.rate;
        washHasM2 = true;
        washNames.push(d.label + ' (' + m2 + ' m²)');
      }
    });

    if (washHasM2) {
      var flooredWash = Math.max(washSub, WASH_FLOOR);
      var washDisc = applyCare(flooredWash, careOn);
      var washLabel = 'Drive / patio wash: ' + washNames.join(', ');
      if (flooredWash > washSub) washLabel += ' (min £200 applied)';
      push({
        label: washLabel,
        amount: washDisc.post,
        display: money(washDisc.post),
        pre: washDisc.discounted ? washDisc.pre : null,
        careOff: washDisc.discounted
      });
    }

    var sealCb = form.querySelector('#drive-seal');
    if (sealCb && sealCb.checked) {
      anyService = true;
      var sealM2 = parseM2(form.querySelector('#m2-seal'));
      if (sealM2 == null) {
        push({ label: 'Seal (after wash)', amount: 0, display: 'measure on site', measure: true });
      } else {
        var sealRaw = sealM2 * 5;
        var sealFloored = Math.max(sealRaw, SEAL_FLOOR);
        var sealDisc = applyCare(sealFloored, careOn);
        var sealLabel = 'Seal (' + sealM2 + ' m²)';
        if (sealFloored > sealRaw) sealLabel += ' (min £200 applied)';
        push({
          label: sealLabel,
          amount: sealDisc.post,
          display: money(sealDisc.post),
          pre: sealDisc.discounted ? sealDisc.pre : null,
          careOff: sealDisc.discounted
        });
      }
    }

    if (svcRoof && svcRoof.checked) {
      anyService = true;
      var roofM2 = parseM2(form.querySelector('#m2-roof'));
      if (roofM2 == null) {
        push({ label: 'Roof softwash', amount: 0, display: 'measure on site', measure: true });
      } else {
        var roofRaw = roofM2 * ROOF_RATE;
        var roofFloored = Math.max(roofRaw, ROOF_FLOOR);
        var roofDisc = applyCare(roofFloored, careOn);
        var roofLabel = 'Roof softwash (' + roofM2 + ' m²)';
        if (roofFloored > roofRaw) roofLabel += ' (min £500 applied)';
        push({
          label: roofLabel,
          amount: roofDisc.post,
          display: money(roofDisc.post),
          pre: roofDisc.discounted ? roofDisc.pre : null,
          careOff: roofDisc.discounted
        });
      }
    }

    total = Math.round(total * 100) / 100;
    return { lines: lines, total: total, anyService: anyService, size: size, careOn: careOn };
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function render() {
    syncVisibility();
    var q = calculate();
    if (!linesEl || !totalEl) return q;

    if (!q.lines.length) {
      linesEl.innerHTML = '<li class="quote-line muted">Select services to see a guide estimate.</li>';
    } else {
      linesEl.innerHTML = q.lines
        .map(function (line) {
          var right;
          if (line.measure) {
            right = '<span class="quote-amt measure">measure on site</span>';
          } else if (line.pending) {
            right = '<span class="quote-amt muted">' + escapeHtml(line.display) + '</span>';
          } else if (line.careOff && line.pre != null) {
            right =
              '<span class="quote-amt">' +
              '<span class="quote-pre">' +
              money(line.pre) +
              '</span> ' +
              escapeHtml(line.display) +
              '</span>' +
              '<span class="care-tag">Care plan 15% off</span>';
          } else {
            right = '<span class="quote-amt">' + escapeHtml(line.display) + '</span>';
          }
          return (
            '<li class="quote-line">' +
            '<span class="quote-label">' +
            escapeHtml(line.label) +
            '</span>' +
            '<span class="quote-right">' +
            right +
            '</span></li>'
          );
        })
        .join('');
    }

    if (q.total > 0) {
      totalEl.textContent = money(q.total);
    } else if (q.anyService && q.lines.some(function (l) { return l.measure; })) {
      totalEl.textContent = 'measure on site';
    } else {
      totalEl.textContent = money(0);
    }

    return q;
  }

  function getAccessKey() {
    var fromData = (form.getAttribute('data-access-key') || '').trim();
    var fromWin =
      typeof window.DIMENSION_WEB3FORMS_KEY === 'string'
        ? window.DIMENSION_WEB3FORMS_KEY.trim()
        : '';
    var key = fromData || fromWin;
    if (!key || key === PLACEHOLDER_KEY) return '';
    return key;
  }

  function validate(q) {
    var errors = [];
    if (!((form.querySelector('#q-name') || {}).value || '').trim()) errors.push('Enter your name.');
    if (!((form.querySelector('#q-phone') || {}).value || '').trim()) errors.push('Enter your phone number.');
    if (!((form.querySelector('#q-email') || {}).value || '').trim()) errors.push('Enter your email.');
    if (!((form.querySelector('#q-postcode') || {}).value || '').trim()) errors.push('Enter your postcode.');
    if (!q.anyService) errors.push('Select at least one service.');
    if (needsHouseSize() && !q.size) errors.push('Select your house size.');
    return errors;
  }

  function buildEmailBody(q) {
    var name = (form.querySelector('#q-name') || {}).value || '';
    var phone = (form.querySelector('#q-phone') || {}).value || '';
    var email = (form.querySelector('#q-email') || {}).value || '';
    var postcode = (form.querySelector('#q-postcode') || {}).value || '';
    var notes = (form.querySelector('#q-notes') || {}).value || '';
    var sizeLabel = q.size && SIZE_LABELS[q.size] ? SIZE_LABELS[q.size] : '(not selected)';

    var lineText = q.lines
      .map(function (line) {
        var amt;
        if (line.measure) amt = 'measure on site';
        else if (line.pending) amt = line.display;
        else if (line.careOff && line.pre != null) {
          amt = money(line.amount) + ' (was ' + money(line.pre) + ', care plan 15% off)';
        } else amt = money(line.amount);
        return '- ' + line.label + ': ' + amt;
      })
      .join('\n');

    var totalText = q.total > 0 ? money(q.total) : 'measure on site';
    var stamp = new Date().toLocaleString('en-GB', { timeZone: 'Europe/London' });

    return [
      'Name: ' + name,
      'Phone: ' + phone,
      'Email: ' + email,
      'Postcode: ' + postcode,
      'House size: ' + sizeLabel,
      '',
      'Selected services:',
      lineText || '(none)',
      '',
      'Guide total: ' + totalText,
      '',
      'Notes:',
      notes || '(none)',
      '',
      'Submitted: ' + stamp + ' (UK)'
    ].join('\n');
  }

  function subjectLine(q, postcode) {
    var totalBit = q.total > 0 ? 'guide ' + money(q.total) : 'measure on site';
    return 'Quote enquiry — ' + (postcode || 'no postcode') + ' — ' + totalBit;
  }

  function showSuccess(msg) {
    if (successEl) {
      successEl.textContent = msg;
      successEl.classList.add('is-visible');
    }
    if (errorEl) {
      errorEl.textContent = '';
      errorEl.classList.remove('is-visible');
    }
  }

  function showError(msg) {
    if (errorEl) {
      errorEl.textContent = msg;
      errorEl.classList.add('is-visible');
    }
    if (successEl) successEl.classList.remove('is-visible');
  }

  function mailtoFallback(q) {
    var postcode = ((form.querySelector('#q-postcode') || {}).value || '').trim();
    window.location.href =
      'mailto:' +
      JOE_EMAIL +
      '?subject=' +
      encodeURIComponent(subjectLine(q, postcode)) +
      '&body=' +
      encodeURIComponent(buildEmailBody(q));
    showSuccess(
      'Your email app should open with the quote details. If it doesn’t, email ' +
        JOE_EMAIL +
        ' or call 07494 503865.'
    );
  }

  function submitWeb3Forms(key, q) {
    var name = (form.querySelector('#q-name') || {}).value || '';
    var email = (form.querySelector('#q-email') || {}).value || '';
    var phone = (form.querySelector('#q-phone') || {}).value || '';
    var postcode = ((form.querySelector('#q-postcode') || {}).value || '').trim();
    return fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        access_key: key,
        subject: subjectLine(q, postcode),
        from_name: name,
        name: name,
        email: email,
        phone: phone,
        postcode: postcode,
        message: buildEmailBody(q)
      })
    }).then(function (res) {
      return res.json().then(function (data) {
        if (!res.ok || data.success === false) {
          throw new Error((data && data.message) || 'Submit failed');
        }
        return data;
      });
    });
  }

  if (svcGutter) {
    svcGutter.addEventListener('change', function () {
      if (svcGutter.checked && svcCare) svcCare.checked = false;
      render();
    });
  }
  if (svcCare) {
    svcCare.addEventListener('change', function () {
      if (svcCare.checked && svcGutter) svcGutter.checked = false;
      render();
    });
  }

  form.addEventListener('change', function () { render(); });
  form.addEventListener('input', function () { render(); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var q = render();
    var errors = validate(q);
    if (errors.length) {
      showError(errors.join(' '));
      return;
    }

    var key = getAccessKey();
    var btn = form.querySelector('[type="submit"]');
    if (btn) btn.disabled = true;

    if (!key) {
      mailtoFallback(q);
      if (btn) btn.disabled = false;
      return;
    }

    submitWeb3Forms(key, q)
      .then(function () {
        showSuccess(
          'Thanks. We’ve sent your guide estimate to Dimension Exterior Cleaning. We’ll confirm the final price before work starts.'
        );
        form.reset();
        var fasciasOnly = form.querySelector('#fascias-only');
        if (fasciasOnly) fasciasOnly.checked = true;
        render();
      })
      .catch(function () {
        mailtoFallback(q);
      })
      .finally(function () {
        if (btn) btn.disabled = false;
      });
  });

  render();
})();
