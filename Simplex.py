from scipy.optimize import linprog

c = [-60, -50]  
A = [
    [2, 4], 
    [3, 2]   
] 

b = [100, 90]

x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if res.success:
    print(f"Number of units of Product A to produce: {res.x[0]:.2f}")
    print(f"Number of units of Product B to produce: {res.x[1]:.2f}")
    print(f"Maximum Profit: ₹{-res.fun:.2f}")
else:
    print("No solution found!")