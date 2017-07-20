import pygame
import time
from random import randint
from pygame.locals import *
pygame.init()
#importing the pygame module, the time module and the random module and initializing the pygame module


size = (400, 435)
#this will be the size of the game window
screen = pygame.display.set_mode(size)
#setting the size of the game window
pygame.display.set_caption("THE CLASSROOM")
#this sets the title of the game window
background = pygame.image.load("newbackground.jpg").convert()
#this will be the background of the window during gameplay
infoscreen = pygame.image.load("blue.png").convert()
#this will be the background of the window when instructions are displayed


#STRINGS
myfont = pygame.font.SysFont("franklingothicmedium", 17)
bigfont = pygame.font.SysFont("franklingothicmedium", 50)
medfont = pygame.font.SysFont("franklingothicmedium", 30)
#these are the different sizes of fonts which will be used

#the following lines are strings of text which will be displayed at some point during the game
#it has the text, followed by antialias, and then the colour in RGB 
deskreach = myfont.render("YOU REACHED YOUR DESK!!!!!!!!", 20, (255, 255, 255))
notreach = myfont.render("YOU HAVEN'T REACHED YOUR DESK YET :(", 20, (255, 255, 255))

level1complete = myfont.render("LEVEL 1 COMPLETE!", 20, (135,206,235))
level2complete = myfont.render("LEVEL 2 COMPLETE!", 20, (135,206,235))
level3complete = myfont.render("LEVEL 3 COMPLETE!", 20, (135,206,235))
level4complete = myfont.render("LEVEL 4 COMPLETE!", 20, (135,206,235))
level5complete = myfont.render("LEVEL 5 COMPLETE!", 20, (135,206,235))
level6complete = myfont.render("YOU HAVE COMPLETED THE GAME!", 20, (135,206,235))

bumpteacher = myfont.render("YOU BUMPED INTO THE TEACHER!", 20, (255, 0, 0))
restart = myfont.render("YOU HAVE TO START AGAIN :(", 20, (0,191,255))

title = bigfont.render("THE CLASSROOM", 50, (20, 20, 20))
aim1 = myfont.render("AIM: You need to reach your desk using the arrow ", 1, (20, 20, 20))
aim2 = myfont.render("keys without bumping into any of the teachers. If you ", 1, (20, 20, 20))
aim3 = myfont.render("do bump into one, you will have to start again. When " , 1, (20, 20, 20))
aim4 = myfont.render("you reach your desk, press SPACE to sit down.", 1, (20, 20, 20))
giveup1 = myfont.render("If at any time during the game you would like to", 1, (20, 20, 20))
giveup2 = myfont.render("give up and stop playing, press G", 1, (20, 20, 20))

pagecollected = myfont.render("YOU COLLECTED A PAGE", 20, (135,206,235))
lefttocollect = myfont.render("YOU STILL NEED TO COLLECT ", 20, (255, 255, 255))
pages = myfont.render("PAGE(S)", 20, (255, 255, 255))
pagerequired = myfont.render("YOU HAVE COLLECTED ALL REQUIRED PAGES!", 20, (255, 255, 255))
pagecongrats = myfont.render("YOU HAVE COLLECTED 1 EXTRA PAGE!", 20, (255, 255, 255))
allpagescollected = myfont.render("YOU HAVE COLLECTED ALL POSSIBLE PAGES!", 20, (255, 255, 255))
notpages = myfont.render("YOU HAVEN'T COLLECTED ALL REQUIRED PAGES", 20, (255, 255, 255))

levfour1 = myfont.render("For further levels, you must collect a minimum " , 1, (20, 20, 20))
levfour2 = myfont.render("number of pages to sit down at your desk. You can " , 1, (20, 20, 20))
levfour3 = myfont.render("collect pages by pressing X when you reach them. " , 1, (20, 20, 20))
levfour4 = myfont.render("You can collect extra pages for bonus points!" , 1, (20, 20, 20))
levfour5 = myfont.render("For the next level, you must collect at least 3 pages." , 1, (20, 20, 20))

levfive1 = myfont.render("For LEVEL 5, you must collect at least 4 pages while" , 1, (20, 20, 20))
levfive2 = myfont.render("while also outrunning the teachers for at least 40 " , 1, (20, 20, 20))
levfive3 = myfont.render("seconds. New pages will appear every 10 seconds" , 1, (20, 20, 20))

