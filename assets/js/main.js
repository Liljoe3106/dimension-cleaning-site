(function () {
  'use strict';

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (!open) {
        document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
          d.classList.remove('open');
          var btn = d.querySelector('button');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        });
      }
    });
  }

  document.querySelectorAll('.nav-dropdown > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var parent = btn.parentElement;
      var willOpen = !parent.classList.contains('open');
      document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
        if (d !== parent) {
          d.classList.remove('open');
          var b = d.querySelector('button');
          if (b) b.setAttribute('aria-expanded', 'false');
        }
      });
      parent.classList.toggle('open', willOpen);
      btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
        d.classList.remove('open');
        var b = d.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
        d.classList.remove('open');
        var b = d.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
      if (nav && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      }
    }
  });

  // Contact form → mailto fallback
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = (form.querySelector('[name="name"]') || {}).value || '';
      var phone = (form.querySelector('[name="phone"]') || {}).value || '';
      var email = (form.querySelector('[name="email"]') || {}).value || '';
      var postcode = (form.querySelector('[name="postcode"]') || {}).value || '';
      var service = (form.querySelector('[name="service"]') || {}).value || '';
      var message = (form.querySelector('[name="message"]') || {}).value || '';

      var subject = 'Quote request' + (service ? ' — ' + service : '') + (postcode ? ' (' + postcode + ')' : '');
      var body = [
        'Name: ' + name,
        'Phone: ' + phone,
        'Email: ' + email,
        'Postcode: ' + postcode,
        'Service: ' + service,
        '',
        'Message:',
        message
      ].join('\n');

      var mailto =
        'mailto:joe@dimensioncleaning.co.uk' +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);

      var success = document.getElementById('form-success');
      if (success) {
        success.textContent = 'Your email app should open… If it doesn’t, email joe@dimensioncleaning.co.uk or call 07494 503865.';
        success.classList.add('is-visible');
      }

      window.location.href = mailto;
    });
  }

  // Before/after gallery sliders
  function initGallerySliders() {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var mq = window.matchMedia('(min-width: 641px)');

    document.querySelectorAll('[data-gallery-slider]').forEach(function (root) {
      var track = root.querySelector('.gallery-slider__track');
      var slides = Array.prototype.slice.call(root.querySelectorAll('.gallery-slider__slide'));
      var dotsWrap = root.querySelector('.gallery-slider__dots');
      var prevBtn = root.querySelector('.gallery-slider__btn--prev');
      var nextBtn = root.querySelector('.gallery-slider__btn--next');
      if (!track || !slides.length || !dotsWrap) return;

      if (reduced) root.classList.add('is-reduced');

      var page = 0;
      var pageSize = 1;

      function computePageSize() {
        return mq.matches ? 2 : 1;
      }

      function maxPage() {
        return Math.max(0, Math.ceil(slides.length / pageSize) - 1);
      }

      function applyTransform() {
        var gap = 16; // matches 1rem gap in CSS
        var slideWidth = slides[0].getBoundingClientRect().width;
        var offset = page * pageSize * (slideWidth + gap);
        track.style.transform = 'translateX(-' + offset + 'px)';
      }

      function updateDots() {
        var buttons = dotsWrap.querySelectorAll('.gallery-slider__dot');
        buttons.forEach(function (btn, i) {
          var active = i === page;
          btn.classList.toggle('is-active', active);
          btn.setAttribute('aria-selected', active ? 'true' : 'false');
          btn.tabIndex = active ? 0 : -1;
        });
      }

      function buildDots() {
        dotsWrap.innerHTML = '';
        var pageCount = maxPage() + 1;
        if (pageCount <= 1) {
          dotsWrap.hidden = true;
          return;
        }
        dotsWrap.hidden = false;
        for (var i = 0; i < pageCount; i++) {
          (function (idx) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'gallery-slider__dot';
            btn.setAttribute('role', 'tab');
            btn.setAttribute('aria-label', 'Show photo page ' + (idx + 1));
            btn.addEventListener('click', function () {
              goTo(idx);
            });
            dotsWrap.appendChild(btn);
          })(i);
        }
        updateDots();
      }

      function goTo(next) {
        var pageCount = maxPage() + 1;
        if (pageCount <= 0) return;
        page = ((next % pageCount) + pageCount) % pageCount;
        applyTransform();
        updateDots();
      }

      function refresh() {
        pageSize = computePageSize();
        if (page > maxPage()) page = maxPage();
        buildDots();
        applyTransform();
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', function () {
          goTo(page - 1);
        });
      }
      if (nextBtn) {
        nextBtn.addEventListener('click', function () {
          goTo(page + 1);
        });
      }

      root.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') {
          e.preventDefault();
          goTo(page - 1);
        } else if (e.key === 'ArrowRight') {
          e.preventDefault();
          goTo(page + 1);
        }
      });

      var touchStartX = null;
      var touchStartY = null;
      root.addEventListener('touchstart', function (e) {
        if (!e.changedTouches || !e.changedTouches.length) return;
        touchStartX = e.changedTouches[0].clientX;
        touchStartY = e.changedTouches[0].clientY;
      }, { passive: true });
      root.addEventListener('touchend', function (e) {
        if (touchStartX == null || !e.changedTouches || !e.changedTouches.length) return;
        var dx = e.changedTouches[0].clientX - touchStartX;
        var dy = e.changedTouches[0].clientY - touchStartY;
        touchStartX = null;
        touchStartY = null;
        if (Math.abs(dx) < 40 || Math.abs(dx) < Math.abs(dy)) return;
        if (dx < 0) goTo(page + 1);
        else goTo(page - 1);
      }, { passive: true });

      var resizeTimer = null;
      window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(refresh, 120);
      });
      if (typeof mq.addEventListener === 'function') {
        mq.addEventListener('change', refresh);
      } else if (typeof mq.addListener === 'function') {
        mq.addListener(refresh);
      }

      root.querySelectorAll('img').forEach(function (img) {
        if (!img.complete) {
          img.addEventListener('load', function () {
            applyTransform();
          });
        }
      });

      refresh();
    });
  }

