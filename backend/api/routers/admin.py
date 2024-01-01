# This module contains logic for administrative actions.
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api.models import models
from api.utils.email import send_mail
from dotenv import load_dotenv
import os


router = APIRouter(tags=['Admin'], prefix="/api/v1")
load_dotenv()


FRONTEND_URL = os.getenv("FRONTEND_URL")


@router.get("/pending_verification")
async def get_all_pending_verifications(db: Session = Depends(get_db)):
    """
    Gets all clinics that are pending verification form the database
    so they can get verified.

    Return: all unverified clinics
    """

    # Get all unverified clinics from the database.
    try:
        unverified_clinics = db.query(models.ClinicVerification).filter(
            models.ClinicVerification.is_verified == False
        ).all()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong!"
            )
    
    if not unverified_clinics:
        return []
    else:
        return unverified_clinics


@router.patch("/verify_clinic")
async def verify_clinics(clinic_id: str, db: Session = Depends(get_db)):
    """
    Route for clinic verification by admin.

    Parameters:
        clinic_id: id of the clinic to be verified

    Return:
        on error: HTTP Exception that contains the error details.
        on success: message (success message)
    """

    try:
        # Get the clinic from db and update the is_verified status.
        clinic = db.query(models.ClinicVerification).filter(
            models.ClinicVerification.id == clinic_id
        ).first()

        if clinic:
            clinic.is_verified == True
            db.commit()
        else:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Clinic with id '{clinic_id}' does not exist!"
            )
    except Exception as e:
        # Rise and exceptin in case of error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
    
    if clinic:
        # Send next step email to the clinic
        clinic_email = clinic.contact_email
        url = f"{FRONTEND_URL}/details?id={clinic.id}"

        content = f"""
                <html>
                <body>
                    <b>Hello {clinic.legal_name}.</b></br>
                    <p>
                        Congratulations 🎉, your account with HealthDatum has been successfully verified🥰.
                    </p>
                    <p>
                        Now that you're verified, the next step is to complete your details and create
                        a superuser that will have admin access to the platform on behalf of your clinic.
                    </p>
                    <p>
                        Click <a href="{url}">here</a> to verify your account, or follow this link {url}
                    </p>
                    <p><b>Sincerely, HealthDatum.</b></p>
            
                </body>
                </html>
            """

        await send_mail(email=clinic_email, content=content)
    
    
    return {"message": f"Clinic with id {clinic_id} verified successfuly"}

