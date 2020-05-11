from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
from environs import Env
import os

app = Flask(__name__)
CORS(app)
heroku = Heroku(app)
 
env = Env()
env.read_env()
DATABASE_URL = env("DATABASE_URL")

# test

basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


# Create ASL Quiz One Table
class AslQuizOne(db.Model):
    __tablename__ = "aslQuizOne"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    optionOneName = db.Column(db.String(500), nullable=False)
    optionOneUrl = db.Column(db.String(500), nullable=False)
    optionTwoName = db.Column(db.String(500), nullable=False)
    optionTwoUrl = db.Column(db.String(500), nullable=False)
    optionThreeName = db.Column(db.String(500), nullable=False)
    optionThreeUrl = db.Column(db.String(500), nullable=False)
    optionFourName = db.Column(db.String(500), nullable=False)
    optionFourUrl = db.Column(db.String(500), nullable=False)

    def __init__(self, questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        self.optionOneName = optionOneName 
        self.optionOneUrl = optionOneUrl 
        self.optionTwoName = optionTwoName
        self.optionTwoUrl = optionTwoUrl 
        self.optionThreeName = optionThreeName 
        self.optionThreeUrl = optionThreeUrl 
        self.optionFourName = optionFourName 
        self.optionFourUrl = optionFourUrl 


class AslQuizOneSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl', 'optionOneName', 'optionOneUrl', 'optionTwoName', 'optionTwoUrl', 'optionThreeName', 'optionThreeUrl', 'optionFourName', 'optionFourUrl')


aslQuizOne_schema = AslQuizOneSchema()
aslQuizOnes_schema = AslQuizOneSchema(many=True)


# Create ASL Quiz Two Table
class AslQuizTwo(db.Model):
    __tablename__ = "aslQuizTwo"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    optionOneName = db.Column(db.String(500), nullable=False)
    optionOneUrl = db.Column(db.String(500), nullable=False)
    optionTwoName = db.Column(db.String(500), nullable=False)
    optionTwoUrl = db.Column(db.String(500), nullable=False)
    optionThreeName = db.Column(db.String(500), nullable=False)
    optionThreeUrl = db.Column(db.String(500), nullable=False)
    optionFourName = db.Column(db.String(500), nullable=False)
    optionFourUrl = db.Column(db.String(500), nullable=False)

    def __init__(self, questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        self.optionOneName = optionOneName 
        self.optionOneUrl = optionOneUrl 
        self.optionTwoName = optionTwoName
        self.optionTwoUrl = optionTwoUrl 
        self.optionThreeName = optionThreeName 
        self.optionThreeUrl = optionThreeUrl 
        self.optionFourName = optionFourName 
        self.optionFourUrl = optionFourUrl 


class AslQuizTwoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl', 'optionOneName', 'optionOneUrl', 'optionTwoName', 'optionTwoUrl', 'optionThreeName', 'optionThreeUrl', 'optionFourName', 'optionFourUrl')


aslQuizTwo_schema = AslQuizTwoSchema()
aslQuizTwos_schema = AslQuizTwoSchema(many=True)

# Create ASL Quiz Three Table
class AslQuizThree(db.Model):
    __tablename__ = "aslQuizThree"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    

    def __init__(self, questionNum, answerName, answerUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        


class AslQuizThreeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl')


aslQuizThree_schema = AslQuizThreeSchema()
aslQuizThrees_schema = AslQuizThreeSchema(many=True)

# Create Braille Quiz One Table
class BrailleQuizOne(db.Model):
    __tablename__ = "brailleQuizOne"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    optionOneName = db.Column(db.String(500), nullable=False)
    optionOneUrl = db.Column(db.String(500), nullable=False)
    optionTwoName = db.Column(db.String(500), nullable=False)
    optionTwoUrl = db.Column(db.String(500), nullable=False)
    optionThreeName = db.Column(db.String(500), nullable=False)
    optionThreeUrl = db.Column(db.String(500), nullable=False)
    optionFourName = db.Column(db.String(500), nullable=False)
    optionFourUrl = db.Column(db.String(500), nullable=False)

    def __init__(self, questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        self.optionOneName = optionOneName 
        self.optionOneUrl = optionOneUrl 
        self.optionTwoName = optionTwoName
        self.optionTwoUrl = optionTwoUrl 
        self.optionThreeName = optionThreeName 
        self.optionThreeUrl = optionThreeUrl 
        self.optionFourName = optionFourName 
        self.optionFourUrl = optionFourUrl 


class BrailleQuizOneSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl', 'optionOneName', 'optionOneUrl', 'optionTwoName', 'optionTwoUrl', 'optionThreeName', 'optionThreeUrl', 'optionFourName', 'optionFourUrl')


brailleQuizOne_schema = BrailleQuizOneSchema()
brailleQuizOnes_schema = BrailleQuizOneSchema(many=True)


# Create Braille Quiz Two Table
class BrailleQuizTwo(db.Model):
    __tablename__ = "brailleQuizTwo"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    optionOneName = db.Column(db.String(500), nullable=False)
    optionOneUrl = db.Column(db.String(500), nullable=False)
    optionTwoName = db.Column(db.String(500), nullable=False)
    optionTwoUrl = db.Column(db.String(500), nullable=False)
    optionThreeName = db.Column(db.String(500), nullable=False)
    optionThreeUrl = db.Column(db.String(500), nullable=False)
    optionFourName = db.Column(db.String(500), nullable=False)
    optionFourUrl = db.Column(db.String(500), nullable=False)

    def __init__(self, questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        self.optionOneName = optionOneName 
        self.optionOneUrl = optionOneUrl 
        self.optionTwoName = optionTwoName
        self.optionTwoUrl = optionTwoUrl 
        self.optionThreeName = optionThreeName 
        self.optionThreeUrl = optionThreeUrl 
        self.optionFourName = optionFourName 
        self.optionFourUrl = optionFourUrl 


class BrailleQuizTwoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl', 'optionOneName', 'optionOneUrl', 'optionTwoName', 'optionTwoUrl', 'optionThreeName', 'optionThreeUrl', 'optionFourName', 'optionFourUrl')


brailleQuizTwo_schema = BrailleQuizTwoSchema()
brailleQuizTwos_schema = BrailleQuizTwoSchema(many=True)

# Create Braille Quiz Three Table
class BrailleQuizThree(db.Model):
    __tablename__ = "brailleQuizThree"
    id = db.Column(db.Integer, primary_key=True)
    questionNum = db.Column(db.String(10), nullable=False)
    answerName = db.Column(db.String(500), nullable=False)
    answerUrl = db.Column(db.String(500), nullable=False)
    

    def __init__(self, questionNum, answerName, answerUrl):
        self.questionNum = questionNum
        self.answerName = answerName
        self.answerUrl = answerUrl
        


class BrailleQuizThreeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'questionNum', 'answerName', 'answerUrl')


brailleQuizThree_schema = BrailleQuizThreeSchema()
brailleQuizThrees_schema = BrailleQuizThreeSchema(many=True)


@app.route('/', methods=["GET"])
def home():
    return "<h1>ASL and Braille Quiz API</h1>"


# Endpoints for ASL quiz one -------------------------------------------------------
@app.route('/aslq1', methods=['POST'])
def add_aslq1():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']
    optionOneName = request.json['optionOneName']
    optionOneUrl = request.json['optionOneUrl']
    optionTwoName = request.json['optionTwoName']
    optionTwoUrl = request.json['optionTwoUrl']
    optionThreeName = request.json['optionThreeName']
    optionThreeUrl = request.json['optionThreeUrl']
    optionFourName = request.json['optionFourName']
    optionFourUrl = request.json['optionFourUrl']

    new_aslq1 = AslQuizOne(questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl)

    db.session.add(new_aslq1)
    db.session.commit()

    aslq1 = AslQuizOne.query.get(new_aslq1.id)
    return aslQuizOne_schema.jsonify(aslq1)


@app.route('/aslq1s', methods=["GET"])
def get_aslq1s():
    all_aslq1s = AslQuizOne.query.all()
    result = aslQuizOnes_schema.dump(all_aslq1s)

    return jsonify(result)


@app.route('/aslq1/<id>', methods=['GET'])
def get_aslq1(id):
    aslq1 = AslQuizOne.query.get(id)

    result = aslQuizOne_schema.dump(aslq1)
    return jsonify(result)


@app.route('/aslq1/<id>', methods=['DELETE'])
def delete_aslq1(id):
    record = AslQuizOne.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')

# Endpoints for ASL quiz two -------------------------------------------------------
@app.route('/aslq2', methods=['POST'])
def add_aslq2():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']
    optionOneName = request.json['optionOneName']
    optionOneUrl = request.json['optionOneUrl']
    optionTwoName = request.json['optionTwoName']
    optionTwoUrl = request.json['optionTwoUrl']
    optionThreeName = request.json['optionThreeName']
    optionThreeUrl = request.json['optionThreeUrl']
    optionFourName = request.json['optionFourName']
    optionFourUrl = request.json['optionFourUrl']

    new_aslq2 = AslQuizTwo(questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl)

    db.session.add(new_aslq2)
    db.session.commit()

    aslq2 = AslQuizTwo.query.get(new_aslq2.id)
    return aslQuizTwo_schema.jsonify(aslq2)


@app.route('/aslq2s', methods=["GET"])
def get_aslq2s():
    all_aslq2s = AslQuizTwo.query.all()
    result = aslQuizTwos_schema.dump(all_aslq2s)

    return jsonify(result)


@app.route('/aslq2/<id>', methods=['GET'])
def get_aslq2(id):
    aslq2 = AslQuizTwo.query.get(id)

    result = aslQuizTwo_schema.dump(aslq2)
    return jsonify(result)


@app.route('/aslq2/<id>', methods=['DELETE'])
def delete_aslq2(id):
    record = AslQuizTwo.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')

# Endpoints for ASL quiz three -------------------------------------------------------
@app.route('/aslq3', methods=['POST'])
def add_aslq3():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']

    new_aslq3 = AslQuizThree(questionNum, answerName, answerUrl)

    db.session.add(new_aslq3)
    db.session.commit()

    aslq3 = AslQuizThree.query.get(new_aslq3.id)
    return aslQuizThree_schema.jsonify(aslq3)


@app.route('/aslq3s', methods=["GET"])
def get_aslq3s():
    all_aslq3s = AslQuizThree.query.all()
    result = aslQuizThrees_schema.dump(all_aslq3s)

    return jsonify(result)


@app.route('/aslq3/<id>', methods=['GET'])
def get_aslq3(id):
    aslq3 = AslQuizThree.query.get(id)

    result = aslQuizThree_schema.dump(aslq3)
    return jsonify(result)


@app.route('/aslq3/<id>', methods=['DELETE'])
def delete_aslq3(id):
    record = AslQuizThree.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')


# Endpoints for Braille quiz one -------------------------------------------------------
@app.route('/brailleq1', methods=['POST'])
def add_brailleq1():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']
    optionOneName = request.json['optionOneName']
    optionOneUrl = request.json['optionOneUrl']
    optionTwoName = request.json['optionTwoName']
    optionTwoUrl = request.json['optionTwoUrl']
    optionThreeName = request.json['optionThreeName']
    optionThreeUrl = request.json['optionThreeUrl']
    optionFourName = request.json['optionFourName']
    optionFourUrl = request.json['optionFourUrl']

    new_brailleq1 = BrailleQuizOne(questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl)

    db.session.add(new_brailleq1)
    db.session.commit()

    brailleq1 = BrailleQuizOne.query.get(new_brailleq1.id)
    return brailleQuizOne_schema.jsonify(brailleq1)


@app.route('/brailleq1s', methods=["GET"])
def get_brailleq1s():
    all_brailleq1s = BrailleQuizOne.query.all()
    result = brailleQuizOnes_schema.dump(all_brailleq1s)

    return jsonify(result)


@app.route('/brailleq1/<id>', methods=['GET'])
def get_brailleq1(id):
    brailleq1 = BrailleQuizOne.query.get(id)

    result = brailleQuizOne_schema.dump(brailleq1)
    return jsonify(result)


@app.route('/brialleq1/<id>', methods=['DELETE'])
def delete_brailleq1(id):
    record = BrailleQuizOne.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')

# Endpoints for Braille quiz two -------------------------------------------------------
@app.route('/brailleq2', methods=['POST'])
def add_brailleq2():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']
    optionOneName = request.json['optionOneName']
    optionOneUrl = request.json['optionOneUrl']
    optionTwoName = request.json['optionTwoName']
    optionTwoUrl = request.json['optionTwoUrl']
    optionThreeName = request.json['optionThreeName']
    optionThreeUrl = request.json['optionThreeUrl']
    optionFourName = request.json['optionFourName']
    optionFourUrl = request.json['optionFourUrl']

    new_brailleq2 = BrailleQuizTwo(questionNum, answerName, answerUrl, optionOneName, optionOneUrl, optionTwoName, optionTwoUrl, optionThreeName, optionThreeUrl, optionFourName, optionFourUrl)

    db.session.add(new_brailleq2)
    db.session.commit()

    brailleq2 = BrailleQuizTwo.query.get(new_brailleq2.id)
    return brailleQuizTwo_schema.jsonify(brailleq2)


@app.route('/brailleq2s', methods=["GET"])
def get_brailleq2s():
    all_brailleq2s = BrailleQuizTwo.query.all()
    result = brailleQuizTwos_schema.dump(all_brailleq2s)

    return jsonify(result)


@app.route('/brailleq2/<id>', methods=['GET'])
def get_brailleq2(id):
    brailleq2 = BrailleQuizTwo.query.get(id)

    result = brailleQuizTwo_schema.dump(brailleq2)
    return jsonify(result)


@app.route('/brailleq2/<id>', methods=['DELETE'])
def delete_brailleq2(id):
    record = BrailleQuizTwo.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')

# Endpoints for Braille quiz three -------------------------------------------------------
@app.route('/brailleq3', methods=['POST'])
def add_brailleq3():
    questionNum = request.json['questionNum']
    answerName = request.json['answerName']
    answerUrl = request.json['answerUrl']

    new_brailleq3 = BrailleQuizThree(questionNum, answerName, answerUrl)

    db.session.add(new_brailleq3)
    db.session.commit()

    brailleq3 = BrailleQuizThree.query.get(new_brailleq3.id)
    return brailleQuizThree_schema.jsonify(brailleq3)


@app.route('/brailleq3s', methods=["GET"])
def get_brailleq3s():
    all_brailleq3s = BrailleQuizThree.query.all()
    result = brailleQuizThrees_schema.dump(all_brailleq3s)

    return jsonify(result)


@app.route('/brailleq3/<id>', methods=['GET'])
def get_brailleq3(id):
    brailleq3 = BrailleQuizThree.query.get(id)

    result = brailleQuizThree_schema.dump(brailleq3)
    return jsonify(result)


@app.route('/brailleq3/<id>', methods=['DELETE'])
def delete_brailleq3(id):
    record = BrailleQuizThree.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return jsonify('Item deleted')


if __name__ == "__main__":
    app.debug = True
    app.run()
