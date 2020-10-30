from flask import Flask, render_template
from flask import request
import csv
from time import gmtime, strftime
from datetime import datetime

app = Flask(__name__)
  
@app.route('/')
@app.route('/homepage')
def index():
	return render_template('Homepage.html')

@app.route('/booking')
def bookings():
   with open('static/bookings.csv', 'r') as inFile:
      reader = csv.reader(inFile)
      aList = [row for row in reader]# For each row in the reader create a row in a List. // 
         
   return render_template('Request_booking.html', aList = aList)
   
@app.route('/book', methods=['POST'])
def get_booking():
   room= request.form['room'] # get their room choice and compare it
   if room == 'r1':
      roomchoice = 'Room 1'
   elif room =='r2':
      roomchoice = 'Room 2'
   elif room == 'r3':
      roomchoice = 'Room 3'
   elif room == 'r4':
      roomchoice = 'Room 4'
   elif room == 'r5':
      roomchoice = 'Room 5'
   else:
      roomchoice = 'Room 6'


   # add the new entry
   name = request.form[('name')]
   email = request.form[('email')]
   
   checkIn = request.form[('checkIn')]    # get check in information
   checkIn, checkInStr = processDate(checkIn)
   
   checkOut = request.form[('checkOut')]  # get check out information
   checkOut, checkOutStr = processDate(checkOut)
   
   error = "" # create an error string that we can populate if there is an error
   
   if checkIn < datetime.now():
      error = "Please enter a valid check in date."
   
   if checkOut < datetime.now():
      error = "Please enter a valid check out date."
   
   if checkIn > checkOut:
      error = "Please enter a check in date before check out date."
   bookingFile = 'static/bookings.csv'

      # save the updated booking list back to the file if their is no error
   if not error:
      time= strftime("%d-%m-%Y %H:%M:%S", gmtime())

	  # read the bookings from the csv
      bookingList = readFile(bookingFile)

	  # if user hasn't added anything then dont add it
      newBooking = [name, email, roomchoice, checkInStr, checkOutStr, time]
      bookingList.append(newBooking)

      writeFile(bookingList, bookingFile)

   with open('static/bookings.csv', 'r') as inFile:
      reader = csv.reader(inFile)
      aList = [row for row in reader]# For each row in the reader create a row in a List. 
		
   return render_template('request_booking.html', error=error, bookingFile = bookingFile, aList = aList)   

@app.route('/local_attractions') 
def local_attractions():
	return render_template('Local_Attractions.html')

@app.route('/reviews')
def reviews():
   with open('static/reviews.csv', 'r') as inFile: # reads reviews in file
      reader = csv.reader(inFile)
      aList = [row for row in reader]# For each row in the reader create a row in a List.  
         
   return render_template('reviews.html', aList = aList)

@app.route('/addReview', methods=['POST']) 
def addReview():
   # read the reviews from the csv
   reviewFile = 'static/reviews.csv'
   reviewList = readFile(reviewFile)
   
   # add the new entry
   userName = request.form[('name')]
   review = request.form[('review')]
   time= strftime("%d-%m-%Y %H:%M:%S", gmtime())
   
   # if user hasn't added anything then don't add it
   newReview = [userName, review, time]
   reviewList.append(newReview)
   
   # save the updated review list back to the file
   writeFile(reviewList, reviewFile)
   
   with open('static/reviews.csv', 'r') as inFile:
      reader = csv.reader(inFile)
      aList = [row for row in reader]# For each row in the reader create a row in a List. //
   
   return render_template('reviews.html', reviewFile = reviewFile, aList = aList)

def readFile(aFile):
#read in 'aFile'
   with open(aFile, 'r') as inFile:
      reader = csv.reader(inFile)
      reviewList = [row for row in reader]
   return reviewList


def writeFile(aList, aFile):
#write 'aList' to 'aFile'
   with open(aFile, 'w', newline='') as outFile:
      writer = csv.writer(outFile)
      writer.writerows(aList)
   return
  
def processDate(aDate): # function used to standardise the date input
   dt = None
   try:
      dt = datetime.strptime(aDate, '%d-%m-%Y')
   except:
      dt = datetime.strptime(aDate, '%Y-%m-%d')
   print(dt)
   return dt, datetime.strftime(dt, "%d-%m-%Y")



if __name__ == '__main__':
    app.run(debug = True)

