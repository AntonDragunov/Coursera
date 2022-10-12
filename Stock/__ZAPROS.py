query = """select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock, kmr_dayly.stock, round(kmr_dayly.d_order_dnp * 1.2 * 1.15, 0) as price, partition_dayly.brand from public.partition_dayly
inner join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no WHERE kmr_dayly.cur_day = 27 And kmr_dayly.cur_month = 5 And kmr_dayly.stock > 0;"""



select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock, kmr_dayly.stock,
IIf(partition_dayly.time_period < 0,1,round(kmr_dayly.d_order_dnp * 1.2 * 1.15, 0), 100000) AS price,
partition_dayly.brand from public.partition_dayly
inner join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no WHERE kmr_dayly.cur_day = 27 And kmr_dayly.cur_month = 5 And kmr_dayly.stock > 0



# select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock, kmr_dayly.stock,
# CASE WHEN (partition_dayly.time_period) < 3 THEN round(kmr_dayly.d_order_dnp * 1.2 * 1.15, 0)
# WHEN (partition_dayly.time_period) > 12 THEN round(partition_dayly.price, 0)
# ELSE round(kmr_dayly.d_order_dnp * 1.2 * 1.05, 0) END AS price,
# partition_dayly.brand
# from public.partition_dayly
# left join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no WHERE kmr_dayly.cur_day = 27 And kmr_dayly.cur_month = 5 And kmr_dayly.stock > 0
# And partition_dayly.brand NOT LIKE 'Kia'

select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock, kmr_dayly.stock,
CASE WHEN (partition_dayly.time_period) < 3 THEN round(kmr_dayly.d_order_dnp * 1.2 * 1.25, 0)
WHEN (partition_dayly.time_period) > 12 THEN round(partition_dayly.price, 0)
ELSE round(kmr_dayly.d_order_dnp * 1.2 * 1.05, 0) END AS price,
partition_dayly.brand
from public.partition_dayly
left join kmr_dayly ON partition_dayly.part_no = kmr_dayly.part_no WHERE kmr_dayly.cur_day = 27 And kmr_dayly.cur_month = 5 And kmr_dayly.stock > 0



#выборка только опреледенной группы
select partition_dayly.part_no, partition_dayly.part_name, partition_dayly.free_stock, partition_dayly.price, partition_dayly.brand from partition_dayly
JOIN total_sales ON partition_dayly.part_no = total_sales.part_no
where total_sales.abc_group <> 'B'