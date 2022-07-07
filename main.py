from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)         #to automatically load changes development server in prodcution server it is false