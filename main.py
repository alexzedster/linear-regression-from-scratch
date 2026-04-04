import numpy as np

# просто на Дом клик посмотрел короче цены на 2 комнатные квартиры в моем городе x-кв метров y-цена
x_in = np.array([59, 66, 65, 53, 56, 54, 70, 60, 45, 59, 63])
y_in = np.array([7900000, 12700000, 8902000, 4170000, 7061000, 6600000, 7600000, 6300000, 5350000, 7800000, 6700000])

# нормирую данные
norm_x = x_in/np.max(x_in)
norm_y = y_in/np.max(y_in)

def J_wb(w, b, x_input, y_input):
    cost = 0
    m = x_input.shape[0]
    for i in range(m):
        f_wb = w*x_input[i]+b
        cost+= pow((f_wb - y_input[i]),2)
    total_cost = (1/(2*m)) * cost
    return total_cost

def GradientComputing(w, b, x, y):
    m = x.shape[0]
    dw = 0
    db = 0
    for i in range(m):
        f_wb = w*x[i]+b
        dw_i = ((f_wb - y[i])*x[i])
        db_i = (f_wb - y[i])
        dw += dw_i
        db += db_i
    dw = dw/m
    db = db/m

    return dw, db

def GradientDescent(w, b , x, y ,alpha,max_iter):
    epsilon = 1e-4
    dw, db = GradientComputing(w, b, x, y)
    counter = 0
    while (abs(dw) > epsilon or abs(db) > epsilon) and counter < max_iter:
        w = w - alpha*dw
        b = b - alpha*db
        if counter%10000 == 0:
            print(f"Номер операции: {counter}")
            print(f"Ошибка: {J_wb(w,b,x,y)}")
            print(f"Значение w: {w} Значение b: {b} \n")
        dw, db = GradientComputing(w, b ,x, y)
        counter+=1
    return w, b


def Prediction(x, x_i, y_i, w_norm, b_norm):
    x_norm = x/ np.max(x_i)
    y_norm = w_norm*x_norm + b_norm
    y = y_norm*np.max(y_i)
    return y


alpha_temp = 1e-2
w_temp = 0
b_temp = 0
temp_iter = 100000

square_meters  = 40


w_final, b_final = GradientDescent(w_temp, b_temp, norm_x, norm_y, alpha_temp, temp_iter)
print(f"\nФинальные значения w и b: {w_final}, {b_final}")

cost_of_apartment = int(Prediction(square_meters, x_in, y_in, w_final,b_final))
print(f"\nПримерная Цена квартиры в {square_meters} м^2: {cost_of_apartment:}₽.")
