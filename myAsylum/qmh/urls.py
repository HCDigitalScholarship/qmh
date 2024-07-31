
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.contrib.flatpages import views as flat_views
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [

    #flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', views.home, name='home'),
    # topnav
    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),# summer 2019 team decided that a contact form no longer needed; contact button is a link to "mailto:<hc-libraries>"
    path('related-projects/', views.related_projects, name='related-projects'),

    # home
    path('visualizations/', views.visualizations, name='visualizations'),
        path('visualizations/scatterplot-patient-admit-age-admit-year/', views.visual_scatterplotPatientAdmitAgeVsAdmitYear, name="visual_scatterplotPatientAdmitAgeVsAdmitYear"),
        path('visualizations/heatmap-patient-monthly-admission-frequency/', views.visual_heatmapPatientMonthlyAdmissionFrequency, name="visual_heatmapPatientMonthlyAdmissionFrequency"),
        path('visualizations/sankey-philanthropists-organizations-association/', views.visual_sankeyPhilanthropistsOrganizationsAssociation, name="visual_sankeyPhilanthropistsOrganizationsAssociation"),


    # sidebar
    # learn
    #path('learn/', views.learn, name='learn')

        # "the asylum"
        path('the-york-retreat', views.learn_theYorkRetreat, name='learn_theYorkRetreat'),
        path('foundation', views.learn_foundation, name='learn_foundation'),
        path('structure-and-governance', views.learn_structureAndGovernance, name='learn_structureAndGovernance'),
        path('changes-in-admin-over-time', views.learn_changesInAdminOverTime, name='learn_changesInAdminOverTime'),
        path('asylum-architecture', views.learn_asylumArchitecture, name='learn_asylumArchitecture'),
        path('gender-and-staff', views.learn_genderAndStaff, name='learn_genderAndStaff'),
        path('gurney-cottage/', views.learn_gurneyCottage, name='learn_gurneyCottage'),
        path('training-of-doctors', views.learn_trainingOfDoctors, name='learn_trainingOfDoctors'),
        path('training-of-nurses', views.learn_trainingOfNurses, name='learn_trainingOfNurses'),
        path('race-and-staff', views.learn_raceAndStaff, name='learn_raceAndStaff'),
        path('philanthropic-networks', views.learn_philanthropicNetworks, name='learn_philanthropicNetworks'),
        path('survey-for-the-committee-on-lunacy', views.learn_surveyForTheCommitteeOnLunacy, name='learn_surveyForTheCommitteeOnLunacy'),
        #path('learn/from-york-retreat-to-friends-asylumf', views.learn_fromYorkRetreatToFriendsAsylum, name='learn_fromYorkRetreatToFriendsAsylum'),# one of the new grouping topic of articles; effort aborted
        #path('learn/reasoning-about-insanity', views.learn_reasoningAboutInsanity, name='learn_reasoningAboutInsanity'),# one of the new grouping topic of articles; effort aborted

        # "medical treatment"
        path('types-of-mental-illness', views.learn_typesOfMentalIllness, name='learn_typesOfMentalIllness'),
        path('moral-treatment', views.learn_moralTreatment, name='learn_moralTreatment'),
        path('occupational-therapy', views.learn_occupationalTherapy, name='learn_occupationalTherapy'),
        path('asylum-library', views.learn_asylumLibrary, name='learn_asylumLibrary'),
        path('medical-treatment', views.learn_medicalTreatment, name='learn_medicalTreatment'),
        path('learn-medicalAdvancements', views.learn_medicalAdvancements, name='learn_medicalAdvancements'),
        path('gender-and-length-of-stay', views.learn_genderAndLengthOfStay, name='learn_genderAndLengthOfStay'),
        path('gender-and-treatment', views.learn_genderAndTreatment, name='learn_genderAndTreatment'),
        path('moral-treatment-and-family', views.learn_moralTreatmentAndFamily, name='learn_moralTreatmentAndFamily'),
        path('gender-and-death', views.learn_GenderAndDeath, name='learn_GenderAndDeath'),    

        # "patients"
        path('case-studies', views.learn_caseStudies, name='learn_caseStudies'),
        path('patient-hometowns', views.learn_patientHometowns, name='learn_patientHometowns'),
        path('patient-demographics', views.learn_patientDemographics, name='learn_patientDemographics'),

        # "religion"
        path('mental-health-and-quaker-theology', views.learn_mentalHealthAndQuakerTheology, name='learn_mentalHealthAndQuakerTheology'),
        path('religious-life', views.learn_religiousLife, name='learn_religiousLife'),
        path('religious-diversity', views.learn_religiousDiversity, name='learn_religiousDiversity'),
        path('decision-to-admit-nonquakers', views.learn_decisionToAdmitNonQuakers, name='learn_decisionToAdmitNonQuakers'),
        path('theology-and-family', views.learn_theologyAndFamily, name='learn_theologyAndFamily'),

    path('glossary/', views.glossary, name='glossary'),
    path('bibliography/', views.bibliography, name='bibliography'),

    # essays
    path('essays/', views.essays, name='essays'),
    path('essays/20cbattis/', views.essay_20cbattis, name='essay_20cbattis'),
    path('essays/18bkaplow/', views.essay_18bkaplow, name='essay_18bkaplow'),
    path('essays/18cmichel/', views.essay_18cmichel, name='essay_18cmichel'),
    path('essays/17acorcoran/', views.essay_17acorcoran, name='essay_17acorcoran'),
    path('essays/21zhu/', views.essay_21zhu, name='essay_21zhu'),
    path('essays/21scully/', views.essay_21scully, name='essay_21scully'),
    path('essays/22Bratt/', views.essay_22Bratt, name='essay_22Bratt'),
    path('essays/23Roark/', views.essay_23Roark, name='essay_23Roark'),
    path('essays/25Anna_Hannah_Bussom/', views.essay_25Anna_Hannah_Bussom, name='essay_25Anna_Hannah_Bussom'),
    path('essays/25Caldwell_Matthews/', views.essay_25Caldwell_Matthews, name='essay_25Caldwell_Matthews'),
    path('essays/25Claire_Molly_Blumberg/', views.essay_25Claire_Molly_Blumberg, name='essay_25Claire_Molly_Blumberg'),
    path('essays/25Clara_M_McAdam/', views.essay_25Clara_M_McAdam, name='essay_25Clara_M_McAdam'),
    path('essays/25Clara_Thompson/', views.essay_25Clara_Thompson, name='essay_25Clara_Thompson'),
    path('essays/25Frank_Atwood/', views.essay_25Frank_Atwood, name='essay_25Frank_Atwood'),
    path('essays/25Herman_Chaykin/', views.essay_25Herman_Chaykin, name='essay_25Herman_Chaykin'),
    path('essays/25Ida_Eubank_Lena_Jent_Case_Study/', views.essay_25Ida_Eubank_Lena_Jent_Case_Study, name='essay_25Ida_Eubank_Lena_Jent_Case_Study'),
    path('essays/25Jean_Steward/', views.essay_25Jean_Steward, name='essay_25Jean_Steward'),
    path('essays/25Katie_Pantales/', views.essay_25Katie_Pantales, name='essay_25Katie_Pantales'),
    path('essays/25Louis_Spaeth/', views.essay_25Louis_Spaeth, name='essay_25Louis_Spaeth'),
    path('essays/25Quaker_Triangle/', views.essay_25Quaker_Triangle, name='essay_25Quaker_Triangle'),
    path('essays/25RoarkScattergood_FinalDraft/', views.essay_25RoarkScattergood_FinalDraft, name='essay_25RoarkScattergood_FinalDraft'),
    path('essays/25RoyECobb/', views.essay_25RoyECobb, name='essay_25RoyECobb'),
    path('essays/25SadieMcCaffery_CaseStudyNotes/', views.essay_25SadieMcCaffery_CaseStudyNotes, name='essay_25SadieMcCaffery_CaseStudyNotes'),
    path('essays/25WilliamPNorris/', views.essay_25WilliamPNorris, name='essay_25WilliamPNorris'),
    path('essays/25WillieBachman/', views.essay_25WillieBachman, name='essay_25WillieBachman'),
    path('essays/25publicvsprivate/', views.essay_25publicvsprivate, name='essay_25publicvsprivate'),

    path('essays/27AnnaBroomall/', views.essay_27AnnaBroomall, name='essay_27AnnaBroomall'),
    path('essays/27CaseHistoryofHelenCLinsley/', views.essay_27CaseHistoryofHelenCLinsley, name='essay_27CaseHistoryofHelenCLinsley'),
    path('essays/27CaseHistoryofNellieSchofield/', views.essay_27CaseHistoryofNellieSchofield, name='essay_27CaseHistoryofNellieSchofield'),
    path('essays/27CaseHistoryofYestaLefkowitz/', views.essay_27CaseHistoryofYestaLefkowitz, name='essay_27CaseHistoryofYestaLefkowitz'),
    path('essays/27LeilaniFinalEssay/', views.essay_27LeilaniFinalEssay, name='essay_27LeilaniFinalEssay'),

    path('admission-data/', views.patientTable, name='patientTable'),

    ]
