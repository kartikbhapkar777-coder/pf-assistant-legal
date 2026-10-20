import os
from generator import PAGES, render_html_page

# -------------------------------------------------------------
# 1. HOME PAGE
# -------------------------------------------------------------
home_body = """
    <div class="container">
      <section class="page-header" style="text-align: center; border-bottom: none; padding-top: 3rem; padding-bottom: 2rem;">
        <div style="margin-bottom: 1.25rem;">
          <img src="./images/app-logo.png?v=1792519988" alt="PF Pension Assistant Logo" style="width: 110px; height: 110px; object-fit: contain; border-radius: var(--radius-lg); box-shadow: var(--shadow-md);">
        </div>
        <div class="badge badge-primary" style="margin-bottom: 1rem;">AlgoAuraX Legal & Support Portal</div>
        <h1 style="font-size: 2.5rem; max-width: 800px; margin-left: auto; margin-right: auto;">
          Clear, Reliable Information for Your EPF & Pension Inquiries
        </h1>
        <p class="page-subtitle" style="margin-left: auto; margin-right: auto; font-size: 1.15rem;">
          PF Pension Assistant is an independent Android mobile application designed to simplify complex Provident Fund processes, claim tracking, transfer guidance, and pension rules.
        </p>

        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.75rem;">
          <a href="./contact/" class="btn btn-primary">Contact Support</a>
          <a href="./privacy-policy/" class="btn btn-secondary">Read Privacy Policy</a>
        </div>
      </section>

      <!-- App Disclaimer Banner -->
      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Notice of Independent Operation:</strong> PF Pension Assistant is an independent assistance application developed by AlgoAuraX. It is <strong>NOT</strong> affiliated with, authorized, endorsed, sponsored, or operated by the Employees' Provident Fund Organisation (EPFO), Ministry of Labour and Employment, or the Government of India. Official services are conducted solely on government portals.
        </div>
      </div>

      <!-- App Features Grid -->
      <section style="margin: 3.5rem 0;">
        <h2 style="text-align: center; margin-bottom: 2rem;">What PF Pension Assistant Provides</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
          <div class="card">
            <h3 class="card-title">PF & Pension Knowledge Hub</h3>
            <p class="card-subtitle">Comprehensive step-by-step guidance on Member Portal navigation, passbook viewing, online transfer Form 13, and withdrawal procedures (Form 19, 10C, 31).</p>
          </div>
          <div class="card">
            <h3 class="card-title">EPS 95 Pension Guidance</h3>
            <p class="card-subtitle">Understand pension calculation methodologies, eligibility criteria (10+ years of service), scheme certificate options, and life certificate (Digital Jeevan Pramaan) requirements.</p>
          </div>
          <div class="card">
            <h3 class="card-title">Grievance Advisory</h3>
            <p class="card-subtitle">Understand how to draft and file official grievance petitions through EPFiGMS (EPFO Grievance Management System) and track pending claim issues.</p>
          </div>
        </div>
      </section>

      <!-- Paid Service Feature Section -->
      <section style="margin: 3.5rem 0;">
        <div class="card" style="border: 2px solid var(--color-primary); background: var(--color-surface);">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1.5rem;">
            <div style="max-width: 600px;">
              <span class="badge badge-primary" style="margin-bottom: 0.5rem;">One-on-One Service</span>
              <h2>PF Expert Assistance — ₹299 per Request</h2>
              <p style="color: var(--color-text-secondary); margin-bottom: 1rem;">
                Stuck with a rejected claim, KYC father name mismatch, joint declaration issue, or dual passbook problem? Our personalized assistance service connects you directly with guidance via WhatsApp.
              </p>
              <ul style="margin-bottom: 1.25rem;">
                <li>Personal review of your procedural query by a support specialist</li>
                <li>Clear guidance on necessary documents, forms, and correction letters</li>
                <li>Direct communication handoff to our dedicated WhatsApp support desk</li>
                <li>Fixed transparent pricing with zero recurring subscriptions</li>
              </ul>
              <div style="font-size: 0.85rem; color: var(--color-text-muted);">
                * Note: This service fee covers informational consultation and procedural advisory only. It does not and cannot guarantee claim settlement or outcome from EPFO authorities.
              </div>
            </div>

            <div style="text-align: center; min-width: 220px; padding: 1.5rem; background: var(--color-surface-subtle); border-radius: var(--radius-md); border: 1px solid var(--color-border);">
              <div style="font-size: 0.85rem; text-transform: uppercase; font-weight: 700; color: var(--color-text-secondary);">One-Time Fee</div>
              <div style="font-size: 2.75rem; font-weight: 800; color: var(--color-primary); margin: 0.25rem 0;">₹299</div>
              <div style="font-size: 0.82rem; color: var(--color-text-muted); margin-bottom: 1.25rem;">Per Assistance Request</div>
              <a href="./contact/" class="btn btn-primary" style="width: 100%;">Inquire via Support</a>
            </div>
          </div>
        </div>
      </section>

      <!-- App Download / Configuration Note -->
      <section style="margin: 3rem 0; text-align: center; padding: 2rem; background: var(--color-surface-subtle); border-radius: var(--radius-lg); border: 1px solid var(--color-border);">
        <h3>Google Play Store Release</h3>
        <p style="max-width: 650px; margin: 0.5rem auto 1.5rem; color: var(--color-text-secondary);">
          PF Pension Assistant is currently in production readiness and compliance review for distribution on Android through the Google Play Store. The verified store link will be published upon release completion.
        </p>
        <span class="badge badge-primary">Android Platform Application</span>
      </section>

      <!-- Comprehensive Legal Links Grid -->
      <section style="margin: 4rem 0;">
        <h2 style="margin-bottom: 1.5rem;">Legal Agreements & Compliance Documentation</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
          <a href="./privacy-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Privacy Policy &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Full disclosures on SQLite local storage, Google Auth, and zero collection of Aadhaar/UAN.</p>
          </a>
          <a href="./terms/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Terms & Conditions &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Terms of use, scope of ₹299 service, user obligations, and non-outcome guarantees.</p>
          </a>
          <a href="./refund-policy/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Refund & Cancellation &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Refund eligibility, duplicate payments, cancellation windows, and dispute resolution.</p>
          </a>
          <a href="./disclaimer/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Official Disclaimer &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Notice of non-affiliation with EPFO or Ministry of Labour, plus official government links.</p>
          </a>
          <a href="./data-deletion/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Data & Account Deletion &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Process for requesting permanent removal of personal information and transaction logs.</p>
          </a>
          <a href="./contact/" class="card" style="text-decoration: none; color: inherit;">
            <h4 style="margin-bottom: 0.35rem; color: var(--color-primary);">Contact & Support &rarr;</h4>
            <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Direct access to our verified WhatsApp desk and support email address.</p>
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
        <div class="badge badge-primary">Google Play Compliance Document</div>
        <h1 class="page-title">Privacy Policy</h1>
        <p class="page-subtitle">Effective Date: October 18, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant (Android)</p>
        <div class="meta-info">
          <span>Target Audience: 18+ (Working professionals & pensioners)</span>
          <span>Contact: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Privacy Commitment:</strong> PF Pension Assistant is built with a privacy-by-design architecture. We <strong>never</strong> ask for, store, or transmit your Aadhaar card number, UAN password, OTPs, or EPF portal login credentials.
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Introduction</h2>
          <p>
            This Privacy Policy governs the manner in which <strong>PF Pension Assistant</strong> (the "Application"), developed and maintained under the brand <strong>AlgoAuraX</strong> ("we", "us", or "our"), collects, uses, maintains, and discloses information collected from users ("User" or "you") of the Android application and this legal portal website.
          </p>
          <p>
            By downloading, installing, accessing, or using PF Pension Assistant, you acknowledge and agree to the practices described in this Privacy Policy. If you do not agree with this policy, please do not use the Application.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Information We Collect (Verified Application Behavior)</h2>
          <p>
            We adhere strictly to data minimization principles. Our code architecture deliberately restricts data collection to what is strictly required to provide functionality and support:
          </p>
          
          <h3>A. Optional Account Information (Firebase Authentication)</h3>
          <p>
            If you choose to sign in to the Application using Google Sign-In, we receive basic authentication token details provided by Google Credential Manager and Firebase Authentication:
          </p>
          <ul>
            <li>Your Google account display name</li>
            <li>Your verified Google email address</li>
            <li>Your Google profile picture URL (if provided by your Google account profile)</li>
          </ul>
          <p>
            These details are used solely to personalize your local interface and authenticate your session. We do not access your Google contacts, drive, emails, or personal calendar.
          </p>

          <h3>B. PF Expert Assistance Service Intake Information</h3>
          <p>
            When you choose to request the paid "PF Expert Assistance" service (₹299), you voluntarily submit the following details into the application's intake form:
          </p>
          <ul>
            <li><strong>Full Name:</strong> To identify the member or inquirer</li>
            <li><strong>Mobile Number:</strong> 10-digit Indian mobile number for communication</li>
            <li><strong>Assistance Category:</strong> The topic of inquiry (e.g., PF Claim Settlement, EPS 95 Pension, Joint Declaration, Transfer / KYC)</li>
            <li><strong>Problem Description:</strong> A written summary of your issue or question</li>
            <li><strong>Transaction References:</strong> Generated unique Request ID (e.g., <code>REQ-xxxxxx</code>), payment order reference, and payment ID returned upon successful checkout</li>
          </ul>

          <div class="highlight-box danger">
            <strong>CRITICAL NOTICE — STRICTLY PROHIBITED SENSITIVE DATA:</strong><br>
            We <strong>DO NOT</strong> collect, store, or request:
            <ul style="margin-top: 0.5rem; margin-bottom: 0;">
              <li>Universal Account Number (UAN) passwords or Member Portal credentials</li>
              <li>Aadhaar card numbers or biometric records</li>
              <li>EPFO SMS One-Time Passwords (OTPs)</li>
              <li>Bank account login credentials, debit/credit card PINs, or UPI PINs</li>
            </ul>
            Users are explicitly instructed <strong>NEVER</strong> to input, submit, or message passwords or OTPs to our support team or anyone else.
          </div>
        </section>

        <section class="legal-section">
          <h2>3. Data Storage & Local Persistence Architecture</h2>
          <p>
            Transparency regarding how and where your data lives:
          </p>
          <ul>
            <li>
              <strong>On-Device SQLite Database:</strong> The intake requests and transaction identifiers for PF Expert Assistance are stored locally on your Android device in a secure SQLite database (<code>ExpertRequestDbHelper</code>). This allows your service history and Request ID to persist across app updates, device restarts, and offline periods.
            </li>
            <li>
              <strong>No Cloud Synchronized User Database:</strong> The Application does not currently maintain a centralized remote database synchronizing your entire personal device profile to third-party cloud servers.
            </li>
            <li>
              <strong>WhatsApp Communications:</strong> When you tap the button to proceed to WhatsApp support, the verified details (Request ID, Name, Mobile, Service Category, Problem Summary, and Payment Reference) are formatted into an encrypted WhatsApp text message. <em>Note:</em> The message is only transmitted when you manually press "Send" inside the WhatsApp application.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. Third-Party Service Providers & Payment Gateways</h2>
          <p>
            The Application interacts with reputable third-party infrastructure providers to perform specific operational functions:
          </p>
          <ul>
            <li>
              <strong>Google Play Services & Firebase:</strong> Provides Google Sign-In session management and core runtime compatibility. Firebase operates under Google's stringent privacy standards.
            </li>
            <li>
              <strong>Razorpay (Payment Gateway):</strong> When purchasing the ₹299 service, payments are processed by Razorpay Software Private Limited. We do not collect or store full credit/debit card numbers or net banking credentials; these are handled directly on Razorpay's PCI-DSS compliant secure infrastructure.
            </li>
            <li>
              <strong>WhatsApp Business (Meta):</strong> Customer support interactions take place over WhatsApp. Messages sent over WhatsApp are subject to WhatsApp's Terms of Service and End-to-End Encryption protocol.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. How We Use Collected Information</h2>
          <p>We process your information exclusively for the following purposes:</p>
          <ol>
            <li>To operate and deliver the features of the PF Pension Assistant app.</li>
            <li>To provide the ₹299 personalized procedural advisory service requested by you.</li>
            <li>To verify payment status, reconcile transactions, and prevent fraudulent claims.</li>
            <li>To communicate with you via WhatsApp or Email regarding your specific support ticket.</li>
            <li>To comply with statutory accounting and tax obligations applicable under Indian law.</li>
          </ol>
        </section>

        <section class="legal-section">
          <h2>6. Data Retention Policy</h2>
          <p>
            <strong>Local Data:</strong> Form submissions and request records saved in your device's local SQLite database remain on your phone until you clear the application's storage via Android Settings or uninstall the app.
          </p>
          <p>
            <strong>Support Records & Accounting Data:</strong> Communications sent to our support email or WhatsApp number, along with Razorpay financial settlement records, are retained for a minimum period of 3 years to comply with financial audits, consumer dispute resolution, and applicable taxation regulations, after which they are securely purged.
          </p>
        </section>

        <section class="legal-section">
          <h2>7. User Rights & Data Deletion</h2>
          <p>
            Every user retains full rights regarding their personal data under applicable data privacy frameworks:
          </p>
          <ul>
            <li><strong>Right to Erase / Delete:</strong> You can request immediate erasure of your support conversations, email records, and stored customer references by contacting us. Detailed steps are provided on our dedicated <a href="../data-deletion/">Account and Data Deletion Page</a>.</li>
            <li><strong>Right to Rectify:</strong> If you supplied an incorrect mobile number or email in your assistance request, you can contact our support team to update your record.</li>
            <li><strong>Right to Withdraw Consent:</strong> You may discontinue using the service or disconnect your Google account at any time.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>8. Children's Privacy</h2>
          <p>
            PF Pension Assistant is designed for working employees, PF subscribers, and pensioners eligible for retirement benefits. It is not intended for or directed toward children under 18 years of age. We do not knowingly collect personal information from minors.
          </p>
        </section>

        <section class="legal-section">
          <h2>9. Security Measures</h2>
          <p>
            We implement industry-standard security practices, including TLS/HTTPS network encryption, secure Android Credential Manager tokenization, and strict prohibition of plaintext password/OTP storage. However, please remember that no method of electronic storage or mobile transmission is 100% immune from security threats.
          </p>
        </section>

        <section class="legal-section">
          <h2>10. Changes to This Privacy Policy</h2>
          <p>
            We reserve the right to update this Privacy Policy to reflect changes in our operational practices, new app releases, or evolving regulatory requirements. Any modifications will be posted to this URL with a revised "Effective Date" at the top of the document.
          </p>
        </section>

        <section class="legal-section">
          <h2>11. Contacting Us Regarding Privacy</h2>
          <p>
            If you have questions, concerns, or grievances regarding this Privacy Policy, please reach out directly:
          </p>
          <div class="card" style="margin-top: 1rem;">
            <p style="margin-bottom: 0.5rem;"><strong>Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Application:</strong> PF Pension Assistant</p>
            <p style="margin-bottom: 0.5rem;"><strong>Privacy & Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
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
        <div class="badge badge-primary">Legal Agreement</div>
        <h1 class="page-title">Terms and Conditions</h1>
        <p class="page-subtitle">Effective Date: October 18, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant (Android)</p>
        <div class="meta-info">
          <span>Version: 1.0.0</span>
          <span>Contact: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Agreement to Terms</h2>
          <p>
            These Terms and Conditions constitute a legally binding agreement made between you, whether personally or on behalf of an entity ("User", "you"), and <strong>AlgoAuraX</strong> ("we", "us", or "our"), concerning your access to and use of the <strong>PF Pension Assistant</strong> Android mobile application as well as this legal and support website.
          </p>
          <p>
            By downloading, installing, registering for, or using the Application, you agree that you have read, understood, and agreed to be bound by all of these Terms. If you do not agree, you are prohibited from using the Application.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Non-Affiliation & Scope of the Application</h2>
          <p>
            PF Pension Assistant is strictly an <strong>independent informational, educational, and navigational utility</strong>.
          </p>
          <div class="highlight-box warning">
            <strong>CRITICAL LEGAL NOTICE ON OFFICIAL STATUS:</strong><br>
            PF Pension Assistant is <strong>NOT</strong> an official app of the Employees' Provident Fund Organisation (EPFO), the Ministry of Labour and Employment, or any governmental department. We do not represent, hold authorization from, or maintain partnership with any statutory authority. Official EPFO filings and transactions must always be performed through the official portal at <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">epfindia.gov.in</a>.
          </div>
        </section>

        <section class="legal-section">
          <h2>3. Scope of Paid Service: PF Expert Assistance (₹299)</h2>
          <p>
            The Application offers a voluntary, one-time paid procedural advisory service called <strong>"PF Expert Assistance"</strong> at the fixed rate of <strong>₹299 per request</strong>.
          </p>
          <h3>A. What the ₹299 Fee Covers:</h3>
          <ul>
            <li>Review and analysis of your specific procedural problem (e.g., rejected claim reasons, joint declaration requirements, KYC mismatches) by an assistance specialist.</li>
            <li>Step-by-step guidance on how to correctly fill out required forms, obtain employer attestation, or file a grievance on EPFiGMS.</li>
            <li>Dedicated one-on-one communication support via our official WhatsApp desk (+91 9921200935).</li>
          </ul>

          <h3>B. Explicit Limitations & Non-Outcome Guarantees:</h3>
          <ul>
            <li><strong>No Outcome Guarantee:</strong> The fee pays strictly for advisory time and guidance. It does <strong>NOT</strong> guarantee that your claim will be approved, your transfer will be accepted, your pension will be sanctioned, or your funds will be disbursed by EPFO.</li>
            <li><strong>No Official Processing Power:</strong> We do not have internal access to EPFO servers or claim approval queues. Final decisions rest solely with your jurisdictional Regional PF Commissioner.</li>
            <li><strong>Single Incident Scope:</strong> Each ₹299 payment covers guidance for one distinct assistance request. Multiple unrelated inquiries require separate service bookings.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. User Responsibilities & Prohibited Misuse</h2>
          <p>As a user of the Application and its support channels, you agree that you will:</p>
          <ul>
            <li>Provide accurate, truthful, and up-to-date information in all intake forms and communications.</li>
            <li><strong>Never submit sensitive credentials:</strong> You must never share your UAN password, OTP, Aadhaar number, or banking credentials with our team. We will never ask for them.</li>
            <li>Not use the Application for any unlawful, fraudulent, or harassing purpose.</li>
            <li>Not attempt to reverse engineer, decompile, or extract the source code of the Android application.</li>
            <li>Respect the intellectual property rights and trademarks of AlgoAuraX.</li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. Payment Terms & Third-Party Processors</h2>
          <p>
            Payments for PF Expert Assistance are conducted via authorized third-party payment gateways (e.g., Razorpay). By initiating a transaction, you authorize the collection of the fee of ₹299. All applicable taxes (if any) are displayed at the point of checkout. We are not responsible for delays caused by your issuing bank or payment gateway downtime.
          </p>
        </section>

        <section class="legal-section">
          <h2>6. Limitation of Liability</h2>
          <p>
            To the maximum extent permitted by applicable Indian law, AlgoAuraX and its developers shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including loss of profits, data, or EPFO interest, arising out of your access to or inability to use the Application, or reliance on any informational content provided.
          </p>
          <p>
            Nothing in these Terms shall limit or exclude any statutory consumer rights that cannot be disclaimed under applicable law.
          </p>
        </section>

        <section class="legal-section">
          <h2>7. Service Modifications & Interruptions</h2>
          <p>
            We reserve the right to modify, suspend, or discontinue any feature or content within the Application at any time without notice. We are not liable to you or any third party for any modification, price change, suspension, or discontinuance of the service.
          </p>
        </section>

        <section class="legal-section">
          <h2>8. Governing Law & Dispute Resolution</h2>
          <p>
            These Terms and any dispute or claim arising out of or in connection with them shall be governed by and construed in accordance with the laws of India. In the event of any grievance, users are encouraged to contact our support desk first at <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> for amicable resolution.
          </p>
        </section>

        <section class="legal-section">
          <h2>9. Contact for Legal Inquiries</h2>
          <p>For any questions regarding these Terms and Conditions, please contact:</p>
          <div class="card" style="margin-top: 1rem;">
            <p style="margin-bottom: 0.5rem;"><strong>Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>WhatsApp Desk:</strong> +91 9921200935</p>
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
        <h1 class="page-title">Refund & Cancellation Policy</h1>
        <p class="page-subtitle">Effective Date: October 18, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
        <div class="meta-info">
          <span>Fee: ₹299 per Assistance Request</span>
          <span>Contact: sachinvr141@gmail.com</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Overview & Fair Review Philosophy</h2>
          <p>
            At AlgoAuraX, we are committed to transparent, honest, and fair consumer relations. The <strong>PF Expert Assistance</strong> service is provided at a nominal fixed fee of <strong>₹299</strong> to assist users with individual PF and pension queries.
          </p>
          <p>
            We do not apply a blanket "all fees are non-refundable" rule. Every refund or cancellation request is reviewed individually and decided fairly based on the criteria outlined below.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. What the ₹299 Fee Pays For</h2>
          <p>
            The ₹299 service fee pays exclusively for personalized consultation time, procedural review, and navigational assistance delivered through our WhatsApp support team. It is a service fee for professional analysis and advisory.
          </p>
        </section>

        <section class="legal-section">
          <h2>3. Scenarios Eligible for a Full Refund</h2>
          <p>A 100% refund of the ₹299 fee will be granted under the following circumstances:</p>
          <ul>
            <li>
              <strong>Duplicate or Multiple Charges:</strong> If you were accidentally charged twice or multiple times for the same single inquiry due to a network glitch or payment gateway error.
            </li>
            <li>
              <strong>Payment Succeeded but Request Not Delivered:</strong> If your payment was deducted, but our system failed to generate a Request ID or our support desk failed to initiate contact within 48 hours of payment verification.
            </li>
            <li>
              <strong>Cancellation Before Service Inception:</strong> If you submit a formal cancellation request via email or WhatsApp <em>before</em> our support specialist has reviewed your case documents or drafted an advisory response.
            </li>
            <li>
              <strong>Service Ineligibility:</strong> If upon initial review, our team determines that your query falls outside the scope of EPF/EPS procedural guidance and we cannot provide assistance.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>4. Scenarios Not Eligible for a Refund</h2>
          <p>Refunds cannot be granted in the following cases:</p>
          <ul>
            <li>
              <strong>Advisory Already Delivered:</strong> Once our support specialist has reviewed your case and provided the personalized procedural advice, document guidance, or grievance draft via WhatsApp or Email, the service is deemed completed and non-refundable.
            </li>
            <li>
              <strong>EPFO Authority Rejection or Outcome:</strong> The service fee covers procedural guidance only. If the EPFO department rejects your official claim due to employer issues, non-contributions, service gaps, or jurisdictional decisions beyond procedural control, this does not constitute grounds for a refund.
            </li>
            <li>
              <strong>User Refusal to Cooperate:</strong> If a user refuses to provide basic non-sensitive information necessary to guide them or requests illegal interventions that violate EPFO rules.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>5. How to Request a Refund</h2>
          <p>To submit a cancellation or refund request, please contact us within <strong>7 days</strong> of your transaction:</p>
          <ol>
            <li>Send an email to <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a> with the subject line: <code>Refund Request - [Your Request ID]</code>, or reach us on WhatsApp at <strong>+91 9921200935</strong>.</li>
            <li>Include your:
              <ul>
                <li>Full Name and registered 10-digit mobile number</li>
                <li>Request ID (e.g., <code>REQ-xxxxxx</code>)</li>
                <li>Payment Reference ID (provided by Razorpay or bank SMS)</li>
                <li>Brief explanation of the reason for your refund request</li>
              </ul>
            </li>
            <li>Our team will acknowledge your request within 24–48 business hours.</li>
          </ol>
        </section>

        <section class="legal-section">
          <h2>6. Refund Processing & Timelines</h2>
          <p>
            Once approved, refunds are credited back to the original payment source (bank account, UPI, or card) through our payment gateway (Razorpay). Depending on your bank's processing cycles, the amount typically reflects in your statement within <strong>5 to 7 business days</strong>.
          </p>
        </section>

        <section class="legal-section">
          <div class="highlight-box warning">
            <strong>CRITICAL NOTICE FOR GOOGLE PLAY POLICY COMPLIANCE:</strong><br>
            The PF Expert Assistance service is a real-world human consulting service delivered via communication channels. Before publishing the app for global in-app transactions on Google Play, the owner must verify compliance with Google Play's Payments Policy and ensure whether external payment processing (Razorpay) qualifies under Play Store exceptions or requires Google Play Billing.
          </div>
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
        <h1 class="page-title">Official Disclaimer</h1>
        <p class="page-subtitle">Effective Date: October 18, 2026 &bull; Published by AlgoAuraX for PF Pension Assistant</p>
      </div>

      <div class="disclaimer-banner" style="border-left: 4px solid var(--color-warning);">
        <svg class="disclaimer-banner-icon" style="color: var(--color-warning);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        <div>
          <strong>IMPORTANT INDEPENDENT STATUS NOTICE:</strong><br>
          PF Pension Assistant is an independent consumer assistance and educational application created by AlgoAuraX. It is <strong>NOT</strong> an official application of the Employees' Provident Fund Organisation (EPFO), the Government of India, or any state statutory board.
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Independent Operation & Non-Affiliation</h2>
          <p>
            Neither PF Pension Assistant nor AlgoAuraX:
          </p>
          <ul>
            <li>Is affiliated with, associated with, sponsored by, authorized by, or endorsed by the Employees' Provident Fund Organisation (EPFO).</li>
            <li>Is affiliated with the Ministry of Labour and Employment or any official Government of India department.</li>
            <li>Claims to be an official government app or a certified government grievance cell.</li>
          </ul>
          <p>
            Any visual assets, color choices, and iconography used within the Application are original designs intended solely for user experience and do not incorporate any official government emblem, seal, or copyrighted logo.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. Informational & Educational Nature of Content</h2>
          <p>
            All information provided in the Application — including calculation walkthroughs, form guides, FAQ articles, and procedure explanations — is gathered from publicly accessible government publications and acts (such as the Employees' Provident Funds and Miscellaneous Provisions Act, 1952, and the Employees' Pension Scheme, 1995).
          </p>
          <p>
            While we strive to keep information accurate and updated, statutory rules, interest rates, and online portal interfaces change periodically. Users must always verify their specific case details against the official EPFO announcements.
          </p>
        </section>

        <section class="legal-section">
          <h2>3. No Guarantee of Government Decisions or Timelines</h2>
          <p>
            Neither the free guidance within the Application nor the ₹299 PF Expert Assistance consultation has the authority to approve, settle, accelerate, or modify any official EPF/EPS claim. All decisions, settlement dates, and transfer verifications are exclusively determined by the jurisdictional Regional PF Commissioner.
          </p>
        </section>

        <section class="legal-section">
          <h2>4. Verified Official Government Portals</h2>
          <p>
            To access your official PF passbook, submit online claim forms, or lodge official statutory grievances, please visit the verified Government of India portals:
          </p>
          <div class="card" style="margin-top: 1rem;">
            <ul style="margin: 0; padding-left: 1.25rem;">
              <li style="margin-bottom: 0.75rem;">
                <strong>Official EPFO Main Portal:</strong><br>
                <a href="https://www.epfindia.gov.in" target="_blank" rel="noopener noreferrer">https://www.epfindia.gov.in/</a>
              </li>
              <li style="margin-bottom: 0.75rem;">
                <strong>EPFO Member Passbook & Claim Status Portal:</strong><br>
                <a href="https://passbook.epfindia.gov.in" target="_blank" rel="noopener noreferrer">https://passbook.epfindia.gov.in/</a>
              </li>
              <li style="margin-bottom: 0.75rem;">
                <strong>EPFO Unified Member Portal (UAN Login):</strong><br>
                <a href="https://unifiedportal-mem.epfindia.gov.in/memberinterface/" target="_blank" rel="noopener noreferrer">https://unifiedportal-mem.epfindia.gov.in/memberinterface/</a>
              </li>
              <li style="margin-bottom: 0;">
                <strong>EPFiGMS Official Grievance Portal:</strong><br>
                <a href="https://epfigms.gov.in" target="_blank" rel="noopener noreferrer">https://epfigms.gov.in/</a>
              </li>
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
        <p class="page-subtitle">Instructions for requesting deletion of personal data and associated records under AlgoAuraX.</p>
        <div class="meta-info">
          <span>Dedicated Support: sachinvr141@gmail.com</span>
          <span>WhatsApp: +91 9921200935</span>
        </div>
      </div>

      <div class="legal-content">
        <section class="legal-section">
          <h2>1. Our Data Retention & Deletion Principles</h2>
          <p>
            At AlgoAuraX, we respect your right to control your personal information. In full compliance with Google Play's User Data policy on Account Deletion, this page provides a clear, publicly accessible, and straightforward path for users of <strong>PF Pension Assistant</strong> to request the permanent deletion of their account records and associated personal data.
          </p>
        </section>

        <section class="legal-section">
          <h2>2. What Data Is Stored & Where</h2>
          <ul>
            <li>
              <strong>On Your Device (Local Storage):</strong> The intake requests and transaction records are stored in your device's local SQLite database. You can instantly delete all local data at any time by clearing the app data through your phone settings: <code>Settings &gt; Apps &gt; PF Pension Assistant &gt; Storage &gt; Clear Data</code>.
            </li>
            <li>
              <strong>Support Communications:</strong> Emails sent to our support inbox and messages exchanged on our official WhatsApp desk.
            </li>
            <li>
              <strong>Payment Transaction Logs:</strong> Razorpay payment identifiers and order IDs associated with the ₹299 service.
            </li>
          </ul>
        </section>

        <section class="legal-section">
          <h2>3. Step-by-Step Manual Deletion Request Process</h2>
          <p>
            Because the Application operates with on-device persistence rather than an automated cloud user-management backend, data deletion requests are reviewed and processed manually by our privacy team to ensure all associated records are thoroughly purged.
          </p>

          <div class="card" style="margin: 1.5rem 0;">
            <h3>Option A: Request Deletion via Email (Recommended)</h3>
            <p>Send an email from your registered email address to our data privacy desk:</p>
            <p>
              <a href="mailto:sachinvr141@gmail.com?subject=Account%20and%20Data%20Deletion%20Request%20-%20PF%20Pension%20Assistant&body=Dear%20AlgoAuraX%20Support%20Team%2C%0A%0AI%20am%20requesting%20the%20permanent%20deletion%20of%20my%20data%20and%20account%20records%20associated%20with%20the%20PF%20Pension%20Assistant%20application.%0A%0AMy%20Registered%20Details%3A%0AFull%20Name%3A%20%0AMobile%20Number%3A%20%0AEmail%20Address%3A%20%0A%0AThank%20you." class="btn btn-primary">
                Open Pre-filled Deletion Email
              </a>
            </p>
            <p class="form-help">
              Or write to: <strong>sachinvr141@gmail.com</strong> with the subject <code>Account and Data Deletion Request - PF Pension Assistant</code>.
            </p>
          </div>

          <div class="card" style="margin: 1.5rem 0;">
            <h3>Option B: Request Deletion via WhatsApp Support</h3>
            <p>You may also contact our verified WhatsApp support desk to submit your deletion request:</p>
            <p>
              <a href="https://wa.me/919921200935?text=Hello%20AlgoAuraX%20Support%2C%20I%20would%20like%20to%20request%20the%20deletion%20of%20my%20data%20and%20account%20records%20from%20PF%20Pension%20Assistant." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">
                Message WhatsApp Support (+91 9921200935)
              </a>
            </p>
          </div>
        </section>

        <section class="legal-section">
          <h2>4. Information Required & What NEVER to Send</h2>
          <p>
            To locate your records, you only need to provide:
          </p>
          <ul>
            <li>Your Full Name</li>
            <li>Your 10-digit mobile number</li>
            <li>Your email address (if authenticated via Google)</li>
          </ul>

          <div class="highlight-box danger">
            <strong>NEVER SEND PASSWORDS OR PRIVATE NUMBERS:</strong><br>
            We will <strong>NEVER</strong> ask for your UAN password, OTP, Aadhaar number, or bank details. Do not include these in any deletion request.
          </div>
        </section>

        <section class="legal-section">
          <h2>5. What Happens Upon Deletion</h2>
          <ol>
            <li><strong>Verification:</strong> Our support desk verifies your ownership of the contact details within 48 business hours.</li>
            <li><strong>Purging:</strong> Your personal profile, submitted inquiry notes, and communication threads are permanently deleted from our support inboxes and customer logs.</li>
            <li><strong>Statutory Retentions:</strong> Please note that financial transaction records (such as payment IDs and tax invoice logs) may be retained for the minimum period mandated by Indian tax and accounting statutes before permanent disposal.</li>
          </ol>
        </section>
      </div>
    </div>
"""

