import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic" # 윈도우는 Malgun Gothic

prices = [68500, 71800, 73100, 75700, 71400]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices) :
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
                xytext=(0, 8), ha="center")

ax.set_title("두산 로보틱스 주가(10월 초)")
fig.savefig("my_first_chart.png")