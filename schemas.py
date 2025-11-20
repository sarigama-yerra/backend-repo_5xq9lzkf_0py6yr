"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (keep for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Landing page specific schemas

class Lead(BaseModel):
    """Early access leads"""
    email: EmailStr = Field(..., description="Email for early access")
    name: Optional[str] = Field(None, description="Optional name")
    source: str = Field("landing_page", description="Lead source")
    consent: bool = Field(True, description="Consent to be contacted")

class Preorder(BaseModel):
    """Pre-purchase intents/orders"""
    email: EmailStr = Field(..., description="Customer email")
    plan: str = Field(..., description="Plan identifier, e.g., early_lifetime, pro_monthly")
    price_cents: Optional[int] = Field(None, ge=0, description="Price in cents if known")
    status: str = Field("initiated", description="initiated, pending, paid, cancelled")
    stripe_session_id: Optional[str] = Field(None, description="Stripe Checkout session id if created")
