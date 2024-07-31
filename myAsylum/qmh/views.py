from django.shortcuts import render
from django.shortcuts import redirect

from qmh.models import Glossary, Patient
# yrong2019: for in-text glossary fetching with custom tag to work, coding for glossary_list has to be added under every views function - is there a way for all function to inherit these lines, so that the custom tag is enabled on every page?

###### topnav ######

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def related_projects(request):
    return render(request, 'related-projects.html')

#def contact(request):# summer 2019 team decided that a contact form no longer needed; contact button is a link to "mailto:<hc-libraries>"
#    return render(request, 'contact.html')


###### home visualizations ######

def visualizations(request):
    return render(request, 'visualizations.html')

def visual_scatterplotPatientAdmitAgeVsAdmitYear(request):
    admitYear = [1850]
    admitAge = [24]
    firstName = ["John"]
    lastName = ["Doe"]
    rawAdmitYear = [str(p.admitYear) for p in Patient.objects.all()]# module_object has to pass thru str() before passing thru int(), or django will raise error
    rawAdmitAge = [str(p.admitAge) for p in Patient.objects.all()]
    rawFirstName = [str(p.firstName) for p in Patient.objects.all()]
    rawLastName = [str(p.lastName) for p in Patient.objects.all()]
    for (y, a, f, l) in zip(rawAdmitYear, rawAdmitAge, rawFirstName, rawLastName):
        if not y == '' and not a == '0':
            admitYear.append(int(y))# module_object has to pass thru str() before passing thru int(), or django will raise error
            admitAge.append(int(a))
            firstName.append(f)
            lastName.append(l)
            
    # Of all 2208 patient entries,
    # 336 entries either have empty year entry ('') or have zero age entry (0),
    # leaving only 1872 valid points entered for making the scatterplot.
    nameList = []
    for (f, l) in zip(firstName, lastName):
        nameList.append(f+' '+l)
    yearRange = str([min(admitYear)-5, max(admitYear)+5])
    ageRange = str([min(admitAge)-5, max(admitAge)+5])
    #traceName = [('p%d' % (x)) for x in list(range(1,len(nameList)+1))]
    if len(admitYear)==len(admitAge)==len(nameList):# removed len(traceName)
        scatterplot = zip(admitYear, admitAge, nameList)# removed traceName
    else:
        scatterplot = [('error',) * 4]
    return render(request, 'visual_scatterplotPatientAdmitAgeVsAdmitYear.html', {'scatterplot': scatterplot, 'yearRange': yearRange, 'ageRange': ageRange})

def visual_heatmapPatientMonthlyAdmissionFrequency(request):
    return render(request, 'visual_heatmapPatientMonthlyAdmissionFrequency.html')

def visual_sankeyPhilanthropistsOrganizationsAssociation(request):
    return render(request, 'visual_sankeyPhilanthropistsOrganizationsAssociation.html')


###### sidebar learn ######


# yrong2019: Sarah Horowitz does not like the name "learn", but the summer 2019 team had not settled on an alternative name for the entire body of short articles

#def learn(request):# the summer 2019 team wanted to write a landing page for each topic in "learn", but we aborted the effort 
#    return render(request, 'learn.html')

#    "the asylum"

def learn_theYorkRetreat(request):
    return render(request, 'learn_theYorkRetreat.html')

def learn_foundation(request):
    glossary_list = Glossary.objects.order_by('term')
    term_list = [glossary.term for glossary in glossary_list]
    meaning_list = [glossary.meaning for glossary in glossary_list]
    glossary_dict = {}
    for (term, meaning) in zip(term_list, meaning_list):
        glossary_dict[term] = meaning
    return render(request, 'learn_foundation.html', {'glossary_dict': glossary_dict})

def learn_structureAndGovernance(request):
    return render(request, 'learn_structureAndGovernance.html')

def learn_changesInAdminOverTime(request):
    return render(request, 'learn_changesInAdminOverTime.html')

def learn_asylumArchitecture(request):
    return render(request, 'learn_asylumArchitecture.html')

def learn_gurneyCottage(request):
    return render(request, 'learn_gurneyCottage.html')

def learn_trainingOfDoctors(request):
    return render(request, 'learn_trainingOfDoctors.html')

def learn_trainingOfNurses(request):
    return render(request, 'learn_trainingOfNurses.html')

def learn_genderAndStaff(request):
    return render(request, 'learn_genderAndStaff.html')

def learn_raceAndStaff(request):
    return render(request, 'learn_raceAndStaff.html')

def learn_philanthropicNetworks(request):
    return render(request, 'learn_philanthropicNetworks.html')

def learn_surveyForTheCommitteeOnLunacy(request):
    return render(request, 'learn_surveyForTheCommitteeOnLunacy.html')

#def learn_fromYorkRetreatToFriendsAsylum(request):# one of the new grouping topic of articles; effort aborted
#    return render(request, 'learn_fromYorkRetreatToFriendsAsylum.html')

#def learn_reasoningAboutInsanity(request):# one of the new grouping topic of articles; effort aborted
#    return render(request, 'learn_reasoningAboutInsanity.html')

#    "medical treatment"

def learn_typesOfMentalIllness(request):
    return render(request, 'learn_typesOfMentalIllness.html')

def learn_moralTreatment(request):
    return render(request, 'learn_moralTreatment.html')

def learn_occupationalTherapy(request):
    return render(request, 'learn_occupationalTherapy.html')

def learn_asylumLibrary(request):
    return render(request, 'learn_asylumLibrary.html')

def learn_medicalTreatment(request):
    return render(request, 'learn_medicalTreatment.html')

