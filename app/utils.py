import os
import markdown
import shutil
import hashlib
from datetime import datetime
import random
import yaml

NOTES_DIR = 'notes'
HTML_DIR = 'app/static/compiled_notes'
QUIZ_DIR = 'quizzes'

def search_notes(query):
    results = []
    for root, _, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, HTML_DIR)[:-5]  # Remove .html extension
                with open(file_path, 'r') as f:
                    content = f.read()
                    title = content.split('</h1>')[0].split('>')[-1] if '<h1>' in content else rel_path
                    if query.lower() in title.lower() or query.lower() in content.lower():
                        results.append({'id': rel_path, 'title': title})
    return results

def md5_file(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def compile_markdown():
    if not os.path.exists(HTML_DIR):
        os.makedirs(HTML_DIR)

    changes_made = False
    hash_file = os.path.join(HTML_DIR, 'file_hashes.txt')
    old_hashes = {}

    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            for line in f:
                path, hash_value = line.strip().split('|')
                old_hashes[path] = hash_value

    new_hashes = {}

    for root, _, files in os.walk(NOTES_DIR):
        for file in files:
            if file.endswith('.md'):
                md_path = os.path.join(root, file)
                rel_path = os.path.relpath(md_path, NOTES_DIR)
                html_path = os.path.join(HTML_DIR, rel_path[:-3] + '.html')
                
                current_hash = md5_file(md_path)
                new_hashes[rel_path] = current_hash

                if rel_path not in old_hashes or old_hashes[rel_path] != current_hash:
                    os.makedirs(os.path.dirname(html_path), exist_ok=True)
                    with open(md_path, 'r') as md_file:
                        md_content = md_file.read()
                        # Split the content and skip the first heading
                        md_lines = md_content.split('\n')
                        first_non_heading = next((i for i, line in enumerate(md_lines) if not line.startswith('#')), 0)
                        md_content_without_title = '\n'.join(md_lines[first_non_heading:])
                        html_content = markdown.markdown(md_content_without_title, extensions=['fenced_code', 'codehilite', 'tables'])
                        with open(html_path, 'w') as html_file:
                            html_file.write(html_content)
                    changes_made = True

    # Remove old HTML files
    for root, _, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith('.html'):
                html_path = os.path.join(root, file)
                rel_path = os.path.relpath(html_path, HTML_DIR)[:-5] + '.md'
                if rel_path not in new_hashes:
                    os.remove(html_path)
                    changes_made = True

    # Update hash file
    with open(hash_file, 'w') as f:
        for path, hash_value in new_hashes.items():
            f.write(f"{path}|{hash_value}\n")

    return changes_made

def get_all_notes():
    notes_by_dir = {}
    
    for root, _, files in os.walk(HTML_DIR):
        dir_notes = []
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, HTML_DIR)[:-5]  # Remove .html extension
                with open(file_path, 'r') as f:
                    content = f.read()
                    title = content.split('</h1>')[0].split('>')[-1] if '<h1>' in content else rel_path
                    dir_notes.append({'id': rel_path, 'title': title})
        
        if dir_notes:
            dir_path = os.path.relpath(root, HTML_DIR)
            notes_by_dir[dir_path] = dir_notes

    return notes_by_dir

def get_note_by_id(note_id):
    html_path = os.path.join(HTML_DIR, note_id + '.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            content = f.read()
            title = content.split('</h1>')[0].split('>')[-1] if '<h1>' in content else note_id
            return {'id': note_id, 'title': title, 'content': content}
    return None

def parse_quiz_yaml(file_path):
    with open(file_path, 'r') as f:
        quiz_data = yaml.safe_load(f)
    
    for question in quiz_data:
        question['question'] = markdown.markdown(question['question'])
        question['options'] = [markdown.markdown(option) for option in question['options']]
        question['correct_answer'] = markdown.markdown(question['correct_answer'])
    
    return quiz_data

def get_quiz_files():
    quiz_files = []
    for root, _, files in os.walk(QUIZ_DIR):
        for file in files:
            if file.endswith('.yaml'):
                quiz_files.append(os.path.join(root, file))
    return quiz_files

def generate_quiz(directory='', num_questions=10):
    all_questions = []
    quiz_files = get_quiz_files()
    
    for file in quiz_files:
        if directory and not os.path.basename(file).startswith(directory):
            continue
        all_questions.extend(parse_quiz_yaml(file))
    
    selected_questions = random.sample(all_questions, min(num_questions, len(all_questions)))
    
    formatted_questions = []
    for q in selected_questions:
        formatted_questions.append({
            'question': q['question'],
            'options': q['options'],
            'correct_answer': q['correct_answer']
        })
    
    return formatted_questions

def render_markdown(text):
    return markdown.markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])