import os
from generator import PAGES, render_html_page

play_badge_svg = '''<svg width="24" height="24" viewBox="0 0 512 512" style="flex-shrink: 0;">
  <path fill="#4285F4" d="M47.1 23.3c-4.4 5.3-7.1 13.5-7.1 24.3v416.8c0 10.8 2.7 19 7.1 24.3l3.6 3.6 233.5-233.5v-5.6L50.7 19.7l-3.6 3.6z"/>
  <path fill="#FBBC04" d="M361.3 335.7l-77.1-77.1v-5.6l77.1-77.1 1.7 1 91.5 52c26.1 14.8 26.1 39.1 0 54l-91.5 52-1.7.8z"/>
  <path fill="#EA4335" d="M284.2 253L50.7 486.5c8.6 9.1 22.8 10.3 39 1.1l271.6-154.4-77.1-77.2z"/>
  <path fill="#34A853" d="M284.2 258.6l77.1-77.1L89.7 27.1C73.5 17.9 59.3 19.1 50.7 28.2L284.2 258.6z"/>
</svg>'''

gov_sources_component = """
      <!-- MANDATORY OFFICIAL GOVERNMENT SOURCE LINKS (Google Play Compliant) -->
      <section style="margin: 3.5rem 0; padding: 2.25rem; background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-xl); box-shadow: var(--shadow-sm);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 0.75rem;">
          <div style="display: flex; align-items: center; gap: 0.65rem;">
            <span class="badge badge-primary">Official Portals</span>
            <h3 style="margin: 0; font-size: 1.35rem;">Official Government Sources</h3>
          </div>
          <span style="font-size: 0.82rem; color: var(--color-text-muted);">Verified Government of India Links</span>
        </div>
        <p style="color: var(--color-text-secondary); margin-bottom: 1.25rem; font-size: 0.92rem;">
          PF Pension Assistant is an independent informational utility. For all official submissions, live passbook downloads, claim status checks, and official grievance tracking, please access the authorized government portals directly:
        </p>
        <div class="gov-sources-grid">
          <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer" class="gov-source-card">
            <div>
              <h4>Official EPFO Portal <span>&nearr;</span></h4>
              <p>Main website of Employees' Provident Fund Organisation. Official circulars, notifications &amp; scheme rules.</p>
            </div>
            <div class="gov-source-url">https://www.epfindia.gov.in</div>
          </a>
          <a href="https://unifiedportal-mem.epfindia.gov.in/memberinterface/" target="_blank" rel="noopener noreferrer" class="gov-source-card">
            <div>
              <h4>EPFO Member e-Sewa <span>&nearr;</span></h4>
              <p>Unified Member Portal for UAN login, online claim submission (Form 19, 10C, 31, 10D) &amp; KYC linking.</p>
            </div>
            <div class="gov-source-url">unifiedportal-mem.epfindia.gov.in</div>
          </a>
          <a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer" class="gov-source-card">
            <div>
              <h4>EPFO Member Passbook <span>&nearr;</span></h4>
              <p>Official portal to download updated EPF statement, contribution logs, and real-time claim status.</p>
            </div>
            <div class="gov-source-url">passbook.epfindia.gov.in</div>
          </a>
          <a href="https://epfigms.gov.in" target="_blank" rel="noopener noreferrer" class="gov-source-card">
            <div>
              <h4>EPFiGMS Grievance Portal <span>&nearr;</span></h4>
              <p>Centralized official grievance registration and redressal system for EPF and EPS subscribers.</p>
            </div>
            <div class="gov-source-url">https://epfigms.gov.in</div>
          </a>
        </div>
      </section>
"""