def learn_medicalAdvancements(request):
    return render(request, 'learn_medicalAdvancements.html')

def learn_genderAndLengthOfStay(request):
    return render(request, 'learn_genderAndLengthOfStay.html')

def learn_genderAndTreatment(request):
    return render(request, 'learn_genderAndTreatment.html')

def learn_moralTreatmentAndFamily(request):
    return render(request, 'learn_moralTreatmentAndFamily.html')

def learn_GenderAndDeath(request):
    return render(request, 'learn_GenderAndDeath.html')


#    "patients"

def learn_caseStudies(request):
    return render(request, 'learn_caseStudies.html')

def learn_patientHometowns(request):
    return render(request, 'learn_patientHometowns.html')

def learn_patientDemographics(request):
    return render(request, 'learn_patientDemographics.html')

#    "religion"

def learn_mentalHealthAndQuakerTheology(request):
    glossary_list = Glossary.objects.order_by('term')
    term_list = [glossary.term for glossary in glossary_list]
    meaning_list = [glossary.meaning for glossary in glossary_list]
    glossary_dict = {}
    for (term, meaning) in zip(term_list, meaning_list):
        glossary_dict[term] = meaning
    return render(request, 'learn_mentalHealthAndQuakerTheology.html', {'glossary_dict': glossary_dict})

def learn_religiousLife(request):
    return render(request, 'learn_religiousLife.html')

def learn_religiousDiversity(request):
    return render(request, 'learn_religiousDiversity.html')

def learn_decisionToAdmitNonQuakers(request):
    return render(request, 'learn_decisionToAdmitNonQuakers.html')

def learn_theologyAndFamily(request):
    return render(request, 'learn_theologyAndFamily.html')

###### sidebar other ######

def glossary(request):
    glossary_object_list = Glossary.objects.order_by('term')
    glossary_list = [(glossary.term, glossary.meaning) for glossary in glossary_object_list]
    return render(request, 'glossary.html', {'glossary_list': glossary_list})


def bibliography(request):
    return render(request, 'bibliography.html')


###### essays ######

def essays(request):
    return render(request, 'essays.html')

def essay_27AnnaBroomall(request):
    return render(request, 'essay_27AnnaBroomall.html')

def essay_27CaseHistoryofHelenCLinsley(request):
    return render(request, 'essay_27CaseHistoryofHelenCLinsley.html')

def essay_27CaseHistoryofNellieSchofield(request):
    return render(request, 'essay_27CaseHistoryofNellieSchofield.html')

def essay_27CaseHistoryofYestaLefkowitz(request):
    return render(request, 'essay_27CaseHistoryofYestaLefkowitz.html')

def essay_27LeilaniFinalEssay(request):
    return render(request, 'essay_27LeilaniFinalEssay.html')

def essay_25Anna_Hannah_Bussom(request):
    return render(request, 'essay_25Anna_Hannah_Bussom.html')

def essay_25Caldwell_Matthews(request):
    return render(request, 'essay_25Caldwell_Matthews.html')

def essay_25Claire_Molly_Blumberg(request):
    return render(request, 'essay_25Claire_Molly_Blumberg.html')

def essay_25Clara_M_McAdam(request):
    return render(request, 'essay_25Clara_M_McAdam.html')

def essay_25Clara_Thompson(request):
    return render(request, 'essay_25Clara_Thompson.html')

def essay_25Frank_Atwood(request):
    return render(request, 'essay_25Frank_Atwood.html')

def essay_25Herman_Chaykin(request):
    return render(request, 'essay_25Herman_Chaykin.html')

def essay_25Ida_Eubank_Lena_Jent_Case_Study(request):
    return render(request, 'essay_25Ida_Eubank_Lena_Jent_Case_Study.html')

def essay_25Jean_Steward(request):
    return render(request, 'essay_25Jean_Steward.html')

def essay_25Katie_Pantales(request):
    return render(request, 'essay_25Katie_Pantales.html')

def essay_25Louis_Spaeth(request):
    return render(request, 'essay_25Louis_Spaeth.html')

def essay_25Quaker_Triangle(request):
    return render(request, 'essay_25Quaker_Triangle.html')

def essay_25RoarkScattergood_FinalDraft(request):
    return render(request, 'essay_25RoarkScattergood_FinalDraft.html')

def essay_25RoyECobb(request):
    return render(request, 'essay_25RoyECobb.html')

def essay_25SadieMcCaffery_CaseStudyNotes(request):
    return render(request, 'essay_25SadieMcCaffery_CaseStudyNotes.html')

def essay_25WilliamPNorris(request):
    return render(request, 'essay_25WilliamPNorris.html')

def essay_25WillieBachman(request):
    return render(request, 'essay_25WillieBachman.html')

def essay_25publicvsprivate(request):
    return render(request, 'essay_25publicvsprivate.html')

def essay_23Roark(request):
    return render(request, 'essay_23Roark.html')

def essay_22Bratt(request):
    return render(request, 'essay_22Bratt.html')

def essay_21scully(request):
    return render(request, 'essay_21scully.html')

def essay_21zhu(request):
    return render(request, 'essay_21zhu.html')

def essay_20cbattis(request):
    return render(request, 'essay_20cbattis.html')

def essay_18bkaplow(request):
    return render(request, 'essay_18bkaplow.html')

def essay_18cmichel(request):
    return render(request, 'essay_18cmichel.html')

def essay_17acorcoran(request):
    return render(request, 'essay_17acorcoran.html')

#datatables
def index_redirect(request):
    return redirect('/table/')

def patientTable(request):
    return render(request, 'patientTable.html')
