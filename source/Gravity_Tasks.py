from Objects            import Gravity_obj
from Utilities          import read_data_string
from Report_Generator   import Creat_Report
from Logo               import *
from Solvers            import *
from matplotlib.pyplot  import *
from Power_Spectrum     import Power_Spectrum_Plot_Construction, Real_Space_Power_Spectrum_Plot_Construction
from Data_generator     import *

def Gravity_Solver():
    #Solver Type
    Geometry_type_name = read_data_string(tag_name='Geometry_type',file_name='parameters/parameters.xml')
    Solver_type_name   = read_data_string(tag_name ='Solver_type',file_name ='parameters/parameters.xml')
    Solver_type        = Geometry_type_name + "+" + Solver_type_name
    if (Solver_type == "AdS4+RK4"):
       return AdS4_RK4_solver
    else:
       print "ERROR : THE SOLVER IS NOT DEFINED FOR THIS GEOMETRY + SOLVER TYPE"
       return NO_SOLVER


def main_tasks():
   
    Print_logo()

    print "\n"

    Gravity_object = Gravity_obj()    
    Solver         = Gravity_Solver() 
    Solver(Gravity_object)

    if Gravity_object.field.Horizon :
       print "Horizon time is : ", Gravity_object.field.time
    else:
       print "Horizon is not formed ...! (You may want to increase i_max)"

    Create_data(Gravity_object)#added, generates just the data without the report.

    if Gravity_object.output.Real_Space_Power_Spectrum_status:
       Real_Space_Power_Spectrum_Plot_Construction(Gravity_obj,file_loc_save="Output/Real_Space_Power_Spectrum/")

    if Gravity_object.output.Power_Spectrum_status:
       Power_Spectrum_Plot_Construction(Gravity_obj,file_loc_save="Output/Power_Spectrum_data/",file_loc_load="Output/Power_Spectrum_data/")

    if Gravity_object.output.Report_status:
       Creat_Report(Gravity_object)

    #figure(1)
    #plot(Gravity_object.field.r,Gravity_object.field.Pi)
    #show()
    #figure(2)
    #plot(Gravity_object.field.r,Gravity_object.field.Phi)
    #show()

    Print_ending()
