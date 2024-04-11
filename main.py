import manager
import customers
import animals


# MANAGER / CUSTOMER
anm = animals.Animals()
mgr = manager.Manager()
ctr = customers.Customer()

choice = input('\nAre you the Manager or a Customer : ')


# INITIALIZING COUNTS
mgr.initializeCounts()


# MANAGER
if (choice == 'Manager' or choice == 'manager' or choice == 'm' or choice == 'M'):
    
    choice = int(input('\nPress 1 to Login\nPress 2 to Change Password\n\nChoice : '))
    isPassValid = True
    
    # INPUTTING PASSWORD
    if (choice == 1):
        
        isPassValid = False
        mgr.initializePassword()

        passwordEntered = input('\nPassword : ')
        isPassValid = mgr.checkPassword(passwordEntered)

    # Change Password
    if (choice == 2):
        isCodeValid = mgr.verifyIdentity()

        if (isCodeValid == True):
            mgr.changePassword()

    # PROCEEDING FURTHER
    if (isPassValid == True):
        mgr.initializeBalance()
        choice = int(input('\n1 : Add an Animal\n2 : Remove an Animal\n3 : Show all Available Animals\n4 : Show Number of Animals\n5 : Show Adoption History (with Customer Info)\n6 : Show all Customers & their Adoptions\n7 : Show Animal Preference Statistics\n8 : Review Adoption Requests\n9 : Show Earnings\n10 : Show Return History\n11 : Show Customer Reviews\n\nChoice : '))
        
        if (choice == 1):
            mgr.addAnimal()

        if (choice == 2):
            mgr.removeAnimal()

        if (choice == 3):
            mgr.showAvailableAnimals()

        if (choice == 4):
            mgr.showAnimalNumbers()

        if (choice == 5):
            mgr.showAdoptionHistory()

        if (choice == 6):
            mgr.showCustomers()

        if (choice == 7):
            mgr.showAnimalPreferenceStatistics()
        
        if (choice == 8):
            mgr.reviewAdoptionRequests()

        if (choice == 9):
            mgr.showBalance()

        if (choice == 10):
            mgr.showReturnHistory()

        if (choice == 11):
            mgr.showReviews()


    # Why is pyWhatKit no working?

# CUSTOMER
if (choice == 'Customer' or choice == 'customer' or choice == 'c' or choice == 'C'):
    choice = int(input('\nPress 1 to Login\nPress 2 to Create a New Account\n\nChoice : '))

    loginCheck = False

    if (choice == 1):
        loginCheck = ctr.login()

    if (choice == 2):
        loginCheck = ctr.createAccount()

    if (loginCheck == True):

        mgr.checkForAdoptionRequestReply(ctr.username)
        ctr.hasAdopted()

        print('\n1 : See Available Animals\n2 : Donate an Animal\n3 : Donate Funds\n4 : Submit an Adoption Request\n5 : General Tips for taking Care of a specific Animal\n6 : Proceedure of Adoption\n7 : See Other Customers\' Reviews\n8 : See FAQs')
        
        if ctr.adopted == True:
            print('9 : Submit a Review\n10 : Return your Adopted Animal\n')

        choice = int(input('Choice : '))

        if (choice == 1):
            mgr.showAvailableAnimals()

        if (choice == 2):
            mgr.addAnimal()

        if (choice == 3):
            mgr.donateFunds()

        if (choice == 4):
            ctr.adoptionRequest()

        if (choice == 5):
            ctr.showTips()

        if (choice == 6):
            ctr.showProceedure()

        if (choice == 7):
            mgr.showReviews()

        if (choice == 8):
            mgr.seeFAQs()

        if (choice == 9 and ctr.adopted == True):
            ctr.submitReview()

        if (choice == 10 and ctr.adopted == True):
            petType = ctr.returnAnimal()
            mgr.addAnimalAutomatically(petType)