import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from datetime import datetime
from flask import Flask, request, jsonify
from database import db  
from models.refeicao import Refeicao 
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash  
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

app.config['SECRET_KEY'] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/refeicao", methods=["POST"])
def register():
  data = request.json
  
  required_fields = ["nome", "date_time", "is_within_diet"]
  missing_fields = [field for field in required_fields if field not in data]

  if missing_fields:
    return jsonify({"error": f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"}), 400
  
  try:
    date_time = datetime.fromisoformat(data["date_time"])
  except ValueError:
    return jsonify({"error": "Formato inválido para o campo 'date_time'. Use ISO 8601 (ex: 2024-12-25T12:00:00)."}), 400

  meal = Refeicao(
      nome=data["nome"],
      description=data.get("description"),
      date_time=date_time,
      is_within_diet=bool(data["is_within_diet"]), 
  )


  db.session.add(meal)
  db.session.commit()

  return jsonify({
      "message": "Refeição criada com sucesso!",
      "meal": {
          "id": meal.id,
          "name": meal.nome,
          "description": meal.description,
          "date_time": meal.date_time.isoformat(),
          "is_within_diet": meal.is_within_diet,
      },
  }), 201

@app.route('/refeicao', methods=["GET"])
def get_ref():
  ref = Refeicao.query.all()

  if not ref:
    return jsonify({"message": "Nenhum usuário encontrado"}), 404

  ref_data = []
  for meal in ref:
    ref_data.append({
      "id": meal.id,
      "name": meal.nome,
      "description": meal.description,
      "date_time": meal.date_time.strftime("%d/%m/%Y %H:%M:%S"),  # Formata para padrão PT-BR
      "Está dentro da dieta": "Sim" if meal.is_within_diet else "Não",  # Converte booleano para texto
    })

  return jsonify(ref_data), 200

@app.route("/refeicao/<int:id>", methods=["GET"])
def get_ref_id(id):
  meal = Refeicao.query.get(id)

  if meal is None:
    return jsonify({"error": "Refeição não encontrada"}), 404
  
  response = {
    "id": meal.id,
    "name": meal.nome,
    "description": meal.description,
    "date_time": meal.date_time.strftime("%d/%m/%Y %H:%M:%S"),  # Formata para padrão PT-BR
    "Está dentro da dieta": "Sim" if meal.is_within_diet else "Não",  # Converte booleano para texto
  }

  return jsonify(response), 200

@app.route('/refeicao/<int:id>', methods=["PUT"])
def update_ref_id(id):

  ref_to_update = Refeicao.query.get(id)

  if not ref_to_update:
    return jsonify({"message": "Refeição não encontrada."}), 404
  
  data = request.json


  if "nome" in data:
    ref_to_update.name = data["nome"]
  if "description" in data:
    ref_to_update.description = data["description"]
  if "date_time" in data:
    ref_to_update.date_time = datetime.strptime(data["date_time"], "%d/%m/%Y %H:%M:%S")
  if "is_within_diet" in data:
    ref_to_update.is_within_diet = data["is_within_diet"]

  db.session.commit()

  return jsonify({"message": "Dados atualizados com sucesso!"}), 200


@app.route('/refeicao/<int:id>', methods=["DELETE"])
def delete_ref(id):

  ref_to_delete = Refeicao.query.get(id)
  
  if not ref_to_delete:
    return jsonify({"message": "Refeição não encontrada."}), 404
  

  try:
    db.session.delete(ref_to_delete) 
    db.session.commit() 
    return jsonify({"message": "Refeição deletada com sucesso!"}), 200
  
  except SQLAlchemyError as e:
    db.session.rollback() 
    return jsonify({"message": f"Erro ao deletar o refeição: {str(e)}"}), 500
  

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)