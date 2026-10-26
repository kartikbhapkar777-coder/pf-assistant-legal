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

    verified_email = "BhimaBhapkar777@gmail.com"
    phone_digits = "9921200935"

    for p in pages:
        full_path = os.path.join(base_dir, p)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        assert "<title>" in content and "</title>" in content, f"Missing title in {p}"
        assert '<meta name="description"' in content, f"Missing meta description in {p}"

        # 1. Mandatory Global Header Disclaimer on EVERY page
        assert "global-gov-disclaimer-banner" in content, f"Mandatory global disclaimer class missing in {p}"
        assert "independent educational" in content, f"Mandatory global disclaimer text missing in {p}"
        assert "DOES NOT represent, and is NOT affiliated with, endorsed by, or authorized by" in content, f"Mandatory wording missing in {p}"

        # 2. Verified contact
        assert verified_email in content, f"Verified email missing in {p}"
        assert phone_digits in content, f"Verified Phone missing in {p}"

        # 3. Check for government sources links on Home, Terms, Disclaimer
        if p in ["index.html", "terms/index.html", "disclaimer/index.html"]:
            assert "https://www.epfindia.gov.in" in content, f"Official EPFO Portal missing in {p}"
            assert "https://unifiedportal-mem.epfindia.gov.in/memberinterface/" in content, f"Member e-Sewa missing in {p}"
            assert "https://passbook.epfindia.gov.in" in content, f"Member Passbook missing in {p}"
            assert "https://epfigms.gov.in" in content, f"EPFiGMS missing in {p}"

        # 4. Check specific Terms clauses
        if p == "terms/index.html":
            assert "This fee is NOT an official EPFO government fee" in content, "Fee disclaimer missing in Terms"
            assert "epfindia.gov.in" in content, "Verification responsibility missing in Terms"

        # 5. Check Privacy Policy clauses
        if p == "privacy-policy/index.html":
            assert "We NEVER ask for, collect, or store your EPFO UAN password" in content, "Password disclaimer missing in Privacy"
            assert "Firebase Auth" in content or "Firebase Authentication" in content, "Firebase clause missing in Privacy"

        print(f" [PASS] Google Play Policy Compliance passed for: {p}")

    print("=== ALL 7 PAGES PASSED 100% GOOGLE PLAY VERIFICATION! ===")

if __name__ == "__main__":
    test_site()
