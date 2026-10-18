# PF Pension Assistant — Legal & Compliance Website

Official public legal and customer support documentation portal for the **PF Pension Assistant** Android application, published under the brand **AlgoAuraX**.

Built with privacy-by-design standards, an Apple-inspired minimal UI/UX matching the Android application's teal/blue palette, responsive mobile-first architecture, and strict Google Play compliance declarations.

---

## 🌐 Public Routes Overview

| Route | Page | Purpose & Compliance Scope |
|---|---|---|
| `/` | **Home** | Overview of app capabilities, ₹299 PF Expert Assistance service, and legal links |
| `/privacy-policy/` | **Privacy Policy** | Verified data disclosures, local SQLite persistence, Firebase Google Sign-In, and zero-collection of UAN passwords/Aadhaar/OTPs |
| `/terms/` | **Terms and Conditions** | User agreements, advisory scope, non-outcome guarantees, and dispute procedures |
| `/refund-policy/` | **Refund & Cancellation** | Fair refund review framework, duplicate payment handling, and cancellation windows |
| `/disclaimer/` | **Official Disclaimer** | Strict non-affiliation statement (not EPFO or Govt of India) & verified official portals |
| `/data-deletion/` | **Account & Data Deletion** | Clear instructions & mailto/WhatsApp options for permanent data deletion |
| `/contact/` | **Contact & Support** | Direct access to official email and verified WhatsApp Business support channel |

---

## 🎨 Design System & Palette

Directly matches the Android application (`com.example.ui.theme`):
- **Primary Teal:** `#176B87`
- **Secondary Accent:** `#087E8B`
- **Light Background:** `#F2F6F8`
- **Light Surfaces:** `#FFFFFF`
- **Main Text:** `#172B3A`
- **Secondary Text:** `#637381`
- **Borders:** `#E1E8ED`
- **Dark Background:** `#101820`
- **Dark Surface:** `#18232D`
- **Dark Text:** `#F4F7FA`
- **Dark Accent:** `#58B7C5`

Features interactive **Light/Dark theme toggling** that respects system preferences and persists user preference in `localStorage`.

---

## 🚀 Setup & Local Preview Instructions

### 1. View Locally
You can preview the website immediately using Python's built-in HTTP server:
```bash
cd pf-assistant-legal
python -m http.server 8000
```
Open your browser and navigate to:
```
http://localhost:8000/
```

### 2. Regenerate Pages (If Making Updates)
All pages are maintained via structured Python generation scripts:
```bash
python build_site.py
python verify_site.py
```

---

## 🚢 GitHub Pages Deployment Steps

This repository is pre-configured with a GitHub Actions workflow (`.github/workflows/deploy.yml`) for seamless deployment.

### Instructions for the Repository Owner:
1. Push these commits to GitHub:
   ```bash
   git add .
   git commit -m "feat: complete legal and compliance static website for PF Pension Assistant"
   git push origin main
   ```
2. Navigate to your GitHub repository in your web browser:
   `https://github.com/kartikbhapkar777-coder/pf-assistant-legal`
3. Click on the **Settings** tab.
4. In the left sidebar, click on **Pages** (under the "Code and automation" section).
5. Under **Build and deployment** > **Source**:
   - Select **GitHub Actions** (recommended) or **Deploy from a branch** (`main` / root `/`).
6. The GitHub Actions workflow will trigger automatically and deploy the site.
7. Your verified live public URL will be:
   ```
   https://kartikbhapkar777-coder.github.io/pf-assistant-legal/
   ```

---

## 📋 Google Play Release Checklist

### 1. Verified & Implemented in this Repository
- [x] **Public Privacy Policy URL:** Accessible directly at `/privacy-policy/`.
- [x] **Public Account/Data Deletion URL:** Accessible directly at `/data-deletion/`.
- [x] **Transparent Disclaimer:** Clearly discloses non-affiliation with EPFO or Govt of India.
- [x] **Clear Data Minimization Disclosures:** Prohibits collection of UAN passwords, OTPs, Aadhaar numbers, and bank credentials.
- [x] **Official Contact Channels:** Verified email (`sachinvr141@gmail.com`) and WhatsApp (`+91 9921200935`).

### 2. Manual Action Required in Google Play Console (By Owner)
- [ ] **Policy > App Content > Privacy Policy:** Paste `https://kartikbhapkar777-coder.github.io/pf-assistant-legal/privacy-policy/`
- [ ] **Policy > App Content > Data Deletion:** Paste `https://kartikbhapkar777-coder.github.io/pf-assistant-legal/data-deletion/` and declare that users can request deletion via email/WhatsApp.
- [ ] **Data Safety Form:**
  - *Data collected:* Name and Phone Number (when voluntarily submitted for PF Expert Assistance; not shared with third parties for advertising).
  - *Data encrypted in transit:* Yes (HTTPS/TLS).
  - *Deletion mechanism:* Yes (User can request deletion).
- [ ] **App Category & Content Rating:** Complete IARC questionnaire (Target Audience: 18+).
- [ ] **Government Apps Declaration:** Accurately select **"No, this app does not represent a government entity"**.

### 3. Critical Release-Blocking Review Items (Owner Decision Required)
- [ ] **Google Play Payments Policy for the ₹299 Assistance Service:**
  The app currently implements or prepares Razorpay for the ₹299 advisory service. Under Google Play policies:
  - *In-app digital content/services* typically require **Google Play Billing**.
  - *Physical services or human consulting* may qualify for exceptions in specific regions/categories, or under the User Choice Billing / Alternative Billing programs in India.
  - **Action Required:** Consult Google Play developer counsel to confirm whether Razorpay direct integration is permitted for this service on Play Store, or if Google Play In-App Billing must be enabled prior to public production release.
- [ ] **Legal Business Entity Verification:** AlgoAuraX is treated as the brand identity. If registering as a Private Limited, LLP, or Proprietorship with a registered GST number, update the legal disclosure accordingly.

---

## 🛡️ Integrity & Security
- Zero external advertising scripts or analytics tracking cookies.
- No secrets, credentials, or private keys committed.
- Validated with `verify_site.py`.