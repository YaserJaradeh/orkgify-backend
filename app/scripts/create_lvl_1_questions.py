from app.components import Database, DatabaseQuestion

question = DatabaseQuestion(
    level=1,
    type="MCQ",
    question="What is the capital of France?",
    candidates=["Paris", "London", "Berlin"],
    ai_help="Paris is the capital of France",
    context="https://en.wikipedia.org/wiki/France",
)

db = Database()

db.insert_question(question)
