# Write your MySQL query statement below
select sample_id, dna_sequence, species
        , sum(case when dna_sequence like 'ATG%' then 1 else 0 end) has_start
        , sum(case when dna_sequence like '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA' then 1 else 0 end) has_stop
        , sum(case when dna_sequence like '%ATAT%' then 1 else 0 end) has_atat 
        , sum(case when dna_sequence like '%GGG%' then 1 else 0 end) has_ggg 
from Samples
group by sample_id, dna_sequence, species
order by sample_id