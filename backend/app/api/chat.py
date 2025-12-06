from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat import handle_session_chat_turn


router = APIRouter(prefix="/api", tags=["chat"])


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "homebrain-backend",
    }



@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    
    try:
        LLM_reply, new_history, sid = handle_session_chat_turn(req.session_id, req.message)
    except HTTPException:
        raise
    except Exception as e:
        print(f"LLM error: {e!r}")
    
    return ChatResponse(
        reply=LLM_reply, 
        history=new_history,
        session_id=sid,
    )
        
