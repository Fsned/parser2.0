

from logger.log import log
import datetime
import csv








class Post:

    def __init__(self, row):
        for it, val in enumerate(row):
            if it == 0:
                self.date = str(val)
            elif it == 1:
                self.amount = float(val)
            elif it == 2:
                pass
            elif it == 3:
                pass
            elif it == 4:
                self.name = str(val)
            elif it == 5:
                self.description = str(val)
            elif it == 6:
                self.balance = float(val)
            elif it == 7:
                pass
            elif it == 8:
                pass
            
            self.excluded = False

            

    def printPost(self):
        print("Date: " + str(self.date))
        print("Amount: " + str(self.amount))
        print("Name: " + str(self.name))
        print("Description: " + str(self.description))
        print("Balance: " + str(self.balance))
        print("Excluded: " + str(self.excluded))

    def getAmount(self):
        return int (self.amount)




class postList:

    def __init__(self):
        self.listOfPosts = []
        self.expenseSum = 0
        self.incomeSum = 0

    def addPost(self, post):
        self.listOfPosts.append(Post(post))
        if self.listOfPosts[-1].getAmount() < 0:
            self.expenseSum += self.listOfPosts[-1].getAmount()

        else:
            self.incomeSum += self.listOfPosts[-1].getAmount()

    def removePost(self, index):
        try:
            print("Removing post " + str(index))
            self.listOfPosts[index].remove()

        except Exception as e:
            print(e)

    def printPosts(self):
        for it, post in enumerate(self.listOfPosts):
            print()
            print("ID: " + str(it))
            post.printPost()

    def setPostExclusion(self, postId, excluded):
        self.listOfPosts[postId].excluded = excluded

    def getExpenses(self):
        return self.expenseSum

    def getIncome(self):
        return self.incomeSum

    def getInOutBalance(self):
        return self.expenseSum + self.incomeSum

    def getExpensesPerDay(self):

        self.calculateExpenses()

        daysInMonth = datetime.datetime.today().day
        return self.expenseSum/daysInMonth

    def calculateExpenses(self):


        self.expenseSum = 0

        for post in self.listOfPosts:
            if post.amount < 0 and post.excluded == False:
                self.expenseSum += post.amount

    

    def runthroughExclude(self):

        for it, post in enumerate(self.listOfPosts):
            print()
            print("ID: " + str(it))
            post.printPost()
            exclude = input("Exclude [y/n]: ")

            match exclude:
                case 'y':
                    print("Exluding post: " + str(it))
                    self.listOfPosts[it].excluded = True
                case 'Y':
                    print("Exluding post: " + str(it))
                    self.listOfPosts[it].excluded = True
            #if exclude == "y" or exclude == "Y":
                

        print("Exclusion done!")


    def categorizePosts(self):
        pass


listObj = postList()

def parseFile(fileName):
    

    with open(fileName, mode='r') as infile:
        readers = csv.reader(infile)
        for it, row in enumerate(readers):
            if it == 0:
                continue
            listObj.addPost(row)

    print("Expenses: " + str(listObj.getExpenses()) + " DKK")
    print("Income: " + str(listObj.getIncome()) + " DKK")
    print("In/Out Balance: " + str(listObj.getInOutBalance()) + " DKK")
    print("Expenses / Day: " + str(listObj.getExpensesPerDay()) + " DKK")



    