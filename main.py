MOON_WEIGHT_RATIO = 0.165
ANNUAL_GROWTH = 0.5
current_earth_weight = float(input("请输入你当前在地球上的体重(kg): "))
print("\n未来10年地球和月球上的体重变化:")
print("年份\t地球体重(kg)\t月球体重(kg)")
print("-------------------------------------")
for year in range(10):
    earth_weight = current_earth_weight + year * ANNUAL_GROWTH
    moon_weight = earth_weight * MOON_WEIGHT_RATIO
    print(f"{year+1}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
