from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Maximize_Production", LpMaximize)

x = LpVariable("Lemonade", lowBound=0, cat="Integer")
y = LpVariable("FruitJuice", lowBound=0, cat="Integer")

model += x + y, "Total_Production"

model += 2 * x + y <= 100, "Water_Constraint"
model += x <= 50, "Sugar_Constraint"
model += x <= 30, "LemonJuice_Constraint"
model += 2 * y <= 40, "FruitPuree_Constraint"

model.solve()

print("Optimal Production Plan:")
print(f"Lemonade: {x.varValue}")
print(f"Fruit Juice: {y.varValue}")
print(f"Total Products: {x.varValue + y.varValue}")
