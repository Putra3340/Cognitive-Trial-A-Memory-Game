import random
import os
import time
import threading
import sys

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

# 1 = Classic
# 2 = Advanced
game_mode = "0"

game_timer = 60 # default 60 seconds

# Timer Logic
def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(f"⌛{timeout}s {prompt}")

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return None  # waktu habis
    else:
        return user_input[0]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def printRandomColor(text):
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    color = random.choice(colors)
    reset = "\033[0m"
    print(f"{color}{text}{reset}")

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
    #validasi jumlah huruf
    if(len(answer) != len(user_answer)):
        return False
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
    global difficulty
    global score
    global game_mode
    clear_screen()
    print("=== Cognitive Trial: A Memory Game ===\n\n")
    print("Pilih Mode Game:")
    print("1. Classic")
    print("2. Advanced")
    game_mode = input("Masukkan pilihan (1-2): ").strip()
    
    while True:
        clear_screen()
        print("=== Cognitive Trial: A Memory Game ===\n\n")
        print("Mode Game:", "Classic" if game_mode == "1" else "Advanced")
        print("Pilih tingkat kesulitan:")
        print("1. Easy (Arah panah)")
        print("2. Normal (Angka)")
        print("3. Hard (Huruf)")
        print("4. Impossible (Kata)")
        print("5. Kembali ke menu utama")
        
        difficulty = input("Masukkan pilihan (1-5): ").strip()
        choices = get_choices()

        if choices is None:
            print("Pilihan tidak valid!")
            return
        
        sequence = []
        score = 0

        while True:
            # menambah satu item random ke sequence
            sequence.append(random.choice(choices))

            # tampilkan sequence ke pemain
            for item in sequence:
                clear_screen()
                print("==============================")
                print("Skor anda :", score)
                print("Ingat urutan berikut:")
                printRandomColor("==============================")
                printRandomColor(f"            {item}           ")
                printRandomColor("==============================")
                time.sleep(1)

            # hapus layar
            clear_screen()
            print("==============================")
            print("Skor anda :", score)
            print("Masukkan ulang urutan tadi:")
            if(game_mode == "1"):
                # classic mode: waktu bertambah sesuai panjang sequence + 60 detik + 5 detik
                answer = timed_input(">> ", game_timer + len(sequence) + 5)
            elif(game_mode == "2"):
                # advanced mode : waktu panjang sequence + 5 detik
                answer = timed_input(">> ", len(sequence) + 5)

            clear_screen()

            # jika waktu habis
            if(answer is None):
                print("\nWaktu habis! Permainan berakhir.")
                if(difficulty == "1"):
                    print("Urutan yang benar (WASD): ", arrowToWasd("".join(sequence)))
                print("Urutan yang benar: ", ("".join(sequence)).lower())
                print("Skor Akhir:", score)
                input("Tekan Enter untuk kembali ke menu utama")
                clear_screen()
                break

            # validasi jawaban
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
