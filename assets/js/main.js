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
})();
