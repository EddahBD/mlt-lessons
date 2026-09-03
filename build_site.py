# -*- coding: utf-8 -*-
"""Build index.html + 50 video pages with correct numbering and titles."""
import os, re
from lessons_data import LESSONS

REPO = os.path.dirname(os.path.abspath(__file__))
VIDEO_DIR = os.path.join(REPO, 'video')

def slug(title):
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    return re.sub(r'[\s]+', '-', s).strip('-')

def fname(n, vid_id, title):
    return f'lesson-{n}-{slug(title)}.html'

# Pre-build sidebar HTML (all 50 lessons)
def sidebar_html(active_n=None):
    items = []
    for n in range(1, 51):
        vid_id, title, series = LESSONS[n]
        fn = fname(n, vid_id, title)
        cls = ' active' if n == active_n else ''
        label = f'{n}. {title}'
        if vid_id:
            items.append(f'<a href="../video/{fn}" class="lesson-item{cls}" style="text-decoration:none;"><span class="num">{n}</span><span class="flex-grow-1 small" style="font-weight:600;">{label}</span></a>')
        else:
            items.append(f'<span class="lesson-item" style="text-decoration:none;opacity:0.5;cursor:default;"><span class="num">{n}</span><span class="flex-grow-1 small" style="font-weight:600;">{label} <em style="font-size:0.75rem;color:var(--text-soft);">(Coming Soon)</em></span></span>')
    return '\n'.join(items)

def nav_html():
    return '''<nav class="navbar navbar-expand-lg navbar-app">
  <div class="container">
    <a class="navbar-brand brand" href="../index.html">
      <span class="logo"><i class="bi bi-mortarboard-fill"></i></span>
      MISSIONS LEADERSHIP
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="mainNav">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link active" href="../index.html"><i class="bi bi-house-door me-1"></i>Home</a></li>
        <li class="nav-item"><a class="nav-link" href="../index.html#lessons"><i class="bi bi-collection-play me-1"></i>All Lessons</a></li>
      </ul>
      <div class="d-flex align-items-center gap-2">
        <button class="theme-toggle" id="themeToggle" type="button" title="Toggle dark mode" aria-label="Toggle dark mode">
          <i class="bi bi-moon-stars"></i>
        </button>
      </div>
    </div>
  </div>
</nav>'''

def footer_html():
    return '''<footer class="footer-app">
  <div class="container d-flex flex-column flex-md-row justify-content-between align-items-center gap-2">
    <div class="d-flex align-items-center gap-2">
      <span class="logo" style="width:28px;height:28px;border-radius:8px;display:grid;place-items:center;background:var(--brand-gradient);color:#fff;">
        <i class="bi bi-mortarboard-fill" style="font-size:0.85rem"></i>
      </span>
      <span>&copy; 2026 MISSIONS LEADERSHIP. All rights reserved.</span>
    </div>
    <div class="d-flex gap-3">
      <a href="../index.html" class="text-muted-app">Home</a>
      <a href="../index.html#lessons" class="text-muted-app">Lessons</a>
    </div>
  </div>
</footer>'''

HEAD = '''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link href="../style.css" rel="stylesheet">
</head>
<body>'''

TAIL = '''<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="../main.js"></script>
</body>
</html>'''

