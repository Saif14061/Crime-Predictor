from sklearn.linear_model import LinearRegression
import pandas as pd
def predict_machine():
    df = pd.read_csv("data_crime.csv")

    monthly_crime = df.groupby("month")["id"].count()
    print(monthly_crime)

    monthly_crime = monthly_crime.reset_index()
    monthly_crime["month_num"] = monthly_crime["month"].factorize()[0]
    x = monthly_crime[["month_num"]]
    y = monthly_crime["id"]

    model = LinearRegression()

    model.fit(x,y)

    prediction = model.predict([[1]])
    return prediction[0]
