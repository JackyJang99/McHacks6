
# coding: utf-8

# In[22]:


csv1 = open("infection.csv", "r").read().split()
csv2 = open("obesity.csv", "r").read().split()
csv3 = open("diabetehypertension.csv", "r").read().split()
csv4 = open("dyslipidemia.csv", "r").read().split()
csvs = [csv1, csv2, csv3, csv4]
import pickle
with open('patientIDs.pkl', 'rb') as f:
    allPatients = pickle.load(f)
names = ["infection", "obesity", "diabetehypertension", "dyslipidemia"]
# print(csv2)
def identify_disease(patientID):
    disease = []
    for csvNum in range(len(csvs)):
        for line in csvs[csvNum]:
            if line[line.index(",")+1:] == patientID:
                disease.append(names[csvNum])
    if disease == []:
        return -1
    return disease

# sick people
for patient in allPatients:
    html = open("template.html", "r").read()
    id = patient
    if identify_disease(id) != -1:
        diseases = str(identify_disease(id))[2:-2].replace("'", "")
        html = html.replace("diseases", diseases)
    else:
        html = html.replace("have", "are")
        html = html.replace("#FF0000", "#7CFC00")
        html = html.replace("diseases", "healthy")

    # changing image references
    graphs = ["activityEnergy", "blood_oxygen", "bmi", "body_temperature", "cumulativeSleep", "dias", "fat_ratio", "glucose", "glucose_post_meal", "height", "mood", "pulse_rate", "steps", "sys", "waist", "weight"]
    len(graphs)
    for i in range(16):
        html = html.replace(str(i+1) + ".JPG", id + "_" + graphs[i] + ".png", 1)

    # writing to new html file
    newFile = open(id + ".html", "w+")
    newFile.write(html)
    newFile.close()

