from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_index(idx):
    candidate = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден("
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidates_index(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def skill_candidates_index(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


if __name__ == '__main__':
    app.run(debug=True)
