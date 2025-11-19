import random
import os
import time
import threading
import base64

# Global Variable
KEY = 69  # boleh diganti angka 0–255

score = 0

mapping = {
    "↑": "w",
    "↓": "s",
    "←": "a",
    "→": "d"
}

# HighScore Data
classic_easy_highscore = 0
classic_normal_highscore = 0
classic_hard_highscore = 0
classic_impossible_highscore = 0
advanced_easy_highscore = 0
advanced_normal_highscore = 0
advanced_hard_highscore = 0
advanced_impossible_highscore = 0
extreme_easy_highscore = 0
extreme_normal_highscore = 0
extreme_hard_highscore = 0
extreme_impossible_highscore = 0

# 1 = Easy
# 2 = Normal
# 3 = Hard
# 4 = Impossible
difficulty = "0"

# 1 = Classic - High Time, Low Score
# 2 = Advanced - Low Time, High Score
# 3 = Extreme - Low Time, Very High Score and Random Combination each round
game_mode = "0"

# 0 = Only Classic Mode
# 1 = Classic + Advanced Mode
# 2 = Classic + Advanced + Extreme Mode
# 3 = All Modes Beated
unlocked_modes = "0"

# For pop-up notification easter egg / achievement
alreadynotified = False

game_timer = 60 # default 60 seconds

# Lebar keseluruhan box (ubah bebas)
BOX_WIDTH = 65  # responsif
INNER_WIDTH = BOX_WIDTH - 4  # ruang dalam antara │    │

def pad(text):
    return f"{text:<{INNER_WIDTH}}"

def encrypt(text):
    encrypted_bytes = bytes([b ^ KEY for b in text.encode()])
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(encoded):
    try:
        encrypted_bytes = base64.b64decode(encoded.encode())
        decrypted_bytes = bytes([b ^ KEY for b in encrypted_bytes])
        return decrypted_bytes.decode()
    except:
        return None

def showCredits():
    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
    print("║" + "🧠  COGNITIVE TRIAL: MEMORY GAME  🧠".center(INNER_WIDTH) + "║")
    print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
    print("║" + pad("Developer 1 : Rahmad Dwi Syaputra") + "  ║")
    print("║" + pad("Developer 2 : Marcellino Putra Kurniawan") + "  ║")
    print("║" + pad("SMKN 1 Dlanggu - XII RPL 3") + "  ║")
    print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
    print("║" + pad("Thank you for playing!") + "  ║")
    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")

# Save Data Logic
def save_score():
    global classic_easy_highscore
    global classic_normal_highscore
    global classic_hard_highscore
    global classic_impossible_highscore
    global advanced_easy_highscore
    global advanced_normal_highscore
    global advanced_hard_highscore
    global advanced_impossible_highscore
    global extreme_easy_highscore
    global extreme_normal_highscore
    global extreme_hard_highscore
    global extreme_impossible_highscore
    global unlocked_modes

    filename = f"scores.dat"
    with open(filename, "w") as file: # overwrite
        file.write(encrypt(f"{classic_easy_highscore}|{classic_normal_highscore}|{classic_hard_highscore}|{classic_impossible_highscore}|{advanced_easy_highscore}|{advanced_normal_highscore}|{advanced_hard_highscore}|{advanced_impossible_highscore}|{extreme_easy_highscore}|{extreme_normal_highscore}|{extreme_hard_highscore}|{extreme_impossible_highscore}|{unlocked_modes}"))