# -------------------------------------------------------------
# 1. HOME PAGE
# -------------------------------------------------------------
home_body = f"""
    <div class="container">
      <!-- Hero Section -->
      <section class="page-header" style="text-align: center; border-bottom: none; padding-top: 2.75rem; padding-bottom: 2rem;">
        <div style="margin-bottom: 1.25rem;">
          <img src="./images/app-logo.png?v=8" alt="PF Pension Assistant Logo" style="width: 105px; height: 105px; object-fit: cover; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); border: 2px solid var(--color-border);">
        </div>
        <div class="badge badge-primary" style="margin-bottom: 1rem;">AlgoAuraX Independent Legal &amp; Support Portal</div>
        <h1 style="font-size: 2.55rem; max-width: 820px; margin-left: auto; margin-right: auto;">
          Intelligent Guidance for Your EPF Savings &amp; EPS-95 Pension
        </h1>
        <p class="page-subtitle" style="margin-left: auto; margin-right: auto; font-size: 1.12rem;">
          PF Pension Assistant is an independent educational Android application engineered with a privacy-first, zero-credential-storage architecture to help Indian subscribers estimate pensions, project compound interest growth, and navigate EPFO claim procedures.
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

      <!-- App Core Features Grid -->
      <section style="margin: 3.5rem 0;">
        <div style="text-align: center; margin-bottom: 2.25rem;">
          <span class="badge badge-primary" style="margin-bottom: 0.5rem;">Powerful Utilities</span>
          <h2>Everything You Need for EPF &amp; EPS Management</h2>
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
            <h3 class="card-title">2. EPF Balance &amp; Interest Growth Estimator</h3>
            <p class="card-subtitle">
              Projects compound provident fund savings based on your monthly basic wage, employee/employer contributions, and the official EPFO annual interest rate (8.25% p.a.). See year-by-year accumulation and forecast your lump-sum corpus at retirement.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="card">
            <div style="display: inline-flex; width: 44px; height: 44px; border-radius: var(--radius-md); background: var(--color-primary-container); align-items: center; justify-content: center; color: var(--color-primary); margin-bottom: 1.15rem;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            </div>
            <h3 class="card-title">3. EPFO Claim Forms &amp; Procedures Guide</h3>
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
            <h3 class="card-title">5. 100% Privacy &amp; Zero Credential Storage</h3>
            <p class="card-subtitle" style="max-width: 850px;">
              We NEVER ask for, collect, or store your EPFO UAN password, Aadhaar OTP, or banking passwords. Basic login uses Firebase Auth (Google Sign-In) solely for authentication. All financial estimations run strictly on-device. Zero data shared with third parties or advertisers.
            </p>
          </div>
        </div>
      </section>

{gov_sources_component}

      <!-- Transparent Pricing Card Section (Razorpay Merchant Compliant) -->
      <section style="margin: 3.5rem 0;">
        <div class="card" style="border: 2px solid var(--color-primary); background: var(--color-surface); padding: 2.25rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem;">
            <div style="max-width: 620px;">
              <div style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
                <span class="badge badge-primary">Private Consulting Fee</span>
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
              <div style="font-size: 0.85rem; color: var(--color-text-muted); background: var(--color-surface-subtle); padding: 0.85rem 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--color-warning);">
                <strong>Important Disclosure:</strong> This ₹299 fee is strictly an optional private consulting fee for 1-on-1 assistance, form review, and guidance. <strong>This fee is NOT an official EPFO government fee and does NOT guarantee claim approval or pension sanction by EPFO authorities.</strong> Official claims must be submitted by users directly on official portals.
              </div>
            </div>

            <div style="text-align: center; min-width: 260px; padding: 2rem; background: var(--color-surface-subtle); border-radius: var(--radius-lg); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
              <div style="font-size: 0.82rem; text-transform: uppercase; font-weight: 700; color: var(--color-text-muted); letter-spacing: 0.05em;">Private Advisory Fee</div>
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
        <h2 style="margin-bottom: 1.5rem;">Legal Agreements &amp; Policy Documentation</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
          <a href="./privacy-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Privacy Policy &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Zero credential storage, Firebase auth disclosures, and Google Play Data Safety compliance.</p>
          </a>
          <a href="./terms/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Terms of Service &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Non-government status, scope of ₹299 assisted advisory, and disclaimer of government outcomes.</p>
          </a>
          <a href="./refund-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Refund &amp; Cancellation &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">100% refund guarantee within 48-hour response window, duplicate charge resolution, 5-7 days credit.</p>
          </a>
          <a href="./disclaimer/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Disclaimer &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Notice of non-affiliation with EPFO or Govt of India, plus direct official government links.</p>
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
        <p class="page-subtitle">Effective Date: October 26, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant (Android)</p>
        <div class="meta-info">
          <span>Target Audience: 18+ (Working professionals &amp; pensioners)</span>
          <span>Contact Email: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Privacy Commitment:</strong> PF Pension Assistant is built with strict privacy-by-design standards. <strong>We NEVER ask for, collect, or store your EPFO UAN password, Aadhaar OTP, or banking passwords.</strong>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Introduction &amp; Scope</h2>
          <p>
            This Privacy Policy explains how <strong>PF Pension Assistant</strong> (the "Application"), developed and maintained under the brand <strong>AlgoAuraX</strong> ("we", "us", or "our"), handles personal information. This policy applies to the Android application (Package: <code>com.algoaurax.pfpensionassistant</code>) and this official support website.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Zero Sensitive Credential Storage</h2>
          <div class="highlight-box danger">
            <strong>CRITICAL PRIVACY SAFEGUARD:</strong><br>
            <strong>We NEVER ask for, collect, or store your EPFO UAN password, Aadhaar OTP, or banking passwords.</strong>
            <p style="margin-top: 0.5rem; margin-bottom: 0;">
              Users are strictly instructed never to share passwords, OTPs, or financial secrets with our app, support staff, or any third party. The Application does not connect directly to EPFO servers to capture credentials.
            </p>
          </div>
        </section>

        <section class="legal-section">
          <h2>3. Information Collected &amp; Authentication Flow</h2>
          <p>We adhere strictly to Google Play Data Safety requirements and minimal data collection:</p>
          
          <h3>A. Google Sign-In via Firebase Authentication</h3>
          <p>
            When a user signs in, Google Sign-In via Firebase Auth collects only basic profile information:
          </p>
          <ul>
            <li><strong>Email Address:</strong> Used strictly for secure account identification.</li>
            <li><strong>Display Name:</strong> Used to personalize the app interface.</li>
          </ul>
          <p>
            This data is encrypted in transit and at rest using industry-standard Firebase infrastructure. We do not access your Google contacts, Google Drive, or external account services.
          </p>

          <h3>B. Assisted Service Queries (₹299 Advisory)</h3>
          <p>
            When users request our optional ₹299 assisted advisory service, contact details are submitted securely:
          </p>
          <ul>
            <li><strong>Name and Phone Number:</strong> Submitted through the assisted service form for support communication.</li>
            <li><strong>Query Message &amp; Category:</strong> Description of the procedural issue (e.g., claim rejection reason, joint declaration inquiry).</li>
            <li><strong>Sole Purpose:</strong> Contact details are used <strong>solely for query resolution</strong> and support follow-up.</li>
            <li><strong>No Advertising Sharing:</strong> Data is <strong>never sold, rented, or shared with third-party advertisers or marketing data brokers</strong>.</li>
          </ul>

          <h3>C. Calculations &amp; Estimations</h3>
          <p>
            All EPS-95 pension calculations and EPF compound interest projections run locally on-device. Input parameters (wages, years of service) are processed in volatile memory and are not uploaded to our servers.
          </p>
        </section>

        <section class="legal-section">
          <h2>4. Security Standards</h2>
          <p>
            We implement industry-standard security measures, including <strong>HTTPS/TLS encryption</strong> for all network transmissions and Firebase Cloud security protocols. Local database records (if any) are restricted by Android's sandbox permissions.
          </p>
        </section>

        <section class="legal-section">
          <h2>5. Third-Party Service Providers</h2>
          <ul>
            <li><strong>Google / Firebase:</strong> Authentication infrastructure and runtime hosting.</li>
            <li><strong>Razorpay Software Private Limited:</strong> Secure payment gateway processing for the ₹299 consultation fee. Payments occur on PCI-DSS certified infrastructure; we never store full card numbers or banking passwords.</li>
            <li><strong>WhatsApp (Meta):</strong> Optional user-initiated support communication protected by WhatsApp's end-to-end encryption.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>6. User Rights &amp; Data Deletion Process</h2>
          <p>
            Every user has the right to access, rectify, or request permanent deletion of their inquiry records. To delete your contact details or support ticket history:
          </p>
          <ul>
            <li>Visit our dedicated <a href="../data-deletion/">Account and Data Deletion Page</a>.</li>
            <li>Email your request directly to <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> with the subject line <code>Data Deletion Request - PF Pension Assistant</code>.</li>
            <li>Message WhatsApp support at <strong>+91 9921200935</strong>.</li>
          </ul>
          <p>
            Verified requests are processed and permanently purged from support records within 48 business hours.
          </p>
        </section>

        <section class="legal-section">
          <h2>7. Contact Us Regarding Privacy</h2>
          <div class="card">
            <p style="margin-bottom: 0.5rem;"><strong>Brand / Publisher:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Privacy Desk Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>WhatsApp Support:</strong> <a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer">+91 9921200935</a></p>
          </div>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 3. TERMS OF SERVICE
# -------------------------------------------------------------
terms_body = f"""
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Legal Terms &amp; Conditions</div>
        <h1 class="page-title">Terms of Service</h1>
        <p class="page-subtitle">Effective Date: October 26, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Agreement to Terms</h2>
          <p>
            These Terms of Service constitute a legally binding agreement between you ("User", "you") and <strong>AlgoAuraX</strong> ("we", "us", or "our"), regarding your use of the <strong>PF Pension Assistant</strong> Android application and this legal portal.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Non-Government &amp; Private Status Notice</h2>
          <div class="highlight-box warning">
            <strong>STRICT STATUTORY DISCLOSURE:</strong><br>
            PF Pension Assistant and AlgoAuraX are strictly <strong>independent, private, non-government entities</strong>. We are NOT affiliated with, endorsed by, authorized by, or sponsored by the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India. The application is an educational and informational resource designed to assist users in understanding published rules and procedures.
          </div>
        </section>

        <section class="legal-section">
          <h2>3. Informational &amp; Estimation Purpose Only</h2>
          <p>
            All calculations generated by the app — including EPS-95 monthly pension projections, 2-year bonus weightage calculations, and EPF interest growth estimations — are <strong>indicative mathematical estimates based on published rules</strong>.
          </p>
          <ul>
            <li>Calculations do NOT constitute official statements of balance, legal entitlement, or guaranteed pension sanctions.</li>
            <li>Statutory interest rates, pension rules, and administrative thresholds are subject to amendment by the Central Board of Trustees, EPFO, and Government gazette notifications.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. The ₹299 Assisted Advisory Service</h2>
          <p>
            The Application offers an optional 1-on-1 private assistance service for an advisory fee of <strong>₹299 per request</strong>:
          </p>
          <ul>
            <li><strong>Nature of Service:</strong> The ₹299 fee is strictly an optional private consulting fee for 1-on-1 assistance, form review, document guidance, and procedural explanation.</li>
            <li><strong>Not an EPFO Government Fee:</strong> <span style="color: var(--color-error); font-weight: 700;">This fee is NOT an official EPFO government fee and does NOT guarantee claim approval or pension sanction by EPFO authorities.</span></li>
            <li><strong>No Authority to Adjudicate:</strong> AlgoAuraX specialists have no internal administrative access to EPFO portals or claim approval queues. Final decisions rest solely with your jurisdictional Regional PF Commissioner.</li>
            <li><strong>User Submission:</strong> Official claims (Form 19, 10C, 31, 10D) and grievances must be independently submitted by the user on official government portals.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. User Responsibilities &amp; Official Verification</h2>
          <p>
            Users are strictly responsible for verifying official balances, contribution records, and claim status directly on official government portals:
          </p>
          <ul>
            <li><strong>Official Portals for Verification:</strong> Always verify official balances directly on <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">epfindia.gov.in</a> or the official Member Passbook portal (<a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer">passbook.epfindia.gov.in</a>).</li>
            <li><strong>Accuracy of Information:</strong> Users agree to supply truthful details when inquiring for assisted advisory.</li>
            <li><strong>Prohibition on Sensitive Data:</strong> Users must never input or message UAN passwords, Aadhaar OTPs, or banking PINs to our team.</li>
          </ul>
        </section>

