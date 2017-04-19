from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import os

names = ['HRHHID','HRMONTH','HRYEAR4','HURESPLI','HUFINAL','HUSPNISH',\
        'HETENURE','HEHOUSUT','HETELHHD','HETELAVL','HEPHONEO','HEFAMINC',\
        'HUTYPEA','HUTYPB','HUTYPC','HWHHWGT','HRINTSTA','HURNUMHOU','HRHTYPE',\
        'HRMIS','HUINTTYP','HUPRSCNT','HRLONGLK','HRHHID2','HWHHWTLN','FILLER0',\
        'HUBUS','HUBUSL1','HUBUSL2','HUBUSL3','HUBUSL4','GEREG','GEDIV','FILLER1',\
        'GESTFIPS','FILLER2','GTCBSA','GTCO','GTCBSAST','GTMETSTA','GTINDVPC',\
        'GTCBSASZ','GTCSA','FILLER3','FILLER4','PERRP','PEPARENT','PRTAGE','PRTFAGE',\
        'PEMARITL','PESPOUSE','PESEX','PEAFEVER','FILLER5','PEAFNOW','PEEDUCA',\
        'PTDTRACE','PRDTHSP', 'PUCHINHH','FILLER6','PULINENO','FILLER7','PRFAMNUM',\
        'PRFAMREL','PRFAMTYP','PEHSPNON','PRMARSTA']
colspecs = ((0,15),(15,17),(17,21),(21,23),(23,26),(26,28),\
            (28,30),(30,32),(32,34),(34,36),(36,38),(38,40),\
            (40,42),(42,44),(44,46),(46,56),(56,58),(58,60),(60,62),\
            (62,64),(64,66),(66,68),(68,70),(70,75),(75,77),(77,78),\
            (78,80),(80,82),(82,84),(84,86),(86,88),(88,90),(90,91),(91,92),\
            (92,94),(94,95),(95,100),(100,103),(103,104),(104,105),(105,106),\
            (106,107),(107,110),(110,113),(113,117),(117,119),(119,121),(121,123),(123,124),\
            (124,126),(126,128),(128,130),(130,132),(132,134),(134,136),(136,138), \
            (138,140),(140,142),(142,144),(144,146),(146,148),(148,150),(150,152), \
            (152,154),(154,156),(156,158),(158,160))
data = pd.read_fwf('jan16pub.dat', names = names, colspecs=colspecs, indexcol = False)

# Part d
# HEHOUSUT : TYPE OF HOUSING UNIT
# d = {0: OTHER UNIT; 1:HOUSE, APARTMENT, FLAT; 2: HU IN NONTRANSIENT HOTEL, MOTEL, ETC.;\
#      3: HU PERMANENT IN TRANSIENT HOTEL, MOTEL; 4: HU IN ROOMING HOUSE; 5: MOBILE HOME OR \
#      TRAILER W/NO PERM. ROOM ADDED; 6: MOBILE HOME OR TRAILER W/1 OR MORE PERM. ROOMS ADDED;\
#      7: HU NOT SPECIFIED ABOVE; 8: QUARTERS NOT HU IN ROOMING OR BRDING HS; 9: UNIT NOT PERM.\
#      IN TRANSIENT HOTL, MOTL; 10: UNOCCUPIED TENT SITE OR TRLR SITE; 11: STUDENT QUARTERS IN \
#      COLLEGE DORM; 12: OTHER UNIT NOT SPECIFIED ABOVE}
print(data['HEHOUSUT'].quantile(q=0.25))
print(data['HEHOUSUT'].median())
print(data['HEHOUSUT'].quantile(q=0.75))
print(data['HEHOUSUT'].mode())

# HEFAMINC: FAMILY INCOME                                  
# d = {1: LESS THAN 5,000; 2: 5,000 TO 7,499; 3: 7,500 TO 9,999; 4: 10,000 TO 12,499; \
#      5: 12,500 TO 14,999; 6: 15,000 TO 19,999; 7: 20,000 TO 24,999; 8: 25,000 TO 29,999; \
#      9: 30,000 TO 34,999; 10: 35,000 TO 39,999; 11: 40,000 TO 49,999; 12: 50,000 TO 59,999; \
#      13: 60,000 TO 74,999; 14: 75,000 TO 99,999; 15: 100,000 TO 149,999; 16: 150,000 OR MORE}
print(data['HEFAMINC'].quantile(q=0.25))
print(data['HEFAMINC'].median())
print(data['HEFAMINC'].quantile(q=0.75))
print(data['HEFAMINC'].mode())

# HURNUMHOU: TOTAL NUMBER OF PERSONS LIVING IN THE HOUSEHOLD
print(data['HURNUMHOU'].quantile(q=0.25))
print(data['HURNUMHOU'].median())
print(data['HURNUMHOU'].quantile(q=0.75))
print(data['HURNUMHOU'].mode())

