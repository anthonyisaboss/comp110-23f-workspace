"""Dictionary practice."""

ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")


   

ice_cream["vanilla"] += 2
print(ice_cream)
print(ice_cream["chocolate"])

print(f"there are {ice_cream['chocolate']} orders of chocolate")\

print(len(ice_cream))

print("mint" in ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint.")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")