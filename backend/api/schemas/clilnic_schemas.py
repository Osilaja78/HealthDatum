# This module contains schemas for clinic registration and onboarding.

from pydantic import BaseModel, EmailStr, HttpUrl


# Model for Verification Phase
class VerificationPhase(BaseModel):
    legal_name: str
    cac_reg_number: str
    contact_email: str

# Model for Clinic Registration
class ClinicRegistration(BaseModel):
    legal_name: str
    short_bio: str
    address: str
    lga: str
    state: str
    cac_reg_number: str
    contact_person_name: str
    contact_email: EmailStr
    contact_phone: str

# Model for Initial Screening
class InitialScreening(BaseModel):
    clinic_registration: ClinicRegistration

