import numpy as np

U_0 = np.array([[6], [0], [3], [6]])  # Initial U (4x1)
V_0 = np.array([[4, 2, 1]])  # V (1x3)

Y = np.array([
    [5, np.nan, 7],
    [np.nan, 2, np.nan],
    [4, np.nan, np.nan],
    [np.nan, 3, 6]
])

lambda_reg = 1

VTV = V_0 @ V_0.T  # (1x3) @ (3x1) = (1x1)
I = np.eye(VTV.shape[0])  # Identity matrix

inv_term = np.linalg.inv(VTV + lambda_reg * I)

Y_filled = np.nan_to_num(Y)  # Replace NaNs with 0 for the update

U_1 = (Y_filled @ V_0.T) @ inv_term

print(U_1.flatten().tolist())
