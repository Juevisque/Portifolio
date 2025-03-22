import pandas as pd

df = pd.DataFrame(
    {
        "Name":[
            "Gabriel Peixoto",
            "Rafael Matos",
            "Vitoral Tista"
        ],
        "Age":[15,15,16],
        "Sex":["male","male","male"]
    }
)

ages = pd.Series([15,15,16],name="Age")
print(ages)