levsix1 = myfont.render("For LEVEL 6, you must collect at least 5 pages while" , 1, (20, 20, 20))
levsix2 = myfont.render(" also outrunning the teachers for at least 40  " , 1, (20, 20, 20))
levsix3 = myfont.render("seconds. New pages will appear every 10 seconds" , 1, (20, 20, 20))

entertocont = myfont.render("Press ENTER to continue" , 1, (20, 20, 20))

tryagain = myfont.render("Would you like to play again?" , 1, (20, 20, 20))
tryagain2 = medfont.render("Y/N" , 1, (20, 20, 20))
gameover = bigfont.render("GAME OVER" , 1, (20, 20, 20))
bestscorestr = myfont.render("Best Score: " , 1, (20, 20, 20))
avgscorestr = myfont.render("Average Score: " , 1, (20, 20, 20))
scorestr = myfont.render("Score: " , 1, (20, 20, 20))


clock = pygame.time.Clock() 
#to control the frame rate

#NUMERICAL VARIABLES
teachpos = [(280, 164), (140, 164)]
#list with position of the two teachers displayed in LEVEL 1
teachercounter = 0
Score = 0 
avgscore = 0
bestscore = 0
steps = 0
#used to count the steps taken in each level 
scores = []
#list to store all scores, used to calculate best score and average score
collected = 0
#number of pages collected in each level
pagecounter = 0
levelstart = 0
#used for levels with timer
lastpagespawn = levelstart
#used for levels with timer, a new page is spawned every 10 seconds
teacherspeed = 0
#speed of teacher (how maany pixels the teacher moves each turn)
keep_going = True
#for the main game loop
LEVEL = 0
#keeps track of the current level
teacherlimit = 0          
game = True
#used for the loop that runs the movement function
giveup = False
#if the user gives up, their score will not be added to the list of scores