def load_scores():
    global classic_easy_highscore
    global classic_normal_highscore
    global classic_hard_highscore
    global classic_impossible_highscore
    global advanced_easy_highscore
    global advanced_normal_highscore
    global advanced_hard_highscore
    global advanced_impossible_highscore
    global extreme_easy_highscore
    global extreme_normal_highscore
    global extreme_hard_highscore
    global extreme_impossible_highscore
    global unlocked_modes

    filename = f"scores.dat"
    if not os.path.exists(filename):
        # buat file baru dengan skor 0
        filename = f"scores.dat"
        with open(filename, "w") as file: # overwrite
            file.write(encrypt(f"{classic_easy_highscore}|{classic_normal_highscore}|{classic_hard_highscore}|{classic_impossible_highscore}|{advanced_easy_highscore}|{advanced_normal_highscore}|{advanced_hard_highscore}|{advanced_impossible_highscore}|{extreme_easy_highscore}|{extreme_normal_highscore}|{extreme_hard_highscore}|{extreme_impossible_highscore}|{unlocked_modes}"))
        return  # file tidak ada, lewati
    with open(filename, "r") as file:
        data = decrypt(file.read().strip())
        data = data.split("|")
        if len(data) == 13:
            classic_easy_highscore = int(data[0])
            classic_normal_highscore = int(data[1])
            classic_hard_highscore = int(data[2])
            classic_impossible_highscore = int(data[3])
            advanced_easy_highscore = int(data[4])
            advanced_normal_highscore = int(data[5])
            advanced_hard_highscore = int(data[6])
            advanced_impossible_highscore = int(data[7])
            extreme_easy_highscore = int(data[8])
            extreme_normal_highscore = int(data[9])
            extreme_hard_highscore = int(data[10])
            extreme_impossible_highscore = int(data[11])
            unlocked_modes = int(data[12])

# Timer Logic
def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(f"⌛ {timeout}s {prompt}")

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
        return [
    # 50 kata umum Indonesia
    "air ","tanah ","api ","angin ","batu ","pohon ","daun ","langit ","awan ","hujan ",
    "petir ","matahari ","bulan ","bintang ","rumah ","jalan ","kursi ","meja ","pintu ","jendela ",
    "buku ","kertas ","pena ","air ","makanan ","minuman ","orang ","teman ","guru ","murid ",
    "waktu ","hari ","malam ","siang ","pagi ","sore ","mobil ","motor ","kereta ","jalan ",
    "hewan ","ikan ","burung ","kucing ","anjing ","tas ","dompet ","kamar ","taman ","pasar ",

    # 30 benda/tempat Jawa Timur
    "Surabaya ","Malang ","Batu ","Probolinggo ","Lumajang ","Jember ","Bondowoso ","Situbondo ","Banyuwangi ","Madiun ",
    "Kediri ","Blitar ","Tulungagung ","Nganjuk ","Mojokerto ","Jombang ","Sidoarjo ","Gresik ","Lamongan ","Bojonegoro ",
    "Madura ","Bangil ","Pasuruan ","Trenggalek ","Magetan ","Ngawi ","Pacitan ","Bromo ","Ijen ","Baluran ",

    # 20 kata umum Bahasa Inggris
    "apple ","water ","house ","car ","street ","friend ","school ","paper ","book ","music ",
    "light ","dark ","fast ","slow ","small ","big ","happy ","sad ","hot ","cold "
]
    else:
        return None

def arrowToWasd(text):
    for arrow, key in mapping.items():
        text = text.replace(arrow, key)
    return text

def validate(answer, user_answer):
    # panjang harus sama
    if len(answer) != len(user_answer):
        return False
    # mode impossible → case-sensitive exact match
    if difficulty == "4":
        return answer == user_answer
    # mode arrow → convert ke WASD, abaikan kapital
    if difficulty == "1":
        converted = ''.join(arrowToWasd(ch).lower() for ch in answer)
        return converted == user_answer.lower()
    # mode lain → abaikan kapital
    return answer.lower() == user_answer.lower()


