from django.core.management import setup_environ
import sys, random, string
sys.path.append('/opt/django-projects/')
from stimulustracker import settings
setup_environ(settings)

from stimulustracker.schools.models import SchoolType, SchoolStatus, DistrictType, DistrictStatus, StateEducationDepartment, District, School
from stimulustracker.geography.models import State, County, City, CongressionalDistrict, Zipcode
from stimulustracker.demographics.models import DistrictDemographics, SchoolDemographics

from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from django.template.defaultfilters import slugify, urlize
from django.contrib.gis.geos import Point


#mapping = {'state_name' : 'NAME', # The 'name' model field maps to the 'str' layer field.
#           'state_fips' : 'STATEFP',
#           'poly' : 'POLYGON', # For geometry fields use OGC name.
#          } # The mapping is a dictionary
#lm = LayerMapping(State, 'tl_2008_us_state.shp', mapping)
#lm.save(verbose=True) # Save the layermap, imports the data.
#
# mapping = {'county_name' : 'NAME', # The 'name' model field maps to the 'str' layer field.
#            'county_fips' : 'COUNTYFP',
#            'state_fips' : 'STATEFP',
#            'poly' : 'POLYGON', # For geometry fields use OGC name.
#           } # The mapping is a dictionary
# lm = LayerMapping(County, '/Users/mwaite/django-projects/stimulustracker/data/shapefiles/tl_2008_us_county.shp', mapping, encoding='windows-1251')
# lm.save(verbose=True) # Save the layermap, imports the data.
# 
# c = County.objects.all()
# for o in c:
#     s = State.objects.get(state_fips=o.state_fips)
#     cu = County(id=o.id, state=s, state_fips=o.state_fips, county_name=o.county_name, county_slug=o.county_slug, county_fips=o.county_fips, poly=o.poly)
#     cu.save()
#     print "updated %s" % o.county_name
#
# mapping = {'state_name' : 'NAME', # The 'name' model field maps to the 'str' layer field.
#            'state_fips' : 'STATEFP',
#            'poly' : 'POLYGON', # For geometry fields use OGC name.
#           } # The mapping is a dictionary
# lm = LayerMapping(State, '/Users/mwaite/django-projects/stimulustracker/data/shapefiles/tl_2008_us_state.shp', mapping)
# lm.save(verbose=True) # Save the layermap, imports the data.
#
# mapping = {'zipcode' : 'ZCTA5CE', # The 'name' model field maps to the 'str' layer field.
#            'poly' : 'POLYGON', # For geometry fields use OGC name.
#           } # The mapping is a dictionary
# lm = LayerMapping(Zipcode, '/Users/mwaite/django-projects/stimulustracker/data/shapefiles/tl_2008_us_zcta5.shp', mapping)
# lm.save(verbose=True) # Save the layermap, imports the data.
#
# mapping = {'state_fips' : 'STATE', # The 'name' model field maps to the 'str' layer field.
#            'congressional_district_number' : 'NAME',
#            'poly' : 'POLYGON', # For geometry fields use OGC name.
#           } # The mapping is a dictionary
# lm = LayerMapping(CongressionalDistrict, '/Users/mwaite/django-projects/stimulustracker/data/shapefiles/cd99_110.shp', mapping)
# lm.save(verbose=True) # Save the layermap, imports the data.
#
# c = CongressionalDistrict.objects.all()
# for o in c:
#     s = State.objects.get(state_fips=o.state_fips)
#     cu = CongressionalDistrict(id=o.id, state=s, state_fips=o.state_fips, congressional_district_number=o.congressional_district_number, congressional_district=o.congressional_district, congressional_district_slug=o.congressional_district_slug, poly=o.poly)
#     cu.save()
#     print "updated %s" % o.congressional_district