# ===== BUILD INDEX.HTML =====
def build_index():
    cards = []
    for n in range(1, 51):
        vid_id, title, series = LESSONS[n]
        fn = fname(n, vid_id, title)
        badge_cls = 'badge-published' if series == 'MLT' else 'badge-approved'
        if vid_id:
            cards.append(f'''<div class="col-md-6 col-lg-4 lesson-card" data-series="{series}">
      <div class="card-app course-card hoverable h-100 fade-in">
        <a href="video/{fn}" class="text-decoration-none" style="color:inherit;">
          <div class="thumb">
            <img src="images/{vid_id}.jpg" alt="{title}" loading="lazy">
            <span class="badge-float"><span class="badge {badge_cls}">{n}</span></span>
            <span class="badge-float" style="top:auto;bottom:12px;left:12px;right:auto;">
              <span class="badge" style="background:rgba(0,0,0,0.6);color:#fff;"><i class="bi bi-play-fill"></i> Watch</span>
            </span>
          </div>
          <div class="card-body">
            <h5 class="mb-1" style="color:var(--text);font-size:1.05rem;">{n}. {title}</h5>
            <div class="d-flex justify-content-between align-items-center">
              <span class="text-muted-app small"><i class="bi bi-collection-play me-1"></i>{series} Lesson</span>
              <span class="btn btn-primary btn-sm-app">Play <i class="bi bi-play-fill"></i></span>
            </div>
          </div>
        </a>
      </div>
    </div>''')
        else:
            cards.append(f'''<div class="col-md-6 col-lg-4 lesson-card" data-series="{series}">
      <div class="card-app course-card h-100" style="opacity:0.55;">
          <div class="thumb" style="background:var(--surface-3);">
            <div style="display:grid;place-items:center;height:100%;color:var(--text-soft);font-size:2.5rem;"><i class="bi bi-clock-history"></i></div>
            <span class="badge-float"><span class="badge badge-draft">{n}</span></span>
          </div>
          <div class="card-body">
            <h5 class="mb-1" style="color:var(--text);font-size:1.05rem;">{n}. {title}</h5>
            <div class="d-flex justify-content-between align-items-center">
              <span class="text-muted-app small"><i class="bi bi-clock me-1"></i>Coming Soon</span>
            </div>
          </div>
      </div>
    </div>''')

    mltn = sum(1 for v in range(1, 51) if LESSONS[v][2] == 'MLT')
    sltn = 50 - mltn

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MISSIONS LEADERSHIP - Video Lessons</title>
<meta name="description" content="Watch all 50 video lessons from the MISSIONS LEADERSHIP channel.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link href="style.css" rel="stylesheet">
</head>
<body>
{nav_html()}

<section class="hero">
  <div class="container">
    <div class="row align-items-center g-4">
      <div class="col-12">
        <span class="badge badge-approved mb-3"><i class="bi bi-mortarboard"></i> Missionary Leadership Training</span>
        <h1>Missionary Leadership &amp; Servant Leadership Lessons</h1>
        <p class="lead mb-4">
          Watch all 50 video lessons from the MISSIONS LEADERSHIP channel &mdash; organized by lesson number 1&ndash;50.
          <span class="badge badge-published me-1">{mltn} MLT</span>
          <span class="badge badge-approved">{sltn} SLT</span>
        </p>
        <div class="d-flex gap-2 flex-wrap">
          <button class="btn btn-gradient filter-btn active" data-filter="all"><i class="bi bi-grid me-1"></i>All Lessons</button>
          <button class="btn btn-outline-app filter-btn" data-filter="MLT"><i class="bi bi-journal-bookmark me-1"></i>MLT</button>
          <button class="btn btn-outline-app filter-btn" data-filter="SLT"><i class="bi bi-person-video3 me-1"></i>SLT</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="py-5" id="lessons">
  <div class="container">
    <div class="d-flex align-items-center justify-content-between mb-4">
      <div>
        <h2 class="section-title mb-1">All 50 Video Lessons</h2>
        <p class="text-muted-app mb-0">Every number 1&ndash;50 has a lesson. Click any lesson to watch.</p>
      </div>
    </div>
    <div class="row g-4" id="lessonGrid">
      {''.join(cards)}
    </div>
  </div>
</section>

