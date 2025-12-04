from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse, ChatMessage
from app.services.chat import generate_response


# Define API router
router = APIRouter(prefix="/api", tags=["chat"])


# Health check endpoint
@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "homebrain-backend",
    }



# Chat endpoint
@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    
    history = req.history or []

    try:
        reply, new_history = generate_response(history, req.message)
    except HTTPException:
        raise
    except Exception as e:
        print(f"LLM error: {e!r}")
    
    return ChatResponse(
        reply=reply, 
        history=new_history,
    )
        
