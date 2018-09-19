class Hospital:   #define the class hospital
    def __init__(self,name,phno): #define the constructor with params as name and phno
        self.name=name #map the name and phonno
        self.phno=phno
    def showDetails(self): #displays the hospital name and phoneno

        print("Name:",self.name)
        print("PhoneNo:",self.phno)

class Doctor(Hospital):  #define the doctor class that inherits hospital class
    doctorcount=0   #defines the counter for no of doctors
    def __init__(self,name,phno,doctor_id): ##define constructor with params doctor id
        super().__init__(name,phno) #calls the super class constructor
        self.doctor_id=doctor_id #map the doctor id
        Doctor.doctorcount+=1 #increment the counter

    def showDetails(self): #override showDetails from hospital class
        print("Doctor Details:")
        Hospital.showDetails(self) #displays the hospital details
        print("Doctor Id:",self.doctor_id)

class Patient(Hospital):   #define the patient class
    patientcount=0
    def __init__(self,name,phno,patient_id): #defines the constructor
        Hospital.__init__(self,name, phno)  #define the superclass constructor to map name and phone no
        self.patient_id=patient_id #map patient id of patient
        Patient.patientcount+=1

    def showDetails(self):
        print("Patient Details:")
        Hospital.showDetails(self)   #prints the details of patient
        print("Patient Id:",self.patient_id)

class clerk: #defines the clerk class
    def __init__(self,name,id):
        self.name=name
        self.__id=id

    def showDetails(self):
        print("clerk Details:")
        print("clerk name:",self.name)
        print("clerk ID:",self.__id)

class Nurse(Hospital):   #defines the nurse class

    def __init__(self,nursename,roomno,nurse_id): #defines the constructor to map nursedetails
        self.nursename=nursename
        self.roomno=roomno
        self.nurse_id=nurse_id


    def showDetails(self):
#displays the details of the nurse
        print("Nurse name:")
        print("nurse roomno", self.roomno)
        print("nurse ID:", self.nurse_id)

class Book(Patient, Nurse):   #defines the book class

    def __init__(self,name,phno,patient_id,nursename,roomno,nurse_id): #defines the constructor to map bookdetails
        Patient.__init__(self,name,phno,patient_id)
        Nurse.__init__(self,nursename,roomno,nurse_id)


    def showDetails(self):
#displays the details of the patient and nurse
        Patient.showDetails(self)
        Nurse.showDetails(self)

#define the list and append the objects

d1=Doctor("Pratty",12345,16)
p1=Patient("Bob",67890,89)
c1=clerk("Nom",78)
p2=Patient("prat",72904789,56)
nurse=Nurse("geeta",12345,16)
p3=Patient("xyz",4444,4)
book1=Book("nemo",35678,56,"ellen",56890,67)
d1.showDetails()
print("\n")
p1.showDetails()
print("\n")
c1.showDetails()
print("\n")
nurse.showDetails()
print("\n")
p2.showDetails()
print("\n")
book1.showDetails()
print("\n")


print("Total no of Doctors are:",Doctor.doctorcount)
print("Total no of Patients are:",Patient.patientcount)