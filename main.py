current_weight = float(input("请输入你当前的体重(kg): "))
moon_gravity_percent = 16.5
annual_gain = 0.5
print(f"\n未来10年你的体重变化 (当前体重: {current_weight}kg)")
print("=" * 50)
print(f"{'年份':<10}{'地球体重(kg)':<20}{'月球体重(kg)':<20}")
print("-" * 50)
for year in range(10):
     earth_weight = current_weight + annual_gain * year
     moon_weight = earth_weight * (moon_gravity_percent / 100)
     print(f"{year+1:<10}{earth_weight:<20.2f}{moon_weight:<20.2f}")