{footer_html()}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="main.js"></script>
</body>
</html>'''
    with open(os.path.join(REPO, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Built index.html ({len(cards)} cards)')

# ===== BUILD VIDEO PAGES =====
def build_video_page(n):
    vid_id, title, series = LESSONS[n]
    fn = fname(n, vid_id, title)
    badge_cls = 'badge-published' if series == 'MLT' else 'badge-approved'
    
    # Prev/Next
    prev_n = n - 1 if n > 1 else None
    next_n = n + 1 if n < 50 else None
    prev_fn = fname(prev_n, LESSONS[prev_n][0], LESSONS[prev_n][1]) if prev_n else None
    next_fn = fname(next_n, LESSONS[next_n][0], LESSONS[next_n][1]) if next_n else None
    prev_title = LESSONS[prev_n][1] if prev_n else None
    next_title = LESSONS[next_n][1] if next_n else None
    
    if prev_n:
        prev_html = f'<a class="btn btn-outline-app" href="../video/{prev_fn}"><i class="bi bi-arrow-left me-1"></i> {prev_n}. {prev_title}</a>'
    else:
        prev_html = '<button class="btn btn-outline-app" disabled><i class="bi bi-arrow-left me-1"></i> Prev</button>'
    
    if next_n:
        next_html = f'<a class="btn btn-gradient" href="../video/{next_fn}">{next_n}. {next_title} <i class="bi bi-arrow-right ms-1"></i></a>'
    else:
        next_html = '<button class="btn btn-gradient" disabled>Next <i class="bi bi-arrow-right ms-1"></i></button>'
    
    # Sidebar
    sb = sidebar_html(active_n=n)
    
    # Video player or coming soon
    if vid_id:
        player = f'''<div class="video-wrap mb-4">
          <iframe src="https://www.youtube.com/embed/{vid_id}?rel=0"
                  title="YouTube video player" frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>'''
    else:
        player = f'''<div class="video-wrap mb-4" style="display:grid;place-items:center;min-height:300px;background:var(--surface-3);">
          <div class="text-center p-4">
            <i class="bi bi-clock-history" style="font-size:3rem;color:var(--text-soft);"></i>
            <h5 class="mt-3" style="color:var(--text-muted);">Coming Soon</h5>
            <p class="text-muted-app">This lesson will be available soon.</p>
          </div>
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{n}. {title} - MISSIONS LEADERSHIP</title>
<meta name="description" content="{n}. {title} - MISSIONS LEADERSHIP">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link href="../style.css" rel="stylesheet">
</head>
<body>
{nav_html()}

<section class="py-4">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb mb-3">
        <li class="breadcrumb-item"><a href="../index.html">Home</a></li>
        <li class="breadcrumb-item active" style="color:var(--text-muted);">{n}. {title}</li>
      </ol>
    </nav>
    <div class="row g-4">
      <div class="col-lg-8">
        <div class="d-flex align-items-start justify-content-between gap-2 mb-3">
          <div>
            <span class="badge {badge_cls} mb-2"><i class="bi bi-play-circle"></i> {series} {n}</span>
            <h1 class="h3 mb-1">{title}</h1>
          </div>
        </div>
        {player}
        <div class="d-flex align-items-center justify-content-between gap-2 flex-wrap mb-4">
          <div>{prev_html}</div>
          <div>{next_html}</div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="lesson-sidebar" style="position:sticky;top:calc(var(--nav-h) + 16px);">
          <div class="p-3" style="background:var(--surface-3);border-bottom:1px solid var(--border);">
            <h6 class="mb-0"><i class="bi bi-list-ul me-1"></i>All Lessons</h6>
            <small class="text-muted-app d-block">Lessons 1&ndash;50</small>
          </div>
          <div class="list-group list-group-flush" style="max-height:480px;overflow-y:auto;">
            {sb}
          </div>
          <div class="p-3 border-top" style="border-color:var(--border);">
            <a href="../index.html" class="btn btn-outline-app btn-sm-app w-100"><i class="bi bi-arrow-left me-1"></i> Back to All Lessons</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{footer_html()}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="../main.js"></script>
</body>
</html>'''
    return fn, html

# ===== MAIN =====
if __name__ == '__main__':
    os.makedirs(VIDEO_DIR, exist_ok=True)
    
    build_index()
    
    for n in range(1, 51):
        fn, html = build_video_page(n)
        with open(os.path.join(VIDEO_DIR, fn), 'w', encoding='utf-8') as f:
            f.write(html)
        status = 'OK' if LESSONS[n][0] else 'COMING SOON'
        print(f'  Built {fn} [{status}]')
    
    # Remove old video files
    existing = set(os.listdir(VIDEO_DIR))
    kept = set(fname(n, LESSONS[n][0], LESSONS[n][1]) for n in range(1, 51))
    for old in existing - kept:
        os.remove(os.path.join(VIDEO_DIR, old))
        print(f'  Removed old: {old}')
    
    print(f'\nDone! {len(kept)} video pages built.')
