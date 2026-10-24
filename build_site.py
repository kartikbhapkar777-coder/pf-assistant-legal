import os
from generator import PAGES, render_html_page

play_badge_svg = '''<svg width="24" height="24" viewBox="0 0 512 512" style="flex-shrink: 0;">
  <path fill="#4285F4" d="M47.1 23.3c-4.4 5.3-7.1 13.5-7.1 24.3v416.8c0 10.8 2.7 19 7.1 24.3l3.6 3.6 233.5-233.5v-5.6L50.7 19.7l-3.6 3.6z"/>
  <path fill="#FBBC04" d="M361.3 335.7l-77.1-77.1v-5.6l77.1-77.1 1.7 1 91.5 52c26.1 14.8 26.1 39.1 0 54l-91.5 52-1.7.8z"/>
  <path fill="#EA4335" d="M284.2 253L50.7 486.5c8.6 9.1 22.8 10.3 39 1.1l271.6-154.4-77.1-77.2z"/>
  <path fill="#34A853" d="M284.2 258.6l77.1-77.1L89.7 27.1C73.5 17.9 59.3 19.1 50.7 28.2L284.2 258.6z"/>
</svg>'''

# -------------------------------------------------------------
# 1. HOME PAGE
# -------------------------------------------------------------
home_body = f"""
    <div class="container">
      <!-- Hero Section -->
      <section class="page-header" style="text-align: center; border-bottom: none; padding-top: 3rem; padding-bottom: 2rem;">
        <div style="margin-bottom: 1.25rem;">
          <img src="./images/app-logo.png?v=6" alt="PF Pension Assistant Logo" style="width: 105px; height: 105px; object-fit: cover; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); border: 2px solid var(--color-border);">
        </div>
        <div class="badge badge-primary" style="margin-bottom: 1rem;">AlgoAuraX Legal & Support Portal</div>
        <h1 style="font-size: 2.55rem; max-width: 820px; margin-left: auto; margin-right: auto;">
          Intelligent Guidance for Your EPF Savings & EPS-95 Pension
        </h1>
        <p class="page-subtitle" style="margin-left: auto; margin-right: auto; font-size: 1.12rem;">
          PF Pension Assistant is an independent Android application engineered with a privacy-first, zero-login architecture to help Indian subscribers calculate pension entitlements, estimate provident fund growth, and navigate complex claim procedures.
        </p>

        <!-- Primary Call to Actions -->
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 2rem;">
          <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn" style="background: #000000; color: #FFFFFF !important; padding: 0.65rem 1.6rem; display: inline-flex; align-items: center; gap: 0.85rem; box-shadow: 0 4px 14px rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15);">
            {play_badge_svg}
            <div style="text-align: left; line-height: 1.15;">
              <span style="display: block; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.06em; opacity: 0.85; font-weight: 500;">GET IT ON</span>
              <span style="display: block; font-size: 1.05rem; font-weight: 700; letter-spacing: -0.01em;">Google Play</span>
            </div>
          </a>
          <a href="https://wa.me/919921200935?text=Hello%20PF%20Pension%20Assistant%20Support" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="padding: 0.75rem 1.45rem;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            Chat with Support on WhatsApp
          </a>
          <a href="./privacy-policy/" class="btn btn-secondary">Privacy Policy</a>
        </div>
      </section>

      <!-- App Disclaimer Banner -->
      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Statutory Disclaimer & Non-Affiliation Notice:</strong> PF Pension Assistant is an independent utility application developed by <strong>AlgoAuraX</strong>. It is <strong>NOT</strong> affiliated with, authorized, endorsed, or sponsored by the Employees' Provident Fund Organisation (EPFO), the Ministry of Labour and Employment, or the Government of India. Official government services must be conducted solely on official portals (<a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">epfindia.gov.in</a>).
        </div>
      </div>

      <!-- App Core Features Grid -->
      <section style="margin: 3.5rem 0;">
        <div style="text-align: center; margin-bottom: 2.25rem;">
          <span class="badge badge-primary" style="margin-bottom: 0.5rem;">Powerful Utilities</span>
          <h2>Everything You Need for EPF & EPS Management</h2>
          <p style="color: var(--color-text-secondary); max-width: 620px; margin: 0 auto;">Engineered to clarify complex retirement calculations and procedural rules without compromising your privacy.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
          <!-- Feature 1 -->
          <div class="card">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-primary-container); align-items: center; justify-content: center; color: var(--color-primary); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>
            </div>
            <h3 class="card-title">1. EPS-95 Monthly Pension Calculator</h3>
            <p class="card-subtitle">
              Accurately estimates monthly pension entitlement based on pensionable service years, 60-month average salary, and retirement age (early pension from age 50 vs full superannuation at 58). Automatically applies the statutory 2-year bonus service weightage for 20+ years of eligible service.
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="card">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-primary-container); align-items: center; justify-content: center; color: var(--color-primary); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            </div>
            <h3 class="card-title">2. EPF Balance & Interest Growth Estimator</h3>
            <p class="card-subtitle">
              Projects compound provident fund savings based on your monthly basic wage, employee/employer contributions, and the official EPFO annual interest rate (8.25% p.a.). See year-by-year accumulation and forecast your lump-sum corpus at retirement.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="card">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-primary-container); align-items: center; justify-content: center; color: var(--color-primary); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            </div>
            <h3 class="card-title">3. EPFO Claim Forms & Procedures Guide</h3>
            <p class="card-subtitle">
              Step-by-step guidance for Form 19 (Final PF Settlement), Form 10C (EPS Withdrawal / Scheme Certificate), Form 31 (Advance for Illness, Housing, Marriage), and Form 10D (Monthly Pension Application). Clear requirements on necessary attestation and joint declarations.
            </p>
          </div>

          <!-- Feature 4 -->
          <div class="card">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-primary-container); align-items: center; justify-content: center; color: var(--color-primary); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <h3 class="card-title">4. Personalized Expert Assistance (₹299)</h3>
            <p class="card-subtitle">
              One-on-one assisted guidance for resolving claim rejections, UAN activation errors, joint declarations, father name mismatches, and Aadhaar/bank KYC discrepancies. Direct support desk via WhatsApp (+91 9921200935) with unique Request IDs (e.g., PF-REQ-XXXXX).
            </p>
          </div>

          <!-- Feature 5 -->
          <div class="card" style="grid-column: 1 / -1;">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-success-bg); align-items: center; justify-content: center; color: var(--color-success); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            </div>
            <h3 class="card-title">5. 100% Privacy & Zero-Login Architecture</h3>
            <p class="card-subtitle" style="max-width: 850px;">
              No user account or password required. Zero collection or storage of sensitive EPFO credentials, UAN passwords, OTPs, or CAPTCHAs. All financial calculations run strictly on-device without external server transmission. Zero data shared with third parties or advertisers.
            </p>
          </div>
        </div>
      </section>

      <!-- Transparent Pricing Card Section (Razorpay Merchant Compliant) -->
      <section style="margin: 3.5rem 0;">
        <div class="card" style="border: 2px solid var(--color-primary); background: var(--color-surface); padding: 2.25rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem;">
            <div style="max-width: 620px;">
              <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
                <span class="badge badge-primary">Transparent Pricing</span>
                <span class="badge badge-success">Razorpay Verified</span>
              </div>
              <h2>PF Expert Assistance — ₹299 per Request</h2>
              <p style="color: var(--color-text-secondary); margin-bottom: 1.25rem; line-height: 1.6;">
                Stuck with a rejected claim, KYC discrepancy, joint declaration requirement, or multiple UAN accounts? Our dedicated specialist reviews your documentation and provides clear procedural guidance.
              </p>
              <ul style="margin-bottom: 1.25rem;">
                <li>Individual review of your specific procedural problem and rejection grounds</li>
                <li>Clear guidance on required documentation, forms, and employer attestation</li>
                <li>Direct handoff to our dedicated WhatsApp support desk (+91 9921200935)</li>
                <li>Assigned unique Request ID (e.g. <code>PF-REQ-XXXXX</code>) for end-to-end tracking</li>
                <li><strong>100% Refund Guarantee</strong> if our specialist fails to respond within 48 business hours</li>
              </ul>
              <div style="font-size: 0.85rem; color: var(--color-text-muted);">
                * Note: The ₹299 fee is strictly a private consultancy and procedural advisory fee. It does not and cannot guarantee claim approval or expedite government processing times. Official claims must be submitted by the user through official EPFO portals.
              </div>
            </div>

            <div style="text-align: center; min-width: 260px; padding: 2rem; background: var(--color-surface-subtle); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
              <div style="font-size: 0.82rem; text-transform: uppercase; font-weight: 700; color: var(--color-text-muted); letter-spacing: 0.05em;">One-Time Advisory Fee</div>
              <div style="font-size: 3rem; font-weight: 800; color: var(--color-primary); margin: 0.25rem 0; line-height: 1;">₹299</div>
              <div style="font-size: 0.85rem; color: var(--color-text-secondary); margin-bottom: 1.5rem;">Per Assistance Request</div>
              
              <a href="https://wa.me/919921200935?text=Hello%20PF%20Pension%20Assistant%20Support%2C%20I%20would%20like%20to%20request%20the%20Rs%20299%20PF%20Expert%20Assistance" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; margin-bottom: 0.65rem;">
                Inquire via WhatsApp
              </a>
              <div style="font-size: 0.78rem; color: var(--color-text-muted);">Secure payment via Razorpay</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Google Play Store Download Section -->
      <section style="margin: 3.5rem 0; text-align: center; padding: 3rem 1.5rem; background: var(--color-surface); border-radius: var(--radius-xl); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
        <span class="badge badge-primary" style="margin-bottom: 0.75rem;">Android Application</span>
        <h2 style="margin-bottom: 0.5rem;">Get PF Pension Assistant on Google Play</h2>
        <p style="max-width: 620px; margin: 0 auto 1.75rem; color: var(--color-text-secondary); font-size: 1.05rem;">
          Download the latest release to calculate EPS-95 pensions, forecast PF compound interest, and access step-by-step procedure guides directly on your phone.
        </p>
        <div style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.75rem;">
          <a href="https://play.google.com/store/apps/details?id=com.algoaurax.pfpensionassistant" target="_blank" rel="noopener noreferrer" class="btn" style="background: #000000; color: #FFFFFF !important; padding: 0.75rem 2.2rem; display: inline-flex; align-items: center; gap: 0.85rem; box-shadow: 0 6px 20px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.2); border-radius: var(--radius-lg);">
            {play_badge_svg}
            <div style="text-align: left; line-height: 1.15;">
              <span style="display: block; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.85; font-weight: 500;">GET IT ON</span>
              <span style="display: block; font-size: 1.25rem; font-weight: 700; letter-spacing: -0.01em;">Google Play</span>
            </div>
          </a>
          <span style="font-size: 0.82rem; color: var(--color-text-muted); font-family: var(--font-mono);">Package ID: com.algoaurax.pfpensionassistant</span>
        </div>
      </section>

      <!-- Legal Links Grid -->
      <section style="margin: 4rem 0;">
        <h2 style="margin-bottom: 1.5rem;">Legal Agreements & Policy Documentation</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
          <a href="./privacy-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Privacy Policy &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Zero-login architecture, on-device calculations, and zero storage of passwords or OTPs.</p>
          </a>
          <a href="./terms/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Terms & Conditions &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Scope of ₹299 assisted advisory, non-affiliation, and disclaimer of government outcomes.</p>
          </a>
          <a href="./refund-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Refund & Cancellation &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">100% refund guarantee within 48-hour response window, duplicate charge resolution, 5-7 days credit.</p>
          </a>
          <a href="./disclaimer/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Non-Affiliation Disclaimer &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Statutory notice of non-affiliation with EPFO or Govt of India, plus direct official links.</p>
          </a>
          <a href="./contact/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Contact Us &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Email: sachinvr141@gmail.com, WhatsApp: +91 9921200935 (9 AM - 7 PM Mon-Sat).</p>
          </a>
        </div>
      </section>
    </div>
"""

