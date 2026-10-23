with open(r'd:\PF Ass\pf-assistant-legal\build_site.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Official Google Play 4-color triangle badge SVG
play_badge_svg = '''<svg width="24" height="24" viewBox="0 0 512 512" style="flex-shrink: 0;">
  <path fill="#4285F4" d="M47.1 23.3c-4.4 5.3-7.1 13.5-7.1 24.3v416.8c0 10.8 2.7 19 7.1 24.3l3.6 3.6 233.5-233.5v-5.6L50.7 19.7l-3.6 3.6z"/>
  <path fill="#FBBC04" d="M361.3 335.7l-77.1-77.1v-5.6l77.1-77.1 1.7 1 91.5 52c26.1 14.8 26.1 39.1 0 54l-91.5 52-1.7.8z"/>
  <path fill="#EA4335" d="M284.2 253L50.7 486.5c8.6 9.1 22.8 10.3 39 1.1l271.6-154.4-77.1-77.2z"/>
  <path fill="#34A853" d="M284.2 258.6l77.1-77.1L89.7 27.1C73.5 17.9 59.3 19.1 50.7 28.2L284.2 258.6z"/>
</svg>'''

# Official badge style with black pill look (standard Google Play button)
google_play_btn_hero = f'''<a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn" style="background: #000000; color: #FFFFFF !important; padding: 0.65rem 1.45rem; display: inline-flex; align-items: center; gap: 0.75rem; box-shadow: 0 4px 14px rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15);">
            {play_badge_svg}
            <div style="text-align: left; line-height: 1.15;">
              <span style="display: block; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.06em; opacity: 0.85; font-weight: 500;">GET IT ON</span>
              <span style="display: block; font-size: 1.05rem; font-weight: 700; letter-spacing: -0.01em;">Google Play</span>
            </div>
          </a>'''

google_play_btn_section = f'''<a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn" style="background: #000000; color: #FFFFFF !important; padding: 0.8rem 2.2rem; display: inline-flex; align-items: center; gap: 0.9rem; box-shadow: 0 6px 20px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); border-radius: var(--radius-lg);">
            {play_badge_svg}
            <div style="text-align: left; line-height: 1.15;">
              <span style="display: block; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.85; font-weight: 500;">GET IT ON</span>
              <span style="display: block; font-size: 1.25rem; font-weight: 700; letter-spacing: -0.01em;">Google Play</span>
            </div>
          </a>'''

# Replace in hero
import re
hero_pattern = r'<a href="https://play\.google\.com/store/apps/details\?id=com\.algoaurax\.pfpensionassistant"[^>]*>.*?</a>'

# Find all occurrences and replace
matches = list(re.finditer(hero_pattern, c, re.DOTALL))
print(f"Found {len(matches)} play store button matches")

if len(matches) >= 2:
    # First match is hero
    c = c[:matches[0].start()] + google_play_btn_hero + c[matches[0].end():]
    # Re-find second match
    matches2 = list(re.finditer(hero_pattern, c, re.DOTALL))
    if len(matches2) >= 2:
        c = c[:matches2[1].start()] + google_play_btn_section + c[matches2[1].end():]
        print("Replaced both buttons with official 4-color Google Play badges!")

with open(r'd:\PF Ass\pf-assistant-legal\build_site.py', 'w', encoding='utf-8') as f:
    f.write(c)
