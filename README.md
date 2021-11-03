## API-L

Created a HTTP-API that allows reading, writing, deleting & updating data from database.

### Application routes
POST/ - creates a new person

GET/ - view a list of all people

GET/{id} - view a single person

PUT/{id} - update person

DELETE/{id} - delete a person


### Installing Development Environment
#### 1. Install pipenv

     pip install --user pipenv
   
#### 2. Create Virtual Environment & Install dependencies
      
     pipenv install -r requirements.txt --python=python3
   
#### 3. Activate Virtual Environment

     pipenv shell
     
#### 4. Run Server
  
     uvicorn main:app --reload
   
#### 5. Launch browser

     Launch browser to http://localhost:8000/docs/ 
