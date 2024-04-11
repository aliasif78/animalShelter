import animals
import pywhatkit as kit
import random
import os
import datetime


class Manager (animals.Animals):

    password = None
    phoneNumber = '+123456789'  # Replace with actual Phone Number
    balance = 0

    def initializePassword(self):

        with open('manager.txt', 'r') as file:
            temp = file.read()
            self.password = temp

    def checkPassword(self, passwordEntered):
        if (passwordEntered == self.password):
            return True
        else:
            passwordEntered = input('\nIncorrect Password.\nTry Again : ')
            
            if (passwordEntered == self.password):
                return True
            else:
                return False

    def verifyIdentity(self):
        code = random.randint(0000, 9999)
        code = str(code)

        # Send the message to the Manager
        kit.sendwhatmsg_instantly(self.phoneNumber, code)

        codeGuess = input('\nVerification Code : ')
        
        if (codeGuess == code):
            return True
        else:
            print('\nInavlid Code.')
            return False
        
    def changePassword(self):

        check = False
        self.password = input('\nNew Password : ')
        temp = input('Re-Enter Password : ')

        if (self.password == temp):
            with open('manager.txt', 'w') as file:
                file.write(self.password)
        else:
            while (check == False):
                self.password = input('\nPasswords do not match.\nNew Password : ')
                temp = input('Re-Enter Password : ')

                if (self.password == temp):
                    check = True

                    with open('manager.txt', 'w') as file:
                        file.write(self.password)

    def addAnimal(self):
        
        animalType = input('Type : ')
        breed = input('Breed : ')
        name = input('Name : ')
        age = int(input('Age : '))

        if (animalType == 'dog'):
            self.dogCount += 1
            
            with open('dogs.txt', 'a') as file:
                file.write(f' {self.dogCount} {name} {breed} Age{age} \n')
        
        if (animalType == 'cat'):
            self.catCount += 1
            
            with open('cats.txt', 'a') as file:
                file.write(f'{self.catCount} {breed} {name} Age{age} \n')
        
        if (animalType == 'bird'):
            self.birdCount += 1
            
            with open('birds.txt', 'a') as file:
                file.write(f'{self.birdCount} {breed} {name} Age{age} \n')
        
        if (animalType == 'horse'):
            self.horseCount += 1
            
            with open('horses.txt', 'a') as file:
                file.write(f'{self.horseCount} {breed} {name} Age{age} \n')
        
        if (animalType == 'goat'):
            self.goatCount += 1
            
            with open('goats.txt', 'a') as file:
                file.write(f'{self.goatCount} {breed} {name} Age{age} \n')
        
        if (animalType == 'fish'):
            self.fishCount += 1
            
            with open('fishes.txt', 'a') as file:
                file.write(f'{self.fishCount} {breed} {name} Age{age} \n')

        self.totalAnimals += 1

    def addAnimalAutomatically(self, petType):

        name = input('\nName : ')
        breed = input('Breed : ')
        age = int(input ('Age : '))

        if (petType == 'dog'):
            self.dogCount += 1
            
            with open('dogs.txt', 'a') as file:
                file.write(f'{self.dogCount} {name} {breed} Age{age} \n')
        
        if (petType == 'cat'):
            self.catCount += 1
            
            with open('cats.txt', 'a') as file:
                file.write(f'{self.catCount} {breed} {name} Age{age} \n')
        
        if (petType == 'bird'):
            self.birdCount += 1
            
            with open('birds.txt', 'a') as file:
                file.write(f'{self.birdCount} {breed} {name} Age{age} \n')
        
        if (petType == 'horse'):
            self.horseCount += 1
            
            with open('horses.txt', 'a') as file:
                file.write(f'{self.horseCount} {breed} {name} Age{age} \n')
        
        if (petType == 'goat'):
            self.goatCount += 1
            
            with open('goats.txt', 'a') as file:
                file.write(f'{self.goatCount} {breed} {name} Age{age} \n')
        
        if (petType == 'fish'):
            self.fishCount += 1
            
            with open('fishes.txt', 'a') as file:
                file.write(f'{self.fishCount} {breed} {name} Age{age} \n')

        self.totalAnimals += 1

    def removeAnimal(self):

        animalType = input('\nType : ')
        ID = input('ID : ')
        
        first = False
        tempString = ''

        if (animalType == 'dog' or animalType == 'Dog'):
            
            with open('dogs.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    first = True
                    self.dogCount -= 1
                    self.totalAnimals -= 1

                    # Don't add animal to be removed in tempString
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3] + '\n'

            with open('dogs.txt', 'w') as file:
                file.write(tempString)

        if (animalType == 'cat' or animalType == 'Cat'):
            with open('cats.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    # Removal Algorithm wa koko desu
                    first = True
                    self.catCount -= 1
                    self.totalAnimals -= 1
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3]

            with open('cats.txt', 'w') as file:
                file.write(tempString)

        if (animalType == 'bird' or animalType == 'Bird'):
            with open('birds.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    # Removal Algorithm wa koko desu
                    first = True
                    self.birdCount -= 1
                    self.totalAnimals -= 1
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3]

            with open('birds.txt', 'w') as file:
                file.write(tempString)

        if (animalType == 'horse' or animalType == 'Horse'):
            with open('horses.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    # Removal Algorithm wa koko desu
                    first = True
                    self.horseCount -= 1
                    self.totalAnimals -= 1
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3]

            with open('horses.txt', 'w') as file:
                file.write(tempString)

        if (animalType == 'goat' or animalType == 'Goat'):
            with open('goats.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    # Removal Algorithm wa koko desu
                    first = True
                    self.goatCount -= 1
                    self.totalAnimals -= 1
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3]

            with open('goats.txt', 'w') as file:
                file.write(tempString)

        if (animalType == 'fish' or animalType == 'fish'):
            with open('fishes.txt', 'r') as file:
                content = file.readlines()

            for i in content:

                # if ID has not yet been found, do not decrement ID
                if (not i.startswith(ID) and first == False):
                    tempString += i

                if (i.startswith(ID)) :
                    # Removal Algorithm wa koko desu
                    first = True
                    self.fishCount -= 1
                    self.totalAnimals -= 1
                    continue
                
                # Decrement ID if ID has been found
                if (first == True):
                    temp = i.split(' ')
                    temp[0] = str(int(temp[0]) - 1)
                    
                    for j in range(3):
                        tempString += temp[j] + ' '

                    tempString += temp[3]

            with open('fishes.txt', 'w') as file:
                file.write(tempString)

    def showAvailableAnimals(self):

        choice = int(input('\n1. Dogs\n2. Cats\n3. Birds\n4. Horses\n5. Goats\n6. Fishes\n\nType : '))
        
        if (choice == 1):

            # Dogs
            print('\n\nDOGS :\n\n')

            with open('dogs.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

        if (choice == 2):
            # Cats
            print('\n\nCATS :\n\n')

            with open('cats.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

        if (choice == 3):
            # Birds
            print('\n\nBIRDS :\n\n')

            with open('birds.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

        if (choice == 4):
        # Horses
            print('\n\nHORSES :\n\n')

            with open('horses.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

        if (choice == 5):
        # Goats
            print('\n\nGoats :\n\n')

            with open('goats.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

        if (choice == 6):
        # Birds
            print('\n\nFISHES :\n\n')

            with open('fishes.txt', 'r') as file:
                while (True):

                    line = file.readline()

                    if (not line):
                        break

                    tempList = line.split(' ')
                    print(f'Name : {tempList[1]}\nID : 23-{tempList[0]}\nBreed : {tempList[2]}\nAge : {tempList[3]}')

    def showAnimalNumbers(self):
        print(f'\n\nDogs : {self.dogCount}\nCats : {self.catCount}\nBirds : {self.birdCount}\nHorses : {self.horseCount}\nGoats : {self.goatCount}\nFishes : {self.fishCount}\n\nTotal Animals : {self.totalAnimals}\n')

    def initializeCounts(self):
        
        # Dogs
        path = 'dogs.txt'

        if os.path.exists(path):
            
            n = 1

            with open('dogs.txt', 'r') as file:
                line = file.readline()
                self.totalAnimals = 1

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.dogCount = n


        # Cats
        path = 'cats.txt'

        if os.path.exists(path):
            n = 1

            with open('cats.txt', 'r') as file:
                line = file.readline()

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.catCount = n
            

        # Birds
        path = 'birds.txt'

        if os.path.exists(path):
            n = 1

            with open('birds.txt', 'r') as file:
                line = file.readline()

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.birdCount = n
            

        # Horses
        path = 'horses.txt'

        if os.path.exists(path):
            n = 1

            with open('horses.txt', 'r') as file:
                line = file.readline()

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.horseCount = n
            

        # Goats
        path = 'goats.txt'

        if os.path.exists(path):
            n = 1

            with open('goats.txt', 'r') as file:
                line = file.readline()

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.goatCount = n
            

        # Fishes
        path = 'fishes.txt'

        if os.path.exists(path):
            n = 1

            with open('fishes.txt', 'r') as file:
                line = file.readline()

                while True:
                    line = file.readline()
                    
                    if (not line):
                        break

                    self.totalAnimals += 1
                    n += 1

            self.fishCount = n

    def initializeAdoptionCounts(self):
        with open('adoptionHistory.txt', 'r') as file:
            content = file.read()

        individualRequests = content.split('^')
            
        for i in individualRequests:

            individualWords = i.split()
            
            if (not individualWords):
                break

            animalType = individualWords[6]
              
            # Now increment appropriate count according to the animalType
            self.totalAdopted += 1

            if (animalType.lower() == 'dog'):
                self.dogAdopted += 1
            
            if (animalType.lower() == 'cat'):
                self.catAdopted += 1
            
            if (animalType.lower() == 'bird'):
                self.birdAdopted += 1
            
            if (animalType.lower() == 'horse'):
                self.horseAdopted += 1
            
            if (animalType.lower() == 'goat'):
                self.goatAdopted += 1
            
            if (animalType.lower() == 'fish'):
                self.fishAdopted += 1
                
    def reviewAdoptionRequests(self):

        with open('adoptionRequests.txt', 'r') as file:
            content = file.read()

        individualRequests = content.split('^')
        x = 1
        print('\n\n')

        for i in individualRequests:

            # To signal EOF
            if (i == '\n\n'):
                break

            # To get Username
            individualElements = i.split('\n')

            print(f'Adoption Request {x}\n')
            print(i)

            decision = int(input('\n1. Accept Request\n2. Decline Request\n3. Decide Later\n\nChoice : '))

            # To work around correct index of individualElements
            if (x == 1):

                if (decision == 1):
                    with open('adoptionRequestReplies.txt', 'a') as file:
                        file.write(f'{individualElements[0]}\n{individualElements[1]}\n{individualElements[2]}\nAccepted\n\n')

                    self.removeReviewedFromAdoptionRequests(individualElements[0])

                if (decision == 2):
                    with open('adoptionRequestReplies.txt', 'a') as file:
                        declineReason = input('\nReason for Rejection : ')
                        file.write(f'{individualElements[0]}\n{individualElements[1]}\n{individualElements[2]}\nDeclined\nReason : {declineReason}\n\n')

                    self.removeReviewedFromAdoptionRequests(individualElements[0])

            if (x != 1):

                if (decision == 1):
                    with open('adoptionRequestReplies.txt', 'a') as file:
                        file.write(f'{individualElements[2]}\n{individualElements[3]}\n{individualElements[4]}\nAccepted\n\n')

                    self.removeReviewedFromAdoptionRequests(individualElements[2])

                if (decision == 2):
                    with open('adoptionRequestReplies.txt', 'a') as file:
                        declineReason = input('\nReason for Rejection : ')
                        file.write(f'{individualElements[2]}\n{individualElements[3]}\n{individualElements[4]}\nDeclined\nReason : {declineReason}\n\n')

                    self.removeReviewedFromAdoptionRequests(individualElements[2])

            print('\n\n')
            x += 1

    def checkForAdoptionRequestReply(self, USERNAME):

        with open("adoptionRequestReplies.txt", 'r') as file:
            content = file.read()

        individualElements = content.splitlines()
        x = -1
        check = False

        for i in individualElements:
            x += 1

            if (i == f"Username : {USERNAME}"):
                
                if (individualElements[x + 3] == "Accepted"):
                    print(f'\n\nGood News! Your adoption request for the following pet has been accepted.\nYou may visit our outlet within the next 7 Days to take official ownership of your pet.')

                    if (individualElements[x + 1] == "Pet Type : dog"):
                        tempFee = self.dogFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    if (individualElements[x + 1] == "Pet Type : cat"):
                        tempFee = self.catFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    if (individualElements[x + 1] == "Pet Type : bird"):
                        tempFee = self.birdFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    if (individualElements[x + 1] == "Pet Type : horse"):
                        tempFee = self.horseFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    if (individualElements[x + 1] == "Pet Type : fish"):
                        tempFee = self.fishFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    if (individualElements[x + 1] == "Pet Type : goat"):
                        tempFee = self.goatFee
                        print(f"${tempFee} has been charged as adoption fees.\n")

                    print(f"\n\n{individualElements[x+1]}\n{individualElements[x+2]}\n\n")

                    with open("balance.txt", 'r') as file:
                        currentBalance = file.read()
                        newBalance = int(currentBalance) + tempFee
                        self.balance = newBalance
                        
                    with open("balance.txt", 'w') as file:
                        file.write(str(newBalance))

                if (individualElements[x + 3] == "Declined"):
                    print(f'\n\nWe regret to inform you that your adoption request for the following pet has been declined.\n\n{individualElements[x+1]}\n{individualElements[x+2]}\n{individualElements[x+4]}\n\n')

                self.removeReviwedFromAdoptionRequestReplies(i)

    def removeReviwedFromAdoptionRequestReplies(self, USERNAME):

        with open('adoptionRequestReplies.txt', 'r') as file:
            content = file.read()
            individualRequests = content.split('\n\n')

            # Indexes of the Individual Request Replies
            indexes = []
            index = 0

            for i in individualRequests:
                individualWords = i.split('\n')

                # Store indexes of the requests to be removed
                for j in individualWords:
                    if (j == USERNAME):
                        indexes.append(index)

                index += 1

            # Now re-write file without these indexes
            with open('adoptionRequestReplies.txt', 'w') as file:
                for i in range(index - len(indexes)):
                    if i not in indexes:
                        file.write(individualRequests[i])
                        file.write("\n\n")

    def removeReviewedFromAdoptionRequests(self, USERNAME):
        
        with open('adoptionRequests.txt', 'r') as file:
            content = file.read()

        individualRequests = content.split('^')
            
        # Indexes of the Individual Requests
        x = 0
        indexes = []
        
        for i in individualRequests:
            individualElements = i.split('\n')

            for j in individualElements:
                if (j == USERNAME):
                    indexes.append(x)

                    with open("adoptionHistory.txt", "a") as file:
                        file.write(individualRequests[x])
                        adoptionDate = datetime.date.today()
                        file.write(f"Adoption Date : {str(adoptionDate)}")
                        file.write("\n\n^\n\n")

            x += 1

        # Now re-write file without these indexes
        with open('adoptionRequests.txt', 'w') as file:
            for i in range(x):
                if (i not in indexes):
                    file.write(individualRequests[i])

                    if (i != x - 1):
                        file.write("^")

    def showAdoptionHistory(self):
        with open('adoptionHistory.txt', 'r') as file:
            content = file.read()

        individualRequests = content.split('^')
        x = 1
        print('\n\n')
        print(individualRequests)

        for i in individualRequests:

            # To signal EOF
            if (i == ''):
                break

            print(f'Adoption Request {x}\n')
            print(i)

            print('\n\n')
            x += 1

    def initializeBalance(self):
        with open("balance.txt", 'r') as file:
            self.balance = file.read()

    def showBalance(self):
        print(f"\n\nBalance : ${self.balance}\n\n")

    def showAnimalPreferenceStatistics(self):
        
        self.initializeAdoptionCounts()
        print(f'\nThe following statistics show each type of Animal\'s Adoption Rate\n\nTotal Animals : {self.totalAdopted}\n\nDogs   : {int((self.dogAdopted / self.totalAdopted) * 100)} %\nCats   : {int((self.catAdopted / self.totalAdopted) * 100)} %\nBirds  : {int((self.birdAdopted / self.totalAdopted) * 100)} %\nHorses : {int((self.horseAdopted / self.totalAdopted) * 100)} %\nGoats  : {int((self.goatAdopted / self.totalAdopted) * 100)} %\nFishes : {int((self.fishAdopted / self.totalAdopted) * 100)} %\n\n')

    def showCustomers(self):

        with open('customerAccounts.txt', 'r') as file:
            content = file.read()

        individualWords = content.split()
        counter = -1

        for i in individualWords:
            
            counter += 1
            found = False

            # To ignore Passwords
            if (counter % 2 != 0):
                continue

            print(f'\n\nUser : {i}')

            with open('adoptionHistory.txt', 'r') as file2:
                content2 = file2.read()
                
            individualRequests = content2.split('^')

            for j in individualRequests:
                
                individualElements = j.split()

                for k in individualElements:
                    if (k == i):
                        if (found == False):
                            print(f'{i} has made the following Adoption(s) :\n\n')

                        found = True
                        print(f'{individualElements[3]} {individualElements[4]} {individualElements[5]} {individualElements[6]}\n{individualElements[7]} {individualElements[8]} {individualElements[9]} {individualElements[10]}\n')

            if (found == False):
                print(f'{i} has not made any Adoptions.\n')

    def donateFunds(self):
        self.initializeBalance()
        donation = int(input('\nAmount of Donation : '))
        b = int(self.balance)
        b += donation
        self.balance = str(b)

        with open('balance.txt', 'w') as file:
            file.write(self.balance)

    def showReturnHistory(self):
        with open('returnHistory.txt', 'r') as file:
            content = file.read()

        individualRequests = content.split('^')
        x = 1
        print('\n\n')

        for i in individualRequests:

            # To signal EOF
            if (i == ''):
                break

            print(f'Adoption Request {x}\n')
            print(i)

            print('\n\n')
            x += 1

    def showReviews(self):
        with open('reviews.txt', 'r') as file:
            content = file.read()

        individualReviews = content.split('^')
        print('\n')

        for i in individualReviews:
            print(i)

    def seeFAQs(self):
        with open('customerCare.txt', 'r') as file:
            content = file.read()

        individualQuestions = content.split('^')

        print('\nFAQs :')

        for i in individualQuestions:
            if ('-' not in i):
                print(i)

