import hashlib
import time

# Hedef hash (SHA-256 ile hash'lenmiş 5 karakterli mesaj)
TARGET_HASH = "aa72ae411ae8b267df8b6bf5e97ecfe81ba990b2e7d0dd2650a17c9210cb0a97"

# Kullanılan alfabe
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
ALPHABET_LENGTH = len(ALPHABET)
MESSAGE_LENGTH = 5  # Mesajlar 5 karakter uzunluğunda
TOTAL_COMBINATIONS = ALPHABET_LENGTH ** MESSAGE_LENGTH  # 36^5 = 60,466,176

def number_to_word(number: int, alphabet: str, length: int) -> str:
    """Bir sayıyı verilen alfabeye göre string'e çevirir."""
    base = len(alphabet)
    word = ""
    for _ in range(length):
        word = alphabet[number % base] + word
        number //= base
    return word

def brute_force_sha256(target_hash: str) -> str | None:
    """Verilen SHA-256 hash'i brute force yöntemiyle çözmeye çalışır."""
    print(f"Toplam kombinasyon sayısı: {TOTAL_COMBINATIONS}")
    start_time = time.time()

    for num in range(TOTAL_COMBINATIONS):
        message = number_to_word(num, ALPHABET, MESSAGE_LENGTH)
        hashed = hashlib.sha256(message.encode()).hexdigest()

        if hashed == target_hash:
            elapsed = time.time() - start_time
            print(f"{num} denemede bulundu. Süre: {elapsed:.2f} saniye.")
            return message

        if num % 1_000_000 == 0:
            print(f"{num} kombinasyon denendi...")

    return None

# Programı çalıştır
if __name__ == "__main__":
    result = brute_force_sha256(TARGET_HASH)
    if result:
        print(f"✅ Hash çözüldü! Mesaj: {result}")
    else:
        print("❌ Uygun mesaj bulunamadı.")
