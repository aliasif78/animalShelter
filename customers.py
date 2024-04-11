class Customer:

    username = ''
    password = ''
    adopted = False
    
    def login(self):
        
        # Username
        repeat = True

        # Check if username already exits
        while (repeat == True):
            self.username = input('\nUsername : ')

            with open('customerAccounts.txt', 'r') as file:
                temp = file.read()
                lines = temp.splitlines()

            words = []

            for i in lines:
                words += i.split(' ')

            for i in words:
                if (i == self.username):
                    repeat = False
            else:
                if (repeat == True):
                    print('\nUsername does not exist.\n')

        # Password
        repeat = True
        userFound = False

        # Check if username already exits
        while (repeat == True):
            self.password = input('Password : ')

            with open('customerAccounts.txt', 'r') as file:
                temp = file.read()
                lines = temp.splitlines()

            words = []

            for i in lines:
                words += i.split(' ')

            for i in words:
                if (userFound == True and i == self.password):
                    repeat = False
                    return True

                if (i == self.username):
                    userFound = True

        # Check for any Adoptions

    def createAccount(self):

        repeat = True

        # Check if username already exits
        while (repeat == True):
            firstName = input('\nFirst Name : ')
            lastName = input('Last Name : ')
            number = input('Number : ')
            self.username = firstName.lower()
            self.username += lastName.capitalize()
            self.username += number

            with open('customerAccounts.txt', 'r') as file:
                temp = file.read()
                lines = temp.splitlines()

            words = []

            for i in lines:
                words += i.split(' ')

            repeatCheck = False

            for i in words:
                if (i == self.username):
                    repeatCheck = True
                    print('\nUsername already exists.\n')
            else:
                if (repeatCheck == False):
                    repeat = False

        check = False

        while check == False:
            self.password = input('\nPassword : ')
            temp = input('Re-Enter Password : ')

            if (self.password == temp):
                check = True
                print(f'\nYour Account has been created.\n\nUsername : {self.username}\nPassword : {self.password}')

        with open('customerAccounts.txt', 'a') as file:
            file.write(f'{self.username} {self.password}\n')

        return True

    def adoptionRequest(self):
        animal_type = input('\nWhich type of animal do you want to adopt : ')

        while (animal_type.lower() != 'dog' and animal_type.lower() != 'cat' and animal_type.lower() != 'horse' and animal_type.lower() != 'goat' and animal_type.lower() != 'fish' and animal_type.lower() != 'bird'):
            animal_type = input('\nInvalid choice.\nRe-Enter Type : ')

        id = input('Animal ID : ')
        checkID = False

        while (checkID == False):

            # DOGS
            if (animal_type.lower() == 'dog'):
                with open('dogs.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            # CATS
            if (animal_type.lower() == 'cat'):
                with open('cats.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            # HORSES
            if (animal_type.lower() == 'horse'):
                with open('horses.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            # FISH
            if (animal_type.lower() == 'fish'):
                with open('fishes.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            # GOATS
            if (animal_type.lower() == 'goat'):
                with open('goats.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            # BIRDS
            if (animal_type.lower() == 'bird'):
                with open('birds.txt', 'r') as file:
                    content = file.read()
                    individualWords = content.split(' ')

                for i in individualWords:
                    if (i == id):
                        checkID = True

            if (checkID == False):
                id = input('\nInvalid ID.\nRe-Enter ID : ')

        # Add everything to a file (properly formatted)
        name = input("\nYour Name : ")
        address = input("Address : ")
        phone = input("Phone Number : ")
        email = input("Email Address : ")

        residence_type = input("\nType of Residence (apartment/house) : ")
        rent_or_own = input("Rent or Own : ")
        num_adults = int(input("Number of Adults : "))
        num_children = int(input("Number of Children : "))

        owned_pets_before = input("\nHave you owned pets before (yes/no) : ").lower()
        current_pets = input("Do you have any pets now (yes/no) : ").lower()
        experience_with_species = input(f"Do you have experience with {animal_type}s (yes/no) : ").lower()
        
        daily_routine = input("\nDescribe your daily routine and lifestyle : ")
        reason_for_adoption = input("Reason for wanting to adopt : ")
        living_environment = input("Describe where the pet will live : ")

        pet_care_plan = input("\nHow do you plan to care for the pet : ")
        financial_responsibility = input("Are you prepared for the costs of pet ownership (yes/no) : ").lower()
        training_and_behavior = input("How do you plan to train and socialize your pet : ")
        emergency_plans = input("Do you have plans for emergencies : ")

        agreements = input("\nDo you Agree to spay/neuter, provide medical care, and responsible ownership (yes/no) : ").lower()
        home_visit = input("Are you open to a home visit if required (yes/no) : ").lower()

        # Write data to adoptionRequests.txt
        with open('adoptionRequests.txt', 'a') as file:
            file.write(f"Username : {self.username}\nPet Type : {animal_type}\nPet ID : {id}\nCustomer's Name : {name}\nAddress : {address}\nPhone Number : {phone}\nEmail Address : {email}\n\nType of Residence : {residence_type}\nRent or Own : {rent_or_own}\nNumber of Adults : {num_adults}\nNumber of Children : {num_children}\n\nOwned Pets Before : {owned_pets_before}\nCurrently Own Pets : {current_pets}\nExperience with {animal_type}s : {experience_with_species}\n\nDaily routine and Lifestyle : {daily_routine}\nReason for Adoption : {reason_for_adoption}\nWhere the Pet will live : {living_environment}\n\nPlans to take care of the pet : {pet_care_plan}\nPrepared for the Costs of Pet Ownership : {financial_responsibility}\nPlans to Train and Socialize the Pet : {training_and_behavior}\nPlans for Emergencies : {emergency_plans}\n\nAgreed to Neuter, provide Medical Care, and responsible Ownership : {agreements}\nOpen to a Home Visit : {home_visit}\n\n^\n\n")

    def showTips(self):
        choice = input('\nAnimal Type : ')

        if (choice.lower() == 'dog'):
            print('\nFeeding: Provide a balanced diet appropriate for your dog\'s size, age, and breed.\nFresh water should always be available.\n\nExercise: Dogs need regular exercise, both physical and mental.\nDaily walks and playtime are essential.\n\nGrooming: Brush your dog\'s coat, trim their nails, and clean their ears regularly.\n\nHealthcare: Schedule regular vet check-ups, keep up with vaccinations, and use flea and tick prevention.\n\nTraining: Invest in basic obedience training to ensure good behavior and socialization.\n')

        if (choice.lower() == 'cat'):
            print('\nFeeding: Cats require a high-protein diet.\nFeed them on a regular schedule and provide fresh water.\n\nLitter Box: Keep the litter box clean and scoop waste daily.\nChange the litter regularly.\n\nGrooming: Brush your cat\'s coat and trim their nails.\nLong-haired cats may need more grooming.\n\nHealthcare: Regular vet check-ups, vaccinations, and parasite control are essential.\n\nEnrichment: Provide toys, scratching posts, and playtime to keep your cat mentally and physically engaged.\n')

        if (choice.lower() == 'goat'):
            print('\nFeeding: Provide fresh hay, clean water, and a balanced goat feed.\nGoats also need access to browse.\n\nShelter: A secure, dry shelter is important for protection from weather and predators.\n\nExercise: Goats love to explore.\nEncourage them to move around and graze.\n\nGrooming: Brush their coats, trim hooves, and check for signs of parasites.\n\nHealthcare: Regular vet visits, deworming, and vaccinations are necessary.\n')

        if (choice.lower() == 'horse'):
            print('\nFeeding: Horses need a diet of hay, grass, and possibly grains.\nFeed them at regular intervals.\n\nShelter: Ensure they have shelter from harsh weather, such as a stable or run-in shed.\n\nExercise: Horses need ample exercise.\n\nRiding and turnout in a pasture are important.\n\nGrooming: Brush their coat, clean hooves, and provide regular baths.\n\nHealthcare: Regular veterinary care, deworming, and dental check-ups are crucial.\n')

        if (choice.lower() == 'fish'):
            print('\nTank Setup: Set up an appropriate-sized tank with a filter, heater (if needed), and decorations.\n\nWater Quality: Maintain good water quality through regular testing and partial water changes.\n\nFeeding: Feed fish according to their species and avoid overfeeding.\n\nCompatibility: Ensure compatibility among fish species in the same tank.\n\nHealthcare: Be alert to signs of disease, and quarantine sick fish if necessary.\n')

        if (choice.lower() == 'bird'):
            print('\nFeeding: Offer a diet specific to your bird\'s species, which may include seeds, pellets, fruits, and vegetables.\n\nCage: Provide a spacious, clean cage with perches, toys, and fresh water.\n\nSocialization: Spend time interacting with your bird daily.\nThey thrive on social contact.\n\nGrooming: Some birds require feather trimming and nail care.\n\nHealthcare: Regular vet check-ups and attention to signs of illness are crucial.\n')

    def showProceedure(self):
        print('\n\n1. Application:\n\nInterested individuals start by filling out an adoption application.\nThis helps us understand your preferences and ensure we find the right match for your family.\n\n\n2. Screening:\n\nOur team reviews your application to assess your suitability as a pet owner.\nWe may contact you for additional information or clarification.\n\n\n3. Meet and Greet:\n\nOnce your application is approved, you\'ll have the opportunity to meet the animal you\'re interested in.\nThis allows you to get to know each other and ensure it\'s a good fit.\n\n\n4. Adoption Fee :\n\nThere is an adoption fee that helps cover the cost of vaccinations, spaying/neutering and other care the animal has received.\n\n\n5. Adoption Agreement :\n\nYou\'ll be asked to sign an adoption agreement, outlining the terms and conditions of the adoption, including responsibilities and return policies.\n\n\n6. Education and Support :\n\nWe provide information on pet care and can offer guidance and resources to help you become a responsible pet owner.\n\n\n7. Post-Adoption Support :\n\nWe\'re here for you after the adoption, offering support, resources, and answers to your questions or concerns.\n\n\n8. Finalization:\n\nOnce all requirements are met, we\'ll complete the paperwork, transfer ownership, and release the animal to you.\n\n\n9. Follow-Up:\n\nWe schedule follow-up visits to ensure the well-being of your new pet and address any concerns.\nWe encourage regular veterinary care.\n\n\n10. Promotion of Responsible Ownership:\n\nWe encourage spaying/neutering, microchipping, and licensing, as well as responsible pet ownership within the community.\n\n')

    def hasAdopted(self):
        
        with open('adoptionHistory.txt', 'r') as file:
            content = file.read()
            
        individualRequests = content.split('^')

        for j in individualRequests:
            
            individualElements = j.split()

            if (self.username in individualElements):
                self.adopted = True

    def returnAnimal(self):

        petType = "x"
        choice = int(input('\nYou are going to return your Adopted Animal.\nAre you sure that you want to proceed?\n\n1. Yes\n2. No\n\nChoice : '))

        if (choice == 1):
            print('\nPlease enter the following Information about your Pet : ')
            
            while (petType.lower() != 'dog' and petType.lower() != 'cat' and petType.lower() != 'horse' and petType.lower() != 'bird' and petType.lower() != 'fish' and petType.lower() != 'goat'):
                petType = input('\nType : ')

            found = False

            while (found == False):
                petID = input('Pet ID : ')

                with open('adoptionHistory.txt', 'r') as file:
                    content = file.read()

                individualRequests = content.split('^')

                for i in individualRequests:
                    individualElements = i.split()

                    if (individualElements[10] == petID and individualElements[6] == petType):
                        found = True
                        adoptionToBeRemoved = i
                        break

            with open('adoptionHistory.txt', 'w') as file:
                for i in individualRequests:
                    if (i != adoptionToBeRemoved):
                        file.write(i)
            

            with open('returnHistory.txt', 'a') as file:
                file.write(adoptionToBeRemoved)
                file.write('\n^\n')

            return petType
        
        return 0

    def submitReview(self):
        
        petType = 'x'
            
        while (petType.lower() != 'dog' and petType.lower() != 'cat' and petType.lower() != 'horse' and petType.lower() != 'bird' and petType.lower() != 'fish' and petType.lower() != 'goat'):
            petType = input('\nType : ')

        rating = int(input('Rate your Experience : '))
        remarks = input('Remarks : ')

        x = f'Customer Name : {self.username}\nPet Type : {petType}\nRating : {rating}/10\nRemarks : {remarks}\n\n^\n\n'
    
        with open('reviews.txt', 'a') as file:
            file.write(x)
