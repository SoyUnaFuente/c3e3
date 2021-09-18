
score = int(input("Enter your score: "))

# if score in range(1, 51):
#     print (f"There is no prize for {score}")


if 1 <= score <=50:
    print (f"There is no prize for {score}")
elif 51 <= score <=150:
    medal = "Bronze"
    print(f"Congratulations, you won the {medal} medal for having {score} points ")
elif 151 <= score <=180:
    medal = "Silver"
    print(f"Congratulations, you won the {medal} medal for having {score} points ")
elif 181 <= score <=200:
    medal = "Gold"
    print(f"Congratulations, you won the {medal} medal for having {score} points ")