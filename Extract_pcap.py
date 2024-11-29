from scapy.all import rdpcap
import pandas as pd

packets = rdpcap('output.pcap')

actualSpeed = []
actualCurrent = []
actualTorque = []
actualPowerFactor = []
actualOutputVoltage = []
actualVoltage = []

for i in range(len(packets)):
  if packets[i].src=="68:3e:02:40:e3:19":
        b11 = str(hex(packets[i].original[len(packets[i].original)-37]))
        b11_1 = b11.split('0x')
        if len(b11_1[1]) == 1:
            b11='0'+b11_1[1]
        else:
            b11 = b11_1[1]

        b10 = str(hex(packets[i].original[len(packets[i].original)-36]))
        b10_1 = b10.split('0x')
        if len(b10_1[1]) == 1:
            b10='0'+b10_1[1]
        else:
            b10 = b10_1[1]

        b9 = str(hex(packets[i].original[len(packets[i].original)-35]))
        b9_1 = b9.split('0x')
        if len(b9_1[1]) == 1:
            b9='0'+b9_1[1]
        else:
            b9 = b9_1[1]

        b8 = str(hex(packets[i].original[len(packets[i].original)-34]))
        b8_1 = b8.split('0x')
        if len(b8_1[1]) == 1:
            b8='0'+b8_1[1]
        else:
            b8 = b8_1[1]

        b7 = str(hex(packets[i].original[len(packets[i].original)-33]))
        b7_1 = b7.split('0x')
        if len(b7_1[1]) == 1:
            b7='0'+b7_1[1]
        else:
            b7 = b7_1[1]

        b6 = str(hex(packets[i].original[len(packets[i].original)-32]))
        b6_1 = b6.split('0x')
        if len(b6_1[1]) == 1:
            b6='0'+b6_1[1]
        else:
            b6 = b6_1[1]

        b5 = str(hex(packets[i].original[len(packets[i].original)-31]))
        b5_1 = b5.split('0x')
        if len(b5_1[1]) == 1:
            b5='0'+b5_1[1]
        else:
            b5 = b5_1[1]

        b4 = str(hex(packets[i].original[len(packets[i].original)-30]))
        b4_1 = b4.split('0x')
        if len(b4_1[1]) == 1:
            b4='0'+b4_1[1]
        else:
            b4 = b4_1[1]

        b3 = str(hex(packets[i].original[len(packets[i].original)-29]))
        b3_1 = b3.split('0x')
        if len(b3_1[1]) == 1:
            b3='0'+b3_1[1]
        else:
            b3 = b3_1[1]

        b2 = str(hex(packets[i].original[len(packets[i].original)-28]))
        b2_1 = b2.split('0x')
        if len(b2_1[1]) == 1:
            b2='0'+b2_1[1]
        else:
            b2 = b2_1[1]

        b1 = str(hex(packets[i].original[len(packets[i].original)-27]))
        b1_1 = b1.split('0x')
        if len(b1_1[1]) == 1:
            b1='0'+b1_1[1]
        else:
            b1 = b1_1[1]

        b0 = str(hex(packets[i].original[len(packets[i].original)-26]))
        b0_1 = b0.split('0x')
        if len(b0_1[1]) == 1:
            b0='0'+b0_1[1]
        else:
            b0 = b0_1[1]

        actualOutputVoltage_support = '0x'+b1+b0
        actualOutputVoltage_support = (int(actualOutputVoltage_support,16)/int("4000",16))
        actualOutputVoltage.append(actualOutputVoltage_support)
        actualVoltage_support = '0x'+b3+b2
        actualVoltage_support = (int(actualVoltage_support,16)/int("4000",16))
        actualVoltage.append(actualVoltage_support)
        actualPowerFactor_support = '0x'+b5+b4
        actualPowerFactor_support = (int(actualPowerFactor_support,16)/int("4000",16))
        actualPowerFactor.append(actualPowerFactor_support)
        actualTorque_support = '0x'+b7+b6
        actualTorque_support = (int(actualTorque_support,16)/int("4000",16))
        actualTorque.append(actualTorque_support)
        actualCurrent_support = '0x'+b9+b8
        actualCurrent_support = (int(actualCurrent_support,16)/int("4000",16))
        actualCurrent.append(actualCurrent_support)
        actualSpeed_support = '0x'+b11+b10
        actualSpeed_support = (int(actualSpeed_support,16)/int("4000",16))
        actualSpeed.append(actualSpeed_support)


df = pd.DataFrame(actualSpeed,
                  columns=['Speed'])

df['Current'] = pd.DataFrame(actualCurrent,
                  columns=['Current'])

df['Torque'] = pd.DataFrame(actualTorque,
                  columns=['Torque'])

df['PowerFactor'] = pd.DataFrame(actualPowerFactor,
                  columns=['PowerFactor'])

df['OutputVoltage'] = pd.DataFrame(actualOutputVoltage,
                  columns=['OutputVoltage'])

df['ActualVoltage'] = pd.DataFrame(actualVoltage,
                  columns=['ActualVoltage'])

df.to_csv('Data'+'.csv',index=False)