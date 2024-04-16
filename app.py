from flask import Flask, render_template, request, redirect, url_for
import pyautogui
import time

app = Flask(__name__)

def spam_message(message, count, delay):
    for _ in range(count):
        pyautogui.typewrite(message)
        time.sleep(delay)  # Adjust the delay between each message as needed
        pyautogui.press('enter')
        time.sleep(0.01)  # Adjust the delay after sending each message as needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        count = request.form['count']
        delay = request.form['delay']
        try:
            count = int(count)
            delay = float(delay)
            if count > 0 :
                # Redirect to the spamming route after a delay
                return redirect(url_for('spam_with_delay', message=message, count=count, delay=delay))
            else:
                return "Please enter valid values for count and delay."
        except ValueError:
            return "Invalid input for count or delay. Please enter valid numbers."
    return render_template('index.html')

@app.route('/spam_with_delay/<message>/<int:count>/<int:delay>', methods=['GET'])
def spam_with_delay(message, count, delay):
    time.sleep(10)  # 10-second delay only at the start
    spam_message(message, count, delay)
    return "Spamming completed!"


