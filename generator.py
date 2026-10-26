import os

PAGES = [
    {
        "id": "home",
        "title": "PF Pension Assistant — Independent EPF & EPS-95 Guidance",
        "description": "PF Pension Assistant: Independent educational resource for EPS-95 pension calculation, EPF interest estimation, EPFO claim guides, and assisted advisory.",
        "rel_base": "./",
        "out_file": "index.html",
        "header_title": "PF Pension Assistant",
        "header_subtitle": "Independent EPF & EPS-95 Pension Information and Procedure Guidance",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "privacy-policy",
        "title": "Privacy Policy — PF Pension Assistant",
        "description": "Privacy Policy for PF Pension Assistant. Zero credential storage, Firebase authentication, Google Play Data Safety compliance, and user rights.",
        "rel_base": "../",
        "out_file": "privacy-policy/index.html",
        "header_title": "Privacy Policy",
        "header_subtitle": "Complete transparency regarding on-device processing, Firebase authentication, zero credential storage, and Google Play Data Safety.",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "terms",
        "title": "Terms of Service — PF Pension Assistant",
        "description": "Terms of Service for PF Pension Assistant and ₹299 Assisted Advisory service by AlgoAuraX. Strictly non-government and private educational resource.",
        "rel_base": "../",
        "out_file": "terms/index.html",
        "header_title": "Terms of Service",
        "header_subtitle": "Legal agreements, scope of ₹299 assisted advisory, non-government status, official source verification, and user responsibilities.",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "refund-policy",
        "title": "Refund & Cancellation Policy — PF Pension Assistant",
        "description": "Transparent refund and cancellation terms for ₹299 PF Expert Advisory. 100% refund guarantee within 48-hour response window.",
        "rel_base": "../",
        "out_file": "refund-policy/index.html",
        "header_title": "Refund and Cancellation Policy",
        "header_subtitle": "Fair review terms, 100% refund guarantee, duplicate transaction resolution, and 5-7 business day settlement.",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "disclaimer",
        "title": "Disclaimer — PF Pension Assistant",
        "description": "Statutory notice of non-affiliation with EPFO, Ministry of Labour, or Government of India. Direct links to official government portals.",
        "rel_base": "../",
        "out_file": "disclaimer/index.html",
        "header_title": "Disclaimer",
        "header_subtitle": "Official legal notice confirming independent private operation and direct official government source links.",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "data-deletion",
        "title": "Account & Data Deletion — PF Pension Assistant",
        "description": "Instructions for requesting deletion of user data and support inquiries under AlgoAuraX.",
        "rel_base": "../",
        "out_file": "data-deletion/index.html",
        "header_title": "Account and Data Deletion",
        "header_subtitle": "Google Play compliant data deletion instructions and verified support procedures.",
        "last_updated": "October 26, 2026"
    },
    {
        "id": "contact",
        "title": "Contact Us & Support — PF Pension Assistant",
        "description": "Official support desk for PF Pension Assistant. Email: sachinvr141@gmail.com, WhatsApp: +91 9921200935 (9 AM - 7 PM IST, Mon-Sat).",
        "rel_base": "../",
        "out_file": "contact/index.html",
        "header_title": "Contact Us",
        "header_subtitle": "Reach our dedicated support team via WhatsApp Business or official email desk.",
        "last_updated": "October 26, 2026"
    }
]

