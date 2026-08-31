(function () {
  'use strict';
  const THEME_KEY = 'mllessons-theme';
  const html = document.documentElement;
  const toggle = document.getElementById('themeToggle');
  function applyTheme(t) {
    html.setAttribute('data-theme', t);
    try { localStorage.setItem(THEME_KEY, t); } catch (e) {}
    if (toggle) { const i = toggle.querySelector('i'); i.className = t === 'dark' ? 'bi bi-sun' : 'bi bi-moon-stars'; }
  }
  function currentTheme() { try { return localStorage.getItem(THEME_KEY) || 'light'; } catch (e) { return 'light'; } }
  applyTheme(currentTheme());
  if (toggle) { toggle.addEventListener('click', function () { applyTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'); }); }
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.lesson-card');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      cards.forEach(function (c) {
        var show = f === 'all' || c.getAttribute('data-series') === f;
        c.style.display = show ? '' : 'none';
      });
    });
  });
})();
