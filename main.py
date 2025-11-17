import random
import os
import time

# Global Variable
score = 0

mapping = {
    "↑": "w",
    "↓": "s",
    "←": "a",
    "→": "d"
}

# 1 = Easy
# 2 = Normal
# 3 = Hard
# 4 = Impossible
difficulty = "0"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_choices():
    if difficulty == "1":  # Easy
        return ["↑", "↓", "←", "→"]
    elif difficulty == "2":  # Normal
        return [str(i) for i in range(10)]
    elif difficulty == "3":  # Hard
        return [chr(i) for i in range(65, 91)]  # A–Z
    elif difficulty == "4":  # Impossible
        return ["cat", "moon", "red", "blue", "star", "note", "time", "fire"]
    else:
        return None

def arrowToWasd(text):
    for arrow, key in mapping.items():
        text = text.replace(arrow, key)
    return text

def validate(answer, user_answer):
    for i in range(len(answer)):
        if i >= len(user_answer):
            return False  # user kurang huruf
        if(difficulty == "4"): # eksklusif very hard validasi sensitif
            if answer[i] != user_answer[i]:
                return False  # salah
        elif(difficulty == "1"): # eksklusif panah validasi menggunakan WASD
            if arrowToWasd(answer[i]).lower() != user_answer[i].lower():
                return False # salah
        else:
            if answer[i].lower() != user_answer[i].lower():
                return False  # salah
    return True

def main():
    clear_screen()
    print("=== Cognitive Trial: A Memory Game ===\n\n")
    print("Pilih tingkat kesulitan:")
    print("1. Easy (Arah panah)")
    print("2. Normal (Angka)")
    print("3. Hard (Huruf)")
    print("4. Impossible (Kata)")

    global difficulty
    global score
    difficulty = input("Masukkan pilihan (1-4): ").strip()
    choices = get_choices()

    if choices is None:
        print("Pilihan tidak valid!")
        return
    
    sequence = []

    while True:
        # menambah satu item random ke sequence
        sequence.append(random.choice(choices))

        # tampilkan sequence ke pemain
        for item in sequence:
            clear_screen()
            print("Ingat urutan berikut:")
            print(item)
            time.sleep(1)

        # hapus layar
        clear_screen()
        print("Masukkan ulang urutan tadi:")
        answer = input("> ").strip()

        # cek jawaban
        if (validate("".join(sequence),answer)):
            score += 1
            print("Benar! Lanjut ke ronde berikutnya...")
            time.sleep(1)
        else:
            print("\nSalah! Permainan berakhir.")
            print("Jawaban Anda: ", answer)
            if(difficulty == "1"):
                print("Urutan yang benar (WASD): ", arrowToWasd("".join(sequence)))
            print("Urutan yang benar: ", ("".join(sequence)).lower())
            print("Skor Akhir:", score)
            input("Tekan Enter untuk kembali ke menu utama")
            clear_screen()
            break

if __name__ == "__main__":
    while True:
        main()
