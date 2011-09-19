from django.core.management import setup_environ
import sys, random, string, csv
sys.path.append('/opt/django-projects/')
from stimulustracker import settings
setup_environ(settings)

import datetime, string

from stimulustracker.schools.models import SchoolType, SchoolStatus, DistrictType, DistrictStatus, StateEducationDepartment, District, School
from stimulustracker.stimulus.models import Agency, AwardType, PrimaryAward, SecondaryAward

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

#reader = csv.reader(open("All_GrantsY11Q1.csv"), dialect=csv.excel)
#reader.next()
#for row in reader:
#        if row[1] == "P":
#            if row[30] == "G":
#                at = "Grant"
#                ats = "grant"
#            awt, awtcreated = AwardType.objects.get_or_create(award_type=at, award_type_slug=ats)
#            funda = row[11]
#            funda_slug = slugify(funda[0:50])
#            ag, agcreated = Agency.objects.get_or_create(agency_name=funda, agency_name_slug=funda_slug)
#            aid = row[0]
#            aw_date_year = int(row[31][0:4])
#            aw_date_month = int(row[31][5:7])
#            aw_date_day = int(row[31][8:10])
#            aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
#            rname = row[18]
#            rstate = row[20]
#            rzip = row[19]
#            awid = row[21]
#            adesc = row[32]
#            try:
#                amt = float(row[33])
#            except:
#                amt = None
#            try:
#                amtd = float(row[40])
#            except:
#                amtd = None
#            try:
#                numjobs = float(row[38])
#            except:
#                numjobs = None
#            jcdesc = row[37]
#            try:
#                aw = PrimaryAward.objects.get(arra_id=aid)
#                aw.arra_id=aid
#                aw.award_type=awt
#                aw.awarding_agency=ag
#                aw.award_date=aw_date
#                aw.recipient_name=rname
#                aw.recipient_state=rstate
#                aw.recipient_zipcode=rzip
#                aw.award_id=awid
#                aw.award_description=adesc
#                aw.amount_awarded=amt
#                aw.amount_disbursed=amtd
#                aw.reported_number_of_jobs_created=numjobs
#                aw.jobs_created_description=jcdesc
#                aw.save()
#                print "Updated %s" % aw
#            except:
#                aw, awcreated = PrimaryAward.objects.get_or_create(arra_id=aid, award_type=awt, awarding_agency=ag, award_date=aw_date, recipient_name=rname, recipient_state=rstate, recipient_zipcode=rzip, award_id=awid, award_description=adesc, amount_awarded=amt, amount_disbursed=amtd, reported_number_of_jobs_created=numjobs, jobs_created_description=jcdesc)
#                print "Created %s" % aw
#
#reader = csv.reader(open("All_GrantsY11Q1.csv"), dialect=csv.excel)
#reader.next()
#for row in reader:
#    if row[1] == "S":
#        if row[30] == "G":
#                akey = row[0]
#                at = "Grant"
#                ats = "grant"
#                awt = AwardType.objects.get(id=1)
#                funda = row[11]
#                funda_slug = slugify(funda[0:50])
#                ag = Agency.objects.get(agency_name=funda, agency_name_slug=funda_slug)
#                try:
#                    aw_date_year = int(row[31][0:4])
#                    aw_date_month = int(row[31][5:7])
#                    aw_date_day = int(row[31][8:10])
#                    aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
#                except:
#                    continue
#                rduns = row[17]
#                rname = row[18]
#                rstate = row[20]
#                rzip = row[19]
#                awid = row[21]
#                sawid = row[23]
#                adesc = row[32]
#                try:
#                    amt = float(row[34])
#                except:
#                    amt = None
#                try:
#                    amtd = float(row[41])
#                except:
#                    amtd = float(0)
#                try:
#                    numjobs = float(row[38])
#                except:
#                    numjobs = None
#                jcdesc = row[37]
#                try:
#                    aw = PrimaryAward.objects.get(award_id=awid)
#                    try:
#                        sw = SecondaryAward.objects.get(award_id=sawid, award_key=akey, primary_award=aw)
#                        sw.award_description=adesc
#                        sw.amount_awarded=amt
#                        sw.amount_disbursed=amtd
#                        sw.reported_number_of_jobs_created=numjobs
#                        sw.jobs_created_description=jcdesc
#                        sw.save()
#                        print "Updated %s" % sw
#                    except:
#                        sw, swcreated = SecondaryAward.objects.get_or_create(primary_award=aw, award_type=awt, awarding_agency=ag, award_date=aw_date, recipient_name=rname, recipient_state=rstate, recipient_zipcode=rzip, award_id=sawid, award_description=adesc, amount_awarded=amt, amount_disbursed=amtd, reported_number_of_jobs_created=numjobs, jobs_created_description=jcdesc, award_key=akey)
#                        print "Created %s" % sw
#                except:
#                    continue

#To just update what's in place, use these.

# Update the existing Primary Awards

