import pandas as pd
import keras
from sklearn.pipeline import Pipeline
from transform import FullPipeline, AttributeSelector, CustomBinarizer
from tensorflow.keras.models import load_model

model = load_model("model.hdf5")


#3,4,sep,sun,89.6,84.1,714.3,5.7,23.8,35,3.6,0,5.18
observations = {
            "X": 3,
            "Y": 4,
            "month": "sep", 
            "day": "sun",
            "FFMC": 89.6,
            "DMC": 84.1,
            "DC": 714.3,
            "ISI": 5.7,
            "temp": 23.8,
            "RH": 35,
            "wind": 3.6,
            "rain": 0
        }

df = pd.DataFrame([observations], columns=observations.keys())    
pipeline = FullPipeline()
data_prepared = pipeline.prepare_data(df)
print(data_prepared[0][: len(data_prepared) - 2])

prediction = {'area': model.predict(data_prepared[0][: len(data_prepared) - 2])[0]}
print(prediction)