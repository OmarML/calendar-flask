#create dataframe for Monday
Lec = "Lecture"
T = "Tutorial"
Lab = "Lab"
ClassName = ["Systems, Design and Computing", "Mechancis, Machines and Vibrations", "Materials and Structures"]
ClassType = [Lab, Lec, Lab ]
LectureCode = ['FEEG2001','FEEG2002','FEEG2002']
Location = ['177/3011', '07/3009', '05/1021']
Time = ['09:00-12:00', '14:00-15:00', '15:00-18:00']
df = pd.DataFrame(ClassName, columns=["Class Name"])
df["Class Name"]=ClassName
df["Class Type"]=ClassType
df["Location"]=Location
df["Time and Duration"]=Time
print df