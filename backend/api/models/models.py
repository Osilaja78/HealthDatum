from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from api.database import Base

# Base class for clinic verification process.
class ClinicVerification(Base):
    __tablename__ = "ClinicVerification"

    id = Column(String(80), primary_key=True, index=True)
    legal_name = Column(String(500), nullable=False)
    cac_reg_number = Column(String(200), nullable=False, unique=True)
    contact_email = Column(String(50), nullable=False, unique=True)
    is_verified = Column(Boolean, default=False)

# This model stores clinics info
class Clinic(Base):
    __tablename__ = "Clinic"

    id = Column(String(80), primary_key=True, index=True)
    legal_name = Column(String(500))
    short_bio = Column(String(1500))
    full_address = Column(String(1500))
    lga = Column(String(100))
    state = Column(String(100))
    cac_reg_number =  Column(String(200))
    designated_admin_first_name = Column(String(200))
    designated_admin_last_name = Column(String(200))
    designated_admin_title = Column(String(100))
    contact_phone = Column(String(50))
    contact_email = Column(String(50), unique=True)
    superuser_password = Column(String(150))
    is_verified = Column(Boolean, default=False)

    subusers = relationship("Subusers", back_populates="clinic")
    patients = relationship("Patients", back_populates="clinic")


# This models stores subusers info
class Subusers(Base):
    __tablename__ = "Subusers"

    id = Column(String(80), primary_key=True, index=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    title = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    contact_phone = Column(String(50))
    email = Column(String(150), unique=True)
    permissions = Column(Integer)

    clinic = relationship("Clinic", back_populates="subusers")


class MedicalRecord(Base):
    __tablename__ = "MedicalRecord"

    id = Column(String(80), primary_key=True, index=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    record_type = Column(String(100))
    insurance = Column(String(150))
    created_at = Column(DateTime(timezone=True))

    patients = relationship("Patients", back_populates="record")


# This model stores patients basic info
class Patients(Base):
    __tablename__ = "Patients"

    id = Column(String(80), primary_key=True, index=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    record_id = Column(String(80), ForeignKey('MedicalRecord.id'))
    first_name = Column(String(100))
    last_name = Column(String(100))
    other_names = Column(String(200))
    email = Column(String(150))
    phone = Column(String(50))
    address = Column(String(1500))
    emergency_contact_name = Column(String(100))
    emergency_contact_phone = Column(String(50))
    emergency_contact_relation = Column(String(100))
    created_at = Column(DateTime(timezone=True))

    clinic = relationship("Clinic", back_populates="patients")
    record = relationship("MedicalRecord", back_populates="patients")
    biodata = relationship("PatientBiodata", back_populates="patient")


# This model stores patients biodata info
class PatientBiodata(Base):
    __tablename__ = "PatientBiodata"

    patient_id = Column(String(80), ForeignKey('Patients.id'), primary_key=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    sex = Column(String(50))
    dob = Column(DateTime(timezone=True))
    marital_status = Column(String(100))
    occupation = Column(String(500))
    religion = Column(String(500))
    weight = Column(Float)
    height = Column(Float)
    blood_group = Column(String(50))
    genotype = Column(String(50))
    rhesus = Column(String(50))
    medical_problems = Column(String)

    patient = relationship("Patients", back_populates="biodata")


class MedicalHistory(Base):
    __tablename__ = "MedicalHistory"

    patient_id = Column(String(80), ForeignKey('Patients.id'), primary_key=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    previous_admission = Column(String)
    previous_operation = Column(String)
    drug_reactions = Column(String)
    allergies = Column(String)


class VitalSigns(Base):
    __tablename__ =  "VitalSigns"

    patient_id = Column(String(80), ForeignKey('Patients.id'), primary_key=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    systolic_bp = Column(Float)
    diastolic_bp = Column(Float)
    weight = Column(Float)
    height = Column(Float)
    age =  Column(Float)
    temp = Column(Float)
    created_at = Column(DateTime(timezone=True))


class Consultation(Base):
    __tablename__ = "Consultation"

    patient_id = Column(String(80), ForeignKey('Patients.id'), primary_key=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    complaints =  Column(String)
    diagnosis = Column(String)
    plan = Column(String)
    prescriptions = Column(String)


class Test(Base):
    __tablename__ = "Test"

    patient_id = Column(String(80), ForeignKey('Patients.id'), primary_key=True)
    clinic_id = Column(String(80), ForeignKey('Clinic.id'))
    test_type = Column(String)
    result = Column(String)