# -------------------------------------------------------------
# 2. PRIVACY POLICY
# -------------------------------------------------------------
privacy_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Google Play Data Safety Compliant</div>
        <h1 class="page-title">Privacy Policy</h1>
        <p class="page-subtitle">Effective Date: October 24, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant (Android)</p>
        <div class="meta-info">
          <span>Target Audience: 18+ (Working professionals & pensioners)</span>
          <span>Contact Email: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Privacy Commitment:</strong> PF Pension Assistant is built with a zero-login, on-device architecture. We <strong>never</strong> ask for, store, transmit, or sell your UAN passwords, OTPs, Aadhaar numbers, CAPTCHAs, or bank login credentials.
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Introduction & Overview</h2>
          <p>
            This Privacy Policy governs the manner in which <strong>PF Pension Assistant</strong> (the "Application"), developed and maintained under the brand <strong>AlgoAuraX</strong> ("we", "us", or "our"), handles information. We are committed to protecting the privacy of users ("User" or "you") who download our Android app or visit our legal website.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Zero-Login & On-Device Processing Architecture</h2>
          <p>
            The Application is engineered with a strict <strong>"No Data Collected, No Data Shared"</strong> philosophy:
          </p>
          <ul>
            <li><strong>No User Account or Login Required:</strong> Users can freely use the EPS-95 pension calculator, EPF interest estimator, and procedural guides without registering an account.</li>
            <li><strong>Strictly On-Device Execution:</strong> All numerical calculations (service years, pensionable salary, compound interest forecasts) execute strictly within your phone's memory. No inputs are transmitted to external cloud servers.</li>
            <li><strong>Zero Storage of EPFO Credentials:</strong> The app does not request or store your Universal Account Number (UAN) password, Member Portal login, Aadhaar number, or SMS OTPs.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>3. Information Collected for the ₹299 Assisted Advisory</h2>
          <p>
            When a user voluntarily requests the optional <strong>"PF Expert Assistance"</strong> (₹299 fee) service, the following details are submitted to initiate support:
          </p>
          <ul>
            <li><strong>Name & Contact Mobile:</strong> To identify the inquiry and communicate via WhatsApp.</li>
            <li><strong>Service Category & Problem Description:</strong> Summary of the procedural issue (e.g. claim rejection reason, joint declaration inquiry).</li>
            <li><strong>Payment Transaction Identifier:</strong> Razorpay payment ID and generated Request ID (e.g. <code>PF-REQ-XXXXX</code>) for payment reconciliation.</li>
          </ul>
          <div class="highlight-box danger">
            <strong>STRICT PROHIBITION:</strong><br>
            Users are explicitly instructed <strong>NEVER</strong> to send passwords, OTPs, banking PINs, or Aadhaar numbers to our support desk. Our team will never ask for confidential authentication credentials.
          </div>
        </section>

        <section class="legal-section">
          <h2>4. Third-Party Service Providers</h2>
          <ul>
            <li><strong>Google Play Services:</strong> Core runtime compatibility and app delivery.</li>
            <li><strong>Razorpay Software Private Limited:</strong> When purchasing the ₹299 advisory, payments are processed by Razorpay under PCI-DSS certified security. We do not store credit/debit card numbers or net-banking passwords.</li>
            <li><strong>WhatsApp (Meta):</strong> Optional user-initiated support communication taking place under WhatsApp's end-to-end encryption.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. Data Retention & User Rights</h2>
          <p>
            You have the right to request deletion of your support conversation and transaction reference at any time by contacting <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a>. Statutory financial records are retained only for the period mandated by applicable Indian tax regulations.
          </p>
        </section>

        <section class="legal-section">
          <h2>6. Contact Regarding Privacy</h2>
          <div class="card">
            <p style="margin-bottom: 0.5rem;"><strong>Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>WhatsApp Support:</strong> <a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer">+91 9921200935</a></p>
          </div>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 3. TERMS AND CONDITIONS