// Gallery lightbox
  function initGalleryLightbox() {
    var overlay = null;
    var lastFocus = null;

    function ensureOverlay() {
      if (overlay) return overlay;
      overlay = document.createElement('div');
      overlay.className = 'lightbox';
      overlay.hidden = true;
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      overlay.setAttribute('aria-label', 'Photo viewer');
      overlay.innerHTML =
        '<div class="lightbox__backdrop" data-lightbox-close></div>' +
        '<div class="lightbox__panel" role="document">' +
        '<button type="button" class="lightbox__close" aria-label="Close photo" data-lightbox-close>&times;</button>' +
        '<div class="lightbox__media"></div>' +
        '<p class="lightbox__caption"></p>' +
        '</div>';
      document.body.appendChild(overlay);
      overlay.addEventListener('click', function (e) {
        if (e.target.closest('[data-lightbox-close]')) closeLightbox();
      });
      return overlay;
    }

    function trapFocus(e) {
      if (!overlay || overlay.hidden || e.key !== 'Tab') return;
      var focusables = overlay.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!focusables.length) return;
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }

    function closeLightbox() {
      if (!overlay || overlay.hidden) return;
      overlay.hidden = true;
      document.body.classList.remove('lightbox-open');
      document.removeEventListener('keydown', onKey);
      if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
      lastFocus = null;
    }

    function onKey(e) {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeLightbox();
        return;
      }
      trapFocus(e);
    }

    function openFromButton(btn) {
      var figure = btn.closest('figure');
      var captionEl = figure ? figure.querySelector('figcaption span, figcaption') : null;
      var caption = captionEl ? captionEl.textContent.trim() : (btn.getAttribute('aria-label') || '');
      var pictures = btn.querySelectorAll('picture, img');
      var media = ensureOverlay().querySelector('.lightbox__media');
      var cap = overlay.querySelector('.lightbox__caption');
      media.innerHTML = '';
      media.className = 'lightbox__media' + (pictures.length > 1 ? ' lightbox__media--pair' : '');

      function addImg(node) {
        var img = node.tagName === 'IMG' ? node : node.querySelector('img');
        if (!img) return;
        var clone = document.createElement('img');
        clone.src = img.currentSrc || img.src;
        clone.alt = img.alt || caption;
        clone.loading = 'eager';
        media.appendChild(clone);
      }

      if (pictures.length) {
        pictures.forEach(addImg);
      }
      cap.textContent = caption;
      lastFocus = document.activeElement;
      overlay.hidden = false;
      document.body.classList.add('lightbox-open');
      document.addEventListener('keydown', onKey);
      var closeBtn = overlay.querySelector('.lightbox__close');
      if (closeBtn) closeBtn.focus();
    }

    document.querySelectorAll('.gallery-zoom').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        // Avoid fighting slider swipe: ignore if moved a lot after pointerdown
        e.preventDefault();
        openFromButton(btn);
      });
    });
  }

  function boot() {
    initGallerySliders();
    initGalleryLightbox();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
