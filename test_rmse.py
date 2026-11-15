from sklearn.metrics import root_mean_squared_error

actual = [80, 75, 90, 65]

predicted = [82, 74, 88, 67]

score = root_mean_squared_error(
    actual,
    predicted
)

print("RMSE:", score)