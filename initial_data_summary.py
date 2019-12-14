# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:21:44 2018
@author: Diya
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Data:
    FinalData = {}
    def Creating_final_data(self):   
        from csv import reader
        # you have to replace "Titanic_data.csv" with the filepath of the 
        # file on your local machine. 
        File = open("Titanic_data.csv")
        #creating all the empty lists to store info
        listOfClass = []
        listOfSurvival = []
        listOfNames = []
        listOfSexes = []
        listOfAges = []
        listOfSibs = []
        listOfParchs = []
        listOfTickets = []
        listOfFares =[]
        listOfCabins =[]
        listOfEmbarked =[]
        listOfBoats = []
        listOfbodies = []
        listOfdestinations =[]
        firstRow = True
        # filling all the lists with their corresponding information 
        for linePieces in reader(File):
            #makes sure that the first line of the file is ignored
            if firstRow:
                firstRow = False
            else:
                listOfClass += [linePieces[0]]
                listOfSurvival+=[linePieces[1]]
                listOfNames+=[linePieces[2]]
                listOfSexes+=[linePieces[3]]
                listOfAges+=[linePieces[4]]
                listOfSibs+=[linePieces[5]]
                listOfParchs+=[linePieces[6]]
                listOfTickets+=[linePieces[7]]
                listOfFares +=[linePieces[8]]
                listOfCabins+=[linePieces[9]]
                listOfEmbarked+=[linePieces[10]]
                listOfBoats+=[linePieces[11]]
                listOfbodies+=[linePieces[12]]
                listOfdestinations+=[linePieces[13]]
        #putting all the lists into the final Dictionary              
        self.FinalData['Class'] =  listOfClass
        self.FinalData['Survived'] =  listOfSurvival
        self.FinalData['Name'] =  listOfNames
        self.FinalData['Sex'] =  listOfSexes
        self.FinalData['Age'] =  listOfAges
        self.FinalData['Sibling'] =  listOfSibs
        self.FinalData['Parch'] =  listOfParchs
        self.FinalData['Ticket'] =  listOfTickets
        self.FinalData['Fare'] =  listOfFares
        self.FinalData['Cabin'] =  listOfCabins
        self.FinalData['Embark'] =  listOfEmbarked
        self.FinalData['Boat'] =  listOfBoats
        self.FinalData['Body'] =  listOfbodies
        self.FinalData['Destination'] =  listOfdestinations 
        
    #determines the amount of females or males 
    def Sex_distribution(self,sex):
        count = 0
        for s in self.FinalData['Sex']:
            if s == sex:
                count +=1
        return count
    
    #creates a graph to display the distribution of the number of 
    #people acccording to their gender. 
    def drawing_Graph1(self):
        plt.figure(figsize=(4,4))
        X_Axis = ('Female','Male')
        Num_female = self.Sex_distribution(self,'female')
        #print('NumFemale: '+str(Num_female))
        Num_male = self.Sex_distribution(self,'male')
        #print('NumMale: '+str(Num_male))
        Y_Axis = [Num_female,Num_male]
        y_pos = np.arange(len(X_Axis))
        plt.ylabel('No of people')
        plt.xticks(y_pos,X_Axis)
        plt.xlabel('Sex')
        plt.title('Sex Distribution')
        plt.bar(y_pos,Y_Axis, align = 'center',alpha=0.5,width=0.5)
        plt.show()
        
    #creates a graph to display the distribution of the number of 
    #people acccording to their ages  
    def creating_Graph2(self):
        Labels = ['less than 5','5-15','15-30','30-60','60+','Unknown']
        Ages = self.Age_distribution(self)
        #print(Ages)
        positions = [0,1,2,3,4,5]
        plt.bar(positions,Ages,width=0.5,color='red')
        plt.xticks(positions,Labels)
        plt.ylabel('No of people')
        plt.xlabel('Ages')
        plt.title('Age Distribution')
        plt.show()
    
    #creates a graph to display the distribution of the number 
    #of people acccording to their classes on the ship 
    def creating_Graph3(self):
        Labels = ['Class 1','Class 2','Class 3']
        classes = self.Class_distribution(self)
        #print(classes)
        positions = [0,1,2]
        plt.bar(positions,classes,width=0.5,color='pink')
        plt.xticks(positions,Labels)
        plt.ylabel('No of people')
        plt.xlabel('Classes')
        plt.title('Class Distribution')
        plt.show()
    
    #This draws the graph of the distribution of the people survived
    def creating_Graph4(self):
        plt.figure(figsize=(4,4))
        Labels = ['Survived','Death']
        classes = self.survival_distribution(self)
        #print(classes)
        plt.ylabel('No of people')
        plt.xlabel('Status')
        positions = [0,1]
        plt.bar(positions,classes,width=0.5,color='green')
        plt.xticks(positions,Labels)
        plt.title('Survival Distribution')
        plt.show()
        
    #creates a graph to display the distribution of the number of 
    #people acccording to the places from where they embarked    
    def creating_Graph5(self):
        Labels = ['Southampton','Cherbourg','Queenstown','Unknown']
        embarks = self.distribution_of_embarkment(self)
        #print(embarks)
        plt.ylabel('No of people')
        plt.xlabel('Places')
        positions = [0,1,2,3]
        plt.bar(positions,embarks,width=0.5,color='blue')
        plt.xticks(positions,Labels)
        plt.title('Embarkment Location Distribution')
        plt.show()
    
    #creates a graph to display the distribution of the number of 
    #people acccording to number of siblings
    def creating_Graph6(self):
        plt.figure(figsize=(10,4))
        Labels = ['0 Siblings','1 Sibling','2 Siblings','3 Siblings','4 Siblings','5 Siblings','8 Siblings']
        sibs = self.sib_distribution(self)
        #print(sibs)
        plt.ylabel('No of people')
        plt.xlabel('No of Siblings')
        positions = [0,1,2,3,4,5,6]
        plt.bar(positions,sibs,width=0.5,color='red')
        plt.xticks(positions,Labels)
        plt.title('Siblings Distribution')
        plt.show()
    
    #creates a graph to display the distribution of the number of 
    #people acccording to whether their parent/chilren were on board
    def creating_Graph7(self):
        plt.figure(figsize=(5,4))
        Labels = ['Has parents and children aboard','does not have parent or children aboard'] 
        parch = self.Parch_distribution(self)
        #print(parch)
        plt.ylabel('No of people')
        plt.xlabel('Status')
        positions = [0,1]
        plt.bar(positions,parch,width=0.1,color='green')
        plt.xticks(positions,Labels)
        plt.title('Parents or children Distribution')
        plt.show()
    
    #creates a graph to display the distribution of the number of 
    #people acccording to cabins    
    def creating_Graph8(self):
        plt.figure(figsize=(7,4))
        Labels = ['A','B','C','D','E','F','G'] 
        cabins = self.cabin_distribution(self)
        #print(cabins)
        plt.ylabel('No of Cabins')
        plt.xlabel('Cabins')
        positions = [0,1,2,3,4,5,6]
        plt.bar(positions,cabins,width=0.9,color='red')
        plt.xticks(positions,Labels)
        plt.title('Cabin Distribution')
        plt.show()
        
    #creates a graph to display the distribution of the number of 
    #people acccording to fares    
    def creating_Graph9(self):
        plt.figure(figsize=(7,4))
        Labels = ['less than 100','100-250','250-350','350+','unknown'] 
        fares = self.fares_distribution2(self)
        print(fares)
        plt.ylabel('No of people')
        plt.xlabel('Fares')
        positions = [0,1,2,3,4]
        plt.bar(positions,fares,width=0.9,color='blue')
        plt.xticks(positions,Labels)
        plt.title('Fair Distribution')
        plt.show()
        
    def fares_distribution2(self):
        less_than_100= 0 
        from100_250 = 0 
        from250_350 = 0 
        more_than_350 = 0 
        unknown = 0 
        for s in self.FinalData['Fare']:
            if s == '?':
                unknown+=1
            elif float(s)<100:
                less_than_100+=1
            elif float(s)>=100 and float(s)<250:
                from100_250+=1
            elif float(s)>=250 and float(s)<350:
                from250_350+=1
            elif float(s)>=350:
                more_than_350+=1
                
        listOfFares = [less_than_100,from100_250,from250_350,more_than_350,unknown]
        return listOfFares
                
        
    #determines how many passengers were carrying how many plus people
    def Parch_distribution(self):
        parch = 0 
        noparch = 0 
        for s in self.FinalData['Parch']:
            if s=='0':
                noparch+=1
            else:
                parch+=1
        listOfParch = [parch, noparch]
        return listOfParch
        
    #determines the aount of people from different classes    
    def Class_distribution(self):
        class_1  = 0 
        class_2  =0 
        class_3 = 0 
        for s in self.FinalData['Class']:
            if s =="1":
                class_1+=1
            elif s=='2':
                class_2+=1
            else:
                class_3+=1
        classes = [class_1,class_2,class_3]
        return classes
    
    #determines the distribution of all the siblings of the passengers
    def sib_distribution(self):
        Sibs0 = 0 
        Sibs1 = 0 
        Sibs2 = 0 
        Sibs3 = 0 
        Sibs4 = 0 
        Sibs5 = 0 
        Sibs8 = 0 
        for s in self.FinalData['Sibling']:
            if s == '0':
                Sibs0+=1
            elif s == '1':
                Sibs1+=1
            elif s =='2':
                Sibs2+=1
            elif s =='3':
                Sibs3+=1
            elif s =='4':
                Sibs4+=1
            elif s == '5':
                Sibs5+=1
            else:
                Sibs8+=1
        listOfSibs = [Sibs0,Sibs1,Sibs2,Sibs3,Sibs4,Sibs5,Sibs8]
        return listOfSibs
            
    #gets a list of all the unique destinations
    def get_unigue_desinations(self):
        listOfDestinations = self.FinalData['Destination']
        listOfDestinations = list(set(listOfDestinations))
        listOfDestinations.sort()
        return listOfDestinations
     
    #determines how many people embarked from different places        
    def distribution_of_embarkment(self):
        embarkment_S=0
        embarkment_C=0
        embarkment_Q=0
        unknown = 0    
        for s in self.FinalData['Embark']:
            if s =='S':
                embarkment_S+=1
            elif s=='C':
                embarkment_C+=1
            elif s== 'Q':
                embarkment_Q+=1
            else:
                unknown+=1          
        embarks = [embarkment_S,embarkment_C,embarkment_Q,unknown]
        return embarks
    
    #determines how many people survived and how many didn't 
    def survival_distribution(self):
        survived = 0 
        died = 0 
        for s in self.FinalData['Survived']:
            if s =='0':
                died+=1
            else:
                survived+=1
        listOfInfo = [survived,died]
        return listOfInfo            
       
    #gets a list of all the unique cabins
    def get_Unique_Cabins(self):
        listOfCabins = self.FinalData['Cabin']
        listOfCabins = list(set(listOfCabins))
        listOfCabins.sort()
        print(listOfCabins)
        
    
    #determines the amount of people from different ages
    def Age_distribution(self):
        less_than_5=0
        from_5to15=0
        from_15to30=0
        from_30to60=0
        above_60=0
        unknown=0
        for s in self.FinalData['Age']:
            if s == '?':
                #counting the unknown
                unknown+=1
            elif float(s) <= 5:
                #less than and including 5
                less_than_5+=1      
            elif float(s) <=15 and float(s)>5:
                #greater than 5 and less than and including 15
                from_5to15+=1
            elif float(s)<=30 and float(s)>15:
                #greater than 15 and less than and including 30
                from_15to30+=1
            elif float(s)<=60 and float(s)>30:
                #greater than 30 and less than and including 60
                from_30to60+=1
            else:
                #strictly above 60 
                above_60+=1
        listOfAges = [less_than_5,from_5to15,from_15to30,from_30to60,above_60,unknown] 
        return listOfAges
    
    #computed the distribution of the fares of the passengers 
    def fare_distribution(self):
        listOfFares = []
        for i in self.FinalData['Fare']:
            if i =='?':
                pass
            else:
                listOfFares+=[float(i)]
        return listOfFares
    
    #makes the histogram to show thw distribution of the fares amoung the passengers 
    def making_histogram(self):
        listOffares = self.fare_distribution(self)
        df = pd.DataFrame({'Fare': listOffares})
        df.hist(column='Fare')
    
    #determines the differnt number of people in different cabins
    def cabin_distribution(self):
        A = 0 
        B= 0
        C =0 
        D= 0 
        E= 0
        F= 0 
        G = 0 
        listOfCabins = self.FinalData['Cabin']
        listOfCabins = list(set(listOfCabins))
        listOfCabins.sort()
        updatedList= []
        for i in listOfCabins:
            if ' ' in i:
                i = i.split(' ')
                for j in i:
                    updatedList+=[j]
            else:
                 updatedList+=[i]
        listOfFirstLetters = []
        for i in updatedList:
            listOfFirstLetters+=[i[0]]
        for l in listOfFirstLetters:
            if l == 'A':
                A+=1
            elif l =='B':
                B+=1
            elif l =='C':
                C+=1
            elif l =='D':
                D+=1
            elif l =='E':
                E+=1
            elif l == 'F':
                F+=1
            elif l =='G':
                G+=1
        listOfCabinDistribution = [A,B,C,D,E,F,G]
        return listOfCabinDistribution
        
    def main(self):
         self.Creating_final_data(self)
         self.creating_Graph8(self)
         self.fare_distribution(self)
         #self.making_histogram(self)
         self.drawing_Graph1(self)
         self.creating_Graph2(self)
         self.creating_Graph3(self)
         self.creating_Graph4(self)
         self.creating_Graph5(self)
         self.creating_Graph6(self)
         self.creating_Graph7(self)
         self.creating_Graph8(self)
         self.creating_Graph9(self)
         
        

Data.main(Data)