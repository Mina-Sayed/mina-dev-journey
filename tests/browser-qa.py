from pathlib import Path
from playwright.sync_api import sync_playwright

html = Path("index.html").read_text(encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width": 1440, "height": 900})
    errors: list[str] = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.set_content(html, wait_until="load")

    assert page.title() == "Mina's Dev Journey"
    assert page.get_by_role("button", name="▶ PLAY JOURNEY").is_visible()

    page.get_by_role("button", name="◆ QUICK PORTFOLIO").click()
    assert page.get_by_text("Mina Sayed — Senior Full Stack Engineer").is_visible()
    page.get_by_role("button", name="× CLOSE").click()

    page.get_by_role("button", name="▶ PLAY JOURNEY").click()
    assert page.locator("canvas").is_visible()
    page.wait_for_timeout(150)
    page.keyboard.press("e")
    assert page.locator("#modal:not(.hidden)").is_visible()
    assert page.locator("#modalBox h2").get_by_text("Legacy City Migration").is_visible()
    page.get_by_role("button", name="SIMPLIFIED MODE").click()
    assert page.get_by_text("Career Metro // Exacall unlocked").is_visible()
    assert errors == [], errors

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile_errors: list[str] = []
    mobile.on("pageerror", lambda error: mobile_errors.append(str(error)))
    mobile.set_content(html, wait_until="load")
    mobile.get_by_role("button", name="▶ PLAY JOURNEY").click()
    assert mobile.locator("#left").is_visible()
    assert mobile.locator("body").evaluate("(el) => el.scrollWidth <= innerWidth + 1")
    assert mobile_errors == [], mobile_errors

    browser.close()

print("Browser QA passed: desktop journey, portfolio, mission progression and mobile controls.")