reader = csv.reader(open("All_GrantsY11Q2.csv"), dialect=csv.excel)
reader.next()
for row in reader:
        if row[1] == "P":
            adesc = row[32]
            if row[30] == "G":
                try:
                    at = "Grant"
                    ats = "grant"
                    awt = AwardType.objects.get(award_type=at, award_type_slug=ats)
                    funda = row[11]
                    funda_slug = slugify(funda[0:50])
                    ag = Agency.objects.get(agency_name=funda, agency_name_slug=funda_slug)
                    aid = row[0]
                    aw_date_year = int(row[31][0:4])
                    aw_date_month = int(row[31][5:7])
                    aw_date_day = int(row[31][8:10])
                    aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
                    rname = row[18]
                    rstate = row[20]
                    rzip = row[19]
                    awid = row[21]
                    adesc = row[32]
                    try:
                        amt = float(row[33])
                    except:
                        amt = None
                    try:
                        amtd = float(row[40])
                    except:
                        amtd = None
                    try:
                        numjobs = float(row[38])
                    except:
                        numjobs = None
                    jcdesc = row[37]
                    aw = PrimaryAward.objects.get(arra_id=aid)
                    aw.arra_id=aid
                    aw.award_type=awt
                    aw.awarding_agency=ag
                    aw.award_date=aw_date
                    aw.recipient_name=rname
                    aw.recipient_state=rstate
                    aw.recipient_zipcode=rzip
                    aw.award_id=awid
                    aw.award_description=adesc
                    aw.amount_awarded=amt
                    aw.amount_disbursed=amtd
                    aw.reported_number_of_jobs_created=numjobs
                    aw.jobs_created_description=jcdesc
                    aw.save()
                    print "Updated %s" % aw
                except:
                    continue

# Updates the existing secondary awards

reader = csv.reader(open("All_GrantsY11Q2.csv"), dialect=csv.excel)
reader.next()
for row in reader:
    if row[1] == "S":
        if row[30] == "G":
                akey = row[0]
                at = "Grant"
                ats = "grant"
                awt = AwardType.objects.get(id=1)
                funda = row[11]
                funda_slug = slugify(funda[0:50])
                ag = Agency.objects.get(agency_name=funda, agency_name_slug=funda_slug)
                try:
                    aw_date_year = int(row[31][0:4])
                    aw_date_month = int(row[31][5:7])
                    aw_date_day = int(row[31][8:10])
                    aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
                except:
                    continue
                rduns = row[17]
                rname = row[18]
                rstate = row[20]
                rzip = row[19]
                awid = row[21]
                sawid = row[23]
                adesc = row[32]
                try:
                    amt = float(row[34])
                except:
                    amt = None
                try:
                    amtd = float(row[41])
                except:
                    amtd = float(0)
                try:
                    numjobs = float(row[38])
                except:
                    numjobs = None
                jcdesc = row[37]
                try:
                    sw = SecondaryAward.objects.get(award_id=sawid, award_key=akey, recipient_sub_duns_number=rduns)
                except:
                    continue
                sw.award_description=adesc
                sw.amount_awarded=amt
                sw.amount_disbursed=amtd
                sw.reported_number_of_jobs_created=numjobs
                sw.jobs_created_description=jcdesc
                sw.save()
                print "Updated %s" % sw

# This finds a specific primary award and adds it. Replace the numbers in the ids with the award ids you want to add.

#ids = ['H391A090007', 'H391A090103']
#for i in ids:
#    reader = csv.reader(open("All_GrantsY11Q1.csv"), dialect=csv.excel)
#    reader.next()
#    for row in reader:
#        if row[21]==i:
#            if row[1] == "P":
#                adesc = row[32]
#                if row[30] == "G":
#                    try:
#                        at = "Grant"
#                        ats = "grant"
#                        awt = AwardType.objects.get(award_type=at, award_type_slug=ats)
#                        funda = row[11]
#                        funda_slug = slugify(funda[0:50])
#                        ag = Agency.objects.get(agency_name=funda, agency_name_slug=funda_slug)
#                        aid = row[0]
#                        aw_date_year = int(row[31][0:4])
#                        aw_date_month = int(row[31][5:7])
#                        aw_date_day = int(row[31][8:10])
#                        aw_date = datetime.datetime(aw_date_year, aw_date_month, aw_date_day)
#                        rname = row[18]
#                        rstate = row[20]
#                        rzip = row[19]
#                        awid = row[21]
#                        adesc = row[32]
#                        try:
#                            amt = float(row[33])
#                        except:
#                            amt = None
#                        try:
#                            amtd = float(row[40])
#                        except:
#                            amtd = None
#                        try:
#                            numjobs = float(row[38])
#                        except:
#                            numjobs = None
#                        jcdesc = row[37]
#                        aw, awcreated = PrimaryAward.objects.get_or_create(arra_id=aid, award_type=awt, awarding_agency=ag, award_date=aw_date, recipient_name=rname, recipient_state=rstate, recipient_zipcode=rzip, award_id=awid, award_description=adesc, amount_awarded=amt, amount_disbursed=amtd, reported_number_of_jobs_created=numjobs, jobs_created_description=jcdesc)
#                        print "Created %s" % aw
#                    except:
#                        continue