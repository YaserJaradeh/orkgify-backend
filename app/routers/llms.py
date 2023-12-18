from fastapi import APIRouter

from app.components import log
from app.services import LLMsService
from app.models import CompletionRequest

router = APIRouter(prefix="/llm", tags=["LLM"])


@router.post("/", status_code=200)
@log(__name__)
def complete_prompt(request: CompletionRequest):
    llms_service = LLMsService()
    return llms_service.complete(llm=request.model, **request.model_dump())
