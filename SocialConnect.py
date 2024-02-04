

# Programmed three profiles of a social media page using Python Object Oriented Programming.

# define the name of the class
class Profile:
    # creating constructor
    def __init__(self,username,bio):
        
        self.username = username
        self.bio = bio
        #default = followers = 0
        self.followers = 0
    def __str__(self):
        
        return("Profile Username: " + self. username + "  Bio: " + self.bio + "  Followers: " + str(self.followers))
    
    # getter for username
    def getUsername (self):
        return self.username
    # getter for username
    def getBio (self):
        return self.bio
    #getter for followers
    def getFollowers (self):
        return self.followers
    # setter for followers
    def setFollowers (self,newFollowers):
        self.followers = newFollowers 

   


# Function askAcctQuestionnaire asks the user the questions provided as an argument (questionList) and returns their answers as a list
def askAcctQuestionnaire(questionList):
    # Initialize an empty answer list
    answerList = []

    # For each question provided in the list of questions
    for question in questionList:
        # Ask the user for their response to that question
        response = input(question)
        # Add their answer to the list of answers
        answerList.append(response)

    # Return the list of answers
    return answerList

def main():
    #list of questios
    listOfQuestionnaire= ["what is your username?","What is your bio?"]
    # empty list
    listOfMyProfiles = []
    # creating 3 instances of the Profile class
    for x in range(3):
        userAnswers = askAcctQuestionnaire(listOfQuestionnaire) 
        listOfMyProfiles.append(Profile(userAnswers[0],userAnswers[1]))
    # a loop to print each of the 3 Profiles 
    for i in listOfMyProfiles: 
        print (i)
        print()
        
    # calling the setter for followers
    listOfMyProfiles[0].setFollowers (2)
    print(listOfMyProfiles[0])
    
    
    
    
    
    

if __name__ == "__main__":
    main()