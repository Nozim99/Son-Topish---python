import random as r

print("Keling o'ylagan sonni topish o'ynaymiz!")


# Xabar yaratuvchi funksiya
def create_message(number_of_attemps, user_number_of_attemps):

    # Xabarni bir qismi
    message_text = f"Men {number_of_attemps} urinishda Siz esa {user_number_of_attemps} urinishda topdingiz. "

    # Urinishlar farqiga qarab xabar to'liq yoziladi
    if number_of_attemps > user_number_of_attemps:
        message_text += "Siz yutdingiz!"
    elif number_of_attemps < user_number_of_attemps:
        message_text += "Men yutdim!"
    else:
        message_text += "Durrang bo'ldi!"
    print(message_text)


# User o'ylagan sonni topadigan funksiya
def find_user_number(user_number_of_attemps):
    # User'ni son o'ylab olishi uchun vaqt beriladi. Enter bosilsa o'yin boshlanadi
    input("\nEndi siz 0 dan 10 gacha son o'ylang. Tayyor bo'lsangiz \"Enter\"ni bosing")

    # Kompyuter javobni tezroq topishi uchun min va max qiymatlari saqlanib boradi
    min_number = 0  # Tahmin qilingan son saqlanadi agar kichik bo'lsa
    max_number = 11  # Tahmin qilingan son saqlanadi agar katta bo'lsa

    # Kompyuter tahmin qilgan son
    my_value = r.choice(range(min_number, max_number))

    # Urinishlar soni
    number_of_attemps = 0

    # User o'ylagan son topilmaguncha loop ishlaydi
    while True:
        # Har safan son tahmin qilinganda urunishlar soni bitta oshib boradi
        number_of_attemps += 1

        # Kompyuterni tahmini to'g'riligini user'dan so'raladi
        is_my_value_true = input(
            f"{my_value} sonini o'ylagansiz. Topdimmi? > ha(1)/yo'q(0): "
        )

        if is_my_value_true != "1":
            # Kompyuter tahmini hato bo'lsa va 1 ta variant qolgan bo'lsa user'dan to'g'riligini so'ramasdan to'g'ri javobini topish
            if max_number - min_number < 3:
                current_value = max_number - 1 if my_value == min_number else min_number
                print(f"\n\nTopdim! Siz o'ylagan son: >>> {current_value} <<<")
                create_message(number_of_attemps + 1, user_number_of_attemps)
                break

            # Kompyuter kiritgan qiymat eng katta qiymat bo'lsa user'dan katta yoki kichikligini so'ramasdan tahmin qilishni davom etadi
            if my_value == max_number - 1:
                max_number = my_value
                my_value = r.choice(range(min_number, max_number))

            # Kompyuter kiritgan qiymat eng kichik qiymat bo'lsa user'dan katta yoki kichikligini so'ramasdan tahmin qilishni davom etadi
            elif my_value == min_number:
                min_number = my_value + 1
                my_value = r.choice(range(min_number, max_number))
            else:
                my_value_difference = input("Men o'ylagan son kattami? ha(1)/yo'q(0): ")

                # Kompyuter kiritgan son katta bo'lsa ishlaydi
                if my_value_difference == "1":
                    max_number = my_value
                    my_value = r.choice(range(min_number, my_value))

                    # Agar 1 ta variant qolgan bo'lsa javobini ko'rsatish
                    if max_number - min_number == 1:
                        print(f"\n\nTopdim! Siz o'ylagan son: >>> {min_number} <<<")
                        create_message(number_of_attemps + 1, user_number_of_attemps)
                        break

                # Kompyuter kiritgan son kichik bo'lsa ishlaydi
                else:
                    min_number = my_value + 1
                    my_value = r.choice(range(min_number, max_number))

                    # Agar 1 ta variant qolgan bo'lsa javobini ko'rsatish
                    if max_number - min_number == 1:
                        print(f"\n\nTopdim! Siz o'ylagan son: >>> {min_number} <<<")
                        create_message(number_of_attemps + 1, user_number_of_attemps)
                        break

        # Kompyuter to'g'ri javobni topadi va loop tugaydi
        else:
            create_message(number_of_attemps, user_number_of_attemps)
            break


def find_my_number():
    random_num = r.choice(range(11))  # Kompyuter o'ylagan son
    user_number_of_attemps = 0  # User'ni urunishlari hisoblanib boradi

    # User'ni birinchi kiritgan soni
    user_value = int(input("0 dan 10 gacha son o'yladim! O'ylagan sonimni toping: "))

    # User to'g'ri javob topmaguncha ishlaydigan sikl
    while True:
        user_number_of_attemps += 1  # User'ni har urinishida bittaga oshib boradi

        # Katta son kiritilganda bajariladigan shart
        if user_value > random_num:
            user_value = int(input("Katta son kiritdingiz! O'ylagan sonimni toping: "))

        # Kichik son kiritilganda bajariladigan shart
        elif user_value < random_num:
            user_value = int(input("Kichik son kiritdingiz! O'ylagan sonimni toping: "))

        # To'g'ri javob topilsa bajariladigan shart
        else:
            print(f"Siz {user_number_of_attemps} urunishda topdingiz")
            break

    # User'ni o'ylagan sonini topish
    find_user_number(user_number_of_attemps)

    # O'yinni qayta o'ynamoqchiligini so'raladi
    play_again = input("Yana o'ynashni istaysizmi? ha(1)/yo'q(0): ")

    # Agar qayta o'ynashni istasa funksiyani qayta ishga tushiramiz
    if play_again == "1":
        find_my_number()


# O'yinni boshlash
find_my_number()
