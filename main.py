import random

word_hints = {
    "samalyot": "Temir qush",
    "olma": "Ilm mevasi",
    "kompyuter": "Sirlar sandig'i",
    "telefon": "Cho'ntak olami",
    "mashina": "Temir tulpor",
    "kitob": "Jim ustoz",
    "quyosh": "Koinot olovi",
    "soat": "Vaqt o'g'risi",
    "qalam": "Qora yulduz",
    "dengiz": "Moviy olam",
    "oy": "Tungi chiroq",
    "suv": "Hayot manbai",
}

while True:
    secret_word, hint = random.choice(list(word_hints.items()))

    print("===SO'Z TOPISH O'YINI===")
    print(f"🕵️‍♂️ Podskazka: {hint}")
    print(f"So'z uzunligi: {len(secret_word)} ta harfdan iborat.\n")

    full_guess = input(
        "Butun so'zni topishga harakat qiling (yoki o'tkazib yuborish uchun Enter bosing): ").lower().strip()

    if full_guess == secret_word:
        print(f"🏆 Qoyil! Shu qisqa ishoradan topganingiz uchun haqiqiy dahosiz! Yashirin so'z: '{secret_word}'")
    else:
        if full_guess:
            print("❌ Afsuski, bu emas edi. Endi harfma-harf davom etamiz!\n")
        else:
            print("Xo'sh, unda harfma-harf topishga o'tamiz!\n")

        guessed_letters = []
        attempts = 7

        while attempts > 0:
            display_word = ""
            for letter in secret_word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            print(f"So'z --  {display_word.strip()}")
            print(f"Qolgan urunishlar soni {attempts}")

            if "_" not in display_word:
                print(f"\n🎉 Tabriklayman! Siz so'zni to'liq topdingiz: {secret_word}")
                break

            user_guess = input("Birorta harf kiriting: ").lower().strip()

            if len(user_guess) != 1:
                print("Iltimos, faqat bitta harf kiriring!")
                continue

            if user_guess in guessed_letters:
                print("Siz bu harfni allaqachon kiritgansiz!")
                continue

            guessed_letters.append(user_guess)

            if user_guess in secret_word:
                print("✅ To'g'ri! Bunday harf bor.\n")
            else:
                attempts -= 1
                print("❌ Afsuski, bunday harf yo'q.\n")
        else:
            print(f"😢 O'yin tugadi! Urinishlaringiz tugadi. Yashirin so'z '{secret_word}' edi.")
    play_again = input("\nYana o'ynashni xohlaysizmi? (ha/yo'q): ").lower().strip()
    if play_again != "ha" and play_again != "h":
        print("O'yin uchun rahmat! Xayr! 👋")
        break
















