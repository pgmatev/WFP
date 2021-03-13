from numpy.core.records import array
import pandas as pd
import numpy as np
import pickle
import keras
from sklearn.pipeline import Pipeline
from transform import FullPipeline, AttributeSelector, CustomBinarizer
from tensorflow.keras.models import load_model

modelArea = load_model("models/model-area.hdf5")
modelCoef = pickle.load(open('./models/model-coef.pkl','rb'))


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

test = data_prepared.tolist()

test[0].pop()
test[0].pop()
test = np.array(test)

#prediction = {'area': model.predict(test)[0]}
print(modelArea.predict(test)[0])

#temp, oxygen, humidity
coef = [36, 21, 10]
final=[np.array(coef)]

prediction=modelCoef.predict_proba(final)
output='{0:.{1}f}'.format(prediction[0][1], 2)
print(output)