import os
import xml.etree.ElementTree as ET

# Shared CSS styles
SHARED_STYLE = '''
    <style>
      text {
        text-rendering: geometricPrecision;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
      }
      .mono {
        font-family: "Cascadia Code", "Cascadia Mono", "JetBrains Mono", "Fira Code", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      }
      .sans {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", "Inter", Roboto, Helvetica, Arial, sans-serif;
      }
      .pcard { rx: 8px; fill: url(#cardGrad); stroke: #0f2b48; stroke-width: 1.2; }
      .ptag { rx: 11px; fill: #07172b; stroke: #123861; stroke-width: 1; }
      .ptag-txt { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", sans-serif; font-size: 10.5px; font-weight: 500; fill: #38bdf8; text-anchor: middle; }
    </style>
'''

# 1. HERO SCAN
COLS = 21
ROWS = 15
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for r in [1, 2]:
    for c in range(1, 10):
        grid[r][c] = 1
diag = [(3, 7), (3, 8), (4, 6), (4, 7), (5, 5), (5, 6), (6, 5), (6, 6), (7, 4), (7, 5), (8, 3), (8, 4), (9, 3), (9, 4), (10, 2), (10, 3), (11, 1), (11, 2)]
for r, c in diag:
    grid[r][c] = 1
for r in [12, 13]:
    for c in range(1, 10):
        grid[r][c] = 1
for r in range(1, 14):
    grid[r][11] = 1
    grid[r][12] = 1
    grid[r][18] = 1
    grid[r][19] = 1
m_diag = [(2, 13), (2, 17), (3, 13), (3, 17), (4, 14), (4, 16), (5, 14), (5, 16), (6, 15), (7, 15)]
for r, c in m_diag:
    grid[r][c] = 1

def generate_pixel_matrix():
    cell_size = 11
    gap = 2.5
    pitch = cell_size + gap
    start_x = 39
    start_y = 150
    elements = []
    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * pitch
            y = start_y + r * pitch
            if grid[r][c] == 0:
                elements.append(f'    <rect x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2" fill="#061220" stroke="#0b233a" stroke-width="0.6" opacity="0.6"/>')
    elements.append('    <g filter="url(#glow)">')
    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * pitch
            y = start_y + r * pitch
            if grid[r][c] == 1:
                elements.append(f'      <rect x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2" fill="#00e5ff" stroke="#38bdf8" stroke-width="0.8"/>')
    elements.append('    </g>')
    return '\n'.join(elements)

