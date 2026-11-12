/* نمونه کار — رفتارهای مشترک وب‌سایت آریا صنعت توان */
(function () {
  'use strict';

  var reducedMotion = (typeof window.matchMedia === 'function') &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- منوی موبایل (همبرگر) ---------- */
  var menuBtn = document.querySelector('.menu-btn');
  var mainNav = document.querySelector('header nav');
  if (menuBtn && mainNav) {
    menuBtn.addEventListener('click', function () {
      var open = mainNav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'بستن منو' : 'باز کردن منو');
      menuBtn.textContent = open ? '✕' : '☰';
    });
    mainNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mainNav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.setAttribute('aria-label', 'باز کردن منو');
        menuBtn.textContent = '☰';
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mainNav.classList.contains('open')) {
        mainNav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.textContent = '☰';
        menuBtn.focus();
      }
    });
  }

  /* ---------- نمایش تدریجی بخش‌ها (یک IntersectionObserver، یک‌بار، بدون JS همه دیده می‌شود) ---------- */
  var revealEls = document.querySelectorAll('.reveal, .cards > .card, .cards > .tile');
  if ('IntersectionObserver' in window && !reducedMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- شمارش اعداد اعتماد (۷۰۰ میلی‌ثانیه، فقط یک‌بار، با رقم فارسی) ---------- */
  function faNum(n) { return n.toLocaleString('fa-IR'); }
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var suffix = el.getAttribute('data-suffix') || '';
    function render(v) { el.textContent = faNum(v) + suffix; }
    if (reducedMotion || !('IntersectionObserver' in window)) { render(target); return; }
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(el);
        var start = null;
        (function tick(ts) {
          if (start === null) start = ts;
          var p = Math.min(1, (ts - start) / 700);
          render(Math.round(target * p));
          if (p < 1) window.requestAnimationFrame(tick);
        })(performance.now());
      });
    }, { threshold: 0.4 });
    cio.observe(el);
  });

  /* ---------- زبانه‌های مرکز خدمات ---------- */
  document.querySelectorAll('[data-tabs]').forEach(function (group) {
    var buttons = group.querySelectorAll('.tab');
    var scope = group.getAttribute('data-tabs');
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.getAttribute('data-cat');
        document.querySelectorAll('[data-scope="' + scope + '"]').forEach(function (tile) {
          var cats = (tile.getAttribute('data-cat') || '').split(' ');
          tile.style.display = (cat === 'all' || cats.indexOf(cat) !== -1) ? '' : 'none';
        });
      });
    });
  });

  /* ---------- کاروسل افقی ---------- */
  document.querySelectorAll('[data-scroll]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = document.getElementById(btn.getAttribute('data-scroll'));
      if (!target) return;
      var step = target.clientWidth * 0.8;
      target.scrollBy({ left: btn.getAttribute('data-dir') === 'next' ? -step : step, behavior: 'smooth' });
    });
  });

  /* ---------- کاتالوگ محصولات ----------
     مدل‌ها واقعی‌اند و مشخصات از برگه فنی سازنده گرفته شده است؛
     «آریا صنعت توان» نام نمایشی شرکت در این نمونه کار است. */
  var PRODUCTS = [
    { id: 'AT-2500', cat: 'transformer', catFa: 'ترانسفورماتور', brand: 'زیمنس', name: 'ترانسفورماتور خشک رزینی جیافول ۲۵۰۰', desc: 'ترانسفورماتور خشک رزینی بدون روغن، مناسب نصب در فضای بسته و ساختمان‌ها.', volt: '۲۰ / ۰٫۴ کیلوولت', power: '۲۵۰۰ کیلوولت‌آمپر', acc: 'کلاس حرارتی F', key: 'گروه برداری Dyn11', warranty: '۲۴ ماه', stock: 'موجود', art: '⚡', tint: '#eaf2fa' },
    { id: 'AT-1600', cat: 'transformer', catFa: 'ترانسفورماتور', brand: 'ای‌بی‌بی', name: 'ترانسفورماتور توزیع روغنی ۱۶۰۰', desc: 'ترانسفورماتور توزیع روغنی سه‌فاز با خنک‌کاری طبیعی، مناسب شبکه‌های توزیع شهری و صنعتی.', volt: '۲۲ / ۰٫۴ کیلوولت', power: '۱۶۰۰ کیلوولت‌آمپر', acc: 'تلفات بی‌باری ۲۴۰۰ وات', key: 'تلفات بارداری ۱۷۷۰۰ وات در ۷۵ درجه', warranty: '۲۴ ماه', stock: 'موجود', art: '🔌', tint: '#fef6e7' },
    { id: 'AT-33', cat: 'transformer', catFa: 'ترانسفورماتور', brand: 'ای‌بی‌بی', name: 'ترانسفورماتور ولتاژ تک‌فاز تی‌جی‌سی ۷', desc: 'ترانسفورماتور ولتاژ تک‌فاز با عایق رزینی، برای اندازه‌گیری و حفاظت در پست‌های فشار متوسط.', volt: '۳۳/√۳ کیلوولت به ۱۱۰/√۳ ولت', power: 'بار نامی ۱۰۰ ولت‌آمپر', acc: 'کلاس ۰٫۵', key: 'وزن ۵۰ کیلوگرم', warranty: '۱۸ ماه', stock: 'موجود', art: '📐', tint: '#eafaf1' },
    { id: 'TT-5000', cat: 'test', catFa: 'تجهیزات آزمون', brand: 'مگر', name: 'دستگاه آزمون عایقی MIT515', desc: 'آزمون مقاومت عایقی با ولتاژ آزمون تا ۵ کیلوولت، برای نگهداری تجهیزات فشار قوی.', volt: 'ولتاژ آزمون ۲۵۰ تا ۵۰۰۰ ولت', power: 'مقاومت تا ۱۰ ترااهم', acc: '±۵٪ تا ۱ ترااهم', key: 'رده CAT IV 600 ولت', warranty: '۱۲ ماه', stock: 'موجود', art: '🧪', tint: '#f1eafe' },
    { id: 'TT-100', cat: 'test', catFa: 'تجهیزات آزمون', brand: 'مگر', name: 'اهم‌متر ترانسفورماتور MTO210', desc: 'اندازه‌گیری مقاومت مستقیم سیم‌پیچ ترانسفورماتور و موتور با جریان آزمون تا ۱۰ آمپر.', volt: 'تغذیه ۸۵ تا ۲۶۴ ولت', power: 'جریان آزمون تا ۱۰ آمپر', acc: '±۰٫۲۵٪', key: 'بازه ۱۰ میکرواهم تا ۲۰۰۰ اهم', warranty: '۱۲ ماه', stock: 'موجود', art: '🎛️', tint: '#eaf2fa' },
    { id: 'TT-REL', cat: 'test', catFa: 'تجهیزات آزمون', brand: 'اومیکرون', name: 'مجموعه آزمون رله CMC 356', desc: 'مجموعه آزمون رله حفاظتی با شش خروجی جریان و چهار خروجی ولتاژ، برای آزمون همه نسل‌های رله.', volt: 'خروجی ولتاژ ۴×۳۰۰ ولت', power: 'خروجی جریان تا ۳×۶۴ آمپر', acc: 'خطا کمتر از ۰٫۰۸٪', key: 'تغذیه مستقیم ۰ تا ۲۶۴ ولت', warranty: '۱۸ ماه', stock: 'سفارش ۲ هفته‌ای', art: '🛠️', tint: '#fef6e7' },
    { id: 'CB-20', cat: 'cable', catFa: 'کابل و سیم', brand: 'پریسمیان', name: 'کابل قدرت N2XS2Y', desc: 'کابل قدرت سه‌رشته با عایق پلی‌اتیلن شبکه‌ای برای شبکه‌های فشار متوسط.', volt: '۱۲ / ۲۰ کیلوولت', power: '۳×۱۸۵ میلی‌متر مربع', acc: 'مقاومت هادی ۰٫۰۹۹۱ اهم بر کیلومتر', key: 'هادی مس، عایق پلی‌اتیلن شبکه‌ای', warranty: '۱۲ ماه', stock: 'موجود', art: '🔗', tint: '#eafaf1' },
    { id: 'CB-C', cat: 'cable', catFa: 'کابل و سیم', brand: 'لپ', name: 'کابل کنترل اولفلکس کلاسیک ۱۱۰', desc: 'کابل کنترل ۱۲ رشته با رشته‌های شماره‌دار، برای مدارهای فرمان ماشین‌ها و تابلوها.', volt: '۳۰۰ / ۵۰۰ ولت', power: '۱۲×۱٫۵ میلی‌متر مربع', acc: 'ولتاژ آزمون ۴ کیلوولت', key: 'قطر خارجی ۱۲ میلی‌متر', warranty: '۱۲ ماه', stock: 'موجود', art: '🧵', tint: '#f1eafe' },
    { id: 'CB-I', cat: 'cable', catFa: 'کابل و سیم', brand: 'لپ', name: 'کابل کنترل شیلددار اولفلکس کلاسیک ۱۱۰', desc: 'کابل کنترل شیلددار با بافت مسی قلع‌اندود، برای مدارهای فرمان در محیط‌های پرنویز.', volt: '۳۰۰ / ۵۰۰ ولت', power: '۱۲×۱٫۵ میلی‌متر مربع', acc: 'ولتاژ آزمون ۴ کیلوولت', key: 'شیلد بافت مسی قلع‌اندود', warranty: '۱۲ ماه', stock: 'موجود', art: '📡', tint: '#eaf2fa' },
    { id: 'SW-24', cat: 'switch', catFa: 'کلید و حفاظت', brand: 'زیمنس', name: 'کلید خلأ 3AH5', desc: 'کلید خلأ فشار متوسط با مکانیزم فنری، مناسب تابلوهای فشار متوسط و پست‌های توزیع.', volt: '۲۴ کیلوولت', power: 'جریان نامی ۱۲۵۰ آمپر', acc: 'قدرت قطع ۲۵ کیلوآمپر', key: 'ولتاژ ضربه ۱۲۵ کیلوولت', warranty: '۲۴ ماه', stock: 'موجود', art: '🔋', tint: '#fef6e7' },
    { id: 'SW-R', cat: 'switch', catFa: 'کلید و حفاظت', brand: 'ای‌بی‌بی', name: 'رله حفاظتی فیدر REF615', desc: 'رله حفاظتی دیجیتال فیدر با حفاظت اضافه‌جریان، خطای زمین و ثبت رویداد.', volt: 'تغذیه ۸۰ تا ۲۵۰ ولت مستقیم', power: 'ورودی جریان ۱ / ۵ آمپر', acc: 'دقت اندازه‌گیری ±۰٫۵٪', key: 'وزن ۳٫۵ کیلوگرم', warranty: '۲۴ ماه', stock: 'موجود', art: '🛡️', tint: '#eafaf1' },
    { id: 'SW-33', cat: 'switch', catFa: 'کلید و حفاظت', brand: 'زیمنس', name: 'سکسیونر 3DC', desc: 'سکسیونر سه‌پل با عایق رزینی، برای قطع و وصل خطوط فشار متوسط و حفاظت پرسنل.', volt: '۳۶ کیلوولت', power: 'جریان نامی ۶۳۰ آمپر', acc: 'جریان کوتاه‌مدت ۲۰ کیلوآمپر', key: 'ولتاژ ضربه ۱۷۰ کیلوولت', warranty: '۱۸ ماه', stock: 'سفارش ۳ هفته‌ای', art: '🗼', tint: '#f1eafe' },
    { id: 'MT-87', cat: 'measure', catFa: 'ابزار اندازه‌گیری', brand: 'فلوک', name: 'مولتی‌متر صنعتی 87V', desc: 'مولتی‌متر دیجیتال صنعتی با اندازه‌گیری ولتاژ، جریان، مقاومت و ظرفیت.', volt: 'تا ۱۰۰۰ ولت', power: 'جریان تا ۱۰ آمپر', acc: 'دقت ولتاژ مستقیم ±(۰٫۰۵٪ + ۱)', key: 'وزن ۳۵۵ گرم', warranty: '۱۲ ماه', stock: 'موجود', art: '📟', tint: '#eaf2fa' },
    { id: 'MT-C', cat: 'measure', catFa: 'ابزار اندازه‌گیری', brand: 'فلوک', name: 'کلمپ‌متر 376 FC', desc: 'کلمپ‌متر با پروب انعطاف‌پذیر همراه، برای اندازه‌گیری جریان‌های بالا بدون قطع مدار.', volt: 'تا ۱۰۰۰ ولت', power: 'جریان با دهانه تا ۱۰۰۰ آمپر', acc: 'دقت جریان دهانه ۲٪ ±۵ رقم', key: 'با پروب انعطاف‌پذیر تا ۲۵۰۰ آمپر', warranty: '۱۲ ماه', stock: 'موجود', art: '🧲', tint: '#fef6e7' },
    { id: 'MT-Q', cat: 'measure', catFa: 'ابزار اندازه‌گیری', brand: 'فلوک', name: 'تحلیل‌گر کیفیت توان 1775', desc: 'تحلیل‌گر کیفیت توان سه‌فاز با ثبت هارمونیک، افت ولتاژ و گذرای سریع.', volt: 'ورودی تا ۱۰۰۰ ولت', power: '۴ ورودی ولتاژ + ۴ ورودی جریان', acc: 'کلاس ای', key: 'گذرا تا ۸ کیلوولت با نمونه‌برداری ۱ مگاهرتز', warranty: '۱۸ ماه', stock: 'موجود', art: '📊', tint: '#eafaf1' }
  ];

  var grid = document.getElementById('productGrid');
  if (grid) {
    var compareSet = [];
    var activeCat = 'all';
    var query = '';
    var sortMode = 'name';

    function cardHTML(p) {
      var checked = compareSet.indexOf(p.id) !== -1 ? ' checked' : '';
      var stockCls = p.stock === 'موجود' ? '' : ' out';
      return '<article class="pcard" data-cat="' + p.cat + '">' +
        '<div class="art" style="background:' + p.tint + '"><span class="art-cat">' + p.catFa + '</span><span class="art-model">' + p.id + '</span><span class="art-brand">سازنده: ' + p.brand + '</span></div>' +
        '<div class="body">' +
        '<span class="cat">' + p.catFa + '</span>' +
        '<h3>' + p.name + '</h3>' +
        '<span class="model">' + p.id + '</span>' +
        '<span class="brand">سازنده: ' + p.brand + '</span>' +
        '<p class="spec">' + p.desc + '</p>' +
        '<p class="spec"><strong>ولتاژ نامی:</strong> ' + p.volt + ' &nbsp;|&nbsp; <strong>توان:</strong> ' + p.power + '</p>' +
        '<p class="spec"><strong>ویژگی کلیدی:</strong> ' + p.key + '</p>' +
        '<span class="stock' + stockCls + '">● ' + p.stock + '</span>' +
        '<div class="actions">' +
        '<a class="btn btn-small" href="contact.html?product=' + p.id + '">استعلام قیمت</a>' +
        '<a class="link-btn" href="datasheets/' + p.id + '.pdf" download target="_blank" rel="noopener">برگه مشخصات</a>' +
        '</div>' +
        '<label style="font-size:13px;color:#475569;margin-top:4px"><input type="checkbox" data-compare="' + p.id + '"' + checked + '> افزودن به مقایسه</label>' +
        '</div></article>';
    }

    function render() {
      var list = PRODUCTS.filter(function (p) {
        var catOk = activeCat === 'all' || p.cat === activeCat;
        var q = query.trim();
        var qOk = !q || p.name.indexOf(q) !== -1 || p.brand.indexOf(q) !== -1 || p.id.toLowerCase().indexOf(q.toLowerCase()) !== -1 || p.catFa.indexOf(q) !== -1;
        return catOk && qOk;
      });
      if (sortMode === 'cat') {
        list.sort(function (a, b) { return a.catFa.localeCompare(b.catFa, 'fa') || a.name.localeCompare(b.name, 'fa'); });
      } else if (sortMode === 'brand') {
        list.sort(function (a, b) { return a.brand.localeCompare(b.brand, 'fa') || a.name.localeCompare(b.name, 'fa'); });
      } else {
        list.sort(function (a, b) { return a.name.localeCompare(b.name, 'fa'); });
      }
      grid.innerHTML = list.map(cardHTML).join('');
      document.getElementById('emptyState').style.display = list.length ? 'none' : 'block';
      document.getElementById('resultCount').textContent = 'نمایش ' + list.length + ' محصول از ۱۵ محصول';
      bindCompareBoxes();
    }

    function bindCompareBoxes() {
      grid.querySelectorAll('[data-compare]').forEach(function (box) {
        box.addEventListener('change', function () {
          var id = box.getAttribute('data-compare');
          if (box.checked) {
            if (compareSet.length >= 3) {
              box.checked = false;
              alert('برای مقایسه، حداکثر ۳ محصول را انتخاب کنید.');
              return;
            }
            compareSet.push(id);
          } else {
            compareSet = compareSet.filter(function (x) { return x !== id; });
          }
          updateCompareBar();
        });
      });
    }

    function updateCompareBar() {
      var bar = document.getElementById('compareBar');
      var label = document.getElementById('compareCount');
      if (compareSet.length >= 2) {
        bar.classList.add('show');
        label.textContent = compareSet.length + ' محصول انتخاب شده — برای مشاهده جدول مقایسه، دکمه را بزنید.';
      } else {
        bar.classList.remove('show');
        label.textContent = compareSet.length + ' محصول انتخاب شده — دست‌کم ۲ محصول را برای مقایسه انتخاب کنید.';
        if (compareSet.length < 2) document.getElementById('compareWrap').style.display = 'none';
      }
    }

    document.querySelectorAll('#catTabs .tab').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('#catTabs .tab').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        activeCat = btn.getAttribute('data-cat');
        render();
      });
    });

    /* پیش‌انتخاب دسته از نشانی، برای پیوند عمیق از صفحه اصلی */
    var catParam = new URLSearchParams(window.location.search).get('cat');
    if (catParam) {
      var tabBtn = document.querySelector('#catTabs .tab[data-cat="' + catParam + '"]');
      if (tabBtn) {
        document.querySelectorAll('#catTabs .tab').forEach(function (b) { b.classList.remove('active'); });
        tabBtn.classList.add('active');
        activeCat = catParam;
      }
    }

    var search = document.getElementById('productSearch');
    if (search) search.addEventListener('input', function () { query = search.value; render(); });
    var sort = document.getElementById('productSort');
    if (sort) sort.addEventListener('change', function () { sortMode = sort.value; render(); });

    document.getElementById('showCompare').addEventListener('click', function () {
      var rows = [
        ['دسته', 'catFa'], ['سازنده', 'brand'], ['ولتاژ نامی', 'volt'], ['توان / ظرفیت', 'power'],
        ['دقت', 'acc'], ['ویژگی کلیدی', 'key'], ['گارانتی', 'warranty'], ['وضعیت موجودی', 'stock']
      ];
      var sel = compareSet.map(function (id) { return PRODUCTS.find(function (p) { return p.id === id; }); });
      var html = '<table class="compare"><tr><th>مشخصه</th>' +
        sel.map(function (p) { return '<th>' + p.name + '<br><span style="font-weight:normal;font-size:12px">' + p.id + '</span></th>'; }).join('') + '</tr>';
      rows.forEach(function (r) {
        html += '<tr><td>' + r[0] + '</td>' + sel.map(function (p) { return '<td>' + p[r[1]] + '</td>'; }).join('') + '</tr>';
      });
      html += '<tr><td>برگه مشخصات</td>' + sel.map(function (p) {
        return '<td><a class="link-btn" href="datasheets/' + p.id + '.pdf" download target="_blank" rel="noopener">دانلود برگه مشخصات</a></td>';
      }).join('') + '</tr>';
      html += '<tr><td>استعلام</td>' + sel.map(function (p) {
        return '<td><a class="btn btn-small" href="contact.html?product=' + p.id + '">استعلام قیمت</a></td>';
      }).join('') + '</tr></table>';
      var wrap = document.getElementById('compareWrap');
      wrap.innerHTML = html;
      wrap.style.display = 'block';
      if (wrap.scrollIntoView) wrap.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });

    document.getElementById('clearCompare').addEventListener('click', function () {
      compareSet = [];
      document.getElementById('compareWrap').style.display = 'none';
      updateCompareBar();
      render();
    });

    render();
  }

  /* ---------- فرم تماس و استعلام ---------- */
  var form = document.getElementById('inquiryForm');
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('product');
    if (pre) {
      var sel = document.getElementById('product');
      if (sel && sel.querySelector('option[value="' + pre + '"]')) sel.value = pre;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      function check(id, errId, valid) {
        var el = document.getElementById(id);
        var err = document.getElementById(errId);
        if (valid) { el.classList.remove('invalid'); err.style.display = 'none'; }
        else { el.classList.add('invalid'); err.style.display = 'block'; ok = false; }
      }
      var name = document.getElementById('name').value.trim();
      var phone = document.getElementById('phone').value.trim();
      var email = document.getElementById('email').value.trim();
      var qty = document.getElementById('qty').value.trim();
      var msg = document.getElementById('message').value.trim();
      check('name', 'nameError', name.length >= 2);
      check('phone', 'phoneError', /^09[0-9]{9}$/.test(phone.replace(/[\s-]/g, '')));
      check('email', 'emailError', !email || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email));
      check('qty', 'qtyError', !qty || (/^[0-9]+$/.test(qty) && parseInt(qty, 10) > 0));
      check('message', 'messageError', msg.length >= 10);
      if (!ok) return;
      var code = 'AST-1405-' + Math.floor(1000 + Math.random() * 9000);
      document.getElementById('trackCode').textContent = code;
      document.getElementById('successBox').style.display = 'block';
      var sb = document.getElementById('successBox');
      if (sb.scrollIntoView) sb.scrollIntoView({ behavior: 'smooth', block: 'center' });
      form.reset();
    });
  }
})();
