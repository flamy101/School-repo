seasons = {
    "winter": ["december", "january", "february"],
    "spring": ["march", "april", "may"],
    "summer": ["june", "july", "august"],
    "autumn": ["september", "october", "november"],
}

months = [
    "january", "february", "march",
    "april", "may", "june",
    "july", "august", "september",
    "october", "november", "december"
]

res_month = ""
res_season = ""
month_num = int(input("Enter month number 1-12: "))

if 1 <= month_num <= 12:
    month = months[month_num - 1]

    for season, months in seasons.items():
        if month in months:
            res_month = month
            res_season = season
    print(f"\nThe month '{res_month}' is in season: {res_season}.")
else:
    print(f"\nEntered value is invalid. Pleace enter value between 1-12.\n")

