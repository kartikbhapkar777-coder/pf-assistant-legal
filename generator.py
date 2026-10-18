import os

PAGES = [
    {
        "id": "home",
        "title": "PF Pension Assistant — Independent EPF & Pension Guidance",
        "description": "PF Pension Assistant by AlgoAuraX is an independent educational and procedural assistance app for Indian PF and EPS pension members.",
        "rel_base": "./",
        "out_file": "index.html",
        "header_title": "PF Pension Assistant",
        "header_subtitle": "Independent EPF & Pension Information and Step-by-Step Procedure Guide",
        "last_updated": "October 2026"
    },
    {
        "id": "privacy-policy",
        "title": "Privacy Policy — PF Pension Assistant",
        "description": "Comprehensive, verified Privacy Policy for the PF Pension Assistant Android application published under AlgoAuraX.",
        "rel_base": "../",
        "out_file": "privacy-policy/index.html",
        "header_title": "Privacy Policy",
        "header_subtitle": "Transparency on data collection, local SQLite storage, third-party services, and user privacy rights.",
        "last_updated": "October 18, 2026"
    },
    {
        "id": "terms",
        "title": "Terms and Conditions — PF Pension Assistant",
        "description": "Terms of use and service agreements for PF Pension Assistant and the PF Expert Assistance service by AlgoAuraX.",
        "rel_base": "../",
        "out_file": "terms/index.html",
        "header_title": "Terms and Conditions",
        "header_subtitle": "Legal rules, scope of informational assistance, user obligations, and limitations.",
        "last_updated": "October 18, 2026"
    },
    {
        "id": "refund-policy",
        "title": "Refund & Cancellation Policy — PF Pension Assistant",
        "description": "Transparent refund and cancellation terms for the ₹299 PF Expert Assistance service by AlgoAuraX.",
        "rel_base": "../",
        "out_file": "refund-policy/index.html",
        "header_title": "Refund and Cancellation Policy",
        "header_subtitle": "Terms governing service cancellation, duplicate transaction handling, and refund review procedures.",
        "last_updated": "October 18, 2026"
    },
    {
        "id": "disclaimer",
        "title": "Disclaimer — PF Pension Assistant",
        "description": "Important notice regarding non-affiliation with EPFO, Government of India, or any statutory authority.",
        "rel_base": "../",
        "out_file": "disclaimer/index.html",
        "header_title": "Independent Service Disclaimer",
        "header_subtitle": "Official notice clarifying that PF Pension Assistant is an independent tool operated under AlgoAuraX.",
        "last_updated": "October 18, 2026"
    },
    {
        "id": "data-deletion",
        "title": "Account & Data Deletion — PF Pension Assistant",
        "description": "Instructions and verified procedure to request deletion of app data and account records.",
        "rel_base": "../",
        "out_file": "data-deletion/index.html",
        "header_title": "Account and Data Deletion",
        "header_subtitle": "Step-by-step instructions for submitting data removal and account closure requests.",
        "last_updated": "October 18, 2026"
    },
    {
        "id": "contact",
        "title": "Contact & Support — PF Pension Assistant",
        "description": "Official verified support channels for PF Pension Assistant users via Email and WhatsApp Business.",
        "rel_base": "../",
        "out_file": "contact/index.html",
        "header_title": "Contact and Support",
        "header_subtitle": "Reach out directly for application queries, assistance support, or grievance escalation.",
        "last_updated": "October 18, 2026"
    }
]

def render_html_page(page_meta, body_content):
    rel = page_meta["rel_base"]
    page_id = page_meta["id"]

    nav_items = [
        {"id": "home", "href": f"{rel}", "label": "Home"},
        {"id": "privacy-policy", "href": f"{rel}privacy-policy/", "label": "Privacy Policy"},
        {"id": "terms", "href": f"{rel}terms/", "label": "Terms"},
        {"id": "refund-policy", "href": f"{rel}refund-policy/", "label": "Refund Policy"},
        {"id": "disclaimer", "href": f"{rel}disclaimer/", "label": "Disclaimer"},
        {"id": "data-deletion", "href": f"{rel}data-deletion/", "label": "Data Deletion"},
        {"id": "contact", "href": f"{rel}contact/", "label": "Contact"}
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
  <meta name="theme-color" content="#176B87">
  <link rel="stylesheet" href="{rel}css/style.css">
  <link rel="icon" type="image/png" sizes="32x32" href="{rel}images/favicon-32x32.png">
  <link rel="apple-touch-icon" sizes="192x192" href="{rel}images/icon-192.png">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="{rel}" class="brand-link" aria-label="PF Pension Assistant Home">
        <img src="{rel}images/app-logo.png" alt="PF Pension Assistant Logo" class="brand-logo-img">
        <div>
          <span>PF Pension Assistant</span>
          <span class="brand-sub">by AlgoAuraX</span>
        </div>
      </a>

      <nav aria-label="Main Navigation">
        <ul class="nav-links">
{desktop_nav_html}
        </ul>
      </nav>

      <div class="header-actions">
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
          <p style="font-size: 0.9rem; margin-bottom: 0.75rem;">
            An independent educational and navigational guide developed under <strong>AlgoAuraX</strong> to assist Indian employees with EPF, EPS pension rules, online procedures, and grievance handling.
          </p>
          <div class="badge badge-primary">Independent Service</div>
        </div>

        <div class="footer-col">
          <h4>Legal & Policies</h4>
          <ul class="footer-links">
            <li><a href="{rel}privacy-policy/">Privacy Policy</a></li>
            <li><a href="{rel}terms/">Terms and Conditions</a></li>
            <li><a href="{rel}refund-policy/">Refund & Cancellation</a></li>
            <li><a href="{rel}disclaimer/">Independent Disclaimer</a></li>
            <li><a href="{rel}data-deletion/">Account & Data Deletion</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Support & Inquiries</h4>
          <ul class="footer-links">
            <li><a href="{rel}contact/">Contact Support</a></li>
            <li><a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></li>
            <li><a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer">WhatsApp: +91 9921200935</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 AlgoAuraX &bull; PF Pension Assistant. All rights reserved.</div>
        <div style="font-size: 0.8rem;">
          Notice: Not affiliated with or endorsed by EPFO or Government of India.
        </div>
      </div>
    </div>
  </footer>

  <script src="{rel}js/main.js"></script>
</body>
</html>
"""

print("Generator helper defined successfully.")