{gov_sources_component}

        <section class="legal-section">
          <h2>6. Intellectual Property &amp; Prohibitions</h2>
          <p>
            All software code, graphics, layout, text, and original assets of PF Pension Assistant are the intellectual property of AlgoAuraX. Users shall not decompile, reverse-engineer, distribute, or exploit the application for unauthorized commercial gains.
          </p>
        </section>

        <section class="legal-section">
          <h2>7. Limitation of Liability &amp; Governing Law</h2>
          <p>
            AlgoAuraX shall not be liable for any indirect, incidental, or consequential damages resulting from user reliance on informational estimates, portal downtimes, employer non-compliance, or EPFO claim rejection. These Terms are governed by and construed in accordance with the laws of <strong>India</strong>.
          </p>
        </section>

        <section class="legal-section">
          <h2>8. Support &amp; Grievances</h2>
          <div class="card">
            <p style="margin-bottom: 0.5rem;"><strong>Entity:</strong> AlgoAuraX &bull; PF Pension Assistant</p>
            <p style="margin-bottom: 0.5rem;"><strong>Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>WhatsApp Support:</strong> <a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer">+91 9921200935</a> (9:00 AM – 7:00 PM IST, Mon–Sat)</p>
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
        <div class="badge badge-primary">Consumer Transparency</div>
        <h1 class="page-title">Refund &amp; Cancellation Policy</h1>
        <p class="page-subtitle">Effective Date: October 26, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
        <div class="meta-info">
          <span>Fee: ₹299 per Assistance Request</span>
          <span>Support Desk: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Overview &amp; Policy Objective</h2>
          <p>
            AlgoAuraX maintains clear, fair, and prompt refund terms for the ₹299 PF Expert Assistance consultation. Every refund or cancellation request is handled fairly under the conditions specified below.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Refund Eligibility for the ₹299 Advisory Service</h2>
          <p>A full 100% refund of the ₹299 fee is granted in the following circumstances:</p>
          <ul>
            <li>
              <strong>Unfulfilled Requests Prior to Consultation Review:</strong> Eligible if the user requests cancellation or the service request cannot be fulfilled prior to consultation review by our assistance specialist.
            </li>
            <li>
              <strong>48-Hour Response Commitment:</strong> Full refund if our assistance specialist fails to initiate guidance within <strong>48 business hours</strong> of verified payment receipt.
            </li>
            <li>
              <strong>Duplicate or Erroneous Transactions:</strong> Full refund if a user was debited multiple times for the same single inquiry due to network or payment gateway issues.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>3. Non-Refundable Situations</h2>
          <ul>
            <li>
              <strong>Consultation Already Delivered:</strong> Once procedural analysis, document review, or joint declaration guidance has been drafted and delivered via WhatsApp or email, the advisory service is deemed completed and non-refundable.
            </li>
            <li>
              <strong>Official Government Decisions:</strong> The ₹299 fee pays strictly for advisory time. Official claim rejection or pension delay by EPFO authorities due to employer non-contribution, service discrepancies, or statutory ineligibility does not qualify for a refund.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. How to Submit a Refund Request</h2>
          <p>Users can submit a refund claim within 7 calendar days of transaction:</p>
          <ol>
            <li>Send an email to <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> with the subject <code>Refund Request - [Your Request ID]</code>, or message WhatsApp at <a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer"><strong>+91 9921200935</strong></a>.</li>
            <li>Include your Full Name, 10-digit mobile number, Request ID (e.g. <code>PF-REQ-XXXXX</code>), and Razorpay transaction reference ID.</li>
          </ol>
        </section>

        <section class="legal-section">
          <h2>5. Settlement &amp; Credit Timeline</h2>
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
disclaimer_body = f"""
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Statutory Transparency Notice</div>
        <h1 class="page-title">Disclaimer</h1>
        <p class="page-subtitle">Effective Date: October 26, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
      </div>

      <div class="disclaimer-banner" style="border-left: 4px solid var(--color-warning);">
        <svg class="disclaimer-banner-icon" style="color: var(--color-warning);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        <div>
          <strong>MANDATORY STATUTORY NOTICE:</strong><br>
          PF Pension Assistant and this website are independent educational &amp; informational resources. This service <strong>DOES NOT represent, and is NOT affiliated with, endorsed by, or authorized by</strong> the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India.
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Independent Advisory &amp; Educational Status</h2>
          <p>
            Neither PF Pension Assistant nor its publisher, AlgoAuraX, is a government agency or an authorized representative of EPFO. All content, tools, and assisted advisory services are provided strictly for educational and procedural clarification.
          </p>
        </section>

{gov_sources_component}

        <section class="legal-section">
          <h2>2. Mathematical &amp; Calculation Disclaimer</h2>
          <p>
            Pension and interest calculation formulas in this application are derived from publicly published EPFO rules (such as the Employees' Pension Scheme, 1995, and EPF Act, 1952) and <strong>act as estimates only</strong>.
          </p>
          <ul>
            <li>Estimations do not guarantee actual settlement amounts or pension payment orders (PPO).</li>
            <li>Actual benefits are subject to statutory verification of non-contributory periods, service gaps, wage ceilings, and official approval by competent Regional PF Commissioners.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>3. No Representation in Government Proceedings</h2>
          <p>
            The optional ₹299 assisted advisory provides informational guidance and document explanation only. It does not constitute legal advocacy or official representation before any statutory tribunal or EPFO authority.
          </p>
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
          <h2>1. Data Minimization &amp; Zero Credential Storage</h2>
          <p>
            PF Pension Assistant does not collect or store sensitive EPFO credentials, UAN passwords, or Aadhaar OTPs. Basic login information from Firebase Google Sign-In is limited to email and display name.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Clearing On-Device Data</h2>
          <p>
            Users can instantly clear all locally stored preferences by clearing app storage: <code>Android Settings &gt; Apps &gt; PF Pension Assistant &gt; Storage &gt; Clear Data</code>.
          </p>
        </section>

        <section class="legal-section">
          <h2>3. Deleting Assisted Service Inquiries</h2>
          <p>
            To request permanent deletion of your name, phone number, WhatsApp inquiry log, or transaction reference:
          </p>
          <div class="card">
            <p>Email: <a href="mailto:sachinvr141@gmail.com?subject=Data%20Deletion%20Request%20-%20PF%20Pension%20Assistant" class="btn btn-primary" style="margin-right: 0.5rem;">Email Deletion Request</a> or message WhatsApp at <a href="https://wa.me/919921200935" target="_blank" rel="noopener noreferrer"><strong>+91 9921200935</strong></a>.</p>
            <p class="form-help">Please quote your Name, Phone Number, and Request ID (if applicable). Requests are verified and permanently purged within 48 business hours.</p>
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
        <div class="badge badge-primary">Support &amp; Inquiries</div>
        <h1 class="page-title">Contact Us</h1>
        <p class="page-subtitle">Reach out to the AlgoAuraX support desk for assistance, billing queries, or feedback.</p>
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
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Direct messaging &amp; ₹299 advisory</span>
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
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Support, billing &amp; compliance inquiries</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 1.25rem;">
              Send official queries regarding refunds, advisory requests, or policy questions.
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
          <h2>Merchant &amp; Entity Details</h2>
          <div class="card">
            <p style="margin-bottom: 0.65rem;"><strong>Application Name:</strong> PF Pension Assistant</p>
            <p style="margin-bottom: 0.65rem;"><strong>Developer / Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.65rem;"><strong>Operating Country:</strong> India</p>
            <p style="margin-bottom: 0.65rem;"><strong>Support Operating Hours:</strong> 9:00 AM – 7:00 PM IST (Monday to Saturday)</p>
            <p style="margin-bottom: 0.65rem;"><strong>Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
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

print("All 7 pages updated with 100% Google Play policy compliance!")
