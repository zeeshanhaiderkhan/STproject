import pytest
import patient
import doctor
import report
import prescription
import dietPlan

#function based testing

p =patient.Patient(1,"Zeeshan","6110121720769","03070156758",1999)
d = doctor.Doctor(1,"Shehryar","6110121720765","03124567890",1998,"male")



@pytest.mark.details
def test_patient_details():
    assert p.name == "Zeeshan"
    assert p.cnic == "6110121720769"
    assert p.phone == "03070156758"
    assert p.dob == 1999
    assert p.getAge() == 22

@pytest.mark.notassigned
def test_inital_data():
    assert p.getTotalReports() == 0
    assert p.getTotalPrescriptions() == 0
    assert p.getTotalDietPlans() == 0

p.doc =d


@pytest.mark.assigned
def test_doctorAssigned():
    assert p.doc.name == "Shehryar"
    assert p.doc.sex == "male"
    assert p.doc.cnic == "6110121720765"
    assert p.doc.dob == 1998


report1 = report.Report(1,"Blood-CP","2-2-2021","HG 247")
report2 = report.Report(2,"X-ray","3-3-2021","PG 24")
report3 = report.Report(3,"Glucose","4-4-2021","124")

prescription1 = prescription.Prescription(1,"Night","10-10-2021","Khana Khana")
prescription2  = prescription.Prescription(2,"Day","31-10-2021","Lunch Cereals")
prescription3 = prescription.Prescription(3,"Morning","30-11-2021","Nashta")

dietplan1 = dietPlan.DietPlan(1,"Weekly","20-10-2021","Beans")
dietplan2 = dietPlan.DietPlan(2,"Bimonthly","03-10-2021","Cereals")
dietplan3 = dietPlan.DietPlan(3,"Monthly","04-11-2021","Bread")

@pytest.mark.reports
def test_reports():
    p.addReport(report1)
    p.addReport(report2)
    p.addReport(report3)
    assert p.getTotalReports() == 3
    assert p.getLatestReport() == report3
    assert p.getLatestReport().getTitle() == "Glucose"
    assert p.reports == [report1,report2,report3]

@pytest.mark.prescriptions
def test_prescriptions():
    p.addPrescription(prescription1)
    p.addPrescription(prescription2)
    p.addPrescription(prescription3)
    assert p.getTotalPrescriptions() == 3
    assert p.getLatestPrescription() == prescription3
    assert p.getLatestPrescription().getTitle() == "Morning"
    assert p.getPrescriptions() == [prescription1,prescription2,prescription3]

@pytest.mark.dietplans
def test_dietplans():
    p.addDietPlan(dietplan1)
    p.addDietPlan(dietplan2)
    assert p.getTotalDietPlans() == 2
    assert p.getLatestDietPlan() == dietplan2
    assert p.getLatestDietPlan().getTitle() == "Bimonthly"
    p.addDietPlan(dietplan3)
    assert p.getTotalDietPlans() == 3
    assert p.getLatestDietPlan() == dietplan3
    assert p.getLatestDietPlan().getTitle() == "Monthly"
    


