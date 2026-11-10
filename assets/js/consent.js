(function () {
  'use strict';

  // Cookie consent gate for the Meta pixel.
  // Nothing from connect.facebook.net loads until the visitor presses Accept.
  var KEY = 'dimConsent';
  var PIXEL_ID = '2567338176850451';

  function getChoice() {
    try { return window.localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setChoice(v) {
    try { window.localStorage.setItem(KEY, v); } catch (e) { /* ignore */ }
  }
  function clearChoice() {
    try { window.localStorage.removeItem(KEY); } catch (e) { /* ignore */ }
  }

  window.dimConsentGranted = function () { return getChoice() === 'granted'; };

  var pixelLoaded = false;
  function loadPixel() {
    if (pixelLoaded || getChoice() !== 'granted') return;
    pixelLoaded = true;
    /* Meta Pixel base code */
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', PIXEL_ID);
    window.fbq('track', 'PageView');
  }

  var banner = null;
  function hideBanner() {
    if (banner) banner.hidden = true;
    document.body.classList.remove('has-consent-banner');
  }
  function showBanner() {
    if (!banner) {
      banner = document.createElement('div');
      banner.className = 'consent-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', 'Cookie choice');
      banner.innerHTML =
        '<p class="consent-banner__text">We use an advertising cookie to see which ads bring enquiries. Is that OK?</p>' +
        '<div class="consent-banner__actions">' +
        '<button type="button" class="consent-btn" data-consent="granted">Accept</button>' +
        '<button type="button" class="consent-btn" data-consent="denied">Decline</button>' +
        '</div>';
      banner.addEventListener('click', function (e) {
        var b = e.target.closest && e.target.closest('[data-consent]');
        if (!b) return;
        var v = b.getAttribute('data-consent');
        setChoice(v);
        hideBanner();
        if (v === 'granted') loadPixel();
      });
      document.body.appendChild(banner);
    }
    banner.hidden = false;
    document.body.classList.add('has-consent-banner');
  }

  function boot() {
    var c = getChoice();
    if (c === 'granted') loadPixel();
    else if (c !== 'denied') showBanner();

    document.querySelectorAll('[data-consent-reset]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        clearChoice();
        showBanner();
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
