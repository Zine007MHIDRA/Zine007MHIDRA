import os

def make_toolbox():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 290" width="100%" height="100%">
  <defs>
    <linearGradient id="boxBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      .pill { rx: 6px; fill: #071324; stroke: #123356; stroke-width: 1; }
      .pill-text { font-family: ui-monospace, monospace; font-size: 11px; fill: #38bdf8; }
    </style>
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

  <!-- Skill Badges Row 1 -->
  <g transform="translate(30, 92)">
    <!-- TypeScript -->
    <rect x="0" y="0" width="105" height="28" class="pill"/>
    <text x="14" y="18" class="pill-text" fill="#38bdf8">TypeScript</text>

    <!-- Python -->
    <rect x="115" y="0" width="80" height="28" class="pill"/>
    <text x="130" y="18" class="pill-text" fill="#38bdf8">Python</text>

    <!-- Next.js -->
    <rect x="205" y="0" width="85" height="28" class="pill"/>
    <text x="220" y="18" class="pill-text" fill="#38bdf8">Next.js</text>

    <!-- FastAPI -->
    <rect x="300" y="0" width="85" height="28" class="pill"/>
    <text x="316" y="18" class="pill-text" fill="#38bdf8">FastAPI</text>

    <!-- TailwindCSS -->
    <rect x="395" y="0" width="110" height="28" class="pill"/>
    <text x="408" y="18" class="pill-text" fill="#38bdf8">TailwindCSS</text>

    <!-- PyTorch -->
    <rect x="515" y="0" width="85" height="28" class="pill"/>
    <text x="530" y="18" class="pill-text" fill="#38bdf8">PyTorch</text>

    <!-- Docker -->
    <rect x="610" y="0" width="80" height="28" class="pill"/>
    <text x="625" y="18" class="pill-text" fill="#38bdf8">Docker</text>

    <!-- Git -->
    <rect x="700" y="0" width="60" height="28" class="pill"/>
    <text x="715" y="18" class="pill-text" fill="#38bdf8">Git</text>
  </g>

  <!-- Languages Percentage Breakdown Bar -->
  <g transform="translate(30, 155)">
    <text x="0" y="-8" class="mono" font-size="11" fill="#64748b" font-weight="600" letter-spacing="1">LANGUAGE FREQUENCY</text>
    
    <!-- Multi-segment bar (total width 820) -->
    <!-- TS: 55% = 451px, PY: 33% = 270px, HTML: 10% = 82px, Other: 2% = 17px -->
    <rect x="0" y="0" width="820" height="10" rx="5" fill="#0e1726"/>
    
    <path d="M 0 5 A 5 5 0 0 1 5 0 L 451 0 L 451 10 L 5 10 A 5 5 0 0 1 0 5 Z" fill="#3178c6"/>
    <rect x="453" y="0" width="268" height="10" fill="#00e5ff"/>
    <rect x="723" y="0" width="80" height="10" fill="#e34c26"/>
    <path d="M 805 0 L 815 0 A 5 5 0 0 1 820 5 A 5 5 0 0 1 815 10 L 805 10 Z" fill="#f1e05a"/>
  </g>

  <!-- Stat Blocks underneath -->
  <g transform="translate(30, 195)" class="mono">
    <!-- Block 1: TS -->
    <rect x="0" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="20" cy="22" r="4" fill="#3178c6"/>
    <text x="32" y="26" font-size="12" fill="#f8fafc" font-weight="600">TypeScript</text>
    <text x="32" y="48" font-size="16" fill="#38bdf8" font-weight="bold">55%</text>

    <!-- Block 2: Python -->
    <rect x="165" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="185" cy="22" r="4" fill="#00e5ff"/>
    <text x="197" y="26" font-size="12" fill="#f8fafc" font-weight="600">Python</text>
    <text x="197" y="48" font-size="16" fill="#00e5ff" font-weight="bold">33%</text>

    <!-- Block 3: HTML -->
    <rect x="330" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="350" cy="22" r="4" fill="#e34c26"/>
    <text x="362" y="26" font-size="12" fill="#f8fafc" font-weight="600">HTML</text>
    <text x="362" y="48" font-size="16" fill="#e34c26" font-weight="bold">10%</text>

    <!-- Block 4: CSS -->
    <rect x="495" y="0" width="150" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="515" cy="22" r="4" fill="#563d7c"/>
    <text x="527" y="26" font-size="12" fill="#f8fafc" font-weight="600">CSS</text>
    <text x="527" y="48" font-size="16" fill="#a855f7" font-weight="bold">1%</text>

    <!-- Block 5: JavaScript -->
    <rect x="660" y="0" width="160" height="65" rx="6" fill="#050811" stroke="#0e233d"/>
    <circle cx="680" cy="22" r="4" fill="#f1e05a"/>
    <text x="692" y="26" font-size="12" fill="#f8fafc" font-weight="600">JavaScript</text>
    <text x="692" y="48" font-size="16" fill="#f1e05a" font-weight="bold">1%</text>
  </g>
</svg>
'''

def make_projects():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 390" width="100%" height="100%">
  <defs>
    <linearGradient id="projBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      .pcard { rx: 8px; fill: #050811; stroke: #0f2b48; stroke-width: 1.2; }
      .ptag { rx: 4px; fill: #081a30; stroke: #153b66; stroke-width: 0.8; }
      .ptag-txt { font-family: ui-monospace, monospace; font-size: 10px; fill: #38bdf8; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="388" rx="10" fill="url(#projBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Window Header -->
  <circle cx="24" cy="22" r="5" fill="#ff5f56"/>
  <circle cx="42" cy="22" r="5" fill="#ffbd2e"/>
  <circle cx="60" cy="22" r="5" fill="#27c93f"/>
  <text x="85" y="26" class="mono" font-size="12" fill="#00e5ff" font-weight="bold">PROJECTS.LIST <tspan fill="#64748b" font-weight="normal">./projects.sh --all</tspan></text>
  <text x="795" y="26" class="mono" font-size="11" fill="#64748b">4 projects</text>
  <line x1="1" y1="42" x2="879" y2="42" stroke="#172338" stroke-width="1"/>

  <!-- 2x2 Grid: Row 1 -->
  <!-- Card 1: F1LapStratSim -->
  <g transform="translate(20, 56)">
    <rect x="0" y="0" width="405" height="150" class="pcard"/>
    <circle cx="18" cy="20" r="3.5" fill="#00e5ff"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/F1LapStratSim</text>

    <text x="18" y="52" class="mono" font-size="16" fill="#f8fafc" font-weight="bold">F1LapStratSim <tspan fill="#00e5ff">_</tspan></text>
    <text x="18" y="74" class="mono" font-size="10.5" fill="#94a3b8">Vehicle dynamics simulator for F1 lap times,</text>
    <text x="18" y="90" class="mono" font-size="10.5" fill="#94a3b8">tyre degradation, and pit strategy (Monza).</text>

    <!-- Tags -->
    <rect x="18" y="108" width="70" height="20" class="ptag"/>
    <text x="28" y="122" class="ptag-txt">formula1</text>
    
    <rect x="96" y="108" width="72" height="20" class="ptag"/>
    <text x="105" y="122" class="ptag-txt">simulator</text>

    <text x="18" y="140" class="mono" font-size="11" fill="#f1e05a">★ 2</text>
    <text x="50" y="140" class="mono" font-size="10" fill="#64748b">Python</text>

    <!-- Circular Gauge: 100% Python -->
    <circle cx="345" cy="75" r="32" fill="none" stroke="#0d2138" stroke-width="7"/>
    <circle cx="345" cy="75" r="32" fill="none" stroke="#00e5ff" stroke-width="7" stroke-dasharray="201" stroke-dashoffset="0" stroke-linecap="round"/>
    <text x="345" y="80" class="mono" font-size="12" fill="#00e5ff" font-weight="bold" text-anchor="middle">100%</text>
  </g>

  <!-- Card 2: HoneyGrid -->
  <g transform="translate(455, 56)">
    <rect x="0" y="0" width="405" height="150" class="pcard"/>
    <circle cx="18" cy="20" r="3.5" fill="#f97316"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/HoneyGrid</text>

    <text x="18" y="52" class="mono" font-size="16" fill="#f8fafc" font-weight="bold">HoneyGrid <tspan fill="#f97316">_</tspan></text>
    <text x="18" y="74" class="mono" font-size="10.5" fill="#94a3b8">Python grid optimization, compute pipeline</text>
    <text x="18" y="90" class="mono" font-size="10.5" fill="#94a3b8">and distributed dataset orchestration.</text>

    <!-- Tags -->
    <rect x="18" y="108" width="60" height="20" class="ptag"/>
    <text x="28" y="122" class="ptag-txt">python</text>
    
    <rect x="86" y="108" width="70" height="20" class="ptag"/>
    <text x="96" y="122" class="ptag-txt">grid-core</text>

    <text x="18" y="140" class="mono" font-size="11" fill="#f1e05a">★ 1</text>
    <text x="50" y="140" class="mono" font-size="10" fill="#64748b">Python</text>

    <!-- Circular Gauge: 59% -->
    <circle cx="345" cy="75" r="32" fill="none" stroke="#0d2138" stroke-width="7"/>
    <circle cx="345" cy="75" r="32" fill="none" stroke="#f97316" stroke-width="7" stroke-dasharray="201" stroke-dashoffset="82" stroke-linecap="round"/>
    <text x="345" y="80" class="mono" font-size="12" fill="#f97316" font-weight="bold" text-anchor="middle">59%</text>
  </g>

  <!-- 2x2 Grid: Row 2 -->
  <!-- Card 3: portfolio -->
  <g transform="translate(20, 220)">
    <rect x="0" y="0" width="405" height="150" class="pcard"/>
    <circle cx="18" cy="20" r="3.5" fill="#38bdf8"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/portfolio</text>

    <text x="18" y="52" class="mono" font-size="16" fill="#f8fafc" font-weight="bold">portfolio <tspan fill="#38bdf8">_</tspan></text>
    <text x="18" y="74" class="mono" font-size="10.5" fill="#94a3b8">Interactive developer portfolio showcasing</text>
    <text x="18" y="90" class="mono" font-size="10.5" fill="#94a3b8">AI systems, simulation work, and public builds.</text>

    <!-- Tags -->
    <rect x="18" y="108" width="55" height="20" class="ptag"/>
    <text x="28" y="122" class="ptag-txt">nextjs</text>
    
    <rect x="81" y="108" width="75" height="20" class="ptag"/>
    <text x="90" y="122" class="ptag-txt">typescript</text>

    <text x="18" y="140" class="mono" font-size="11" fill="#64748b">★ 0</text>
    <text x="50" y="140" class="mono" font-size="10" fill="#64748b">TypeScript</text>

    <!-- Circular Gauge: 92% -->
    <circle cx="345" cy="75" r="32" fill="none" stroke="#0d2138" stroke-width="7"/>
    <circle cx="345" cy="75" r="32" fill="none" stroke="#38bdf8" stroke-width="7" stroke-dasharray="201" stroke-dashoffset="16" stroke-linecap="round"/>
    <text x="345" y="80" class="mono" font-size="12" fill="#38bdf8" font-weight="bold" text-anchor="middle">92%</text>
  </g>

  <!-- Card 4: aether-audiophile -->
  <g transform="translate(455, 220)">
    <rect x="0" y="0" width="405" height="150" class="pcard"/>
    <circle cx="18" cy="20" r="3.5" fill="#a855f7"/>
    <text x="28" y="24" class="mono" font-size="11" fill="#64748b">Zine007MHIDRA/aether-audiophile</text>

    <text x="18" y="52" class="mono" font-size="16" fill="#f8fafc" font-weight="bold">aether-audiophile <tspan fill="#a855f7">_</tspan></text>
    <text x="18" y="74" class="mono" font-size="10.5" fill="#94a3b8">High-fidelity web application with refined</text>
    <text x="18" y="90" class="mono" font-size="10.5" fill="#94a3b8">audiophile acoustic staging and modern UI.</text>

    <!-- Tags -->
    <rect x="18" y="108" width="75" height="20" class="ptag"/>
    <text x="27" y="122" class="ptag-txt">typescript</text>
    
    <rect x="101" y="108" width="55" height="20" class="ptag"/>
    <text x="110" y="122" class="ptag-txt">audio</text>

    <text x="18" y="140" class="mono" font-size="11" fill="#64748b">★ 0</text>
    <text x="50" y="140" class="mono" font-size="10" fill="#64748b">TypeScript</text>

    <!-- Circular Gauge: 87% -->
    <circle cx="345" cy="75" r="32" fill="none" stroke="#0d2138" stroke-width="7"/>
    <circle cx="345" cy="75" r="32" fill="none" stroke="#a855f7" stroke-width="7" stroke-dasharray="201" stroke-dashoffset="26" stroke-linecap="round"/>
    <text x="345" y="80" class="mono" font-size="12" fill="#a855f7" font-weight="bold" text-anchor="middle">87%</text>
  </g>
</svg>
'''

def make_neofetch():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 270" width="100%" height="100%">
  <defs>
    <linearGradient id="neoBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
    </style>
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
  <g transform="translate(290, 75)" class="mono">
    <!-- Header -->
    <text x="0" y="20" font-size="14" font-weight="bold" fill="#00e5ff">zine007mhidra <tspan fill="#64748b" font-weight="normal">@github</tspan></text>
    <line x1="0" y1="30" x2="520" y2="30" stroke="#172e48" stroke-width="1"/>

    <!-- Spec rows -->
    <text x="0" y="55" font-size="12" fill="#38bdf8">Name</text>
    <text x="120" y="55" font-size="12" fill="#f8fafc">Zine El Abidine MHIDRA</text>

    <text x="0" y="78" font-size="12" fill="#38bdf8">Role</text>
    <text x="120" y="78" font-size="12" fill="#e2e8f0">AI &amp; Full-Stack Developer</text>

    <text x="0" y="101" font-size="12" fill="#38bdf8">Stars</text>
    <text x="120" y="101" font-size="12" fill="#f8fafc">3</text>

    <text x="0" y="124" font-size="12" fill="#38bdf8">Repos</text>
    <text x="120" y="124" font-size="12" fill="#f8fafc">12</text>

    <text x="0" y="147" font-size="12" fill="#38bdf8">Top Lang</text>
    <text x="120" y="147" font-size="12" fill="#38bdf8">TypeScript</text>

    <text x="0" y="170" font-size="12" fill="#38bdf8">Activity</text>
    <text x="120" y="170" font-size="12" fill="#00e5ff" font-weight="bold">158 contributions</text>

    <!-- Color Palette Swatches -->
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

def make_contribution_trail():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 170" width="100%" height="100%">
  <defs>
    <linearGradient id="trailBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="168" rx="10" fill="url(#trailBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Header -->
  <text x="30" y="32" class="mono" font-size="15" font-weight="bold" fill="#00e5ff">Contribution Activity</text>
  <text x="30" y="48" class="mono" font-size="11" fill="#94a3b8">158 contributions in the last year</text>

  <!-- Legend -->
  <g transform="translate(710, 22)" class="mono" font-size="10" fill="#64748b">
    <text x="0" y="10">Less</text>
    <rect x="30" y="0" width="10" height="10" rx="2" fill="#0e1f36"/>
    <rect x="44" y="0" width="10" height="10" rx="2" fill="#0284c7"/>
    <rect x="58" y="0" width="10" height="10" rx="2" fill="#0ea5e9"/>
    <rect x="72" y="0" width="10" height="10" rx="2" fill="#38bdf8"/>
    <rect x="86" y="0" width="10" height="10" rx="2" fill="#00e5ff"/>
    <text x="104" y="10">More</text>
  </g>

  <!-- Heatmap Grid: 50 weeks x 7 days -->
  <g transform="translate(30, 68)">
''' + generate_heatmap_cells() + '''
  </g>
</svg>
'''

def generate_heatmap_cells():
    # 50 columns x 7 rows
    import random
    random.seed(42)
    # Generate realistic clustering of 158 contributions across 32 active days
    colors = ["#0e1f36", "#0284c7", "#0ea5e9", "#38bdf8", "#00e5ff"]
    cells = []
    
    # Let's map active weeks (e.g. weeks 30-50 more dense)
    active_count = 0
    for col in range(50):
        for row in range(7):
            x = col * 16
            y = row * 12
            # default dark empty
            c = colors[0]
            # create clustered activity mainly in weeks 25-49
            if col > 32 and random.random() < 0.28 and active_count < 32:
                intensity = random.choice([1, 2, 3, 4])
                c = colors[intensity]
                active_count += 1
            cells.append(f'    <rect x="{x}" y="{y}" width="12" height="9" rx="2" fill="{c}"/>')
    return "\n".join(cells)

def make_connect():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 120" width="100%" height="100%">
  <defs>
    <linearGradient id="connBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1222"/>
    </linearGradient>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
      .cbtn { rx: 20px; fill: #07172e; stroke: #00e5ff; stroke-width: 1.2; }
      .cbtn-txt { font-family: ui-monospace, monospace; font-size: 12px; fill: #f8fafc; font-weight: 600; }
    </style>
  </defs>

  <!-- Container -->
  <rect x="1" y="1" width="878" height="118" rx="10" fill="url(#connBg)" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Centered Pill Buttons -->
  <g transform="translate(60, 40)">
    <!-- GitHub Button -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="160" height="40" class="cbtn"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#00e5ff" text-anchor="middle" font-weight="bold">G</text>
      <text x="44" y="24" class="cbtn-txt">@Zine007MHIDRA</text>
    </g>

    <!-- Portfolio Button -->
    <g transform="translate(180, 0)">
      <rect x="0" y="0" width="160" height="40" class="cbtn" stroke="#38bdf8"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#38bdf8" text-anchor="middle" font-weight="bold">↗</text>
      <text x="44" y="24" class="cbtn-txt">Live Portfolio</text>
    </g>

    <!-- LinkedIn Button -->
    <g transform="translate(360, 0)">
      <rect x="0" y="0" width="160" height="40" class="cbtn" stroke="#0ea5e9"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#0ea5e9" text-anchor="middle" font-weight="bold">in</text>
      <text x="44" y="24" class="cbtn-txt">LinkedIn Profile</text>
    </g>

    <!-- Email Button -->
    <g transform="translate(540, 0)">
      <rect x="0" y="0" width="220" height="40" class="cbtn" stroke="#22d3ee"/>
      <circle cx="24" cy="20" r="10" fill="#0b2447"/>
      <text x="24" y="24" class="mono" font-size="11" fill="#22d3ee" text-anchor="middle" font-weight="bold">@</text>
      <text x="44" y="24" class="cbtn-txt">zine.mhidra@gmail.com</text>
    </g>
  </g>
</svg>
'''

with open('assets/toolbox.svg', 'w', encoding='utf-8') as f:
    f.write(make_toolbox())

with open('assets/projects.svg', 'w', encoding='utf-8') as f:
    f.write(make_projects())

with open('assets/neofetch.svg', 'w', encoding='utf-8') as f:
    f.write(make_neofetch())

with open('assets/contribution-trail.svg', 'w', encoding='utf-8') as f:
    f.write(make_contribution_trail())

with open('assets/connect.svg', 'w', encoding='utf-8') as f:
    f.write(make_connect())

print("Created all SVG assets!")