def make_hero_scan():
    matrix = generate_pixel_matrix()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 440" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
{SHARED_STYLE}
  </defs>

  <!-- Outer Window -->
  <rect x="1" y="1" width="878" height="438" rx="10" fill="url(#bgGrad)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Window Header -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5" fill="#27c93f"/>

  <text x="85" y="26" class="mono" font-size="12" fill="#64748b">zine007mhidra@github ~ $ <tspan fill="#38bdf8">./profile-scan --live</tspan></text>

  <!-- Live Pulse -->
  <circle cx="820" cy="22" r="4" fill="#00e5ff" filter="url(#glow)"/>
  <text x="832" y="26" class="mono" font-size="11" font-weight="bold" fill="#00e5ff" letter-spacing="1">LIVE</text>

  <line x1="1" y1="42" x2="879" y2="42" stroke="#172338" stroke-width="1"/>

  <!-- Left Card: VISUAL.MAP -->
  <rect x="20" y="58" width="320" height="362" rx="8" fill="#050811" stroke="#0e233d" stroke-width="1.2"/>
  <text x="36" y="86" class="mono" font-size="11" font-weight="700" fill="#00e5ff" letter-spacing="1.5">VISUAL.MAP</text>
  <line x1="36" y1="94" x2="324" y2="94" stroke="#0e233d" stroke-width="1"/>

  <!-- Diagnostic Scan Header -->
  <text x="36" y="116" class="mono" font-size="9.5" fill="#38bdf8" opacity="0.9" letter-spacing="0.5">SCAN: IDENTITY_MATRIX [ZM-007]</text>
  <text x="36" y="131" class="mono" font-size="9" fill="#64748b" letter-spacing="0.5">STATUS: ACTIVE // 21x15 LED_GRID</text>

  <!-- Vector Pixel Matrix Monogram (ZM) -->
{matrix}

  <!-- Sub-label in refined Sans -->
  <text x="180" y="380" class="sans" font-size="11" fill="#38bdf8" letter-spacing="1.5" text-anchor="middle" font-weight="600">ID: ZINE EL ABIDINE MHIDRA</text>

  <!-- Corner Brackets on VISUAL.MAP -->
  <path d="M 32 400 L 32 410 L 42 410" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.8"/>
  <path d="M 328 400 L 328 410 L 318 410" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.8"/>
  <path d="M 32 70 L 32 64 L 42 64" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.8"/>
  <path d="M 328 70 L 328 64 L 318 64" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.8"/>

  <!-- Right Card: SYSTEM.INFO -->
  <rect x="355" y="58" width="505" height="362" rx="8" fill="#050811" stroke="#0e233d" stroke-width="1.2"/>
  <text x="375" y="86" class="mono" font-size="11" font-weight="700" fill="#00e5ff" letter-spacing="1.5">SYSTEM.INFO</text>
  <line x1="375" y1="94" x2="840" y2="94" stroke="#0e233d" stroke-width="1"/>

  <!-- Specs Grid: Monospace Labels + Modern Geometric Sans Values -->
  <g>
    <!-- Row 1 -->
    <text x="375" y="125" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Subject</text>
    <text x="500" y="125" class="sans" font-size="13" fill="#f8fafc" font-weight="600">Zine El Abidine MHIDRA</text>

    <!-- Row 2 -->
    <text x="375" y="153" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Handle</text>
    <text x="500" y="153" class="mono" font-size="12" fill="#00e5ff">@Zine007MHIDRA</text>

    <!-- Row 3 -->
    <text x="375" y="181" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Role</text>
    <text x="500" y="181" class="sans" font-size="13" fill="#e2e8f0" font-weight="500">AI &amp; Full-Stack Developer</text>

    <!-- Row 4 -->
    <text x="375" y="209" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Status</text>
    <text x="500" y="209" class="sans" font-size="12.5" fill="#22d3ee" font-weight="500">Building | Learning | Shipping</text>

    <!-- Row 5 -->
    <text x="375" y="237" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Languages</text>
    <text x="500" y="237" class="sans" font-size="12.5" fill="#cbd5e1">TypeScript, Python, HTML, CSS</text>

    <!-- Row 6 -->
    <text x="375" y="265" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Repositories</text>
    <text x="500" y="265" class="sans" font-size="12.5" fill="#f8fafc">12 public</text>

    <!-- Row 7 -->
    <text x="375" y="293" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Contributions</text>
    <text x="500" y="293" class="sans" font-size="12.5" fill="#f8fafc">158 in the last year</text>

    <!-- Row 8 -->
    <text x="375" y="321" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Stars</text>
    <text x="500" y="321" class="sans" font-size="12.5" fill="#f8fafc">3</text>

    <!-- Row 9 -->
    <text x="375" y="349" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Active Days</text>
    <text x="500" y="349" class="sans" font-size="12.5" fill="#f8fafc">32</text>

    <!-- Row 10 -->
    <text x="375" y="377" class="mono" font-size="11.5" fill="#38bdf8" letter-spacing="0.5">Contact</text>
    <text x="500" y="377" class="mono" font-size="12" fill="#00e5ff">github.com/Zine007MHIDRA</text>
  </g>

  <!-- Watermark border corner accent -->
  <path d="M 850 410 L 850 418 L 842 418" stroke="#00e5ff" stroke-width="1.5" fill="none"/>
