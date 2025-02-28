from fastapi import APIRouter, HTTPException, Request, Header, Depends
# from fastapi.security import OAuth2PasswordRequestForm
# from ..models.trader import TraderCreate, Trader
# from bson import ObjectId
# from passlib.context import CryptContext
# import jwt
# import os
# from pydantic import BaseModel
# from typing import Optional

router = APIRouter()

# Add this near the top with other initializations
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @router.post("/signup", response_model=dict)
# async def create_trader(trader: TraderCreate, request: Request):
#     try:
#         # Check if trader exists
#         existing_trader = await request.state.db.traders.find_one({"email": trader.email})
        
#         if existing_trader:
#             # If trader exists but has no password (e.g., Google signup)
#             if 'password' not in existing_trader or not existing_trader['password']:
#                 # Update with new password
#                 hashed_password = pwd_context.hash(trader.password)
#                 await request.state.db.traders.update_one(
#                     {"email": trader.email},
#                     {"$set": {"password": hashed_password}}
#                 )
#                 return {"id": str(existing_trader['_id']), "message": "Password updated"}
#             else:
#                 # If trader exists with password, prevent registration
#                 raise HTTPException(
#                     status_code=400,
#                     detail="Email already registered"
#                 )
        
#         # Create new trader if doesn't exist
#         trader_dict = trader.model_dump()
#         trader_dict["password"] = pwd_context.hash(trader_dict["password"])
#         trader_dict["user_id"] = str(ObjectId())
#         result = await request.state.db.traders.insert_one(trader_dict)
#         return {"id": str(result.inserted_id)}
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



# @router.get("/traders", response_model=list)
# async def get_traders(request: Request):
#     try:
#         traders = await request.state.db.traders.find().to_list(1000)
#         return traders
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e)) 



# didn't test this
# class SignInRequest(BaseModel):
#     email: str
#     password: str

# @router.post("/signin")
# async def signin(request: Request, credentials: SignInRequest):
#     try:
#         # Find trader by email
#         trader = await request.state.db.traders.find_one({"email": credentials.email})
        
#         if not trader:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Incorrect email or password"
#             )

#         # Check if password exists in trader document
#         if 'password' not in trader:
#             raise HTTPException(
#                 status_code=401,
#                 detail="No password set for this account"
#             )

#         try:
#             print("verifying password")
#             # Verify password with explicit error handling
#             is_valid = pwd_context.verify(credentials.password, trader['password'])
#             if not is_valid:
#                 raise HTTPException(
#                     status_code=401,
#                     detail="Incorrect email or password"
#                 )
#             print("password verified" , is_valid)
#         except Exception as password_error:
#             print(f"Password verification error: {str(password_error)}")
#             raise HTTPException(
#                 status_code=401,
#                 detail="Password verification failed"
#             )
            
#         # Create JWT token
#         auth_token = jwt.encode(
#             {
#                 "email": trader['email'],
#                 "user_id": str(trader['_id'])
#             },
#             os.getenv("SECRET"),
#             algorithm="HS256"
#         )
#         print("auth_token" , auth_token)
#         return {
#             "authToken": auth_token,
#             "user": {
#                 "email": trader['email'],
#                 "user_id": str(trader['_id'])
#             }
#         }
        
#     except Exception as e:
#         print(f"Signin error: {str(e)}")
#         raise HTTPException(status_code=401, detail=str(e))


# @router.post("/verify")
# async def verify_token(request: Request, authorization: Optional[str] = Header(None)):
#     print("verifying token😊")
#     try:
#         if not authorization:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Authorization header missing"
#             )
        
#         token = authorization.replace("Bearer ", "")
        
#         try:
#             # Verify and decode the JWT token
#             payload = jwt.decode(
#                 token,
#                 os.getenv("SECRET"),
#                 algorithms=["HS256"]
#             )
            
#             # Find trader by email from token
#             trader = await request.state.db.traders.find_one({"email": payload["email"]})
            
#             if not trader:
#                 raise HTTPException(
#                     status_code=401,
#                     detail="Invalid token"
#                 )
                
#             return {
#                 "valid": True,
#                 "user": {
#                     "email": trader["email"],
#                     "user_id": str(trader["_id"])
#                 }
#             }
            
#         except jwt.ExpiredSignatureError:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Token has expired"
#             )
#         except jwt.JWTError:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Invalid token"
#             )
            
#     except Exception as e:
#         raise HTTPException(
#             status_code=401,
#             detail=str(e)
#         )
