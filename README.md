## API-L

Created a HTTP-API that allows reading, writing, deleting & updating data from database.

### Application routes
POST/ - creates a new person

GET/ - view a list of all people

GET/{id} - view a single person

PUT/{id} - update person

DELETE/{id} - delete a person


### How to run project
  #install requirements
  
  `pip install -r requirements.txt`
  
  #configure location of database
  
  `export MONGODB_URL="mongodb://localhost:27017/<db>?retryWrites=true&w=majority"`
  
  #start the service
  
  `uvicorn main:app --reload`
