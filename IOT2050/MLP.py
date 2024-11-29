from sklearn.neural_network import MLPClassifier
import pandas as pd
import statistics
import joblib

df = pd.read_csv('Data.csv')

dfExtract = []
Speed = []
auxC1 = []
auxC2 = []
auxC3 = []
auxT1 = []
auxT2 = []
auxT3 = []
auxP1 = []
auxP2 = []
auxP3 = []
auxOV1 = []
auxOV2 = []
auxOV3 = []
auxAV1 = []
auxAV2 = []
auxAV3 = []

inc = 100  #100 = 0.1s  || 1000 = 1s
for i in range(0,len(df),inc):
  if len(df)>i+inc:
    aux_1=statistics.mean(df.Speed[i:i+inc])
    Speed.append(aux_1)

    aux_1=statistics.mean(df.Current[i:i+inc])
    auxC1.append(aux_1)
    aux_1=statistics.stdev(df.Current[i:i+inc])
    auxC2.append(aux_1)
    aux_1=statistics.variance(df.Current[i:i+inc])
    auxC3.append(aux_1)

    aux_1=statistics.mean(df.Torque[i:i+inc])
    auxT1.append(aux_1)
    aux_1=statistics.stdev(df.Torque[i:i+inc])
    auxT2.append(aux_1)
    aux_1=statistics.variance(df.Torque[i:i+inc])
    auxT3.append(aux_1)

    aux_1=statistics.mean(df.PowerFactor[i:i+inc])
    auxP1.append(aux_1)
    aux_1=statistics.stdev(df.PowerFactor[i:i+inc])
    auxP2.append(aux_1)
    aux_1=statistics.variance(df.PowerFactor[i:i+inc])
    auxP3.append(aux_1)

    aux_1=statistics.mean(df.OutputVoltage[i:i+inc])
    auxOV1.append(aux_1)
    aux_1=statistics.stdev(df.OutputVoltage[i:i+inc])
    auxOV2.append(aux_1)
    aux_1=statistics.variance(df.OutputVoltage[i:i+inc])
    auxOV3.append(aux_1)

    aux_1=statistics.mean(df.ActualVoltage[i:i+inc])
    auxAV1.append(aux_1)
    aux_1=statistics.stdev(df.ActualVoltage[i:i+inc])
    auxAV2.append(aux_1)
    aux_1=statistics.variance(df.ActualVoltage[i:i+inc])
    auxAV3.append(aux_1)

dfExtract = pd.DataFrame(Speed,columns=['Speed'])
dfExtract['mean_Current'] = pd.DataFrame(auxC1)
dfExtract['stdev_Current'] = pd.DataFrame(auxC2)
dfExtract['variance_Current'] = pd.DataFrame(auxC3)
dfExtract['mean_Torque'] = pd.DataFrame(auxT1)
dfExtract['stdev_Torque'] = pd.DataFrame(auxT2)
dfExtract['variance_Torque'] = pd.DataFrame(auxT3)
dfExtract['mean_PowerFactor'] = pd.DataFrame(auxP1)
dfExtract['stdev_PowerFactor'] = pd.DataFrame(auxP2)
dfExtract['variance_PowerFactor'] = pd.DataFrame(auxP3)
dfExtract['mean_OutputVoltage'] = pd.DataFrame(auxOV1)
dfExtract['stdev_OutputVoltage'] = pd.DataFrame(auxOV2)
dfExtract['variance_OutputVoltage'] = pd.DataFrame(auxOV3)
dfExtract['mean_ActualVoltage'] = pd.DataFrame(auxAV1)
dfExtract['stdev_ActualVoltage'] = pd.DataFrame(auxAV2)
dfExtract['variance_ActualVoltage'] = pd.DataFrame(auxAV3)

model = joblib.load('my_model.pkl')
prediction = model.predict(dfExtract)

print(statistics.mean(prediction))
print(prediction)
