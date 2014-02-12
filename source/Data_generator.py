def Create_data(Grav_obj):
	print "\n\ncreating datalog\n\n"
	f = open('datalog.txt', 'w')
	
	f.write('Field properties\n')
	f.write('\tGeometry: %s \n' %(Grav_obj.Geometry_type_name))
	f.write('\tCosmological constant = %f \n' %(Grav_obj.Cosmological_cosntant))

	if Grav_obj.field.Horizon:
		f.write('\nHorizon Conditions\n')
		f.write('\tTime of horizon = %.12f seconds \n' %(Grav_obj.field.time))
		f.write('\tRadius of Horizon = %.12f \n' %(Grav_obj.field.Horizon_r))
		
	f.write('\nPotential Conditions\n')
	f.write('\tPotential = %s \n' %(Grav_obj.Potential_type_name))

	f.write('\nInitial Conditions\n')
	f.write('\tInitial Conditional = %s \n' %(Grav_obj.Initial_Condition_type_name))
	
	if Grav_obj.Initial_Condition_type_name == 'Gaussian':
		f.write('\tInitial epsilon = %.12f \n' %(Grav_obj.initial_eps))
		f.write('\tInitial sigma = %.12f \n' %(Grav_obj.initial_sigma))

	f.write('\nNumerical Method\n')
	f.write('\tSolver : %s \n' %(Grav_obj.Solver_type_name))
	f.write('\tGrid Size: %f \n' %(Grav_obj.Grid_size))

	f.write('\nEnding Conditions\n')
	f.write('\tHorizon Condition: %.12f \n' %(Grav_obj.A_min))
	f.write('\tMax iterations: %f \n' %(Grav_obj.Max_interation))
	f.close
	
