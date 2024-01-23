from flask_app import create_app
from flask import render_template

app = create_app()

@app.errorhandler(500)
def internal_error(error):
    return render_template('500_error/500_error.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404_error/404_error.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)