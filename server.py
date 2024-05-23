from flask_app import app

<<<<<<< HEAD
from flask_app.controllers import users, recipes

if __name__=="__main__":
    app.run(debug=True)
=======
from flask_app.controllers import dojos, ninjas

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
>>>>>>> c57550f7a86a6ed1eda65b615e775c83b09aef27
