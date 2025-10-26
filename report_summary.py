total_ok = 0
total_ng = 0

for i in range(1,4):
    count_ok = int(input("良品個数を入力してください："))
    total_ok = total_ok + count_ok
    count_ng = int(input("不良個数を入力してください："))
    total_ng = total_ng + count_ng

print(f"良品個数：{total_ok}  平均個数：{total_ok/3:.1f}  良品率：{total_ok/(total_ng+total_ok)*100:.2f}%")
