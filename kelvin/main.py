import undetected_chromedriver as uc
import email_module
import crawler
import names
import time

def listener(msg):
    print("[MAIL]", msg.get("subject"))
    txt = msg.get("text", "")
    for line in txt.splitlines():
        if "verification code" in line.lower():
            return line.split(": ")[-1].strip()

def run_once():
    mail = email_module.Email()
    mail.register()
    print("Email:", mail.address)

    mail.one_bot_start(listener, interval=3)

    chrome = uc.Chrome()
    try:
        crawler.register(chrome, mail.address, names.get_full_name())
        mail.stop_when_finish()

        code = None
        for _ in range(30):          # tunggu max 60 detik
            code = mail.get_email_content()
            if code:
                break
            time.sleep(2)

        if not code:
            print("Kode verifikasi tidak ditemukan")
            return

        crawler.authenticate(chrome, code)
        print("Registrasi selesai!")
    finally:
        chrome.quit()

if __name__ == "__main__":
    while True:
        try:
            run_once()
            time.sleep(5)
        except KeyboardInterrupt:
            break
