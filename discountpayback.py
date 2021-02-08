#NPV calculator

import numpy as np 
import pandas as pd 
import jinja2


def discount_factor_list_maker(required_ror, inflation_rate, years):
	dis_fact = 1 + required_ror + inflation_rate
	for i in range(max(years) + 1):
		discount_factor_list.append(round(1/(dis_fact)**i, 2))
	
def solver(initial_invest, required_ror, inflation_rate, num_years, expected_revenue, proj_name = "No Title"):
	years = range(num_years + 1)
	cash_flow = [-1 * initial_invest]
	global discount_factor_list
	discount_factor_list = []
	cash_flow = cash_flow + expected_revenue  #input expected cash flow per year
	discount_factor_list_maker(required_ror, inflation_rate, years)
	discount_factor_list_a = np.array(discount_factor_list)
	cash_flow_a = np.array(cash_flow)
	net_inflow = np.multiply(cash_flow_a, discount_factor_list_a)
	cum_net_inflow = [-1 * initial_invest]
	for i in range(len(net_inflow)-1):
		cum_net_inflow.append(round(cum_net_inflow[-1] + net_inflow[i+1], 2))
	#print(cum_net_inflow)
	data = {'Year': years, "Cash Flow": cash_flow, "Discount Factor": discount_factor_list_a, "Net Inflows": net_inflow,
 	"Cumulative Net Inflow": cum_net_inflow}
	sol_table = pd.DataFrame.from_dict(data)
	print(proj_name)

	print(sol_table)

solver(75000, .10, 0, 5, [30000, 30000, 25000, 20000, 20000], proj_name = "3.2 Discounted Payback")


solver(500000, .10, .03, 5, [150000,150000,150000,150000,150000], proj_name = "Project A")
solver(500000, .10, .03, 5, [0, 50000, 200000, 300000, 200000], proj_name = "Project B")