#THE DESKS
#initializing a sprite class for the desks
#it is easier to check collisions between sprites than rects
class Desks (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("newnewnewdesks.png").convert_alpha()
        #the '_alpha()' part makes the image have a transparent background
        self.rect = self.image.get_rect()
        self.rect.topleft = (130, 300)
        
desks = Desks()
#creates an object, 'desks', using the Desk sprite class


#THE STUDENT
#initializing a sprite class for the student
class Student (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bstudent.png").convert_alpha()
        #the '_alpha()' part makes the image have a transparent background
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 35)
            
    #this is where the student moves
    def update(self):
        #global declaration statements are required to edit the variables
        global Score
        global steps
        keys = pygame.key.get_pressed()
        
        if keys[K_LEFT] and self.rect.left  >= 5:
        #if the user has pressed the left arrow key and if moving left will not go off screen
            self.rect.centerx -= 5
            Score += 1
            steps += 1
            if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
            #for levels 5 and 6, the desks will only be available 40 seconds after the level has started
            #if the desk isn't available for the student yet, no need to check for collisions between the student and the desks  
                if (pygame.sprite.collide_rect(self, desks)):
                #this checks if the student is colliding with the desks sprite
                #i.e. will the student walk into one of the desks by moving left
                    self.rect.centerx += 5    #this cancels the previous movement
            if (pygame.sprite.spritecollideany(self, teachergroup)):
            #this checks if the student is colliding with any sprite in the Teacher group (did the student bump into a teacher?)
                displaystuff()
                teacherbump()
                
        elif keys[K_RIGHT] and self.rect.right < 400:
        #if the user has pressed the right arrow key and if moving right will not go off screen
            self.rect.centerx += 5
            Score += 1
            steps += 1
            if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
            #for levels 5 and 6, the desks will only be available 40 seconds after the level has started
                if (pygame.sprite.collide_rect(self, desks)):
                #this checks if the student is colliding with the desks sprite
                #i.e. will the student walk into one of the desks by moving right
                    self.rect.centerx -= 5    #this cancels the previous movement
            if (pygame.sprite.spritecollideany(self, teachergroup)):
            #this checks if the student is colliding with any sprite in the Teacher group (did the student bump into a teacher?)
                displaystuff()
                teacherbump()
                
        elif keys[K_DOWN] and self.rect.top <= 410:
        #if the user has pressed the down arrow key and if moving down will not go off screen
            self.rect.centery += 5
            Score += 1
            steps += 1
            if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
            #for levels 5 and 6, the desks will only be available 40 seconds after the level has started
                if (pygame.sprite.collide_rect(self, desks)):
                #this checks if the student is colliding with the desks sprite
                #i.e. will the student walk into one of the desks by moving down
                    self.rect.centery -= 5    #this cancels the previous movement
            if (pygame.sprite.spritecollideany(self, teachergroup)):
            #this checks if the student is colliding with any sprite in the Teacher group (did the student bump into a teacher?)
                displaystuff()
                teacherbump()
                
        elif keys[K_UP] and self.rect.top >= 40:
        #if the user has pressed the up arrow key and if moving up will not go off screen
            self.rect.centery -= 5
            Score += 1
            steps += 1
            if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
            #for levels 5 and 6, the desks will only be available 40 seconds after the level has started
                if (pygame.sprite.collide_rect(self, desks)):
                #this checks if the student is colliding with the desks sprite
                #i.e. will the student walk into one of the desks by moving up
                    self.rect.centery += 5    #this cancels the previous movement
            if (pygame.sprite.spritecollideany(self, teachergroup)):
            #this checks if the student is colliding with any sprite in the Teacher group (did the student bump into a teacher?)
                displaystuff()
                teacherbump()

student = Student()
#this creates an object, 'student', using the Student sprite class


#THE PAGES
#initializing a sprite class for the pages
class Page (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("page.png").convert_alpha()
        #the '_alpha()' part makes the image have a transparent background
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #the x and y position of the page will be given in the call to this class

pagegroup = pygame.sprite.Group()
#this initializes a sprite group to store all the page objects which will be created later


#this function displays everything in the game to the window
def displaystuff():
    global Score
    score = myfont.render(str(Score), 20, (138,43,226))
    #converting the Score to a string to display it
    screen.blit(background, (0, 0))
    screen.blit(student.image,student.rect)
    teachergroup.draw(screen)
    if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
    #in Levels 5 and 6 the desks will not displayed until 40 seconds have passed since the level began
    #the desks will only be displayed if it has been at least 40 seconds or if it is Level 4 or below
       screen.blit(desks.image,desks.rect)                                         
    screen.blit(score, (360, 0))
    if (LEVEL > 3):
    #if it's LEVEL 3 or higher, the pages will be displayed
        pagegroup.draw(screen)
        
    pygame.display.flip()
    #updates the screen   


#the function which is called when a page is collected by the student
#the total number of pages for the current level will be given as an argument in the call to this function
def collectpage (pagelimit):
    global Score
    screen.blit(pagecollected, (0, 0))
    
    if (collected == (pagelimit-2)):
    #if the student has collected the minimum number of pages
        screen.blit(pagerequired, (0, 15))
        Score -= 75
    elif (collected == (pagelimit-1)):
    #if the student has collected one extra page
        screen.blit(pagecongrats, (0, 15))
        Score -= 100
    elif (collected == pagelimit):
    #if the student has collected all possible pages
        screen.blit(allpagescollected, (0, 15))
        Score -= 125
    else:
    #otherwise, the number of required pages left to collect is displayed
        collectednum = myfont.render(str((pagelimit-2)-collected), 20, (255, 255, 255))
        screen.blit(collectednum, (215, 15))
        screen.blit(lefttocollect, (0, 15))
        screen.blit(pages, (230, 15))
        Score -= 75
        
    pygame.display.flip()
    #updates the screen
    pygame.time.delay(1000)
    #the program is paused for 1 second, so that the displayed text can be read

        
#THE TEACHER
#initializing a sprite class for the teachers
class Teacher (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("redteacher.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #the x and y position of the teacher will be given in the call to this class

    #this is where the teacher(s) will move and follow the student
    def update(self, move):
    #the number of pixels to move in each turn will be given in as an argument in the call to this function
        if (self.rect.centerx != student.rect.centerx):
        #if the teacher is not in the same column as the student
            if (self.rect.centerx < student.rect.centerx):
            #if the teacher is to the left of the student
                self.rect.centerx += move
                #move the teacher right
                if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
                #if the desks are supposed to be displayed 
                    if (pygame.sprite.collide_rect(self, desks)):
                    #this checks if the teacher is colliding with the desks sprite
                        self.rect.centerx -= move
                        #this cancels the previous movement
                    
            elif (self.rect.centerx > student.rect.centerx):
            #if the teacher is to the right of the student
                self.rect.centerx -= move
                #move the teacker left
                if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
                #if the desks are supposed to be displayed
                    if (pygame.sprite.collide_rect(self, desks)):
                    #this checks if the teacher is colliding with the desks sprite
                        self.rect.centerx += move
                    #this cancels the previous movement
                    
        if (self.rect.centery != student.rect.centery):
        #if the teacher is not in the same row as the student
            if (self.rect.centery < student.rect.centery):
            #if the teacher is above the student
                self.rect.centery += move
                #move the teacher down
                if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
                #if the desks are supposed to be displayed
                    if (pygame.sprite.collide_rect(self, desks)):
                    #this checks if the teacher is colliding with the desks sprite
                        self.rect.centery -= move
                        #this cancels the previous movement
                    
            elif (self.rect.centery > student.rect.centery):
            #if the teacher is below the student
                self.rect.centery -= move
                #move the teacher up
                if (LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5):
                #if the desks are supposed to be displayed
                    if (pygame.sprite.collide_rect(self, desks)):
                    #this checks if the teacher is colliding with the desks sprite
                        self.rect.centery += move
                        #this cancels the previous movement
                    
        displaystuff()

teachergroup = pygame.sprite.Group()
#this initializes a sprite group to store the teacher objects which will be created later

    
#the function which is called when the student bumps into a teacher
def teacherbump():
    global teachercounter
    global collected
    global pagecounter
    global Score
    global levelstart
    #declaring the global variables to be able to edit them

    #everything is reset for the current level
    student.__init__()
    #resets the student back to the starting position
    teachercounter = 0
    steps = 0
    pagecounter = 0
    collected = 0
    Score += 100
    #penalty for bumping into the teacher
    
    levelstart = pygame.time.get_ticks()
    #this is for the timed levels, this variable will be used to check if it has been 40 seconds since the level started
    pagegroup.empty()
    teachergroup.empty()
    #the previously created pages and teachers for this level will be deleted
    screen.blit(bumpteacher, (0, 0))
    screen.blit(restart, (0, 15))
    #'you bumped into a teacher' and 'you have to restart' messages displayed
    pygame.display.flip()
    #updates the screen
    pygame.time.delay(1000)
    #the program is paused for 1 second, so that the displayed text can be read
    displaystuff()


#this function is used to check for collisions between newly created pages and teachers and the rest of the game objects
#this is necessary because the pages and teachers will get randomly generated x and y positions
def checkforcollide(check):
#the object to check for collisions will be given as an argument in the call to this function
    if (pygame.sprite.collide_rect(check, desks)):
    #if the given object will overlap the desks
        return (True)
    elif (pygame.sprite.spritecollideany(check, teachergroup)):
    #if the given object will overlap any of the already created teachers
        return (True)
    elif (pygame.sprite.spritecollideany(check, pagegroup)):
    #if the given object will overlap any of the already created pages
        return (True)
    elif (pygame.sprite.collide_rect(check, student)):
    #if the given object will overlap with the student
        return (True)

#function for the movement of the player
#the main gameplay and creation of teachers and pages occur here
def maingamecode():
    global collected
    global teachercounter
    global steps
    global pagecounter
    global LEVEL
    global teacherlimit
    global levelstart
    global lastpagespawn
    #all global variables are declared so they can be edited
    
    clock.tick(30)
    #constant frame rate, argument -> frames per second
    displaystuff()

    if (steps == 1):
    #if the student has moved once in the current level
        levelstart = pygame.time.get_ticks()
        lastpagespawn = levelstart
        #this is so that the 40 second timer for Levels 4, 5, and 6 only starts when the student moves
        #otherwise the student can just stay in the initial position until the desks are displayed with no teachers to outrun

    if (LEVEL == 1):
    #for Level 1, the two teachers are stationary with predetermined positions
        for i in range (2):
            teacher = Teacher(teachpos[i][0], teachpos[i][1])
            #this creates a teacher object with the teacher sprite class
            #the position of the teacher is taken from a list initialized at the top
            teachergroup.add(teacher)
            #this adds the newly created teacher object to the teacher group

    elif (LEVEL == 2):
        teacherlimit = 15
        #15 teachers will be spawned randomly on the screen for Level 2
                
    elif (LEVEL == 3):
        teacherlimit = 3
        #3 teachers will follow the student in Level 3
            
    elif (LEVEL >= 4):
        teacherlimit = 2
        #2 teachers will follow the student in Level 4 and higher
            
    if ((LEVEL == 2 and steps %7 == 0 and steps > 0) or LEVEL >= 3):
    #for Level 2, the teachers will spawn at even intervals so they could possibly spawn right in front of the teacher
    #otherwise, the teachers will spawn before the student begins moving and it will be easier - not as fun
    #for Levels 3 and higher however, the teachers will begin following the student as soon as the level starts
        if (teachercounter < teacherlimit):
            loop = True
            #this while loop will keep running until a teacher object which does not collide with any other game object has been created
            while loop:
                teacher = Teacher(randint(0, 380), randint(35, 375))
                #a teacher object is created using the teacher sprite class
                #the x and y position are randomly generated
                if (checkforcollide(teacher) != True):
                #if the new teacher object doesn't collide with anything
                    if ((teacher.rect[0] >= 275 and teacher.rect[0] <= 295) and teacher.rect[1] == 280):
                    #if the teacher is in front of the student's desk, that is unfair
                    #so in that case, the new teacher object will not be added to the group
                        continue
                    else:
                        teachergroup.add(teacher)
                        #the new teacher object is added to the teacher group
                        teachercounter += 1
                        loop = False
                        #loop will stop
     
    if (LEVEL == 4):
        teacherspeed = 1
        pagelimit = 5
        #for Level 4, 5 total pages to collect and the teacher will move 1 pixel at a time
    elif (LEVEL == 5):
        teacherspeed = 1
        pagelimit = 6
        #for Level 5, 6 total pages to collect and the teacher will move 1 pixel at a time
    else:
        teacherspeed = 2
        pagelimit = 7
        #for Level 6, 7 total pages to collect and the teacher will move 2 pixels at a time (slightly faster)

    if (LEVEL >= 3):
    #the teachers only follow the student in Levels 3 and higher
        teachergroup.update(teacherspeed)
        #the teacher update function is called with the 'speed' of the teacher for the current level
        if (pygame.sprite.spritecollideany(student, teachergroup)):
        #this checks if the student is colliding with any sprite in the Teacher group
            displaystuff()
            teacherbump()

    if (LEVEL >= 4):
    #the pages are only an element of the game in Levels 4 and higher
        x = pygame.time.get_ticks() - lastpagespawn
        if (pagecounter < pagelimit and steps != 0):
        #the pages will only be displayed after the student begins moving
            if ((LEVEL >= 5 and (x >= 10000 or pagecounter >= pagelimit-2)) or (LEVEL == 4)):
            #in Level 4, the pages are displayed all at once
            #in Levels 5 and 6, the required pages are only displayed every 10 seconds
            #the last required page and all extra pages will be displayed at once
                loop = True
                #this while loop will continue looping until a page object which does not collided with anything is created
                while loop:
                    page = Page(randint(0, 380), randint(35, 375))
                    #a page object is created using the page sprite class
                    #the x and y position are randomly generated
                    if (checkforcollide(page) != True):
                        pagegroup.add(page)
                        #the new page object is added to the page group
                        pagecounter += 1
                        lastpagespawn = pygame.time.get_ticks()
                        #the last time a page spawned is stored for the timer (page every 10 seconds)
                        loop = False
                        #the loop will stop
                    
    student.update()
    #this updates the position of the student with the user input
    
    keyy = pygame.key.get_pressed()
    if (LEVEL > 3):
    #the user has to press 'X' to collect pages and pages are only available in Level 4 and higher
        if keyy[K_x]:
        #if the user has pressed 'X'
            if (pygame.sprite.spritecollide(student, pagegroup, True)):
            #if the student is colliding with any of the pages in the page group
            #that particular page will be removed from the page group
                collected += 1
                collectpage(pagelimit)
                
    if keyy[K_SPACE]:
    #if the user has pressed the spacebar
        if ((LEVEL >= 5 and pygame.time.get_ticks()-levelstart >=40000) or (LEVEL < 5)):
        #if the desk is available to the student
            if ((student.rect[0] >= 275 and student.rect[0] <= 295) and student.rect[1] == 280):
            #if the student is actually in front of their desk
                if ((LEVEL > 3 and collected >=3) or (LEVEL < 4)):
                #if pages must be collected for the current level, have they collected the required pages?
                    displaystuff()
                    screen.blit(deskreach, (0, 0))
                    pygame.display.flip()
                    #updates the screen
                    pygame.time.delay(1000)
                    #the program is paused for 1 second, so that the displayed text can be read
                    displaystuff()
                    
                    if LEVEL == 1:
                        screen.blit(level1complete, (0, 0))
                    elif LEVEL == 2:
                        screen.blit(level2complete, (0, 0))
                    elif LEVEL == 3:
                        screen.blit(level3complete, (0, 0))
                    elif LEVEL == 4:
                        screen.blit(level4complete, (0, 0))
                    elif LEVEL == 5:
                        screen.blit(level5complete, (0, 0))
                    elif LEVEL == 6:
                        screen.blit(level6complete, (0, 0))
                    #the respective level success messages are displayed according to the current level
                    
                    pygame.display.flip()
                    #updates the screen
                    pygame.time.delay(1000)
                    #the program is paused for 1 second, so that the displayed text can be read
                    displaystuff()
                    LEVEL += 1
                    #the player will proceed to the next level
            
                    return (True)
                
                elif (LEVEL > 3 and collected < 3):
                #if the student has not collected all the required pages
                    collectednum = myfont.render(str(3-collected), 20, (255,255,255))
                    screen.blit(notpages, (0, 0))
                    screen.blit(collectednum, (215, 15))
                    screen.blit(lefttocollect, (0, 15))
                    screen.blit(pages, (230, 15))
                    #the number of pages they still have to collect is displayed
                    pygame.display.flip()
                    #updates the screen
                    pygame.time.delay(1000)
                    #the program is paused for 1 second, so that the displayed text can be read
                        
            else:
                screen.blit(notreach, (0, 0))
                #'you have not reached your desk yet' message displayed
                pygame.display.flip()
                    #updates the screen
                pygame.time.delay(1000)
                    #the program is paused for 1 second, so that the displayed text can be read
                    
    

#this function displays instructions for the starting screen
def startscreen():
    global LEVEL
    
    screen.blit(infoscreen, (0, 0))
    screen.blit(title, (12, 5))
    screen.blit(aim1, (10, 80))
    screen.blit(aim2, (10, 100))
    screen.blit(aim3, (10, 120))
    screen.blit(aim4, (10, 140))
    screen.blit(giveup1, (10, 180))
    screen.blit(giveup2, (10, 200))
    screen.blit(entertocont, (110, 270))
    #the title of the game and the objective along with instructions are displayed
    #give up option displayed too
    pygame.display.flip()
    #updates the screen
    going = True
    #this loop will continue until the user presses enter
    while going:
        for ev in pygame.event.get():
            if ev.type == KEYDOWN:
            #if the user has pressed a key
                if ev.key == K_RETURN:
                #if the user has pressed enter
                    LEVEL += 1
                    #will proceed to Level 1
                    going = False
                    #loop will stop


"""MAIN CODE"""
#this loop will continue until 'keep_going' becomes false
#(until the game ends and user does not want to play again or they close the window)
while keep_going:
        
    if (LEVEL == 0):
    #starting screen is displayed first
        startscreen()
        
    student.__init__()
    #student is initialized and reset to the starting position
    teachercounter = 0
    steps = 0
    pagecounter = 0
    collected = 0
    pagelimit = 0
    game = True
    teachergroup.empty()
    pagegroup.empty()
    #teacher and page groups are emptied of all objects
    displaystuff()
    
    if (LEVEL == 6):
    #the instructions specific to Level 6 will be displayed
        levelstart = pygame.time.get_ticks()
        screen.blit(infoscreen, (0, 0))
        screen.blit(levsix1, (10, 80))
        screen.blit(levsix2, (10, 100))
        screen.blit(levsix3, (10, 120))
        screen.blit(entertocont, (110, 270))
        pygame.display.flip()
        #updates the screen

        going = True
        #this while loop will continue until the user presses enter
        while going:
            for ev in pygame.event.get():
                if ev.type == KEYDOWN:
                #if the user has pressed a key
                    if ev.key == K_RETURN:
                    #if the user has pressed enter
                        going = False
                        #the loop will stop

    elif (LEVEL == 5):
    #the instructions specific to Level 5 will be displayed
        levelstart = pygame.time.get_ticks()
        screen.blit(infoscreen, (0, 0))
        screen.blit(levfive1, (10, 80))
        screen.blit(levfive2, (10, 100))
        screen.blit(levfive3, (10, 120))
        screen.blit(entertocont, (110, 270))
        pygame.display.flip()
        #updates the screen
            
        going = True
        #this while loop will continue until the user presses enter
        while going:
            for ev in pygame.event.get():
                if ev.type == KEYDOWN:
                #if the user has pressed a key
                    if ev.key == K_RETURN:
                    #if the user has pressed enter
                        going = False
                        #the loop will stop
                        
    elif (LEVEL == 4):
    #the instructions specific to Level 4 will be displayed
        screen.blit(infoscreen, (0, 0))
        screen.blit(levfour1, (10, 80))
        screen.blit(levfour2, (10, 100))
        screen.blit(levfour3, (10, 120))
        screen.blit(levfour4, (10, 140))
        screen.blit(levfour5, (10, 160))
        screen.blit(entertocont, (110, 270))
        pygame.display.flip()
            
        going = True
        #this while loop will continue until the user presses enter
        while going:
            for ev in pygame.event.get():
                if ev.type == KEYDOWN:
                #if the user has pressed a key
                    if ev.key == K_RETURN:
                    #if the user has pressed enter
                        going = False
                        #the loop will stop
                        
    while game and maingamecode() != True:
    #'game' is true
    #this loop will continue until either 'game' becomes false or the maingamecode function returns True
    #the function will only return True when a level has been completed
        for ev in pygame.event.get():
            if ev.type == QUIT:
            #if the user closes the game window
                pygame.quit()
                exit()
                #the window will close
            if ev.type == KEYDOWN:
            #if the user has pressed a key
                if ev.key == K_g:
                #if the user has pressed 'G'
                    LEVEL = 7
                    #the end screen
                    giveup = True
                    #somwthing
                    game = False
                    #this loop will stop
                    

    if (LEVEL == 7):
    #if all the levels have been completed or if the user has given up
        if giveup == False:
            scores.append(Score)
            #the current score is added to the scores list
        scores.sort()
        #the scores list is sorted in ascending order
        if (giveup == False):
        #if the user hasn't just given up
            bestscore = scores[0]
        #the first element of the scores list will be the lowest
        #since the aim is to get the lowest score, the first element will be the best score
            avgscore =(sum(scores))/(len(scores))
            #the sum of all elements of the scores list divided by the length of the scores list gives the average score
        if (giveup == True and bestscore == 0):
        #if the user has given up and hasn't finished the game completely at least once
            avgscore = 0
        screen.blit(infoscreen, (0, 0))
        screen.blit(tryagain, (97, 270))
        screen.blit(tryagain2, (173, 290))
        screen.blit(gameover, (68, 15))
        screen.blit(avgscorestr, (105, 70))
        screen.blit(bestscorestr, (105, 85))
        screen.blit(scorestr, (105, 100))
        avgscorenum = myfont.render(str(avgscore), 20, (20, 20, 20))
        bestscorenum = myfont.render(str(bestscore), 20, (20, 20, 20))
        scorenum = myfont.render(str(Score), 20, (20, 20, 20))
        screen.blit(avgscorenum, (245, 70))
        screen.blit(bestscorenum, (245, 85))
        screen.blit(scorenum, (245, 100))
        #the 'game over' message, try again option, and the scores are displayed
        pygame.display.flip()
            
        going = True
        #this while loop will continue until the user presses enter
        while going:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                #if the user closes the game window
                    pygame.quit()
                    exit()
                    #the window will close
                    
                if ev.type == KEYDOWN:
                #if the user presses a key
                    if ev.key == K_y:
                    #if the user presses 'Y', if they want to play again
                        LEVEL = 0
                        #they will be taken to the starting screen
                        Score = 0
                        #current score is reset to 0
                        giveup = False
                        #giveup checker reset
                        going = False
                        #this loop will stop

                    elif ev.key == K_n:
                    #if the user does not want to play again
                        pygame.quit()
                        exit()
                        #the window will close
                        
