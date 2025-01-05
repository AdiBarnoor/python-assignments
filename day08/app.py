from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Necessary for session handling

# Generate a new random number
@app.route('/new_game')
def new_game():
    session['secret_number'] = random.randint(1, 20)
    session['guesses'] = 0
    session['message'] = "I have thought of a number between 1 and 20. Try to guess it!"
    session['guess_history'] = []  # Track guesses and feedback
    session['game_over'] = False  # Track if the game is over
    return redirect(url_for('index'))

@app.route('/')
def index():
    # Render the main page
    return render_template(
        'index.html',
        message=session.get('message', ''),
        guesses=session.get('guesses', 0),
        guess_history=session.get('guess_history', []),
        game_over=session.get('game_over', False)
    )

@app.route('/guess', methods=['POST'])
def guess():
    # Handle guesses
    if 'secret_number' not in session:
        return redirect(url_for('new_game'))

    secret_number = session['secret_number']
    user_input = request.form['guess'].strip().lower()

    # If the user chooses to exit the game
    if user_input == 'x':
        session['message'] = "Exiting the game. Thanks for playing!"
        session.pop('secret_number', None)  # Clear session to end the game
        session['game_over'] = True
        return redirect(url_for('index'))

    # Start a new game
    elif user_input == 'n':
        return redirect(url_for('new_game'))

    # Show the secret number
    elif user_input == 's':
        session['message'] = f"The hidden number is: {secret_number}"
        session['guesses'] -= 1  # Don't count showing the number as a guess
        return redirect(url_for('index'))

    # Validate input
    if not user_input.isdigit():
        session['message'] = "Invalid input. Please enter a whole number between 1 and 20."
        return redirect(url_for('index'))

    guess = int(user_input)
    session['guesses'] += 1

    # Process the guess
    if guess < secret_number:
        feedback = f"{guess} is too small!"
    elif guess > secret_number:
        feedback = f"{guess} is too big!"
    else:
        feedback = f"{guess} is correct! You've guessed the number in {session['guesses']} tries."
        session['game_over'] = True
        session.pop('secret_number', None)  # End the game by removing the secret number

        # Save the successful guess and number of tries
        session['guess_history'].append(
            {'guessed_number': guess, 'tries': session['guesses']}
        )

    # Add feedback to guess history for incorrect guesses
    if not session['game_over']:
        session['guess_history'].append(
            {'guessed_number': guess, 'feedback': feedback}
        )

    session['message'] = feedback
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
