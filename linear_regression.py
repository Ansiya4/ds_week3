def linearreg_OLS(x,y):
    n = len(x)
    mean_x= sum(x)/n
    mean_y= sum(y)/n

    numerator = 0
    denominator = 0
    for i in range(n):
        numerator+=(x[i]-mean_x)*(y[i]-mean_y)
        denominator += (x[i]-mean_x)**2
    
    coefficient = numerator/denominator
    intercept = mean_y - coefficient*mean_x

    return coefficient, intercept

def predict(coefficient,intercept,X):
    predictions = [coefficient*x + intercept for x in X]
    return predictions

x = [1,2,3,4,5]
y = [2,4,5,4,5]

coefficient, intercept = linearreg_OLS(x, y)
print (coefficient,intercept)
test_data = [6, 7, 8]
predictions = predict(coefficient, intercept, test_data)
print(predictions)