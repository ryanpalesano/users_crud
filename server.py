from user import User
from flask import Flask, redirect, request, render_template

app = Flask(__nono---name__)

# View ALL USERS

@app.route('/users')
def index():
    return redirect('/')


@app.route('/')
def users():
    context = {
        'users': User.get_all()
    }
    return render_template("read_all.html", **context)

# Create NEW USER


@app.route('/users/new')
def new():
    return render_template("create.html")


@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

# EDIT USER

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    context = {
        'user': User.get_one(data)
    }
    return render_template("edit.html", **context)


@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

# SHOW one user


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    context = {
        'user': User.get_one(data)
    }
    return render_template("read_one.html", **context)

# DELETE one user


@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    data = {
        'id': user_id
    }
    User.delete(data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)


# left one goes in the html

# right one goes in from the data 
