import datetime, time, locale

x = datetime.datetime.now()
seconds = time.time()

s_seconds = "{:.2e}".format(seconds)
c_seconds = "{:,.4f}".format(seconds)

day = x.strftime("%d")
month = x.strftime("%b")
year = x.strftime("%Y")
print(f"Seconds since January 1, 1970: {c_seconds} or {s_seconds} in scientific notation")
print(f"{month} {day} {year}")

