# This module contains clinic onbording routes and logic.
from api.models import models
from api.database import get_db
from fastapi import APIRouter, HTTPException, status, Depends
from api.schemas.clilnic_schemas import ClinicRegistration, VerificationPhase
from sqlalchemy.orm import Session
from api.utils.genarate_ids import generate_short_id
from api.utils.email import send_mail

router = APIRouter(tags=['Onboarding'], prefix="/api/v1")


@router.post("/initial-verification")
async def register_clinic(request: VerificationPhase, db: Session = Depends(get_db)):
    """
    Route for clinics registration.

    Parameters: ClinicRegistration schema.

    Return:
        on error: a proper error code
        on success: nothing
    """

    try:
        clinic = models.ClinicVerification(
            id=generate_short_id(),
            legal_name=request.legal_name,
            contacnt_email=request.contact_email,
            cac_reg_number=request.cac_reg_number,
        )

        db.add(clinic)
        db.commit()
        db.refresh(clinic)
        db.close()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Clinic with email already exist! {e}",
            )
    
    # Email content for successful submission
    content = f"""
            <html>
            <body>
                <b>Warm greetings {request.legal_name}.</b></br>
                <p>
                    Welcome to <b>HealthDatum</b>, your no.1 EHR system that provides 
                    easy means of managing clinical data. Thanks for being part of the community 🥰.
                </p>
                <p>
                    Now that you're registered, the next thing is to wait while your 
                    clinic gets verified by our system, so you can have full access to our product.
                </p>
                <p>
                    You don't have to do anything at this stage, verification usually take at least 
                    24 hours. Once your clinic is successfully verified, you'll recieve further 
                    instructions on how to access or platform.
                </p>
                <p><b>Sincerely, HealthDatum.</b></p>
        
            </body>
            </html>
        """

    await send_mail(email=request.contact_email, content=content)
