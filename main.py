current_earth_weight=float(input("请输入你当前在地球上的体重（kg):"))
moon_ratio=0.165
annual_gain=0.510
years=10
print ("未来10年地球和月球体重变化:")
for year in range (1,years +1):
     earth_weight=current_earth_weight+annual_gain*year\
     moon_weight=earth_weight*moon_ratio
     print (f"第｛year｝年:地球上体重{earth_weight:.2f}kg,月球上体重{moon_weight:.2f}kg")

