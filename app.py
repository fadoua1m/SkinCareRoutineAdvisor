from flask import Flask, render_template, request, redirect, url_for, session
from knowledge_base import questions, suggest_routine

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You need a secret key for sessions

@app.route('/')
def start():
    session['answers'] = {}
    session['current_index'] = 0
    print("Session Initialized: ", session)  # Debugging session initialization
    return redirect(url_for('ask_question'))

@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    current_index = session.get('current_index', 0)
    
    if current_index < len(questions):
        question = questions[current_index]
        
        if request.method == 'POST':
            user_choice = request.form['choice']
            # Debugging: print selected choice and current answers            
            session['answers'][question['question']] = user_choice  # Save answer
            session['current_index'] = current_index + 1  # Move to next question
            
            return redirect(url_for('ask_question'))  # Move to next question
        
        return render_template('chat.html', question=question, index=current_index + 1)
    
    else:
        user_answers = session.get('answers', {})
        routine = suggest_routine(user_answers)  # Suggest a routine based on answers
        
        return render_template('chat.html', routine=routine)

if __name__ == '__main__':
    app.run(debug=True)