# GEREG: REGION          
# d = {1: NORTHEAST; 2: MIDWEST (FORMERLY NORTH CENTRAL); 3: SOUTH; 4: WEST}
print(data['GEREG'].quantile(q=0.25))
print(data['GEREG'].median())
print(data['GEREG'].quantile(q=0.75))
print(data['GEREG'].mode())

          
# PEMARITL: MARITAL STATUS                             
# d = {1: MARRIED - SPOUSE PRESENT; 2: MARRIED - SPOUSE ABSENT; 3: WIDOWED; 4: DIVORCED; \
#      5: SEPARATED; 6: NEVER MARRIED}
print(data['PEMARITL'].quantile(q=0.25))
print(data['PEMARITL'].median())
print(data['PEMARITL'].quantile(q=0.75))
print(data['PEMARITL'].mode())

# PEEDUCA: HIGHEST LEVEL OF SCHOOL                       
# d = {31: LESS THAN 1ST GRADE; 32: 1ST, 2ND, 3RD OR 4TH GRADE; 33: 5TH OR 6TH GRADE; \
#      34: 7TH OR 8TH GRADE; 35: 9TH GRADE; 36: 10TH GRADE; 37: 11TH GRADE; 38 12TH GRADE \
#      NO DIPLOMA; 39: HIGH SCHOOL GRAD-DIPLOMA OR EQUIV (GED); 40: SOME COLLEGE BUT NO DEGREE; \
#      41: ASSOCIATE DEGREE-OCCUPATIONAL/VOCATIONAL; 42: ASSOCIATE DEGREE-ACADEMIC PROGRAM; \
#      43: BACHELOR'S DEGREE (EX: BA, AB, BS); 44: MASTER'S DEGREE (EX: MA, MS, MEng, MEd, MSW); \
#      45: PROFESSIONAL SCHOOL DEG (EX: MD, DDS, DVM); 46: DOCTORATE DEGREE (EX: PhD, EdD)}
print(data['PEEDUCA'].quantile(q=0.25))
print(data['PEEDUCA'].median())
print(data['PEEDUCA'].quantile(q=0.75))
print(data['PEEDUCA'].mode())

# PTDTRACE: RACE                                           
# d = {01: White Only; 02: Black Only; 03: American Indian, Alaskan Native Only; 04: Asian Only; \                  
#      05: Hawaiian/Pacific Islander Only; 06: White-Black; 07: White-AI; 08: White-Asian; 09: White-HP; \                          
#      10: Black-AI; 11: Black-Asian; 12: Black-HP; 13: AI-Asian; 14: AI-HP; 15: Asian-HP; 16: W-B-AI; \                            
#      17: W-B-A; 18: W-B-HP; 19: W-AI-A; 20: W-AI-HP; 21: W-A-HP; 22: B-AI-A; 23: W-B-AI-A; 24: W-AI-A-HP; \                               
#      25: Other 3 Race Combinations; 26: Other 4 and 5 Race Combinations} 
print(data['PTDTRACE'].quantile(q=0.25))
print(data['PTDTRACE'].median())
print(data['PTDTRACE'].quantile(q=0.75))
print(data['PTDTRACE'].mode())

# PRMARSTA : MARITAL STATUS BASED ON ARMED FORCES PARTICIPATION    
# d = {1: MARRIED, CIVILIAN SPOUSE PRESENT; 2: MARRIED, ARMED FORCES SPOUSE PRESENT; 
#      3: MARRIED, SPOUSE ABSENT (EXC. SEPARATED); 4: WIDOWED; 5: DIVORCED; \
#      6: SEPARATED; 7: NEVER MARRIED}
print(data['PRMARSTA'].quantile(q=0.25))
print(data['PRMARSTA'].median())
print(data['PRMARSTA'].quantile(q=0.75))
print(data['PRMARSTA'].mode())
       

# Part e
graph = True

if graph:
    '''
    --------------------------------------------------------------------
    cur_path    = string, path name of current directory
    output_fldr = string, folder in current path to save files
    output_dir  = string, total path of images folder
    output_path = string, path of file name of figure to be saved
    Fig_e  = Boolean, = True if make a 2D histogram 
    --------------------------------------------------------------------
    '''
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)
    
    # Plot the histogram of income
    inc_data = data['HEFAMINC'].abs()
    fig, ax = plt.subplots()
    num_bins = 16
    weights = (1/inc_data.shape[0]) * np.ones_like(inc_data)
    n, bin_cuts, patches = plt.hist(inc_data, num_bins, weights = weights)
    plt.xlim([0,16])
    plt.title('Frequency histogram of the family income index',fontsize = 17)
    plt.xlabel('Family Income Index')
    plt.ylabel('Frequency')
    output_path = os.path.join(output_dir, 'Fig_1')
    plt.savefig(output_path)
    plt.show()
    plt.close()


    # Part f
    data1 = data[data['HUSPNISH']==1]
    # HUSPNISH: is Spanish the only language spoken by all members of this household
    # who are 15 years of age or older? yes 1
    # Plot the histogram of income
    inc_data1 = data1['HEFAMINC'].abs()
    fig, ax = plt.subplots()
    weights1 = (1/inc_data1.shape[0]) * np.ones_like(inc_data1)
    n, bin_cuts, patches = plt.hist(inc_data1, num_bins, weights = weights1)
    plt.xlim([0,16])
    plt.title('Frequency histogram of Spanish only family income index',fontsize = 17)
    plt.xlabel('Family Income Index')
    plt.ylabel('Frequency')
    output_path = os.path.join(output_dir, 'Fig_2')
    plt.savefig(output_path)
    plt.show()
    plt.close()

























