# This module contains schemas for clinic registration and onboarding.

from pydantic import BaseModel, EmailStr, HttpUrl

# Model for Clinic Registration
class ClinicRegistration(BaseModel):
    clinic_name: str
    address: str
    contact_person_name: str
    contact_email: EmailStr
    contact_phone: str

# Model for Initial Screening
class InitialScreening(BaseModel):
    clinic_registration: ClinicRegistration

# Model for Verification Phase
class VerificationPhase(BaseModel):
    clinic_registration: ClinicRegistration
    proof_of_registration: HttpUrl
    representative_contact: str

# Model for Review and Approval
class ReviewAndApproval(BaseModel):
    verification_phase: VerificationPhase

# Model for Onboarding Assistance
class OnboardingAssistance(BaseModel):
    approved: bool
    assistance_message: str

# Model for Training and Orientation
class TrainingAndOrientation(BaseModel):
    approved: bool
    training_materials_link: HttpUrl

# Model for Customization
class Customization(BaseModel):
    approved: bool
    customization_instructions: str

# Model for Go-Live
class GoLive(BaseModel):
    approved: bool
    go_live_message: str

# Model for Ongoing Support
class OngoingSupport(BaseModel):
    clinic_id: int
    support_contact: str
    support_resources_link: HttpUrl
