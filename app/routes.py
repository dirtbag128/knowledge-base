from flask import Blueprint, render_template, request, jsonify, abort, send_from_directory
from app.utils import get_all_notes, get_note_by_id, generate_quiz, get_quiz_files
from app.utils import get_all_notes, get_note_by_id, generate_quiz, get_quiz_files, search_notes
import os

bp = Blueprint('main', __name__)

@bp.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        results = search_notes(query)
    else:
        results = []
    return render_template('search_results.html', results=results, query=query)

@bp.route('/')
def index():
    notes_by_dir = get_all_notes()
    return render_template('index.html', notes_by_dir=notes_by_dir)

@bp.route('/notes/<path:note_id>')
def note(note_id):
    note = get_note_by_id(note_id)
    if note is None:
        abort(404)
    return render_template('note.html', note=note)

@bp.route('/quiz')
def quiz_page():
    quiz_files = get_quiz_files()
    return render_template('quiz.html', quiz_files=quiz_files)

@bp.route('/api/quiz', methods=['GET'])
def get_quiz():
    directory = request.args.get('directory', '')
    num_questions = int(request.args.get('num_questions', 10))
    quiz = generate_quiz(directory, num_questions)
    return jsonify(quiz)

@bp.route('/static/notes/<path:filename>')
def serve_note_images(filename):
    return send_from_directory(os.path.join(bp.root_path, '..', 'notes'), filename)

@bp.route('/static/compiled_notes/<path:filename>')
def serve_compiled_notes(filename):
    return send_from_directory(os.path.join(bp.root_path, 'static', 'compiled_notes'), filename)