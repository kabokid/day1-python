#-----------------------------
#ユーザーの気分に合わせて、英語で返す小悪魔ミコト風メッセージを出すプログラム 
#-----------------------------
def check_mood(mood):
    if mood == "happy":
        print("\nyou look too cute when you smile!\n")
    elif mood == "sad":
        print("\nAww,don't cry~ you'll ruin your pretty face.\n")
    elif mood == "angry":
        print("\nOoh, fiely! I like that passion.\n")
    else:
        print("\nMmm, mysterious mood… tell me more?\n")

mood_input = input("How are you feeling today?:")
check_mood(mood_input)
