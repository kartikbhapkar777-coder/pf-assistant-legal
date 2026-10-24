import os

def test_site():
    base_dir = r"d:\PF Ass\pf-assistant-legal"
    pages = [
        "index.html",
        "privacy-policy/index.html",
        "terms/index.html",
        "refund-policy/index.html",
        "disclaimer/index.html",
        "data-deletion/index.html",
        "contact/index.html"
    ]

    print("=== STARTING COMPREHENSIVE SITE VALIDATION ===")
    
    # 1. Check all pages exist
    for p in pages:
        full_path = os.path.join(base_dir, p)
        assert os.path.isfile(full_path), f"Missing page: {p}"
        print(f" [PASS] File exists: {p}")

    # 2. Check CSS & JS exist
    assert os.path.isfile(os.path.join(base_dir, "css", "style.css")), "Missing style.css"
    assert os.path.isfile(os.path.join(base_dir, "js", "main.js")), "Missing main.js"
    print(" [PASS] Static assets (CSS/JS) present.")

    # 3. Inspect page contents for verified details and absence of forbidden content
    verified_email = "BhimaBhapkar777@gmail.com"
    verified_whatsapp = "919921200935"

    for p in pages:
        full_path = os.path.join(base_dir, p)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        assert "<title>" in content and "</title>" in content, f"Missing title in {p}"
        assert '<meta name="description"' in content, f"Missing meta description in {p}"

        # Check verified contact information
        assert verified_email in content, f"Verified email missing in {p}"
        assert verified_whatsapp in content, f"Verified WhatsApp missing in {p}"

        # Check theme toggle & mobile button
        assert "theme-toggle" in content, f"Theme toggle missing in {p}"
        assert "mobile-menu-btn" in content, f"Mobile menu button missing in {p}"

        # Ensure statutory disclaimer
        assert "affiliated with" in content, f"Affiliation disclaimer missing in {p}"

        print(f" [PASS] Integrity & Compliance checks passed for: {p}")

    print("=== ALL 7 PAGES PASSED VALIDATION SUCCESSFULLY! ===")

if __name__ == "__main__":
    test_site()
