import random
import os
import time
import threading

# Global Variable
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

game_timer = 60 # default 60 seconds

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

    filename = f"scores.txt"
    with open(filename, "w") as file: # overwrite
        file.write(f"{classic_easy_highscore}|{classic_normal_highscore}|{classic_hard_highscore}|{classic_impossible_highscore}|{advanced_easy_highscore}|{advanced_normal_highscore}|{advanced_hard_highscore}|{advanced_impossible_highscore}|{extreme_easy_highscore}|{extreme_normal_highscore}|{extreme_hard_highscore}|{extreme_impossible_highscore}")

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

    filename = f"scores.txt"
    if not os.path.exists(filename):
        return  # file tidak ada, lewati
    with open(filename, "r") as file:
        data = file.read().strip().split("|")
        if len(data) == 12:
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
    print("=== Cognitive Trial: A Memory Game ===\n\n")
    print("Pilih Mode Game:")
    print("1. Classic")
    print("2. Advanced")
    print("3. Extreme")
    print("4. Keluar")
    game_mode = input("Masukkan pilihan (1-4): ").strip()
    
    while True:
        clear_screen()
        print("=== Cognitive Trial: A Memory Game ===\n\n")
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
        print("Mode Game:", game_mode_text)
        print("Pilih tingkat kesulitan:")

        easytext = "1. Easy (Arah panah)\t"
        normaltext = "2. Normal (Angka)\t"
        hardtext = "3. Hard (Huruf)\t\t"
        impossibletext = "4. Impossible (Kata)\t"

        # tampilkan skor tertinggi sesuai mode
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

        print(easytext)
        print(normaltext)
        print(hardtext)
        print(impossibletext)
        print(f"5. Kembali ke menu utama")
        
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

        while True:
            if(game_mode == "3"): # extreme mode: random kombinasi setiap ronde
                sequence_length = len(sequence) + 1
                sequence = [random.choice(choices) for _ in range(sequence_length)]
            else: # classic & advanced mode : menambah satu item random ke sequence
                
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
                print("\nWaktu habis! Permainan berakhir.")
                if(difficulty == "1"):
                    print("Urutan yang benar (WASD): ", arrowToWasd("".join(sequence)))
                print("Urutan yang benar: ", ("".join(sequence)).lower())
                print("Skor Akhir:", score)
                input("Tekan Enter untuk kembali ke menu utama")
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

                print("Benar! Lanjut ke ronde berikutnya...")
                time.sleep(1)
            else:
                print("\nSalah! Permainan berakhir.")
                print("Jawaban Anda: ", answer)
                if(difficulty == "1"):
                    print("Urutan yang benar (WASD): ", arrowToWasd("".join(sequence)))
                
                if(difficulty == "4"):
                    print("Urutan yang benar: ", ("".join(sequence)))
                else:
                    print("Urutan yang benar: ", ("".join(sequence)).lower())
                print("Skor Akhir:", score)
                input("Tekan Enter untuk kembali ke menu utama")
                clear_screen()
                break

if __name__ == "__main__":
    while True:
        main()