</svg>
'''

# 2. TOOLBOX
def make_toolbox():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 290" width="100%" height="100%">
  <defs>
    <linearGradient id="boxBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
{SHARED_STYLE}
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="288" rx="10" fill="url(#boxBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Window Header -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5" fill="#27c93f"/>
  <text x="85" y="26" class="mono" font-size="12" fill="#64748b">zine007mhidra@github ~ $ <tspan fill="#38bdf8">toolbox --list</tspan></text>
  <line x1="1" y1="42" x2="879" y2="42" stroke="#172338" stroke-width="1"/>

  <!-- Command line prompt -->
  <text x="30" y="74" class="mono" font-size="12" fill="#22c55e">zine007mhidra@github <tspan fill="#64748b">:~$</tspan> <tspan fill="#f8fafc">ls skills/</tspan></text>

  <!-- Skill Badges: modern Sans for badges -->
  <g transform="translate(30, 92)">
    <rect x="0" y="0" width="105" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="52" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">TypeScript</text>

    <rect x="115" y="0" width="80" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="155" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">Python</text>

    <rect x="205" y="0" width="85" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="247" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">Next.js</text>

    <rect x="300" y="0" width="85" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="342" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">FastAPI</text>

    <rect x="395" y="0" width="110" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="450" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">TailwindCSS</text>

    <rect x="515" y="0" width="85" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="557" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">PyTorch</text>

    <rect x="610" y="0" width="80" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="650" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">Docker</text>

    <rect x="700" y="0" width="60" height="28" rx="6" fill="#071324" stroke="#123356"/>
    <text x="730" y="18" class="sans" font-size="11.5" font-weight="500" fill="#38bdf8" text-anchor="middle">Git</text>
  </g>

  <!-- Languages Percentage Breakdown Bar -->
  <g transform="translate(30, 155)">
    <text x="0" y="-8" class="mono" font-size="11" fill="#64748b" font-weight="600" letter-spacing="1">LANGUAGE FREQUENCY</text>
    <rect x="0" y="0" width="820" height="10" rx="5" fill="#0e1726"/>
    <path d="M 0 5 A 5 5 0 0 1 5 0 L 451 0 L 451 10 L 5 10 A 5 5 0 0 1 0 5 Z" fill="#3178c6"/>
    <rect x="453" y="0" width="268" height="10" fill="#00e5ff"/>
    <rect x="723" y="0" width="80" height="10" fill="#e34c26"/>
    <path d="M 805 0 L 815 0 A 5 5 0 0 1 820 5 A 5 5 0 0 1 815 10 L 805 10 Z" fill="#f1e05a"/>
  </g>

  <!-- Stat Blocks underneath: Sans headers + Mono percentages -->
  <g transform="translate(30, 195)">
    <rect x="0" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="20" cy="22" r="4" fill="#3178c6"/>
    <text x="32" y="26" class="sans" font-size="12.5" fill="#f8fafc" font-weight="600">TypeScript</text>
    <text x="32" y="48" class="mono" font-size="16" fill="#38bdf8" font-weight="bold">55%</text>

    <rect x="165" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="185" cy="22" r="4" fill="#00e5ff"/>
    <text x="197" y="26" class="sans" font-size="12.5" fill="#f8fafc" font-weight="600">Python</text>
    <text x="197" y="48" class="mono" font-size="16" fill="#00e5ff" font-weight="bold">33%</text>

    <rect x="330" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="350" cy="22" r="4" fill="#e34c26"/>
    <text x="362" y="26" class="sans" font-size="12.5" fill="#f8fafc" font-weight="600">HTML</text>
    <text x="362" y="48" class="mono" font-size="16" fill="#e34c26" font-weight="bold">10%</text>

    <rect x="495" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="515" cy="22" r="4" fill="#563d7c"/>
    <text x="527" y="26" class="sans" font-size="12.5" fill="#f8fafc" font-weight="600">CSS</text>
    <text x="527" y="48" class="mono" font-size="16" fill="#a855f7" font-weight="bold">1%</text>

    <rect x="660" y="0" width="160" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="680" cy="22" r="4" fill="#f1e05a"/>
    <text x="692" y="26" class="sans" font-size="12.5" fill="#f8fafc" font-weight="600">JavaScript</text>
    <text x="692" y="48" class="mono" font-size="16" fill="#f1e05a" font-weight="bold">1%</text>
  </g>
</svg>
'''

