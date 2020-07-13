from gtts import gTTS
import vlc  # pip3 install python-vlc


ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
hundred = ['hundred', 'hundred and ', 'one thousand']


def writez(n):
    """Функция принимает число цифрой, а возвращает строкой"""
    n = int(n)
    if n < 20:
        n = ones[n]
    elif n == 1000:
        n = hundred[2]
    elif n < 100:
        n = twenties[n // 10] + ones[n % 10]
    elif 99 < n < 1000:
        if n % 100 == 0:
            n = ones[n // 100] + hundred[0]
        else:
            if n % 100 < 20:
                n = ones[n // 100] + hundred[1] + ones[n % 100]
            else:
                n = ones[n // 100] + hundred[1] + twenties[n % 100 // 10] + ones[n % 100 % 10]

    return n


def speak():
    '''Функция запрашивает числа, передает их в функци writez которая их возвращает в текстовом варианте.
    Затем функция сохраняет и воспроизводит их. Если делать без прописи текстом тогда функци writez можно упустить'''
    while True:
        n = input('Введите число цифрами >>')
        if n.isdigit(): # Проверяем ввел ли пользователь число.
            k = writez(n)
            sp = gTTS(text=f'{k}')
        else:
            k = 'Нужно ввести число!'
            sp = gTTS(text=f'{k}', lang='ru')

        sp.save('1.mp3') #
        music = vlc.MediaPlayer('1.mp3')
        music.play()
        print(k)


if __name__ == '__main__':
    speak()
