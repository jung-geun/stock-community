from fastapi import APIRouter, Path
# import modules.Rock_Paper_Scissors as rps
import modules.rps as rps

# game_router = APIRouter()

# @game_router.get("/rps/{inputs}")
# async def play_rps(inputs: str = Path(..., title="The input of the game."))->dict:
#     result = rps.Game().play(inputs)
#     return {"result" : result}

game_router = APIRouter()

@game_router.get("/rps/{inputs}")
async def play(inputs: int = Path(..., title="The ID of the todo to retrieve.")):
    result = rps.play(inputs)
    return {"result" : result}

@game_router.get("/rps")    
async def play(inputs: int = Path(..., title="The ID of the todo to retrieve.")):
    result = rps.play(inputs)
    return {"result" : result}