def render_html_page(page_meta, body_content):
    rel = page_meta["rel_base"]
    page_id = page_meta["id"]

    nav_items = [
        {"id": "home", "href": f"{rel}", "label": "Home"},
        {"id": "privacy-policy", "href": f"{rel}privacy-policy/", "label": "Privacy Policy"},
        {"id": "terms", "href": f"{rel}terms/", "label": "Terms of Service"},
        {"id": "refund-policy", "href": f"{rel}refund-policy/", "label": "Refund Policy"},
        {"id": "disclaimer", "href": f"{rel}disclaimer/", "label": "Disclaimer"},
        {"id": "contact", "href": f"{rel}contact/", "label": "Contact Us"}
    ]

    desktop_nav_html = "\n".join([
        f'          <li><a href="{item["href"]}" class="{"active" if item["id"] == page_id else ""}">{item["label"]}</a></li>'
        for item in nav_items
    ])

    mobile_nav_html = "\n".join([
        f'        <li><a href="{item["href"]}" class="{"active" if item["id"] == page_id else ""}">{item["label"]}</a></li>'
        for item in nav_items
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_meta["title"]}</title>
  <meta name="description" content="{page_meta["description"]}">
  <meta name="theme-color" content="#0B1926">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{rel}css/style.css?v=1793026882">
  <link rel="icon" type="image/png" sizes="32x32" href="{rel}images/favicon-32x32.png?v=8">
  <link rel="apple-touch-icon" sizes="192x192" href="{rel}images/icon-192.png?v=8">
</head>
<body>
  <!-- MANDATORY GLOBAL NON-GOVERNMENT DISCLAIMER BANNER (Header Top of EVERY Page) -->
  <div class="global-gov-disclaimer-banner" role="alert">
    <div class="container global-gov-disclaimer-inner">
      <svg class="disclaimer-alert-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
      </svg>
      <p>
        <strong>DISCLAIMER:</strong> PF Pension Assistant and this website are independent educational &amp; informational resources. This service <strong>DOES NOT represent, and is NOT affiliated with, endorsed by, or authorized by</strong> the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India.
      </p>
    </div>
  </div>

  <header class="site-header">
    <div class="container header-inner">
      <a href="{rel}" class="brand-link" aria-label="PF Pension Assistant Home">
        <img src="{rel}images/app-logo.png?v=8" alt="PF Pension Assistant Logo" class="brand-logo-img">
        <div>
          <span>PF Pension Assistant</span>
          <span class="brand-sub">Independent Resource by AlgoAuraX</span>
        </div>
      </a>

      <nav aria-label="Main Navigation">
        <ul class="nav-links">
{desktop_nav_html}
        </ul>
      </nav>

      <div class="header-actions">
        <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn btn-primary nav-play-btn" style="padding: 0.45rem 1rem; font-size: 0.85rem; display: inline-flex; align-items: center; gap: 0.45rem;">
          <svg width="15" height="15" viewBox="0 0 512 512" fill="currentColor"><path fill="#4285F4" d="M47.1 23.3c-4.4 5.3-7.1 13.5-7.1 24.3v416.8c0 10.8 2.7 19 7.1 24.3l3.6 3.6 233.5-233.5v-5.6L50.7 19.7l-3.6 3.6z"/><path fill="#FBBC04" d="M361.3 335.7l-77.1-77.1v-5.6l77.1-77.1 1.7 1 91.5 52c26.1 14.8 26.1 39.1 0 54l-91.5 52-1.7.8z"/><path fill="#EA4335" d="M284.2 253L50.7 486.5c8.6 9.1 22.8 10.3 39 1.1l271.6-154.4-77.1-77.2z"/><path fill="#34A853" d="M284.2 258.6l77.1-77.1L89.7 27.1C73.5 17.9 59.3 19.1 50.7 28.2L284.2 258.6z"/></svg>
          Google Play
        </a>

        <button type="button" class="theme-toggle" aria-label="Toggle dark/light theme">
          <span class="theme-toggle-icon" aria-hidden="true">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          </span>
          <span class="theme-toggle-label">Dark</span>
        </button>

        <button type="button" class="mobile-menu-btn" aria-label="Open navigation menu" aria-expanded="false">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>

    <div class="mobile-nav-menu" aria-label="Mobile Navigation">
      <ul>
{mobile_nav_html}
        <li style="margin-top: 0.5rem; padding-top: 0.5rem; border-top: 1px solid var(--color-border);">
          <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" style="color: var(--color-primary); font-weight: 700;">
            Download on Google Play &rarr;
          </a>
        </li>
      </ul>
    </div>
  </header>

  <main id="main-content">
{body_content}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>PF Pension Assistant</h4>
          <p style="font-size: 0.9rem; margin-bottom: 0.85rem; line-height: 1.6;">
            A privacy-focused mobile and procedural assistance tool developed by <strong>AlgoAuraX</strong>. Built with a zero-credential-storage, on-device architecture to help Indian subscribers calculate EPS-95 pension estimates, project EPF balance, and navigate complex claim procedures.
          </p>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <span class="badge badge-primary">Private Entity</span>
            <span class="badge badge-success">Zero Credential Storage</span>
          </div>
        </div>

        <div class="footer-col">
          <h4>Legal Policies &amp; Compliance</h4>
          <ul class="footer-links">
            <li><a href="{rel}privacy-policy/">Privacy Policy</a></li>
            <li><a href="{rel}terms/">Terms of Service</a></li>
            <li><a href="{rel}refund-policy/">Refund &amp; Cancellation Policy</a></li>
            <li><a href="{rel}disclaimer/">Disclaimer</a></li>
            <li><a href="{rel}data-deletion/">Account &amp; Data Deletion</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Official Government Sources</h4>
          <ul class="footer-links">
            <li><a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">Official EPFO Portal &nearr;</a></li>
            <li><a href="https://unifiedportal-mem.epfindia.gov.in/memberinterface/" target="_blank" rel="noopener noreferrer">EPFO Member e-Sewa Portal &nearr;</a></li>
            <li><a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer">EPFO Member Passbook &nearr;</a></li>
            <li><a href="https://epfigms.gov.in" target="_blank" rel="noopener noreferrer">EPFiGMS Grievance Portal &nearr;</a></li>
          </ul>
        </div>
      </div>

      <div class="disclaimer-banner" style="margin: 1.5rem 0 2rem; background: var(--color-surface-subtle); border-left-color: var(--color-warning);">
        <svg class="disclaimer-banner-icon" style="color: var(--color-warning);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        <div style="font-size: 0.84rem; line-height: 1.55;">
          <strong>Statutory Non-Government Notice:</strong> PF Pension Assistant and AlgoAuraX are independent private entities and are <strong>NOT</strong> affiliated with, endorsed by, or authorized by the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India. The ₹299 fee is strictly a private consulting fee for 1-on-1 assistance and does NOT guarantee claim approval or pension sanction by EPFO authorities. Users must verify official records on government portals: <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">epfindia.gov.in</a> &bull; <a href="https://unifiedportal-mem.epfindia.gov.in/memberinterface/" target="_blank" rel="noopener noreferrer">Member e-Sewa</a> &bull; <a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer">Passbook Portal</a>.
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 AlgoAuraX &bull; PF Pension Assistant. All rights reserved. Support: <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> | WhatsApp: +91 9921200935</div>
        <div>Strictly compliant with Google Play Developer Policies &amp; Razorpay Merchant KYC Guidelines.</div>
      </div>
    </div>
  </footer>

  <script src="{rel}js/main.js"></script>
</body>
</html>
"""
