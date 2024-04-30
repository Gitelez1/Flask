# from flask import Flask, render_template, request, redirect # added request
            
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     return redirect('/')







# from flask import Flask, render_template
# app = Flask(__name__)
# # our index route will handle rendering our form
# @app.route('/')
# def index():
#     return render_template("index.html")
# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase= "Hello!", times=5)  # Return the string 'Hello World!' as a response

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>') 
def hello(name, num):
    return f"Hello, {name * num}"

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
    # app.run(debug=True) should be the very last statement! 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