# 3. PROJECTS
def make_projects():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 395" width="100%" height="100%">
  <defs>
    <linearGradient id="projBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#091322"/>
      <stop offset="100%" stop-color="#040810"/>
    </linearGradient>
    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
{SHARED_STYLE}
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="393" rx="10" fill="url(#projBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Window Header -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5" fill="#27c93f"/>
  <text x="85" y="26" class="mono" font-size="12" fill="#00e5ff" font-weight="bold" letter-spacing="0.5">PROJECTS.LIST <tspan fill="#64748b" font-weight="normal">./projects.sh --all --status=live</tspan></text>
  <text x="795" y="26" class="mono" font-size="11" fill="#64748b">4 projects</text>
  <line x1="1" y1="42" x2="879" y2="42" stroke="#172338" stroke-width="1"/>

  <!-- 2x2 Grid -->
  <!-- Card 1: F1LapStratSim -->
  <g transform="translate(20, 56)">
    <rect x="0" y="0" width="405" height="152" class="pcard"/>
    <line x1="8" y1="1" x2="397" y2="1" stroke="rgba(0, 229, 255, 0.2)" stroke-width="1"/>
    
    <circle cx="18" cy="20" r="3.5" fill="#00e5ff" filter="url(#cyanGlow)"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/F1LapStratSim</text>
    <circle cx="390" cy="20" r="3" fill="#00e5ff" opacity="0.4"/>

    <!-- Title in Modern Sans Bold -->
    <text x="18" y="52" class="sans" font-size="16" fill="#f8fafc" font-weight="700">F1LapStratSim <tspan class="mono" fill="#00e5ff" font-weight="normal">_</tspan></text>
    <!-- Description in Modern Sans -->
    <text x="18" y="73" class="sans" font-size="11.5" fill="#94a3b8">Vehicle dynamics simulator for F1 lap times,</text>
    <text x="18" y="89" class="sans" font-size="11.5" fill="#94a3b8">tyre degradation, and pit strategy (Monza).</text>

    <!-- Refined Capsule Tags -->
    <rect x="18" y="106" width="76" height="22" class="ptag"/>
    <text x="56" y="121" class="ptag-txt">formula1</text>
    
    <rect x="102" y="106" width="80" height="22" class="ptag"/>
    <text x="142" y="121" class="ptag-txt">simulator</text>

    <!-- Meta Info -->
    <text x="18" y="142" class="mono" font-size="11" fill="#f1e05a">★ 2</text>
    <text x="44" y="142" class="sans" font-size="11" fill="#64748b">· updated 2w ago</text>

    <!-- Donut Ring: 100% Python -->
    <circle cx="345" cy="78" r="32" fill="none" stroke="#0d2138" stroke-width="6.5"/>
    <circle cx="345" cy="78" r="32" fill="none" stroke="#00e5ff" stroke-width="6.5" stroke-dasharray="201.1" stroke-dashoffset="0" stroke-linecap="round"/>
    <text x="345" y="83" class="mono" font-size="12" fill="#00e5ff" font-weight="bold" text-anchor="middle">100%</text>
  </g>

  <!-- Card 2: HoneyGrid -->
  <g transform="translate(455, 56)">
    <rect x="0" y="0" width="405" height="152" class="pcard"/>
    <line x1="8" y1="1" x2="397" y2="1" stroke="rgba(249, 115, 22, 0.2)" stroke-width="1"/>

    <circle cx="18" cy="20" r="3.5" fill="#f97316"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/HoneyGrid</text>
    <circle cx="390" cy="20" r="3" fill="#f97316" opacity="0.4"/>

    <text x="18" y="52" class="sans" font-size="16" fill="#f8fafc" font-weight="700">HoneyGrid <tspan class="mono" fill="#f97316" font-weight="normal">_</tspan></text>
    <text x="18" y="73" class="sans" font-size="11.5" fill="#94a3b8">Python grid optimization, compute pipeline</text>
    <text x="18" y="89" class="sans" font-size="11.5" fill="#94a3b8">and distributed dataset orchestration.</text>

    <rect x="18" y="106" width="62" height="22" class="ptag"/>
    <text x="49" y="121" class="ptag-txt">python</text>
    
    <rect x="88" y="106" width="78" height="22" class="ptag"/>
    <text x="127" y="121" class="ptag-txt">grid-core</text>

    <text x="18" y="142" class="mono" font-size="11" fill="#f1e05a">★ 1</text>
    <text x="44" y="142" class="sans" font-size="11" fill="#64748b">· updated 1mo ago</text>

    <g transform="rotate(-90 345 78)">
      <circle cx="345" cy="78" r="32" fill="none" stroke="#0d2138" stroke-width="6.5"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#f97316" stroke-width="6.5" stroke-dasharray="118.6 82.5" stroke-dashoffset="0"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#00e5ff" stroke-width="6.5" stroke-dasharray="66.3 134.8" stroke-dashoffset="-118.6"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#22c55e" stroke-width="6.5" stroke-dasharray="16.1 185.0" stroke-dashoffset="-184.9"/>
    </g>
    <text x="345" y="83" class="mono" font-size="12" fill="#f97316" font-weight="bold" text-anchor="middle">59%</text>
  </g>

  <!-- Card 3: portfolio -->
  <g transform="translate(20, 224)">
    <rect x="0" y="0" width="405" height="152" class="pcard"/>
    <line x1="8" y1="1" x2="397" y2="1" stroke="rgba(56, 189, 248, 0.2)" stroke-width="1"/>

    <circle cx="18" cy="20" r="3.5" fill="#38bdf8"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/portfolio</text>
    <circle cx="390" cy="20" r="3" fill="#38bdf8" opacity="0.4"/>

    <text x="18" y="52" class="sans" font-size="16" fill="#f8fafc" font-weight="700">portfolio <tspan class="mono" fill="#38bdf8" font-weight="normal">_</tspan></text>
    <text x="18" y="73" class="sans" font-size="11.5" fill="#94a3b8">Interactive developer portfolio showcasing</text>
    <text x="18" y="89" class="sans" font-size="11.5" fill="#94a3b8">AI systems, simulation work, and public builds.</text>

    <rect x="18" y="106" width="62" height="22" class="ptag"/>
    <text x="49" y="121" class="ptag-txt">nextjs</text>
    
    <rect x="88" y="106" width="86" height="22" class="ptag"/>
    <text x="131" y="121" class="ptag-txt">typescript</text>

    <text x="18" y="142" class="mono" font-size="11" fill="#64748b">★ 0</text>
    <text x="44" y="142" class="sans" font-size="11" fill="#64748b">· updated 1d ago</text>

    <g transform="rotate(-90 345 78)">
      <circle cx="345" cy="78" r="32" fill="none" stroke="#0d2138" stroke-width="6.5"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#38bdf8" stroke-width="6.5" stroke-dasharray="185.0 16.1" stroke-dashoffset="0"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#a855f7" stroke-width="6.5" stroke-dasharray="12.1 189.0" stroke-dashoffset="-185.0"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#e34c26" stroke-width="6.5" stroke-dasharray="4.0 197.1" stroke-dashoffset="-197.1"/>
    </g>
    <text x="345" y="83" class="mono" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">92%</text>
  </g>

  <!-- Card 4: aether-audiophile -->
  <g transform="translate(455, 224)">
    <rect x="0" y="0" width="405" height="152" class="pcard"/>
    <line x1="8" y1="1" x2="397" y2="1" stroke="rgba(168, 85, 247, 0.2)" stroke-width="1"/>

    <circle cx="18" cy="20" r="3.5" fill="#a855f7"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/aether-audiophile</text>
    <circle cx="390" cy="20" r="3" fill="#a855f7" opacity="0.4"/>

    <text x="18" y="52" class="sans" font-size="16" fill="#f8fafc" font-weight="700">aether-audiophile <tspan class="mono" fill="#a855f7" font-weight="normal">_</tspan></text>
    <text x="18" y="73" class="sans" font-size="11.5" fill="#94a3b8">High-fidelity web application with refined</text>
    <text x="18" y="89" class="sans" font-size="11.5" fill="#94a3b8">audiophile acoustic staging and modern UI.</text>

    <rect x="18" y="106" width="86" height="22" class="ptag"/>
    <text x="61" y="121" class="ptag-txt">typescript</text>
    
    <rect x="112" y="106" width="58" height="22" class="ptag"/>
    <text x="141" y="121" class="ptag-txt">audio</text>

    <text x="18" y="142" class="mono" font-size="11" fill="#64748b">★ 0</text>
    <text x="44" y="142" class="sans" font-size="11" fill="#64748b">· updated 3w ago</text>

    <g transform="rotate(-90 345 78)">
      <circle cx="345" cy="78" r="32" fill="none" stroke="#0d2138" stroke-width="6.5"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#a855f7" stroke-width="6.5" stroke-dasharray="174.9 26.2" stroke-dashoffset="0"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#00e5ff" stroke-width="6.5" stroke-dasharray="20.1 181.0" stroke-dashoffset="-174.9"/>
      <circle cx="345" cy="78" r="32" fill="none" stroke="#f1e05a" stroke-width="6.5" stroke-dasharray="6.0 195.1" stroke-dashoffset="-195.0"/>
    </g>
    <text x="345" y="83" class="mono" font-size="12" fill="#a855f7" font-weight="bold" text-anchor="middle">87%</text>
  </g>

  <!-- Corner Tech Accents -->
  <path d="M 865 378 L 865 385 L 857 385" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.6"/>
  <path d="M 15 378 L 15 385 L 23 385" stroke="#00e5ff" stroke-width="1.2" fill="none" opacity="0.6"/>