# -------------------------------------------------------------
# 7. CONTACT AND SUPPORT
# -------------------------------------------------------------
contact_body = """
    <div class="container content-wrap">
      <div class="page-header">
        <div class="badge badge-primary">Official Support Desk</div>
        <h1 class="page-title">Contact & Support</h1>
        <p class="page-subtitle">Get in touch with the AlgoAuraX support team for assistance inquiries, technical help, or feedback.</p>
      </div>

      <div class="disclaimer-banner">
        <svg class="disclaimer-banner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
        <div>
          <strong>Safety Advisory:</strong> For your security, <strong>never</strong> include your UAN password, OTP, Aadhaar number, or banking PINs in any support message. Our team will never ask for your confidential credentials.
        </div>
      </div>

      <div class="legal-content">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
          <!-- WhatsApp Channel -->
          <div class="card" style="border: 1px solid #25D366; background: var(--color-surface);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
              <span style="display: inline-flex; width: 36px; height: 36px; background: #25D366; border-radius: var(--radius-sm); align-items: center; justify-content: center; color: #FFF;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
              </span>
              <div>
                <h3 style="margin: 0; font-size: 1.15rem;">WhatsApp Support</h3>
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Direct messaging & assistance desk</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 1.25rem;">
              Chat directly with our assistance desk for general app guidance or to follow up on your ₹299 PF Expert Assistance ticket.
            </p>
            <div style="margin-bottom: 1.25rem; font-family: var(--font-mono); font-weight: 600; font-size: 1.05rem;">
              +91 9921200935
            </div>
            <a href="https://wa.me/919921200935?text=Hello%2C%20I%20need%20support%20with%20the%20PF%20Pension%20Assistant%20app." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%;">
              Open WhatsApp Chat
            </a>
          </div>

          <!-- Email Channel -->
          <div class="card" style="border: 1px solid var(--color-primary); background: var(--color-surface);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
              <span style="display: inline-flex; width: 36px; height: 36px; background: var(--color-primary); border-radius: var(--radius-sm); align-items: center; justify-content: center; color: #FFF;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              </span>
              <div>
                <h3 style="margin: 0; font-size: 1.15rem;">Email Support</h3>
                <span style="font-size: 0.8rem; color: var(--color-text-secondary);">Official customer & privacy queries</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin-bottom: 1.25rem;">
              Send inquiries regarding policies, refunds, data deletion requests, or partnership questions.
            </p>
            <div style="margin-bottom: 1.25rem; font-family: var(--font-mono); font-weight: 600; font-size: 1.05rem; word-break: break-all;">
              sachinvr141@gmail.com
            </div>
            <a href="mailto:sachinvr141@gmail.com?subject=Support%20Inquiry%20-%20PF%20Pension%20Assistant" class="btn btn-primary" style="width: 100%;">
              Send an Email
            </a>
          </div>
        </div>

        <section class="legal-section">
          <h2>Application Information</h2>
          <div class="card">
            <p style="margin-bottom: 0.5rem;"><strong>Application Name:</strong> PF Pension Assistant</p>
            <p style="margin-bottom: 0.5rem;"><strong>Developer Brand:</strong> AlgoAuraX</p>
            <p style="margin-bottom: 0.5rem;"><strong>Primary Platform:</strong> Android</p>
            <p style="margin-bottom: 0.5rem;"><strong>Official Support Email:</strong> <a href="mailto:sachinvr141@gmail.com">sachinvr141@gmail.com</a></p>
            <p style="margin-bottom: 0;"><strong>Official WhatsApp Contact:</strong> +91 9921200935</p>
          </div>
        </section>
      </div>
    </div>
"""

# Map page contents
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

print("All 7 static site pages rendered successfully!")