def main():
    global difficulty
    global score
    global game_mode
    global unlocked_modes

    global classic_easy_highscore
    global classic_normal_highscore
    global classic_hard_highscore
    global classic_impossible_highscore
    global advanced_easy_highscore
    global advanced_normal_highscore
    global advanced_hard_highscore
    global advanced_impossible_highscore
    global extreme_easy_highscore
    global extreme_normal_highscore
    global extreme_hard_highscore
    global extreme_impossible_highscore

    load_scores()
    clear_screen()
    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
    print("║" + "🧠  COGNITIVE TRIAL: MEMORY GAME  🧠".center(INNER_WIDTH) + "║")
    print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
    print("║" + pad("Created by Puput") + "  ║")
    print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
    print("║" + pad("Pilih Mode Game:") + "  ║")
    print("║" + pad("") + "  ║")
    print("║" + pad("1. Classic") + "  ║")
    print("║" + pad("2. Advanced") + "  ║")
    print("║" + pad("3. Extreme") + "  ║")
    print("║" + pad("4. Credit") + "  ║")
    print("║" + pad("5. Keluar") + "  ║")
    print("║" + pad("") + "  ║")
    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")

    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
    print("║" + pad("Masukkan pilihan (1-5):") + "  ║")
    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")

    game_mode = input(">>> ").strip()


    
    # Check unlocked modes
    if(game_mode == "1"):
        clear_screen()
    elif(game_mode == "2" and int(unlocked_modes) < 1):
        clear_screen()
        print("╔══════════════════════════════════════════════╗")
        print("║                MODE TERKUNCI 🔒              ║")
        print("╠══════════════════════════════════════════════╣")
        print("║  Mode Advanced masih terkunci!               ║")
        print("║  Selesaikan Classic Mode terlebih dahulu.    ║")
        print("╚══════════════════════════════════════════════╝")
        input("Tekan Enter untuk kembali ke menu utama...")
        clear_screen()
        return
    elif(game_mode == "3" and int(unlocked_modes) < 2):
        clear_screen()
        print("╔══════════════════════════════════════════════╗")
        print("║                MODE TERKUNCI 🔒              ║")
        print("╠══════════════════════════════════════════════╣")
        print("║  Mode Extreme masih terkunci!                ║")
        print("║  Selesaikan Advanced Mode terlebih dahulu.   ║")
        print("╚══════════════════════════════════════════════╝")
        input("Tekan Enter untuk kembali ke menu utama...")

        clear_screen()
        return
    elif(game_mode == "4"):
        clear_screen()
        showCredits()
        input("Tekan Enter untuk kembali ke menu utama...")
    elif(game_mode == "5"):
        clear_screen()
        print("Terima kasih telah bermain!")
        exit()
    elif (game_mode not in ["1","2","3"]):
        clear_screen()
        print("Pilihan tidak valid!")
        return
    while True:
        clear_screen()
        print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
        print("║" + "🧠  COGNITIVE TRIAL: MEMORY GAME  🧠".center(INNER_WIDTH) + "║")
        print("╚" + "═" * (BOX_WIDTH - 2) + "╝")

        game_mode_text = ""
        if(game_mode == "1"):
            game_mode_text = "Classic"
        elif(game_mode == "2"):
            game_mode_text = "Advanced"
        elif(game_mode == "3"):
            game_mode_text = "Extreme"
        else:
            print("Terima kasih telah bermain!")
            break

        print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
        print("║" + pad(f"Mode Game: {game_mode_text}") + "  ║")
        print("║" + pad("Pilih tingkat kesulitan:") + "  ║")
        print("╠" + "═" * (BOX_WIDTH - 2) + "╣")

        # base text
        easytext = "1. Easy (Arah panah) - "
        normaltext = "2. Normal (Angka) - "
        hardtext = "3. Hard (Huruf) - "
        impossibletext = "4. Impossible (Kata) - "

        # highscore append
        if(game_mode == "1"):
            easytext += f"{classic_easy_highscore} (Highscore)"
            normaltext += f"{classic_normal_highscore} (Highscore)"
            hardtext += f"{classic_hard_highscore} (Highscore)"
            impossibletext += f"{classic_impossible_highscore} (Highscore)"
        elif(game_mode == "2"):
            easytext += f"{advanced_easy_highscore} (Highscore)"
            normaltext += f"{advanced_normal_highscore} (Highscore)"
            hardtext += f"{advanced_hard_highscore} (Highscore)"
            impossibletext += f"{advanced_impossible_highscore} (Highscore)"
        elif(game_mode == "3"):
            easytext += f"{extreme_easy_highscore} (Highscore)"
            normaltext += f"{extreme_normal_highscore} (Highscore)"
            hardtext += f"{extreme_hard_highscore} (Highscore)"
            impossibletext += f"{extreme_impossible_highscore} (Highscore)"

        print("║" + pad(easytext) + "  ║")
        print("║" + pad(normaltext) + "  ║")
        print("║" + pad(hardtext) + "  ║")
        print("║" + pad(impossibletext) + "  ║")
        print("║" + pad("5. Kembali ke menu utama") + "  ║")
        print("╚" + "═" * (BOX_WIDTH - 2) + "╝")

        difficulty = input("Masukkan pilihan (1-5): ").strip()


        if(difficulty == "5"):
            clear_screen()
            break
        choices = get_choices()

        if choices is None:
            print("Pilihan tidak valid!")
            return
        
        sequence = []
        score = 0
        alreadynotified = False

        while True:
            # generate sequence baru
            if(game_mode == "3"): # extreme mode: random kombinasi setiap ronde
                sequence_length = len(sequence) + 1
                sequence = [random.choice(choices) for _ in range(sequence_length)]
            else: # classic & advanced mode : menambah satu item random ke sequence
                sequence.append(random.choice(choices))

            # tampilkan sequence ke pemain
            for item in sequence:
                clear_screen()
                print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                print("║" + pad(f"Skor anda : {score}") + "  ║")
                print("║" + pad("Ingat urutan berikut:") + "  ║")
                print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
                q_top = "║" + "═" * (BOX_WIDTH - 2) + "║"

                # item (diposisikan center secara manual agar tetap responsif)
                item_line = f"{item}".center(INNER_WIDTH)
                q_middle = "║" + item_line + "  ║"
                q_down = "╚" + "═" * (BOX_WIDTH - 2) + "╝"

                output = q_top + "\n" + q_middle + "\n" + q_down
                printRandomColor(output)
                time.sleep(1)

            # hapus layar
            clear_screen()
            print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
            print("║" + pad(f"Skor anda : {score}") + "  ║")
            print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
            print("║" + pad("Masukkan ulang urutan tadi:") + "  ║")
            print("╚" + "=" * (BOX_WIDTH - 2) + "╝")
            if(game_mode == "1"):
                # classic mode: waktu bertambah sesuai panjang sequence + 60 detik + 10 detik
                answer = timed_input(">> ", game_timer + len(sequence) + 10)
            elif(game_mode == "2"):
                # advanced mode : waktu panjang sequence + 10 detik
                answer = timed_input(">> ", len(sequence) + 10)
            elif(game_mode == "3"):
                # extreme mode : waktu panjang sequence + 2 detik
                answer = timed_input(">> ", len(sequence) + 10)

            clear_screen()

            # jika waktu habis
            if(answer is None):
                print()
                print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                print("║" + pad("Waktu habis! Permainan berakhir.") + "  ║")
                print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                if difficulty == "1":
                    correct_wasd = arrowToWasd("".join(sequence))
                    print(f"Urutan yang benar (WASD): {correct_wasd}")
                correct_seq = ("".join(sequence)).lower()
                print(f"Urutan yang benar: {correct_seq}")
                print(f"Skor Akhir: {score}")
                print("═" * (BOX_WIDTH))
                print("Tekan Enter 2x untuk kembali ke menu") # seharusnya 1x, tapi karena timed_input pakai threading, perlu 2x
                input()
                clear_screen()
                break

            # validasi jawaban
            if (validate("".join(sequence).strip(),answer.strip())):

                # score modifier
                score += 1
                if(game_mode == "2"): # advanced mode tambahan score
                    score += 5
                elif(game_mode == "3"): # extreme mode tambahan score lebih banyak
                    score += 10
                if(difficulty == "2"): # normal
                    score += 2
                elif(difficulty == "3"): # hard
                    score += 4
                elif(difficulty == "4"): # impossible
                    score += 10
                
                # simpan skor tertinggi
                if(game_mode == "1"): # classic
                    if(difficulty == "1" and score > classic_easy_highscore):
                        classic_easy_highscore = score
                    elif(difficulty == "2" and score > classic_normal_highscore):
                        classic_normal_highscore = score
                    elif(difficulty == "3" and score > classic_hard_highscore):
                        classic_hard_highscore = score
                    elif(difficulty == "4" and score > classic_impossible_highscore):
                        classic_impossible_highscore = score
                elif(game_mode == "2"): # advanced
                    if(difficulty == "1" and score > advanced_easy_highscore):
                        advanced_easy_highscore = score
                    elif(difficulty == "2" and score > advanced_normal_highscore):
                        advanced_normal_highscore = score
                    elif(difficulty == "3" and score > advanced_hard_highscore):
                        advanced_hard_highscore = score
                    elif(difficulty == "4" and score > advanced_impossible_highscore):
                        advanced_impossible_highscore = score
                elif(game_mode == "3"): # extreme
                    if(difficulty == "1" and score > extreme_easy_highscore):
                        extreme_easy_highscore = score
                    elif(difficulty == "2" and score > extreme_normal_highscore):
                        extreme_normal_highscore = score
                    elif(difficulty == "3" and score > extreme_hard_highscore):
                        extreme_hard_highscore = score
                    elif(difficulty == "4" and score > extreme_impossible_highscore):
                        extreme_impossible_highscore = score
                save_score()

                
                # Unlock next gamemode advanced
                if(score >= 70 and game_mode == "1" and difficulty == "4" and not alreadynotified and int(unlocked_modes) < 1):
                    clear_screen()
                    unlocked_modes = "1"
                    save_score()
                    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                    print("║" + pad("🔓 Selamat! Anda telah membuka mode Advanced! 🔓") + "║")
                    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                    input("Tekan Enter untuk melanjutkan permainan...")
                    alreadynotified = True
                    clear_screen()
                # Unlock next gamemode extreme
                if(score >= 90 and game_mode == "2" and difficulty == "4" and not alreadynotified and int(unlocked_modes) < 2):
                    clear_screen()
                    unlocked_modes = "2"
                    save_score()
                    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                    print("║" + pad("🔓 Selamat! Anda telah membuka mode Extreme! 🔓") + "║")
                    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                    input("Tekan Enter untuk melanjutkan permainan...")
                    alreadynotified = True
                    clear_screen()
                # EASTER EGG : jika skor 125 di mode extreme impossible
                if(score >= 125 and game_mode == "3" and difficulty == "4" and not alreadynotified):
                    clear_screen()
                    unlocked_modes = "3"
                    alreadynotified = True
                    save_score()
                    print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                    print("║" + pad("🎉 Selamat! Anda menemukan Easter Egg! 🎉") + "║")
                    print("╠" + "═" * (BOX_WIDTH - 2) + "╣")
                    print("║" + pad("Skor Anda telah mencapai 125 di mode Extreme - Impossible!") + "  ║")
                    print("║" + pad("Anda adalah Master of Memory sejati!") + "  ║")
                    print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                    showCredits()
                    input("Tekan Enter untuk melanjutkan permainan...")
                    clear_screen()
                
                print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                print("║" + pad("Benar! Lanjut ke ronde berikutnya...") + "  ║")
                print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                time.sleep(1.2)
            else:
                save_score()
                print()  
                print("╔" + "═" * (BOX_WIDTH - 2) + "╗")
                print("║" + pad("❌ Salah! Permainan berakhir.") + " ║")
                print("╚" + "═" * (BOX_WIDTH - 2) + "╝")
                print(f"Jawaban Anda : {answer}")
                if difficulty == "1":
                    correct = arrowToWasd("".join(sequence))
                    print(f"Urutan yang benar (WASD): {correct}")
                else:
                    correct = "".join(sequence)
                    if difficulty != "4":
                        correct = correct.lower()
                    print(f"Urutan yang benar: {correct}")
                print(f"Skor Akhir: {score}")
                print("═" * (BOX_WIDTH))
                input("Tekan Enter untuk kembali ke menu utama...")

                clear_screen()
                break

if __name__ == "__main__":
    while True:
        main()