</svg>
'''

# 4. NEOFETCH
def make_neofetch():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" height="100%">
  <defs>
    <linearGradient id="neoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
{SHARED_STYLE}
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="268" rx="10" fill="url(#neoBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Window Header -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5" fill="#27c93f"/>
  <text x="85" y="26" class="mono" font-size="12" fill="#64748b">zine007mhidra@github ~ $ <tspan fill="#38bdf8">neofetch</tspan></text>
  <line x1="1" y1="42" x2="879" y2="42" stroke="#172338" stroke-width="1"/>

  <!-- Left: Cyberpunk ASCII GitHub Badge -->
  <g transform="translate(50, 75)" class="mono" font-size="14" fill="#00e5ff" font-weight="bold" opacity="0.95">
    <text x="0" y="20">  ┌──────────────┐</text>
    <text x="0" y="42">  │  ■■      ■■  │</text>
    <text x="0" y="64">  │  ·  github   │</text>
    <text x="0" y="86">  │  &gt; _         │</text>
    <text x="0" y="108">  └──────────────┘</text>
  </g>

  <!-- Right: Neofetch Info Rows -->
  <g transform="translate(290, 75)">
    <text x="0" y="20" class="mono" font-size="14" font-weight="bold" fill="#00e5ff">zine007mhidra <tspan fill="#64748b" font-weight="normal">@github</tspan></text>
    <line x1="0" y1="30" x2="520" y2="30" stroke="#172e48" stroke-width="1"/>

    <text x="0" y="55" class="mono" font-size="12" fill="#38bdf8">Name</text>
    <text x="120" y="55" class="sans" font-size="13" font-weight="600" fill="#f8fafc">Zine El Abidine MHIDRA</text>

    <text x="0" y="78" class="mono" font-size="12" fill="#38bdf8">Role</text>
    <text x="120" y="78" class="sans" font-size="12.5" fill="#e2e8f0" font-weight="500">AI &amp; Full-Stack Developer</text>

    <text x="0" y="101" class="mono" font-size="12" fill="#38bdf8">Stars</text>
    <text x="120" y="101" class="sans" font-size="12.5" fill="#f8fafc">3</text>

    <text x="0" y="124" class="mono" font-size="12" fill="#38bdf8">Repos</text>
    <text x="120" y="124" class="sans" font-size="12.5" fill="#f8fafc">12</text>

    <text x="0" y="147" class="mono" font-size="12" fill="#38bdf8">Top Lang</text>
    <text x="120" y="147" class="sans" font-size="12.5" fill="#38bdf8" font-weight="500">TypeScript</text>

    <text x="0" y="170" class="mono" font-size="12" fill="#38bdf8">Activity</text>
    <text x="120" y="170" class="mono" font-size="12" fill="#00e5ff" font-weight="bold">158 contributions</text>

    <g transform="translate(0, 185)">
      <rect x="0" y="0" width="22" height="12" rx="2" fill="#00e5ff"/>
      <rect x="26" y="0" width="22" height="12" rx="2" fill="#38bdf8"/>
      <rect x="52" y="0" width="22" height="12" rx="2" fill="#6366f1"/>
      <rect x="78" y="0" width="22" height="12" rx="2" fill="#a855f7"/>
      <rect x="104" y="0" width="22" height="12" rx="2" fill="#ec4899"/>
      <rect x="130" y="0" width="22" height="12" rx="2" fill="#22c55e"/>
    </g>
  </g>
</svg>
'''

