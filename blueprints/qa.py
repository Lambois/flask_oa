from flask import Blueprint,render_template,request,redirect,g,url_for
from .forms import QuestionForm,AnswerForm
from models import QuestionModel,AnswerModel
from exts import db
from decorators import login_required

bp = Blueprint("qa",__name__,url_prefix='/')

@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    # print(questions)
    return render_template('index.html',questions = questions)

@bp.route("/qa/public",methods = ['GET','POST'])
@login_required
def public_qa():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.data['title']
            content = form.data['content']
            question = QuestionModel(title=title,content=content,author = g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for('qa.public_qa'))

@bp.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)



@bp.post("/answer/public")
@login_required
def answer_public():
    form = AnswerForm(request.form)
    if form.validate():
        question_id = form.data['question_id']
        content = form.data['content']
        answer = AnswerModel(content=content,question_id=question_id, author_id = g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail",qa_id = question_id))
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail",qa_id = request.form.get("question_id")))


@bp.route("/search")
def search():
    q = request.args.get("q")
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html",questions=questions)