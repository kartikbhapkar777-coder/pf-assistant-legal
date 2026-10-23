with open(r'd:\PF Ass\pf-assistant-legal\build_site.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update hero buttons
hero_old = """        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.75rem;">
          <a href="./contact/" class="btn btn-primary">Contact Support</a>
          <a href="./privacy-policy/" class="btn btn-secondary">Read Privacy Policy</a>
        </div>"""

hero_new = """        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.75rem;">
          <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3.609 1.814L13.792 12 3.61 22.186a1.996 1.996 0 0 1-1.61-.418c-.463-.387-.732-.977-.732-1.621V3.853c0-.644.269-1.234.732-1.621.464-.388 1.056-.533 1.609-.418zm11.597 11.599L6.96 21.659l9.317-5.38a1.696 1.696 0 0 0 0-2.866l-1.071-.62zm0-2.826l1.071-.62a1.696 1.696 0 0 0 0-2.866l-9.317-5.38 8.246 8.866zm1.414 1.413l3.197-1.846a1.706 1.706 0 0 0 0-2.866L16.62 7.288l-1.414 1.414 1.414 1.414z"/></svg>
            Download on Google Play
          </a>
          <a href="./contact/" class="btn btn-secondary">Contact Support</a>
          <a href="./privacy-policy/" class="btn btn-secondary">Privacy Policy</a>
        </div>"""

# 2. Update Play Store section
play_section_old = """      <!-- App Download / Configuration Note -->
      <section style="margin: 3rem 0; text-align: center; padding: 2rem; background: var(--color-surface-subtle); border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
        <h3>Google Play Store Release</h3>
        <p style="max-width: 650px; margin: 0.5rem auto 1.5rem; color: var(--color-text-secondary);">
          PF Pension Assistant is currently in production readiness and compliance review for distribution on Android through the Google Play Store. The verified store link will be published upon release completion.
        </p>
        <span class="badge badge-primary">Android Platform Application</span>
      </section>"""

play_section_new = """      <!-- Google Play Store Download Section -->
      <section style="margin: 3.5rem 0; text-align: center; padding: 2.5rem 1.5rem; background: var(--color-surface); border-radius: var(--radius-xl); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
        <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Available on Android</span>
        <h2 style="margin-bottom: 0.5rem;">Get PF Pension Assistant on Google Play</h2>
        <p style="max-width: 620px; margin: 0 auto 1.75rem; color: var(--color-text-secondary); font-size: 1.05rem;">
          Currently live in Closed Testing track. Eligible testers can install directly on their Android device to access procedural PF & pension assistance.
        </p>
        <div style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.75rem;">
          <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 1.05rem; padding: 0.85rem 2rem; display: inline-flex; align-items: center; gap: 0.65rem;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M3.609 1.814L13.792 12 3.61 22.186a1.996 1.996 0 0 1-1.61-.418c-.463-.387-.732-.977-.732-1.621V3.853c0-.644.269-1.234.732-1.621.464-.388 1.056-.533 1.609-.418zm11.597 11.599L6.96 21.659l9.317-5.38a1.696 1.696 0 0 0 0-2.866l-1.071-.62zm0-2.826l1.071-.62a1.696 1.696 0 0 0 0-2.866l-9.317-5.38 8.246 8.866zm1.414 1.413l3.197-1.846a1.706 1.706 0 0 0 0-2.866L16.62 7.288l-1.414 1.414 1.414 1.414z"/></svg>
            Install via Google Play
          </a>
          <span style="font-size: 0.82rem; color: var(--color-text-muted); font-family: var(--font-mono);">Package: com.algoaurax.pfpensionassistant</span>
        </div>
      </section>"""

if hero_old in c:
    c = c.replace(hero_old, hero_new)
    print("Updated Hero buttons")
else:
    print("Hero old not found")

if play_section_old in c:
    c = c.replace(play_section_old, play_section_new)
    print("Updated Play Store section")
else:
    print("Play section old not found")

with open(r'd:\PF Ass\pf-assistant-legal\build_site.py', 'w', encoding='utf-8') as f:
    f.write(c)