# 5. CONNECT
def make_connect():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 120" width="100%" height="100%">
  <defs>
    <linearGradient id="connBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
{SHARED_STYLE}
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="118" rx="10" fill="url(#connBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Centered Pill Buttons -->
  <g transform="translate(60, 40)">
    <!-- GitHub Button -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="160" height="40" rx="20" fill="#07172e" stroke="#00e5ff" stroke-width="1.2"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#00e5ff" text-anchor="middle" font-weight="bold">G</text>
      <text x="44" y="24" class="sans" font-size="12" font-weight="600" fill="#f8fafc">@Zine007MHIDRA</text>
    </g>

    <!-- Portfolio Button -->
    <g transform="translate(180, 0)">
      <rect x="0" y="0" width="160" height="40" rx="20" fill="#07172e" stroke="#38bdf8" stroke-width="1.2"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#38bdf8" text-anchor="middle" font-weight="bold">↗</text>
      <text x="44" y="24" class="sans" font-size="12" font-weight="600" fill="#f8fafc">Live Portfolio</text>
    </g>

    <!-- LinkedIn Button -->
    <g transform="translate(360, 0)">
      <rect x="0" y="0" width="160" height="40" rx="20" fill="#07172e" stroke="#0ea5e9" stroke-width="1.2"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#0ea5e9" text-anchor="middle" font-weight="bold">in</text>
      <text x="44" y="24" class="sans" font-size="12" font-weight="600" fill="#f8fafc">LinkedIn Profile</text>
    </g>

    <!-- Email Button -->
    <g transform="translate(540, 0)">
      <rect x="0" y="0" width="220" height="40" rx="20" fill="#07172e" stroke="#22d3ee" stroke-width="1.2"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#22d3ee" text-anchor="middle" font-weight="bold">@</text>
      <text x="44" y="24" class="sans" font-size="12" font-weight="600" fill="#f8fafc">zine.mhidra@gmail.com</text>
    </g>
  </g>
</svg>
'''

# Write assets
files = {
    'assets/hero-scan.svg': make_hero_scan(),
    'assets/toolbox.svg': make_toolbox(),
    'assets/projects.svg': make_projects(),
    'assets/neofetch.svg': make_neofetch(),
    'assets/connect.svg': make_connect()
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    try:
        ET.parse(path)
        print(f"VALID & WRITTEN: {path}")
    except Exception as e:
        print(f"ERROR in {path}: {e}")