#Creates the State Education Departments
#f = open('ag061c.DAT','r') 
#for line in f.xreadlines():
#    try:
#        stfips = line[0:2]
#        s = State.objects.get(state_fips=stfips)
#        sed, sedcreated = StateEducationDepartment.objects.get_or_create(state=s, state_name=s.state_name, state_name_slug=s.state_slug)
#    except:
#        print stfips
#f.close()
#
#f = open('ag061c.DAT','r') 
#for line in f.xreadlines():
#    try:
#        leaid = line[0:7]
#        stfips = line[0:2]
#        s = State.objects.get(state_fips=stfips)
#        sed = StateEducationDepartment.objects.get(state=s)
#        c_st = line[237:239]
#        c_co = line[239:242]
#        try:
#            c = County.objects.get(state_fips=c_st, county_fips=c_co)
#        except:
#            c = None
#        n = string.capwords(line[21:81])
#        n = string.strip(n)
#        ns = slugify(n)[0:50]
#        a = string.strip(line[91:121])
#        a = string.capwords(a)
#        a = a.decode('windows-1251')
#        a = a.encode('utf-8')
#        ci = string.capwords(line[121:151])
#        ci = string.strip(ci)
#        st = line[222:224]
#        zipc = line[224:229]
#        try:
#            x = float(line[288:297])
#            y = float(line[297:308])
#            pnt = Point(y,x)
#        except:
#            pnt = Point(0,0)
#        dt = DistrictType.objects.get(id=line[233:234])
#        ds = DistrictStatus.objects.get(id=line[308:309])
#        d = District(state_education_department=sed, county=c, district_id=leaid, district_name=n, district_name_slug=ns, address=a, city=ci, state=st, zipcode=zipc, point=pnt, district_type=dt, district_status=ds)
#        d.save()
#        sy = "2006-2007"
#        tsc = line[314:319]
#        tst = line[340:347]
#        tt = float(line[319:326])
#        dd = DistrictDemographics(district=d, school_year=sy, total_schools=tsc, total_students=tst, total_teachers=tt)
#        dd.save()
#    except:
#        print line[0:7]
#f.close()
#
#files = ['Sc061cai.dat','Sc061ckn.dat','Sc061cow.dat']
#
#for fi in files:
#    f = open(fi,'r') 
#    for line in f.xreadlines():
#        try:
#            sid = line[0:12]
#            d = District.objects.get(district_id=line[0:7])
#            sn = string.capwords(line[106:156])
#            sn = string.strip(sn)
#            sn = sn.decode('windows-1251')
#            sn = sn.encode('utf-8')
#            sns = slugify(sn)
#            a = string.strip(line[237:267])
#            a = string.capwords(a)
#            a = a.decode('windows-1251')
#            a = a.encode('utf-8')
#            ci = string.capwords(line[267:297])
#            ci = string.strip(ci)
#            st = line[297:299]
#            zipc = line[299:304]
#            try:
#                x = float(line[312:321])
#                y = float(line[321:332])
#                pnt = Point(y,x)
#            except:
#                pnt = Point(0,0)
#            sty = SchoolType.objects.get(id=line[308:309])
#            ss = SchoolStatus.objects.get(id=line[309:310])
#            s = School(district=d, ccd_school_id=sid, school_name=sn, school_name_slug=sns, address=a, city=ci, state=st, zipcode=zipc, school_type=sty, school_status=ss, point=pnt)
#            s.save()
#            sy = "2006-2007"
#            if line[381:382] == "1":
#                t1 = 1
#            else:
#                t1 = 0
#            if line[382:383] == "1":
#                swt1 = 1
#            else:
#                swt1 = 0
#            if line[383:384] == "1":
#                ms = 1
#            else:
#                ms = 0
#            if line[384:385] == "1":
#                cs = 1
#            else:
#                cs = 0
#            frl = line[394:398]
#            mi = line[398:402]
#            ai = line[1366:1370]
#            api = line[1382:1386]
#            hs = line[1398:1402]
#            bs = line[1414:1418]
#            ws = line[1430:1434]
#            tot = line[1362:1366]
#            tottea = float(line[371:376])
#            stutr = float(line[1450:1456])
#            sd = SchoolDemographics(school=s, school_year=sy, title_i=t1, all_school_title_i=swt1, magnet_school=ms, charter_school=cs, frl_students=frl, migrant_students=mi, american_indian_students=ai, asian_pacific_islander_students=api, hispanic_students=hs, black_students=bs, white_students=ws, total_students=tot, total_teachers=tottea, student_teacher_ratio=stutr)
#            sd.save()
#        except:
#            print line[0:12]
#    f.close()

f = open('ag071b.txt', 'r')
#f = open('ag081a.txt','r')
for line in f.xreadlines():
    line = line.split("\t")
    leaid = line[0]
    #    stfips = line[0:2]
    #    s = State.objects.get(state_fips=stfips)
    #    sed = StateEducationDepartment.objects.get(state=s)
    #    c_st = line[237:239]
    #    c_co = line[239:242]
    #    try:
    #        c = County.objects.get(state_fips=c_st, county_fips=c_co)
    #    except:
    #        c = None
    #    n = string.capwords(line[21:81])
    #    n = string.strip(n)
    #    ns = slugify(n)[0:50]
    #    a = string.strip(line[91:121])
    #    a = string.capwords(a)
    #    a = a.decode('windows-1251')
    #    a = a.encode('utf-8')
    #    ci = string.capwords(line[121:151])
    #    ci = string.strip(ci)
    #    st = line[222:224]
    #    zipc = line[224:229]
    #    try:
    #        x = float(line[288:297])
    #        y = float(line[297:308])
    #        pnt = Point(y,x)
    #    except:
    #        pnt = Point(0,0)
    #    dt = DistrictType.objects.get(id=line[233:234])
    #    ds = DistrictStatus.objects.get(id=line[308:309])
    try:
        d = District.objects.get(district_id=leaid)
    except:
        continue
    sy = "2007-2008"
#    sy = "2008-2009"
    tsc = line[30] #this is 30 for 2007-2008
    tst = line[33] #this is 33 in 2007-2008
    tt = float(line[31]) #this is 31 in 2007-2008
    #tsc = line[29] #this is 30 for 2007-2008
    #tst = line[31] #this is 33 in 2007-2008
    #tt = float(line[40]) #this is 31 in 2007-2008
    dd = DistrictDemographics(district=d, school_year=sy, total_schools=tsc, total_students=tst, total_teachers=tt)
    dd.save()
    print dd
    #except:
    #    print "bork"
f.close()