# -------------------------------------------------------------
terms_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Legal Agreement & KYC Compliant</div>
        <h1 class="page-title">Terms & Conditions</h1>
        <p class="page-subtitle">Effective Date: October 24, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Agreement to Terms</h2>
          <p>
            These Terms and Conditions constitute a legally binding agreement between you and <strong>AlgoAuraX</strong> ("we", "us", or "our"), governing your use of the <strong>PF Pension Assistant</strong> Android application and this legal website.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Independent Status & Non-Affiliation Notice</h2>
          <div class="highlight-box warning">
            <strong>CRITICAL STATUTORY NOTICE:</strong><br>
            PF Pension Assistant and AlgoAuraX are independent private entities and are <strong>NOT</strong> affiliated with, authorized, endorsed, or sponsored by the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India. Official government filings and passbook downloads must always be performed through the official portal (<a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">epfindia.gov.in</a>) or the UMANG application.
          </div>
        </section>

        <section class="legal-section">
          <h2>3. Nature of Service: PF Expert Assistance (₹299)</h2>
          <p>
            The Application provides a voluntary, private 1-on-1 consultation service for an assisted advisory fee of <strong>₹299 per request</strong>:
          </p>
          <ul>
            <li><strong>Consultancy & Guidance Only:</strong> The ₹299 fee is strictly a private consultancy and procedural advisory fee for review of paperwork, rejection analysis, and form guidance.</li>
            <li><strong>No Outcome Guarantee:</strong> The fee does <strong>NOT</strong> guarantee claim approval, pension approval, claim settlement, or expedited processing by EPFO authorities. Decisions rest solely with jurisdictional Regional PF Commissioners.</li>
            <li><strong>Official Submission by User:</strong> The user must independently submit all claims and grievances via official government portals.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. User Responsibilities & Prohibitions</h2>
          <ul>
            <li>Users must provide truthful and accurate information during advisory intake.</li>
            <li>Users must <strong>never</strong> share UAN passwords, OTPs, or banking PINs with our support desk.</li>
            <li>Users agree not to use the app for fraudulent, unlawful, or unauthorized activities.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. Payment Terms & Third-Party Gateways</h2>
          <p>
            Payments are collected securely via authorized payment gateways (e.g. Razorpay). The fee of ₹299 is transparently presented prior to transaction initiation.
          </p>
        </section>

        <section class="legal-section">
          <h2>6. Limitation of Liability & Governing Law</h2>
          <p>
            To the maximum extent permitted by applicable Indian laws, AlgoAuraX shall not be liable for any indirect, incidental, or consequential damages resulting from portal downtimes, employer non-compliance, or EPFO decisions. These Terms are governed by the laws of India.
          </p>
        </section>

        <section class="legal-section">
          <h2>7. Contact Information</h2>
          <div class="card">
            <p style="margin-bottom: 0.5rem;"><strong>Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>WhatsApp / Phone:</strong> +91 9921200935 (9:00 AM – 7:00 PM IST, Mon–Sat)</p>
          </div>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 4. REFUND AND CANCELLATION POLICY
# -------------------------------------------------------------
refund_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Razorpay Merchant KYC Compliant</div>
        <h1 class="page-title">Refund & Cancellation Policy</h1>
        <p class="page-subtitle">Effective Date: October 24, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
        <div class="meta-info">
          <span>Fee: ₹299 per Assistance Request</span>
          <span>Desk: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Overview & Commitment</h2>
          <p>
            AlgoAuraX strives to maintain complete consumer transparency for the ₹299 PF Expert Assistance service. We operate under clear, fair, and prompt refund terms.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. 100% Refund Guarantee</h2>
          <p>A full 100% refund of the ₹299 advisory fee will be granted under the following circumstances:</p>
          <ul>
            <li>
              <strong>48-Hour Response Guarantee:</strong> Full refund if our assistance specialist fails to respond or initiate guidance within <strong>48 business hours</strong> of verified payment receipt.
            </li>
            <li>
              <strong>Duplicate or Erroneous Charges:</strong> If a user was charged multiple times for the same request due to a network glitch or payment gateway timeout.
            </li>
            <li>
              <strong>Cancellation Before Advisory:</strong> If the user requests cancellation prior to the specialist reviewing documentation or drafting guidance.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>3. Non-Refundable Situations</h2>
          <ul>
            <li><strong>Advisory Already Delivered:</strong> Once procedural analysis, document review, or joint declaration guidance has been delivered via WhatsApp/email, the consultation fee is non-refundable.</li>
            <li><strong>Government Claim Outcome:</strong> As the fee covers advisory assistance only, rejection of claims by EPFO authorities due to employer non-contribution, service gaps, or statutory ineligibility does not qualify for a refund.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. Refund Request Process</h2>
          <p>Users can submit a refund claim within 7 calendar days of transaction:</p>
          <ol>
            <li>Email <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> or message WhatsApp at <strong>+91 9921200935</strong>.</li>
            <li>Provide your Full Name, 10-digit mobile number, Request ID (e.g. <code>PF-REQ-XXXXX</code>), and Razorpay payment reference ID.</li>
          </ol>
        </section>

        <section class="legal-section">
          <h2>5. Refund Settlement Timeline</h2>
          <p>
            Approved refunds are credited back to the original payment source (bank account, UPI, or card) through Razorpay within <strong>5 to 7 business days</strong>, subject to bank processing cycles.
          </p>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 5. DISCLAIMER
# -------------------------------------------------------------
disclaimer_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Statutory Transparency Notice</div>
        <h1 class="page-title">Non-Affiliation Disclaimer</h1>
        <p class="page-subtitle">Effective Date: October 24, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
      </div>

      <div class="disclaimer-banner" style="border-left: 4px solid var(--color-warning);">
        <svg class="disclaimer-banner-icon" style="color: var(--color-warning);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        <div>
          <strong>IMPORTANT NOTICE ON INDEPENDENT STATUS:</strong><br>
          PF Pension Assistant is an independent educational and procedural assistance application developed by AlgoAuraX. It is <strong>NOT</strong> an official application of the Employees' Provident Fund Organisation (EPFO), the Ministry of Labour and Employment, or the Government of India.
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Private Entity Statement</h2>
          <p>
            Neither PF Pension Assistant nor AlgoAuraX is affiliated with, authorized, endorsed, or sponsored by EPFO or any government agency. The application serves strictly as an educational and procedural calculator utility.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. No Outcome Guarantee</h2>
          <p>
            The calculations and ₹299 assisted advisory do not guarantee claim settlement, pension disbursement, or official claim outcomes. Final adjudication rests solely with the competent Regional PF Commissioners.
          </p>
        </section>

        <section class="legal-section">
          <h2>3. Direct Verified Official Government Portals</h2>
          <p>For official government services, passbook downloads, and statutory claims, please visit:</p>
          <div class="card">
            <ul>
              <li><strong>Official EPFO Portal:</strong> <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">https://www.epfindia.gov.in</a></li>
              <li><strong>EPFO Member Interface (UAN Login):</strong> <a href="https://unifiedportal-mem.epfindia.gov.in" target="_blank" rel="noopener noreferrer">https://unifiedportal-mem.epfindia.gov.in</a></li>
              <li><strong>EPFO Member Passbook & Claim Status:</strong> <a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer">https://passbook.epfindia.gov.in</a></li>
              <li><strong>EPFiGMS Official Grievance Portal:</strong> <a href="https://epfigms.gov.in" target="_blank" rel="noopener noreferrer">https://epfigms.gov.in</a></li>
            </ul>
          </div>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 6. ACCOUNT AND DATA DELETION
# -------------------------------------------------------------
deletion_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Google Play User Data Compliance</div>
        <h1 class="page-title">Account and Data Deletion</h1>
        <p class="page-subtitle">Instructions for requesting deletion of user data under AlgoAuraX.</p>
        <div class="meta-info">
          <span>Support Desk: sachinvr141@gmail.com</span>
          <span>WhatsApp: +91 9921200935</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Zero-Login Architecture</h2>
          <p>
            The PF Pension Assistant mobile app operates with a zero-login architecture. No accounts, UAN credentials, or passwords are created or stored on external servers.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Clearing On-Device Data</h2>
          <p>
            Users can instantly clear any local on-device calculation history by opening Android settings: <code>Settings &gt; Apps &gt; PF Pension Assistant &gt; Storage &gt; Clear Data</code>.
          </p>
        </section>

        <section class="legal-section">
          <h2>3. Deleting Advisory & Support Inquiries</h2>
          <p>
            To purge your WhatsApp support history, name, or payment transaction reference:
          </p>
          <div class="card">
            <p>Email: <a href="mailto:sachinvr141@gmail.com?subject=Data%20Deletion%20Request%20-%20PF%20Pension%20Assistant" class="btn btn-primary" style="margin-right: 0.5rem;">Email Deletion Request</a> or message WhatsApp at <strong>+91 9921200935</strong>.</p>
            <p class="form-help">Quote your Name, Mobile Number, and Request ID (if applicable). Requests are verified and purged within 48 business hours.</p>
          </div>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 7. CONTACT US
# -------------------------------------------------------------
contact_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Razorpay Merchant & User Support Desk</div>
        <h1 class="page-title">Contact Us</h1>
        <p class="page-subtitle">Reach out to AlgoAuraX customer support for assistance, billing inquiries, or technical feedback.</p>
      </div>

      <div class="legal-content">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
          <!-- WhatsApp Channel -->
          <div class="card" style="border: 1px solid #25D366; background: var(--color-surface);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
              <span style="display: inline-flex; width: 40px; height: 40px; background: #25D366; border-radius: var(--radius-sm); align-items: center; justify-content: center; color: #FFF;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
              </span>
              <div>
                <h3 style="margin: 0; font-size: 1.15rem;">WhatsApp Support Desk</h3>
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Direct messaging & ₹299 advisory</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 1.25rem;">
              Chat directly with our support specialist for app guidance or to track your ₹299 advisory ticket.
            </p>
            <div style="margin-bottom: 1.25rem; font-family: var(--font-mono); font-weight: 700; font-size: 1.1rem; color: var(--color-text-main);">
              +91 9921200935
            </div>
            <a href="https://wa.me/919921200935?text=Hello%20PF%20Pension%20Assistant%20Support" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%;">
              Open WhatsApp Chat
            </a>
          </div>

          <!-- Email Channel -->
          <div class="card" style="border: 1px solid var(--color-primary); background: var(--color-surface);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
              <span style="display: inline-flex; width: 40px; height: 40px; background: var(--color-primary); border-radius: var(--radius-sm); align-items: center; justify-content: center; color: #FFF;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </span>
              <div>
                <h3 style="margin: 0; font-size: 1.15rem;">Official Email Desk</h3>
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Support, billing & merchant inquiries</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 1.25rem;">
              Send official queries regarding refunds, advisory requests, or merchant verification.
            </p>
            <div style="margin-bottom: 1.25rem; font-family: var(--font-mono); font-weight: 700; font-size: 1.05rem; color: var(--color-text-main); word-break: break-all;">
              sachinvr141@gmail.com
            </div>
            <a href="mailto:sachinvr141@gmail.com?subject=Support%20Inquiry%20-%20PF%20Pension%20Assistant" class="btn btn-primary" style="width: 100%;">
              Send an Email
            </a>
          </div>
        </div>

        <section class="legal-section">
          <h2>Merchant & Entity Details (Razorpay KYC Compliant)</h2>
          <div class="card">
            <p style="margin-bottom: 0.65rem;"><strong>Application Name:</strong> PF Pension Assistant</p>
            <p style="margin-bottom: 0.65rem;"><strong>Developer / Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.65rem;"><strong>Operating Country:</strong> India</p>
            <p style="margin-bottom: 0.65rem;"><strong>Support Operating Hours:</strong> 9:00 AM – 7:00 PM IST (Monday to Saturday)</p>
            <p style="margin-bottom: 0.65rem;"><strong>Official Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0.65rem;"><strong>Support Phone / WhatsApp:</strong> +91 9921200935</p>
            <p style="margin-bottom: 0;"><strong>Official Package ID:</strong> <code>com.algoaurax.pfpensionassistant</code></p>
          </div>
        </section>
      </div>
    </div>
"""

PAGE_BODIES = {
    "home": home_body,
    "privacy-policy": privacy_body,
    "terms": terms_body,
    "refund-policy": refund_body,
    "disclaimer": disclaimer_body,
    "data-deletion": deletion_body,
    "contact": contact_body
}

base_dir = r"d:\PF Ass\pf-assistant-legal"

for p in PAGES:
    body = PAGE_BODIES[p["id"]]
    html = render_html_page(p, body)
    out_path = os.path.join(base_dir, p["out_file"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {p['out_file']}")

print("All 7 static site pages rendered with complete updates!")
