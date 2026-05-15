# Calculates the average (mean) of a list of numbers
def mean(x):
    total = 0
    for i in x:
        total += i
    return total / len(x)

# Subtracts the mean from each value in the list (centers the data)
def subtract_mean(values, avg):
    result = []
    for i in values:
        result.append(i - avg)
    return result


# Multiplies two lists element-by-element and returns their total sum (AB)
def dot_product(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


# Squares each value in the list and returns their total sum
def sum_of_squares(values):
    total = 0
    for i in values:
        total += i ** 2
    return total


# Calculates predicted y values using the line equation: y = w1*x + w0
def prediction(x, w1, w0):
    y_pred = []
    for i in x:
        y_pred.append(round(w1 * i + w0, 2))
    return y_pred


# Returns squared error (y - y_pred)^2 for each data point
def error_list(y, y_pred):
    errors = []
    for i in range(len(y)):
        errors.append((y[i] - y_pred[i]) ** 2)
    return errors


# Returns the total sum of a list of numbers
def total_sum(values):
    total = 0
    for i in values:
        total += i
    return total

# Prints squared error breakdown for each data point
def error_print(y, y_pred):
    for i in range(len(y)):
        z = (y[i] - y_pred[i]) ** 2
        print(f"(Y:{y[i]} - y_pred:{y_pred[i]})^2 = {round(z, 2)}")

# Generates slope (w1) using Lasso Regression
# Generates slope (w1) using Lasso Regression
def lasso_w1(a, b, alpha):

    omega = dot_product(a, b)

    numerator = max(0, abs(omega) - alpha)

    # restore sign
    if omega < 0:
        numerator = -numerator

    denominator = sum_of_squares(a)

    w1 = numerator / denominator

    return w1

# Main function of linear regression
def linear_regression(x, y):
    avg_x = mean(x)
    avg_y = mean(y)

    a = subtract_mean(x, avg_x)   # x - x_mean
    b = subtract_mean(y, avg_y)   # y - y_mean

    w1 = dot_product(a, b) / sum_of_squares(a)   # slope
    w0 = avg_y - w1 * avg_x                       # intercept

    y_pred = prediction(x, w1, w0)
    errors = error_list(y, y_pred)
    total_error = total_sum(errors)

    print(f"w0: {w0}")
    print(f"w1: {w1}")
    print(f"Input: {x}")
    print(f"Actual Output: {y}")
    print(f"Predicted Value: {y_pred}")
    error_print(y, y_pred)
    print(f"Error: {total_error}")
    print(f"Avg Error: {total_error / len(x)}")

# Runs lasso regression for multiple alpha values
def linear_regression_lasso(x, y, alphas):

    avg_x = mean(x)
    avg_y = mean(y)

    a = subtract_mean(x, avg_x)
    b = subtract_mean(y, avg_y)

    for alpha in alphas:

        w1 = lasso_w1(a, b, alpha)

        w0 = avg_y - w1 * avg_x

        y_pred = prediction(x, w1, w0)

        errors = error_list(y, y_pred)

        total_error = total_sum(errors)

        print("\n========================")
        print(f"Alpha: {alpha}")
        print(f"w1: {round(w1,4)}")
        print(f"w0: {round(w0,4)}")
        print(f"Total Error: {round(total_error,2)}")
        print(f"Avg Error: {round(total_error/len(x),2)}")

x = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7,
     8, 8.5, 9, 10, 11, 12, 13, 14, 15, 16,
     17, 17.5, 18, 19, 19.5, 20, 21, 21.5, 22, 23,
     23.5, 24, 25, 25.5, 26, 27, 27.5, 28, 29, 29.5,
     30, 31, 31.5, 32, 33, 33.5, 34, 35, 35.5, 36,
     37, 37.5, 38, 39, 39.5, 40, 41, 41.5, 42, 43,
     43.5, 44, 45, 45.5, 46, 47, 47.5, 48, 49, 49.5,
     50, 51, 51.5, 52, 53, 53.5, 54, 55, 55.5, 56,
     57, 57.5, 58, 59, 59.5, 60, 61, 61.5, 62, 63,
     63.5, 64, 65, 65.5, 66, 67, 67.5, 68, 69, 69.5]
y = [35, 40, 42, 45, 50, 52, 55, 60, 63, 65,
     70, 72, 75, 78, 82, 85, 88, 90, 93, 95,
     100, 102, 105, 108, 110, 112, 115, 118, 120, 123,
     125, 128, 130, 133, 135, 138, 140, 143, 145, 148,
     150, 153, 155, 158, 160, 163, 165, 168, 170, 173,
     175, 178, 180, 183, 185, 188, 190, 193, 195, 198,
     200, 203, 205, 208, 210, 213, 215, 218, 220, 223,
     225, 228, 230, 233, 235, 238, 240, 243, 245, 248,
     250, 253, 255, 258, 260, 263, 265, 268, 270, 273,
     275, 278, 280, 283, 285, 288, 290, 293, 295, 298]


print(linear_regression(x,y))
alphas = [0, 0.5, 1, 1.5, 2, 2.5]

linear_regression_lasso(x, y, alphas)

